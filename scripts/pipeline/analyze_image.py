#!/usr/bin/env python3
"""
Phase 1: Image Visual Element Analyzer
Analyzes original layout thumbnails using Gemini multimodal API to extract
structured visual element descriptions for SVG regeneration.

Usage:
    python analyze_image.py --id 001                  # Analyze single layout
    python analyze_image.py --range 001-020            # Analyze range
    python analyze_image.py --all                      # Analyze all available
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

# Google Gemini API
try:
    import google.generativeai as genai
except ImportError:
    print("ERROR: google-generativeai not installed. Run: pip install google-generativeai")
    sys.exit(1)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
THUMBNAILS_DIR = BASE_DIR / "assets" / "calibrated_thumbnails"
LAYOUTS_DIR = BASE_DIR / "data" / "layouts"
OUTPUT_DIR = BASE_DIR / "data" / "visual_analysis"

ANALYSIS_PROMPT = """You are a professional graphic design analyst. Analyze this layout composition poster image and extract the CORE GEOMETRIC VISUAL ELEMENTS that form the illustration/diagram portion of the poster.

Focus ONLY on the visual diagram/illustration part (usually in the left half or center), NOT the text labels, tips or keyword badges.

Output a JSON object with this structure:
{
  "layout_id": "<the 3-digit ID visible on the poster>",
  "layout_name": "<Chinese name of the composition>",
  "layout_name_en": "<English name>",
  "visual_description": "<1-2 sentence natural language description of what the illustration shows>",
  "background_color": "<hex color of the illustration area background>",
  "primary_accent_color": "<hex color of the main accent/highlight elements>",
  "geometric_elements": [
    {
      "type": "line|circle|rect|polygon|path|text|arrow|gradient_region|grid",
      "style": "solid|dashed|dotted|filled|stroked",
      "color": "<hex>",
      "opacity": <0-1>,
      "purpose": "<what this element represents: guide_line, focal_point, division, flow_arrow, perspective_line, etc>",
      "position": "<description of position: e.g. 'vertical at 1/3 from left', 'center', 'diagonal from top-left to bottom-right'>",
      "dimensions": "<relative size description>"
    }
  ],
  "composition_structure": {
    "primary_division": "<how the frame is divided: thirds, golden_ratio, diagonal, radial, grid_NxM, etc>",
    "focal_points": ["<position descriptions of focal/anchor points>"],
    "flow_direction": "<visual flow: left-to-right, spiral, converging, expanding, etc>",
    "depth_layers": <number of depth/z layers visible, 1 if flat>,
    "symmetry": "<none|horizontal|vertical|radial|bilateral>"
  },
  "iconic_elements": [
    {
      "type": "<mountain|sun|water|building|person|camera|eye|grid_overlay|etc>",
      "style": "<silhouette|outline|filled|gradient|wireframe>",
      "position": "<where in the composition>",
      "purpose": "<illustrative element, metaphor, scene-setting, etc>"
    }
  ],
  "annotation_markers": [
    {
      "type": "label|number|arrow|circle_highlight|bracket",
      "content": "<text content if any>",
      "position": "<where>",
      "color": "<hex>"
    }
  ]
}

Be extremely precise about positions, colors, and geometric relationships. The output will be used to programmatically recreate this illustration as SVG code.

Important: Output ONLY the JSON object, no markdown fencing, no commentary."""


def analyze_single_image(image_path: Path, layout_data: dict) -> dict:
    """Analyze a single thumbnail image using Gemini."""
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Set GEMINI_API_KEY or GOOGLE_API_KEY environment variable")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Read and encode image
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Build context from layout JSON
    context = f"""
Layout ID: {layout_data.get('id', 'unknown')}
Layout Name: {layout_data.get('name', 'unknown')}
Layout Name EN: {layout_data.get('name_en', 'unknown')}
Category: {layout_data.get('category', 'unknown')}
Theme: {layout_data.get('theme', 'warm-ivory')}
"""

    response = model.generate_content(
        [
            {"mime_type": "image/jpeg", "data": image_data},
            f"{ANALYSIS_PROMPT}\n\nAdditional context:\n{context}",
        ],
        generation_config=genai.GenerationConfig(
            temperature=0.1,
            max_output_tokens=4096,
        ),
    )

    # Parse JSON response
    text = response.text.strip()
    # Remove markdown code fences if present
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        # Try to extract JSON from response
        import re
        match = re.search(r'\{[\s\S]*\}', text)
        if match:
            result = json.loads(match.group())
        else:
            raise ValueError(f"Could not parse JSON from response: {text[:200]}")

    return result


def find_thumbnail(layout_id: str) -> Path | None:
    """Find the thumbnail file for a given layout ID."""
    pattern = f"{layout_id}_*.jpg"
    matches = list(THUMBNAILS_DIR.glob(pattern))
    if matches:
        return matches[0]

    # Also check PNG
    pattern = f"{layout_id}_*.png"
    matches = list(THUMBNAILS_DIR.glob(pattern))
    if matches:
        return matches[0]

    return None


def process_layout(layout_id: str, force: bool = False) -> dict | None:
    """Process a single layout: find thumbnail, analyze, save results."""
    lid = layout_id.zfill(3)
    output_file = OUTPUT_DIR / f"{lid}.json"

    if output_file.exists() and not force:
        print(f"  [{lid}] Already analyzed, skipping (use --force to re-analyze)")
        with open(output_file, "r") as f:
            return json.load(f)

    # Find thumbnail
    thumb = find_thumbnail(lid)
    if not thumb:
        print(f"  [{lid}] ⚠ No thumbnail found, skipping")
        return None

    # Load layout data
    layout_file = LAYOUTS_DIR / f"{lid}.json"
    layout_data = {}
    if layout_file.exists():
        with open(layout_file, "r") as f:
            layout_data = json.load(f)

    print(f"  [{lid}] Analyzing {thumb.name}...")

    try:
        result = analyze_single_image(thumb, layout_data)
        # Save result
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"  [{lid}] ✓ Saved analysis to {output_file.name}")
        return result
    except Exception as e:
        print(f"  [{lid}] ✗ Error: {e}")
        return None


def parse_range(range_str: str) -> list[str]:
    """Parse a range string like '001-020' into list of IDs."""
    start, end = range_str.split("-")
    return [str(i).zfill(3) for i in range(int(start), int(end) + 1)]


def main():
    parser = argparse.ArgumentParser(description="Analyze layout thumbnails for SVG generation")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", help="Single layout ID (e.g. 001)")
    group.add_argument("--range", help="Range of IDs (e.g. 001-020)")
    group.add_argument("--all", action="store_true", help="Process all available thumbnails")
    parser.add_argument("--force", action="store_true", help="Re-analyze even if output exists")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between API calls (seconds)")
    args = parser.parse_args()

    if args.id:
        ids = [args.id.zfill(3)]
    elif args.range:
        ids = parse_range(args.range)
    else:
        # All available thumbnails
        ids = sorted([
            f.stem.split("_")[0]
            for f in THUMBNAILS_DIR.glob("*.jpg")
        ])

    print(f"Processing {len(ids)} layouts...")
    print(f"Thumbnails dir: {THUMBNAILS_DIR}")
    print(f"Output dir: {OUTPUT_DIR}")
    print()

    success = 0
    failed = 0
    skipped = 0

    for lid in ids:
        result = process_layout(lid, force=args.force)
        if result:
            success += 1
        elif result is None:
            # Check if it was skipped vs failed
            output_file = OUTPUT_DIR / f"{lid}.json"
            if output_file.exists():
                skipped += 1
            else:
                failed += 1

        if args.delay > 0 and lid != ids[-1]:
            time.sleep(args.delay)

    print(f"\n{'='*50}")
    print(f"Results: {success} analyzed, {skipped} skipped, {failed} failed")
    print(f"Total: {success + skipped + failed} / {len(ids)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Phase 2: SVG Code Generator
Takes visual analysis JSON (from Phase 1) + original thumbnail and generates
unique SVG code for each layout composition using Gemini code generation.

Usage:
    python generate_svg.py --id 001                    # Generate single SVG
    python generate_svg.py --range 001-020             # Generate range
    python generate_svg.py --all                       # Generate all analyzed
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    print("ERROR: google-generativeai not installed. Run: pip install google-generativeai")
    sys.exit(1)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
THUMBNAILS_DIR = BASE_DIR / "assets" / "calibrated_thumbnails"
ANALYSIS_DIR = BASE_DIR / "data" / "visual_analysis"
LAYOUTS_DIR = BASE_DIR / "data" / "layouts"
SVG_OUTPUT_DIR = BASE_DIR / "data" / "generated_svgs"

# Theme accent color mapping
THEME_ACCENTS = {
    "warm-ivory": {"accent": "#E25238", "bg": "#24211E", "secondary": "#555047", "text": "#FFFFFF"},
    "forest-green": {"accent": "#D4AF37", "bg": "#072018", "secondary": "#2D5A4C", "text": "#FFFFFF"},
    "obsidian-black": {"accent": "#FFD700", "bg": "#0C0C0C", "secondary": "#333333", "text": "#FFFFFF"},
    "cobalt-blue": {"accent": "#FFD000", "bg": "#082154", "secondary": "#133674", "text": "#FFFFFF"},
}

SVG_GENERATION_PROMPT = """You are an expert SVG illustrator specializing in visual composition diagrams for design education.

Your task: Generate a SINGLE, SELF-CONTAINED SVG that illustrates the layout composition technique described below. The SVG must be a faithful recreation of the reference image's geometric illustration.

## SVG Specifications
- ViewBox: `0 0 550 620`
- Must be completely self-contained (no external resources)
- Use `<defs>` for gradients, clip paths, patterns
- Use precise coordinates and clean geometry
- All text must use `font-family="PingFang SC, Noto Sans SC, sans-serif"` for Chinese, `font-family="Montserrat, sans-serif"` for English

## Color Palette for this card
- Background: {bg_color}
- Primary accent: {accent_color}
- Secondary: {secondary_color}
- Text on dark: {text_color}
- Use opacity variations (0.1 to 0.8) for depth and layering

## Layout Composition Being Illustrated
- ID: {layout_id}
- Name: {layout_name}
- English: {layout_name_en}
- Category: {category}

## Visual Analysis of Reference Image
{visual_analysis_json}

## Design Guidelines
1. **Unique illustration**: This SVG must look distinctly different from any other layout in the 350 series. Capture the SPECIFIC visual characteristics of this composition technique.
2. **Educational clarity**: The diagram should clearly demonstrate the composition principle through visual geometry (guide lines, focal points, regions, flow arrows).
3. **Aesthetic quality**: Professional, polished Swiss International Style illustration. Clean geometry, precise proportions.
4. **Iconic scene elements**: Include at least ONE simple illustrative element (mountain, building, portrait, text block wireframe, etc.) that contextualizes how this composition would be applied in real design.
5. **Geometric overlays**: Show the composition's structural grid/guide lines as dashed or semi-transparent overlays on top of the scene.
6. **Labels**: Include 1-2 Chinese text labels on key elements (e.g., "视觉焦点", "引导线", "平衡区域") with colored tag backgrounds.

## Output
Output ONLY the raw SVG code starting with `<svg` and ending with `</svg>`. No markdown fencing, no commentary, no explanation.
"""


def generate_svg(layout_id: str, force: bool = False) -> str | None:
    """Generate SVG code for a single layout using Gemini."""
    lid = layout_id.zfill(3)
    output_file = SVG_OUTPUT_DIR / f"{lid}.svg"

    if output_file.exists() and not force:
        print(f"  [{lid}] Already generated, skipping")
        return output_file.read_text()

    # Load visual analysis
    analysis_file = ANALYSIS_DIR / f"{lid}.json"
    if not analysis_file.exists():
        print(f"  [{lid}] ⚠ No visual analysis found. Run analyze_image.py first.")
        return None

    with open(analysis_file, "r") as f:
        analysis = json.load(f)

    # Load layout metadata
    layout_file = LAYOUTS_DIR / f"{lid}.json"
    if not layout_file.exists():
        print(f"  [{lid}] ⚠ No layout data found.")
        return None

    with open(layout_file, "r") as f:
        layout_data = json.load(f)

    theme = layout_data.get("theme", "warm-ivory")
    colors = THEME_ACCENTS.get(theme, THEME_ACCENTS["warm-ivory"])

    # Find thumbnail for visual reference
    thumb = find_thumbnail(lid)

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Set GEMINI_API_KEY or GOOGLE_API_KEY environment variable")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = SVG_GENERATION_PROMPT.format(
        bg_color=colors["bg"],
        accent_color=colors["accent"],
        secondary_color=colors["secondary"],
        text_color=colors["text"],
        layout_id=lid,
        layout_name=layout_data.get("name", ""),
        layout_name_en=layout_data.get("name_en", ""),
        category=layout_data.get("category", ""),
        visual_analysis_json=json.dumps(analysis, ensure_ascii=False, indent=2),
    )

    # Build content parts
    parts = []
    if thumb and thumb.exists():
        with open(thumb, "rb") as f:
            image_data = f.read()
        parts.append({"mime_type": "image/jpeg", "data": image_data})
        parts.append(f"Reference image above shows the original illustration to recreate.\n\n{prompt}")
    else:
        parts.append(prompt)

    print(f"  [{lid}] Generating SVG for '{layout_data.get('name', '')}'...")

    try:
        response = model.generate_content(
            parts,
            generation_config=genai.GenerationConfig(
                temperature=0.3,
                max_output_tokens=8192,
            ),
        )

        svg_text = response.text.strip()

        # Clean up: extract just the SVG
        if "```" in svg_text:
            # Remove markdown code fences
            lines = svg_text.split("\n")
            in_svg = False
            svg_lines = []
            for line in lines:
                if line.strip().startswith("```"):
                    in_svg = not in_svg
                    continue
                if in_svg or line.strip().startswith("<svg") or (svg_lines and not line.strip().startswith("```")):
                    svg_lines.append(line)
            svg_text = "\n".join(svg_lines)

        # Ensure it starts with <svg
        if "<svg" in svg_text:
            start_idx = svg_text.index("<svg")
            end_idx = svg_text.rindex("</svg>") + 6
            svg_text = svg_text[start_idx:end_idx]
        else:
            raise ValueError("Response does not contain valid SVG")

        # Save
        SVG_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(svg_text)

        print(f"  [{lid}] ✓ SVG saved ({len(svg_text)} bytes)")
        return svg_text

    except Exception as e:
        print(f"  [{lid}] ✗ Error: {e}")
        return None


def find_thumbnail(layout_id: str) -> Path | None:
    """Find the thumbnail file for a given layout ID."""
    for ext in ("jpg", "jpeg", "png"):
        matches = list(THUMBNAILS_DIR.glob(f"{layout_id}_*.{ext}"))
        if matches:
            return matches[0]
    return None


def parse_range(range_str: str) -> list[str]:
    start, end = range_str.split("-")
    return [str(i).zfill(3) for i in range(int(start), int(end) + 1)]


def main():
    parser = argparse.ArgumentParser(description="Generate SVG code from visual analysis")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", help="Single layout ID (e.g. 001)")
    group.add_argument("--range", help="Range of IDs (e.g. 001-020)")
    group.add_argument("--all", action="store_true", help="Process all analyzed layouts")
    parser.add_argument("--force", action="store_true", help="Regenerate even if SVG exists")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay between API calls (seconds)")
    args = parser.parse_args()

    if args.id:
        ids = [args.id.zfill(3)]
    elif args.range:
        ids = parse_range(args.range)
    else:
        ids = sorted([f.stem for f in ANALYSIS_DIR.glob("*.json")])

    print(f"Generating SVGs for {len(ids)} layouts...")
    print(f"Analysis dir: {ANALYSIS_DIR}")
    print(f"SVG output dir: {SVG_OUTPUT_DIR}")
    print()

    success = 0
    failed = 0
    skipped = 0

    for lid in ids:
        result = generate_svg(lid, force=args.force)
        if result:
            success += 1
        else:
            output_file = SVG_OUTPUT_DIR / f"{lid}.svg"
            if output_file.exists():
                skipped += 1
            else:
                failed += 1

        if args.delay > 0 and lid != ids[-1]:
            time.sleep(args.delay)

    print(f"\n{'='*50}")
    print(f"Results: {success} generated, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()

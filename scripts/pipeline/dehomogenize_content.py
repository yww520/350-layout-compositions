#!/usr/bin/env python3
"""
Phase 3: Content De-Homogenizer
Regenerates unique features, tips, checklist, and descriptions for each layout
to replace the auto-generated boilerplate content.

Usage:
    python dehomogenize_content.py --id 001
    python dehomogenize_content.py --range 001-020
    python dehomogenize_content.py --all --detect-only   # List boilerplate entries without changing
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

genai = None  # Lazy import when needed

BASE_DIR = Path(__file__).resolve().parent.parent.parent
LAYOUTS_DIR = BASE_DIR / "data" / "layouts"
THUMBNAILS_DIR = BASE_DIR / "assets" / "calibrated_thumbnails"
BACKUP_DIR = BASE_DIR / "data" / "layouts_backup"

# Boilerplate detection patterns (from compile-prompt.py)
BOILERPLATE_PATTERNS = [
    r"核心锚点.*确立画面第一视觉据点",
    r"视线引导流线.*内在几何规律构建能量流动线",
    r"负空间与呼吸感.*精准掌控实形体块与留白比例",
    r"先确立骨架辅助参考线.*避免元素偏离核心几何轴心",
    r"核心主体位置明确无歧义",
    r"引导线与视觉流向顺畅自然",
    r"留白空间充足.*无视觉拥挤感",
    r"设计法则与空间建构$",
    r"建立画面的几何秩序与视觉张力.*平衡主体叙事与空间留白",
]

CONTENT_PROMPT = """You are a professional design educator writing content for a layout composition encyclopedia card.

## Layout Information
- ID: {layout_id}
- Name: {layout_name} ({layout_name_en})
- Category: {category}
- Subcategory: {subcategory}

## Task
Generate UNIQUE, SPECIFIC content for this composition technique. Every field must be tailored to THIS specific composition — no generic boilerplate.

Output a JSON object with:
{{
  "tagline": "<A punchy one-line Chinese tagline (12-20 chars) that captures the ESSENCE of this specific technique. NOT generic like 'XX设计法则与空间建构'>",
  "description": "<2-3 sentences in Chinese. Explain what this composition IS, its origin/theory, and its most impactful visual effect. Be concrete and specific to this technique.>",
  "features": [
    {{
      "icon": "<one of: target, compass, layers, scale, arrow, eye, grid, frame, triangle, circle>",
      "title": "<4-6 Chinese chars, UNIQUE to this composition>",
      "title_en": "<English title, 1-2 words>",
      "desc": "<2-3 Chinese sentences explaining this specific feature of THIS composition technique. Must reference concrete geometric/visual properties unique to this layout.>"
    }}
  ],
  "tips": [
    {{
      "label": "<Application scenario: e.g. 海报设计, 摄影, UI布局, 商业展示, 插画, etc.>",
      "content": "<Specific, actionable advice for using this composition in that scenario. Include concrete numbers/ratios where applicable.>"
    }}
  ],
  "keywords": [
    {{
      "name": "<Chinese keyword>",
      "name_en": "<English>",
      "icon": "<target|scale|wave|eye|grid|layers|frame|triangle|compass|check>"
    }}
  ],
  "checklist": [
    "<Specific self-check item for this composition (not generic)>"
  ]
}}

Requirements:
- features: exactly 3 items, each MUST be unique to this layout technique
- tips: exactly 3 items, each for a DIFFERENT application scenario
- keywords: exactly 4 items
- checklist: exactly 5 items
- NO boilerplate phrases like "核心锚点", "视线引导流线", "负空间与呼吸感", "骨架辅助参考线"
- Content must demonstrate deep understanding of the specific composition principle
- All content in Chinese unless specified otherwise

Output ONLY the JSON, no markdown fencing."""


def detect_boilerplate(layout_data: dict) -> list[str]:
    """Detect boilerplate patterns in layout data."""
    issues = []
    full_text = json.dumps(layout_data, ensure_ascii=False)

    for pattern in BOILERPLATE_PATTERNS:
        if re.search(pattern, full_text):
            issues.append(f"Boilerplate detected: '{pattern[:50]}...'")

    # Check for generic name_en
    name_en = layout_data.get("name_en", "")
    if name_en.endswith(" COMPOSITION") and not any(c.isalpha() and c.islower() for c in name_en.split(" COMPOSITION")[0]):
        # Check if name_en is just Chinese + "COMPOSITION"
        if re.search(r'[\u4e00-\u9fff]', name_en.split(" COMPOSITION")[0]):
            issues.append(f"Generic name_en: '{name_en}'")

    # Check all keywords have same icon
    keywords = layout_data.get("keywords", [])
    if keywords and len(set(k.get("icon", "") for k in keywords)) == 1 and keywords[0].get("icon") == "check":
        issues.append("All keywords use generic 'check' icon")

    return issues


def regenerate_content(layout_id: str, force: bool = False) -> dict | None:
    """Regenerate unique content for a layout."""
    lid = layout_id.zfill(3)
    layout_file = LAYOUTS_DIR / f"{lid}.json"

    if not layout_file.exists():
        print(f"  [{lid}] ⚠ No layout file found")
        return None

    with open(layout_file, "r") as f:
        layout_data = json.load(f)

    # Check if content needs regeneration
    issues = detect_boilerplate(layout_data)
    if not issues and not force:
        print(f"  [{lid}] ✓ Content appears unique, skipping")
        return layout_data

    if issues:
        print(f"  [{lid}] Found {len(issues)} boilerplate issues:")
        for issue in issues:
            print(f"         - {issue}")

    # Find thumbnail for reference
    thumb = find_thumbnail(lid)

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Set GEMINI_API_KEY or GOOGLE_API_KEY environment variable")

    import google.generativeai as genai
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = CONTENT_PROMPT.format(
        layout_id=lid,
        layout_name=layout_data.get("name", ""),
        layout_name_en=layout_data.get("name_en", ""),
        category=layout_data.get("category", ""),
        subcategory=layout_data.get("subcategory", ""),
    )

    parts = []
    if thumb and thumb.exists():
        with open(thumb, "rb") as f:
            parts.append({"mime_type": "image/jpeg", "data": f.read()})
        parts.append(f"Reference image above shows the original poster for this composition.\n\n{prompt}")
    else:
        parts.append(prompt)

    try:
        response = model.generate_content(
            parts,
            generation_config=genai.GenerationConfig(temperature=0.4, max_output_tokens=4096),
        )

        text = response.text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1]
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

        new_content = json.loads(text)

        # Backup original
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        backup_file = BACKUP_DIR / f"{lid}.json"
        with open(backup_file, "w", encoding="utf-8") as f:
            json.dump(layout_data, f, ensure_ascii=False, indent=2)

        # Merge new content into existing layout data (preserve structural fields)
        for key in ["tagline", "description", "features", "tips", "keywords", "checklist"]:
            if key in new_content:
                layout_data[key] = new_content[key]

        # Fix name_en if it was generic
        if "name_en" in new_content and new_content["name_en"]:
            layout_data["name_en"] = new_content["name_en"]

        # Save updated layout
        with open(layout_file, "w", encoding="utf-8") as f:
            json.dump(layout_data, f, ensure_ascii=False, indent=2)

        print(f"  [{lid}] ✓ Content regenerated and saved")
        return layout_data

    except Exception as e:
        print(f"  [{lid}] ✗ Error: {e}")
        return None


def find_thumbnail(layout_id: str) -> Path | None:
    for ext in ("jpg", "jpeg", "png"):
        matches = list(THUMBNAILS_DIR.glob(f"{layout_id}_*.{ext}"))
        if matches:
            return matches[0]
    return None


def parse_range(range_str: str) -> list[str]:
    start, end = range_str.split("-")
    return [str(i).zfill(3) for i in range(int(start), int(end) + 1)]


def main():
    parser = argparse.ArgumentParser(description="De-homogenize layout content")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", help="Single layout ID")
    group.add_argument("--range", help="Range of IDs")
    group.add_argument("--all", action="store_true", help="Process all layouts")
    parser.add_argument("--force", action="store_true", help="Regenerate even if content seems unique")
    parser.add_argument("--detect-only", action="store_true", help="Only detect boilerplate, don't regenerate")
    parser.add_argument("--delay", type=float, default=1.5, help="Delay between API calls")
    args = parser.parse_args()

    if args.id:
        ids = [args.id.zfill(3)]
    elif args.range:
        ids = parse_range(args.range)
    else:
        ids = sorted([f.stem for f in LAYOUTS_DIR.glob("*.json")])

    if args.detect_only:
        print(f"Scanning {len(ids)} layouts for boilerplate...")
        boilerplate_count = 0
        for lid in ids:
            layout_file = LAYOUTS_DIR / f"{lid}.json"
            if layout_file.exists():
                with open(layout_file, "r") as f:
                    data = json.load(f)
                issues = detect_boilerplate(data)
                if issues:
                    boilerplate_count += 1
                    print(f"  [{lid}] {data.get('name', '?')}: {len(issues)} issues")
        print(f"\nTotal: {boilerplate_count}/{len(ids)} layouts have boilerplate content")
        return

    print(f"Regenerating content for {len(ids)} layouts...")
    success = 0
    for lid in ids:
        result = regenerate_content(lid, force=args.force)
        if result:
            success += 1
        if args.delay > 0 and lid != ids[-1]:
            time.sleep(args.delay)

    print(f"\nDone: {success}/{len(ids)} layouts updated")


if __name__ == "__main__":
    main()

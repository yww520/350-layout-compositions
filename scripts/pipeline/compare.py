#!/usr/bin/env python3
"""
Phase 4: Visual Comparison Tool
Generates side-by-side HTML comparison pages for original thumbnails vs. newly rendered cards.

Usage:
    python compare.py --range 001-020    # Compare specific range
    python compare.py --all              # Compare all available
"""

import argparse
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
THUMBNAILS_DIR = BASE_DIR / "assets" / "calibrated_thumbnails"
DIST_DIR = BASE_DIR / "dist"
COMPARISON_DIR = BASE_DIR / "dist" / "comparison"


def generate_comparison_html(ids: list[str]) -> str:
    """Generate an HTML page showing original vs new side by side."""

    cards_html = ""
    for lid in ids:
        lid = lid.zfill(3)

        # Find original thumbnail
        thumb = None
        for ext in ("jpg", "jpeg", "png"):
            matches = list(THUMBNAILS_DIR.glob(f"{lid}_*.{ext}"))
            if matches:
                thumb = matches[0]
                break

        # Find rendered PNG
        rendered = None
        for f in DIST_DIR.glob(f"{lid}_*.png"):
            rendered = f
            break

        # Load layout name
        layout_file = BASE_DIR / "data" / "layouts" / f"{lid}.json"
        name = lid
        if layout_file.exists():
            with open(layout_file, "r") as f:
                data = json.load(f)
                name = f"{lid} - {data.get('name', '')}"

        thumb_src = f"../../assets/calibrated_thumbnails/{thumb.name}" if thumb else ""
        rendered_src = f"../{rendered.name}" if rendered else ""

        cards_html += f"""
        <div class="comparison-card">
            <h3>{name}</h3>
            <div class="images">
                <div class="image-box">
                    <h4>原版 (Original)</h4>
                    {'<img src="' + thumb_src + '" />' if thumb else '<div class="no-image">无缩略图</div>'}
                </div>
                <div class="image-box">
                    <h4>新生成 (Generated)</h4>
                    {'<img src="' + rendered_src + '" />' if rendered else '<div class="no-image">未渲染</div>'}
                </div>
            </div>
            <div class="status">
                <span class="badge {'ok' if thumb else 'missing'}">原图: {'✓' if thumb else '✗'}</span>
                <span class="badge {'ok' if rendered else 'missing'}">新图: {'✓' if rendered else '✗'}</span>
            </div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>350 Layout Compositions - 原版 vs 新生成 对比</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, 'PingFang SC', sans-serif; background: #111; color: #eee; padding: 40px; }}
        h1 {{ text-align: center; margin-bottom: 10px; font-size: 28px; }}
        .subtitle {{ text-align: center; color: #888; margin-bottom: 40px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(600px, 1fr)); gap: 30px; }}
        .comparison-card {{
            background: #1a1a1a; border: 1px solid #333; border-radius: 12px;
            padding: 20px; transition: border-color 0.2s;
        }}
        .comparison-card:hover {{ border-color: #FFD700; }}
        .comparison-card h3 {{ font-size: 16px; margin-bottom: 12px; color: #FFD700; }}
        .images {{ display: flex; gap: 12px; }}
        .image-box {{ flex: 1; text-align: center; }}
        .image-box h4 {{ font-size: 12px; color: #888; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em; }}
        .image-box img {{ width: 100%; border-radius: 6px; border: 1px solid #333; }}
        .no-image {{ width: 100%; height: 200px; background: #222; border-radius: 6px; display: flex;
                     align-items: center; justify-content: center; color: #555; font-size: 14px; }}
        .status {{ margin-top: 10px; display: flex; gap: 8px; }}
        .badge {{ font-size: 11px; padding: 2px 10px; border-radius: 10px; }}
        .badge.ok {{ background: #0d3320; color: #4ade80; }}
        .badge.missing {{ background: #3b1515; color: #f87171; }}
    </style>
</head>
<body>
    <h1>350 Layout Compositions 对比检视</h1>
    <p class="subtitle">原版 (nevertoday) vs 新生成 (AI SVG Pipeline) · {len(ids)} 项</p>
    <div class="grid">
        {cards_html}
    </div>
</body>
</html>"""


def parse_range(range_str: str) -> list[str]:
    start, end = range_str.split("-")
    return [str(i).zfill(3) for i in range(int(start), int(end) + 1)]


def main():
    parser = argparse.ArgumentParser(description="Generate visual comparison pages")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--range", help="Range of IDs")
    group.add_argument("--all", action="store_true", help="All available")
    args = parser.parse_args()

    if args.range:
        ids = parse_range(args.range)
    else:
        ids = sorted([f.stem.split("_")[0] for f in THUMBNAILS_DIR.glob("*.jpg")])

    COMPARISON_DIR.mkdir(parents=True, exist_ok=True)
    html = generate_comparison_html(ids)
    output_file = COMPARISON_DIR / "comparison.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✓ Comparison page saved to {output_file}")
    print(f"  Covering {len(ids)} layouts")


if __name__ == "__main__":
    main()

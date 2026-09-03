#!/usr/bin/env python3
"""
350 Layouts Batch Renderer
Iterates through all calibrated layouts and compiles high-fidelity cards.
"""

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DIST_DIR = BASE_DIR / "dist"
CALIBRATED_CATALOG = DATA_DIR / "catalog_calibrated.json"
CALIBRATED_ASSETS = BASE_DIR / "assets" / "calibrated_thumbnails"

sys.path.insert(0, str(BASE_DIR / "scripts"))
from render_card import render_card


def main():
    parser = argparse.ArgumentParser(description="Batch Render 350 Layout Cards")
    parser.add_argument("--limit", type=int, default=20, help="Number of cards to render PNG for (default: 20)")
    parser.add_argument("--all-html", action="store_true", help="Compile HTML for all 350 layouts")
    args = parser.parse_args()

    with open(CALIBRATED_CATALOG, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Batch rendering layout cards (Total catalog entries: {len(catalog)})...")

    rendered_png = 0
    compiled_html = 0

    for idx, item in enumerate(catalog):
        lid = item["id"].zfill(3)
        calibrated_img = CALIBRATED_ASSETS / f"{lid}_{item['name']}.jpg"
        img_arg = str(calibrated_img) if calibrated_img.exists() else None

        # Determine format
        if idx < args.limit:
            fmt = "both"
            rendered_png += 1
        elif args.all_html:
            fmt = "html"
        else:
            break

        print(f"[{idx+1}/{len(catalog)}] Rendering {lid} {item['name']}...")
        render_card(lid, str(DIST_DIR), output_format=fmt, image_path=img_arg)
        compiled_html += 1

    print(f"\n✓ Completed: {compiled_html} HTML files compiled, {rendered_png} PNG posters rendered.")


if __name__ == "__main__":
    main()

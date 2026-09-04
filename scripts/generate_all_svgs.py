#!/usr/bin/env python3
"""
Master SVG Generation & Export Script for 350 Layout Compositions.
Populates data/svgs/ with high-fidelity, customized Swiss design SVGs for all 350 layouts.
"""

import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SVGS_DIR = BASE_DIR / "data" / "svgs"
SVGS_DIR.mkdir(parents=True, exist_ok=True)

# Ensure scripts directory is in sys.path
sys.path.insert(0, str(BASE_DIR))

from scripts.svg_generators.procedural_engine import get_svg_for_layout

def main():
    parser = argparse.ArgumentParser(description="Generate all 350 SVGs into data/svgs/")
    parser.add_argument("--overwrite-all", action="store_true", help="Overwrite existing handcrafted SVGs")
    parser.add_argument("--id", type=str, help="Generate single SVG by ID (e.g. 007)")
    args = parser.parse_args()

    if args.id:
        lid = str(args.id).zfill(3)
        svg_content = get_svg_for_layout(lid)
        out_file = SVGS_DIR / f"{lid}.svg"
        out_file.write_text(svg_content.strip(), encoding="utf-8")
        print(f"✓ Generated single SVG for ID {lid} -> {out_file} ({len(svg_content)} chars)")
        return

    print("🚀 Generating SVGs for all 350 layouts...")
    preserved = 0
    generated = 0
    errors = 0

    for i in range(1, 351):
        lid = str(i).zfill(3)
        out_file = SVGS_DIR / f"{lid}.svg"

        if out_file.exists() and not args.overwrite_all:
            # Check if file has substantive content
            try:
                text = out_file.read_text(encoding="utf-8").strip()
                if len(text) > 300 and "<svg" in text and "COMPOSITION SCHEMATIC" not in text:
                    preserved += 1
                    continue
            except Exception:
                pass

        try:
            svg_content = get_svg_for_layout(lid)
            out_file.write_text(svg_content.strip(), encoding="utf-8")
            generated += 1
        except Exception as e:
            print(f"✗ Error generating {lid}: {e}")
            errors += 1

    total_svgs = len(list(SVGS_DIR.glob("*.svg")))
    print("\n" + "=" * 50)
    print("📊 SVG Generation Summary:")
    print(f"  • Preserved existing handcrafted SVGs: {preserved}")
    print(f"  • Newly generated bespoke/procedural SVGs: {generated}")
    print(f"  • Errors: {errors}")
    print(f"  • Total SVGs in data/svgs/: {total_svgs} / 350")
    print("=" * 50)

if __name__ == "__main__":
    main()


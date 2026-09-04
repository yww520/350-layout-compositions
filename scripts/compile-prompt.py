#!/usr/bin/env python3
"""
350 Layout Composition & Prompt Compiler
Automatically deduces professional design parameters, geometric directives,
and AI image generation prompts for all 350 layout types.
"""

import argparse
import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CATALOG_PATH = DATA_DIR / "catalog.json"
LAYOUTS_DIR = DATA_DIR / "layouts"


sys.path.insert(0, str(Path(__file__).resolve().parent))
import layout_knowledge

CATEGORY_KNOWLEDGE = layout_knowledge.SUBCATEGORY_PROFILES


def compile_layout_data(item):
    """Compiles professional design parameters and image prompt using full 33-subcategory knowledge."""
    return layout_knowledge.get_enriched_layout_data(item)


def compile_single(lid, update_json=False):
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)
    
    target = None
    for item in catalog:
        if item["id"].zfill(3) == lid.zfill(3):
            target = item
            break
            
    if not target:
        print(f"Error: Layout ID {lid} not found in catalog.")
        return None

    data = compile_layout_data(target)
    
    if update_json:
        target_path = LAYOUTS_DIR / f"{lid.zfill(3)}.json"
        with open(target_path, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        print(f"✓ Updated layout JSON: {target_path}")

    return data


def compile_all():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    LAYOUTS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    # Keep 001, 002, 004, 084 custom handcrafted data intact
    skip_ids = {"001", "002", "004", "084"}

    for item in catalog:
        lid = item["id"].zfill(3)
        if lid in skip_ids:
            continue
        data = compile_layout_data(item)
        target_path = LAYOUTS_DIR / f"{lid}.json"
        with open(target_path, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        count += 1

    print(f"✓ Compiled and upgraded {count} layouts with professional parameters & prompts.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="350 Layout Prompt & Directive Compiler")
    parser.add_argument("--id", type=str, help="Single layout ID to compile (e.g. 134)")
    parser.add_argument("--all", action="store_true", help="Compile and upgrade all 350 layouts")
    parser.add_argument("--update", action="store_true", help="Write compiled data directly to data/layouts/{id}.json")
    args = parser.parse_args()

    if args.all:
        compile_all()
    elif args.id:
        res = compile_single(args.id, update_json=args.update)
        if res:
            print("\n=== AI Image Generation Prompt ===")
            print(res["ai_prompt"])
            print("\n=== Geometric & Design Directives ===")
            print(json.dumps({
                "theme": res["theme"],
                "features": res["features"],
                "checklist": res["checklist"]
            }, ensure_ascii=False, indent=2))
    else:
        parser.print_help()

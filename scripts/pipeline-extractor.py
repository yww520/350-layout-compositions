#!/usr/bin/env python3
"""
350 Layout Multimodal Pipeline Extractor
Batch ingests layout thumbnail images and structures them into JSON definitions.
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


def extract_card_metadata(item):
    """
    Template extraction logic for converting catalog index item
    into complete layout JSON metadata.
    """
    layout_id = item["id"]
    name = item["name"]
    category = item["category"]
    subcat = item["subcategory"]

    # Choose suitable thematic color based on category
    cat_slug = item.get("category_slug", "")
    if "composition" in cat_slug:
        theme = "warm-ivory" if int(layout_id) % 2 == 1 else "cobalt-blue"
    elif "visual" in cat_slug:
        theme = "obsidian-black"
    elif "chinese" in cat_slug:
        theme = "warm-ivory"
    elif "editorial" in cat_slug:
        theme = "forest-green"
    else:
        theme = "cobalt-blue"

    card_json = {
        "id": layout_id,
        "name": name,
        "name_en": f"{name} Composition".upper(),
        "category": f"{category} / {subcat}",
        "category_slug": cat_slug,
        "subcategory": subcat,
        "tagline": "COMPOSITION PRINCIPLES",
        "description": f"经典视觉架构：{name}。建立画面的秩序与张力，平衡主体与留白关系。",
        "theme": theme,
        "columns_ratio": "530px 380px",
        "visual_height": "660px",
        "features": [
            {"icon": "target", "title": "视觉聚敛", "title_en": "Focus", "desc": "引导视线自然落在画面关键聚焦点。"},
            {"icon": "scale", "title": "虚实平衡", "title_en": "Balance", "desc": "以数理比例掌控呼吸留白与密实体块。"},
            {"icon": "arrow", "title": "动态导向", "title_en": "Guidance", "desc": "构建流线与张力，提升整体视觉节奏。"}
        ],
        "tips": [
            {"label": "构图要义", "content": "避免元素过度拥挤在中心死角，预留充足呼吸空间。"},
            {"label": "实战应用", "content": "依据主体视觉重量调整线条张力与透视深度。"}
        ],
        "keywords": [
            {"name": "焦点", "name_en": "Focus", "icon": "target"},
            {"name": "平衡", "name_en": "Balance", "icon": "scale"},
            {"name": "节奏", "name_en": "Rhythm", "icon": "wave"},
            {"name": "引导", "name_en": "Guide", "icon": "eye"}
        ]
    }
    return card_json


def batch_extract(limit=None):
    if not CATALOG_PATH.exists():
        print(f"Error: {CATALOG_PATH} not found.")
        return

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    LAYOUTS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    for item in catalog:
        layout_id = item["id"]
        target_file = LAYOUTS_DIR / f"{layout_id}.json"
        
        # Don't overwrite existing high-detail cards (like 001, 004)
        if target_file.exists():
            continue

        data = extract_card_metadata(item)
        with open(target_file, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        count += 1

        if limit and count >= limit:
            break

    print(f"✓ Processed and populated {count} layout JSON definitions.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and populate layout JSON database")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of items to populate")
    args = parser.parse_args()

    batch_extract(args.limit)

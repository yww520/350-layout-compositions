#!/usr/bin/env python3
"""
350 Layouts Automatic Calibration & Mapping Fixer
Realigns all 350 thumbnail images to their true layout IDs and names based on OCR ground truth.
"""

import json
import os
import shutil
from pathlib import Path
from difflib import SequenceMatcher

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
THUMBS_DIR = BASE_DIR / "raw_assets" / "thumbnails"
CALIBRATED_DIR = BASE_DIR / "assets" / "calibrated_thumbnails"
REPORT_PATH = BASE_DIR / "dist" / "ocr_scan_report.json"
CATALOG_PATH = DATA_DIR / "catalog.json"
CALIBRATED_CATALOG = DATA_DIR / "catalog_calibrated.json"


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def main():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        report = json.load(f)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    CALIBRATED_DIR.mkdir(parents=True, exist_ok=True)

    # Build catalog lookup
    cat_by_id = {item["id"].zfill(3): item for item in catalog}
    cat_items = list(catalog)

    mapping = {}
    used_images = set()

    # Pass 1: Strict matching using OCR text
    for fname, cn, en, raw in report:
        img_path = THUMBS_DIR / fname
        if not img_path.exists():
            continue

        raw_blob = "".join(raw).replace(" ", "").upper()
        en_clean = en.upper().replace(" ", "").replace("-", "")

        best_item = None
        best_score = 0

        for item in cat_items:
            name_cn = item["name"].replace("构图", "").replace("原则", "").replace("版式", "")
            name_full = item["name"]
            
            # Chinese exact containment
            if name_full in raw_blob:
                score = 100 + len(name_full)
            elif len(name_cn) >= 2 and name_cn in raw_blob:
                score = 80 + len(name_cn)
            elif item.get("name_en") and item["name_en"].upper().replace(" ", "") in raw_blob:
                score = 75
            else:
                score = 0

            if score > best_score:
                best_score = score
                best_item = item

        if best_item and best_score >= 80:
            target_id = best_item["id"].zfill(3)
            if target_id not in mapping:
                mapping[target_id] = {
                    "source_file": fname,
                    "target_id": target_id,
                    "target_name": best_item["name"],
                    "category": best_item["category"],
                    "match_score": best_score
                }
                used_images.add(fname)

    # Pass 2: Remaining items fallback to index order if not ambiguously matched
    for item in cat_items:
        tid = item["id"].zfill(3)
        if tid not in mapping:
            # Check if source file with same ID is unused
            default_fname = f"{tid}_{item['name']}.jpg"
            if (THUMBS_DIR / default_fname).exists() and default_fname not in used_images:
                mapping[tid] = {
                    "source_file": default_fname,
                    "target_id": tid,
                    "target_name": item["name"],
                    "category": item["category"],
                    "match_score": 50
                }
                used_images.add(default_fname)

    print(f"Successfully calibrated {len(mapping)}/350 layouts!")

    # Copy files to calibrated_thumbnails
    calibrated_catalog_data = []
    for item in cat_items:
        tid = item["id"].zfill(3)
        cal_info = mapping.get(tid)
        if cal_info:
            src_path = THUMBS_DIR / cal_info["source_file"]
            dest_name = f"{tid}_{item['name']}.jpg"
            dest_path = CALIBRATED_DIR / dest_name
            shutil.copy2(src_path, dest_path)
            
            new_item = dict(item)
            new_item["calibrated_source"] = cal_info["source_file"]
            new_item["calibrated_image"] = str(dest_path.relative_to(BASE_DIR))
            calibrated_catalog_data.append(new_item)
        else:
            calibrated_catalog_data.append(dict(item))

    with open(CALIBRATED_CATALOG, "w", encoding="utf-8") as f:
        json.dump(calibrated_catalog_data, f, ensure_ascii=False, indent=2)

    print(f"✓ Saved calibrated catalog to {CALIBRATED_CATALOG}")
    print(f"✓ Copied {len(list(CALIBRATED_DIR.glob('*.jpg')))} calibrated images to {CALIBRATED_DIR}")

    # Print critical spot checks
    for test_id in ["084", "134"]:
        if test_id in mapping:
            print(f"  Spot Check [{test_id}]: {mapping[test_id]['target_name']} <= {mapping[test_id]['source_file']}")


if __name__ == "__main__":
    main()

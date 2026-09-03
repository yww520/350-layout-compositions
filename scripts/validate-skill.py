#!/usr/bin/env python3
"""
350 Layout Skill Validator
Performs static integrity checks across catalog, layouts, templates, and scripts.
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CATALOG_FILE = DATA_DIR / "catalog.json"
LAYOUTS_DIR = DATA_DIR / "layouts"
MASTER_TEMPLATE = BASE_DIR / "templates" / "card-master.html"


def validate():
    print("== Starting 350-Layout-Skill Integrity Check ==")
    errors = []

    # 1. Check Master Template
    if not MASTER_TEMPLATE.exists():
        errors.append(f"Missing master template: {MASTER_TEMPLATE}")
    else:
        print("✓ Master template exists.")

    # 2. Check Catalog JSON
    if not CATALOG_FILE.exists():
        errors.append(f"Missing catalog file: {CATALOG_FILE}")
        return False
    
    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    if len(catalog) != 350:
        errors.append(f"Expected 350 catalog items, found {len(catalog)}")
    else:
        print(f"✓ Catalog contains all {len(catalog)} layout definitions.")

    # 3. Check All 350 Layout Files
    valid_count = 0
    for item in catalog:
        layout_id = item["id"]
        json_file = LAYOUTS_DIR / f"{layout_id}.json"
        if not json_file.exists():
            errors.append(f"Missing layout file: {json_file.name}")
            continue

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                required_keys = ["id", "name", "name_en", "category", "theme"]
                for k in required_keys:
                    if k not in data:
                        errors.append(f"Missing key '{k}' in {json_file.name}")
            valid_count += 1
        except Exception as e:
            errors.append(f"Failed to parse {json_file.name}: {e}")

    print(f"✓ Validated {valid_count} / 350 layout JSON definitions.")

    if errors:
        print(f"\n❌ Validation failed with {len(errors)} errors:")
        for err in errors[:10]:
            print(f"  - {err}")
        return False

    print("\n🎉 ALL CHECKS PASSED: Skill repository is production-ready!")
    return True


if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)

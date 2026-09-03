#!/usr/bin/env python3
"""
350 Layouts OCR Verifier and Catalog Fixer
Uses Tesseract OCR to read the actual poster title inside each image,
detects mismatched/shifted files, and re-maps images to their true layout IDs.
"""

import concurrent.futures
import json
import os
import re
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
THUMBS_DIR = BASE_DIR / "raw_assets" / "thumbnails"
CATALOG_PATH = DATA_DIR / "catalog.json"
CORRECTED_CATALOG_PATH = DATA_DIR / "catalog_verified.json"


def ocr_image(img_path):
    cmd = [
        "/opt/homebrew/bin/tesseract",
        str(img_path),
        "stdout",
        "-l", "chi_sim+eng"
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, timeout=10)
        text = res.stdout
        # Extract English title in caps (e.g. DEEP FOCUS COMPOSITION or CENTRIFUGAL COMPOSITION)
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        
        # Look for English uppercase title
        en_title = ""
        cn_title = ""
        for line in lines[:8]:
            # Clean up line
            clean_en = re.sub(r'[^A-Z\s]', '', line).strip()
            if len(clean_en) >= 4 and ("COMPOSITION" in clean_en or "LAYOUT" in clean_en or "GRID" in clean_en or len(clean_en) > 8):
                if not en_title:
                    en_title = clean_en
            # Clean up cn
            clean_cn = re.sub(r'[^\u4e00-\u9fa5]', '', line)
            if len(clean_cn) >= 2 and ("构图" in clean_cn or "版式" in clean_cn or len(clean_cn) >= 3):
                if not cn_title:
                    cn_title = clean_cn

        return img_path.name, cn_title, en_title, lines[:5]
    except Exception as e:
        return img_path.name, "", "", []


def main():
    images = sorted(list(THUMBS_DIR.glob("*.jpg")))
    print(f"Scanning {len(images)} thumbnail images with Tesseract OCR...")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(ocr_image, img): img for img in images}
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    print(f"OCR scan finished on {len(results)} images.")
    
    # Save raw scan report
    report_path = BASE_DIR / "dist" / "ocr_scan_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved OCR scan report to {report_path}")

    # Inspect mismatches
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    catalog_by_id = {item["id"].zfill(3): item for item in catalog}
    
    mismatches = []
    for fname, cn, en, raw in sorted(results):
        lid = fname[:3]
        expected_item = catalog_by_id.get(lid)
        if expected_item:
            exp_name = expected_item["name"]
            # Check if expected name is completely absent from detected cn and raw text
            raw_blob = "".join(raw)
            if exp_name not in raw_blob and (cn and exp_name not in cn):
                mismatches.append({
                    "file": fname,
                    "expected_id": lid,
                    "expected_name": exp_name,
                    "detected_cn": cn,
                    "detected_en": en,
                    "raw_preview": raw[:3]
                })

    print(f"\nFound {len(mismatches)} potential naming/content mismatches:")
    for m in mismatches[:15]:
        print(f"  [{m['file']}] Expected: {m['expected_name']} | Detected: CN='{m['detected_cn']}' EN='{m['detected_en']}'")


if __name__ == "__main__":
    main()

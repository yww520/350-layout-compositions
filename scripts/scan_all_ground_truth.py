#!/usr/bin/env python3
"""
Full OCR Ground Truth Scanner for 350 Layouts
Extracts true Chinese title and English subtitle from each image in assets/original_thumbnails
and maps it to the true catalog entry.
"""

import os
import sys
import glob
import json
import subprocess
from pathlib import Path
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = Path(__file__).resolve().parent.parent
THUMBS_DIR = BASE_DIR / "assets" / "original_thumbnails"
CATALOG_PATH = BASE_DIR / "data" / "catalog.json"
OUTPUT_REPORT = BASE_DIR / "data" / "ocr_ground_truth_raw.json"
OUTPUT_MAPPING = BASE_DIR / "data" / "catalog_ground_truth.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Create fast lookup by name, name_en, and normalized strings
cat_by_id = {item["id"].zfill(3): item for item in catalog}
cat_by_name = {item["name"]: item for item in catalog}

def clean_str(s):
    return "".join(c for c in s if c.isalnum()).upper()

cat_by_clean_en = {}
for item in catalog:
    en = item.get("name_en", "")
    if en:
        cat_by_clean_en[clean_str(en)] = item

def ocr_single_image(img_path):
    cmd = ["/opt/homebrew/bin/tesseract", str(img_path), "stdout", "-l", "chi_sim+eng", "--psm", "6"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        raw_text = res.stdout
    except Exception as e:
        raw_text = ""
    return Path(img_path).name, raw_text

def process_all():
    img_files = sorted(glob.glob(str(THUMBS_DIR / "*.jpg")))
    print(f"Found {len(img_files)} images to scan with Tesseract...", flush=True)

    results = {}
    executor = ThreadPoolExecutor(max_workers=8)
    futures = {executor.submit(ocr_single_image, f): f for f in img_files}
    
    done_cnt = 0
    for fut in as_completed(futures):
        fname, raw_text = fut.result()
        results[fname] = raw_text
        done_cnt += 1
        if done_cnt % 50 == 0 or done_cnt == len(img_files):
            print(f"Scanned {done_cnt}/{len(img_files)} images...", flush=True)
    executor.shutdown()

    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved raw OCR results to {OUTPUT_REPORT}", flush=True)

    # Now match each image to its true catalog entry
    mapping = {}
    unmatched = []

    for fname, raw_text in results.items():
        clean_raw = clean_str(raw_text)
        matched_item = None
        matched_score = 0
        match_reason = ""

        # Strategy 1: Check exact English title containment
        for clean_en, item in cat_by_clean_en.items():
            if len(clean_en) >= 5 and clean_en in clean_raw:
                score = 100 + len(clean_en)
                if score > matched_score:
                    matched_score = score
                    matched_item = item
                    match_reason = f"EN exact match: {item['name_en']}"

        # Strategy 2: Check Chinese title containment
        for item in catalog:
            cn = item["name"]
            cn_core = cn.replace("构图", "").replace("原则", "").replace("版式", "").replace("布局", "")
            if cn in raw_text:
                score = 95 + len(cn)
                if score > matched_score:
                    matched_score = score
                    matched_item = item
                    match_reason = f"CN exact match: {cn}"
            elif len(cn_core) >= 2 and cn_core in raw_text:
                score = 80 + len(cn_core)
                if score > matched_score:
                    matched_score = score
                    matched_item = item
                    match_reason = f"CN core match: {cn_core}"

        if matched_item:
            mapping[fname] = {
                "file_name": fname,
                "matched_id": matched_item["id"].zfill(3),
                "matched_name": matched_item["name"],
                "matched_name_en": matched_item.get("name_en", ""),
                "match_reason": match_reason,
                "score": matched_score
            }
        else:
            unmatched.append((fname, raw_text[:100]))

    print(f"Matched {len(mapping)}/{len(img_files)} images directly.", flush=True)
    print(f"Unmatched: {len(unmatched)}", flush=True)

    # Invert mapping: for each catalog ID, find its true source file
    ground_truth = {}
    id_to_file = {}
    for fname, info in mapping.items():
        tid = info["matched_id"]
        # If conflict, keep highest score
        if tid not in id_to_file or info["score"] > id_to_file[tid]["score"]:
            id_to_file[tid] = info

    for item in catalog:
        tid = item["id"].zfill(3)
        if tid in id_to_file:
            ground_truth[tid] = {
                "id": tid,
                "name": item["name"],
                "name_en": item.get("name_en", ""),
                "category": item.get("category", ""),
                "original_file": id_to_file[tid]["file_name"],
                "match_reason": id_to_file[tid]["match_reason"],
                "status": "calibrated"
            }
        else:
            nominal_fname = f"{tid}_{item['name']}.jpg"
            ground_truth[tid] = {
                "id": tid,
                "name": item["name"],
                "name_en": item.get("name_en", ""),
                "category": item.get("category", ""),
                "original_file": nominal_fname if (THUMBS_DIR / nominal_fname).exists() else None,
                "match_reason": "nominal fallback",
                "status": "unverified"
            }

    with open(OUTPUT_MAPPING, "w", encoding="utf-8") as f:
        json.dump(ground_truth, f, ensure_ascii=False, indent=2)
    print(f"Saved ground truth mapping to {OUTPUT_MAPPING}", flush=True)

if __name__ == "__main__":
    process_all()

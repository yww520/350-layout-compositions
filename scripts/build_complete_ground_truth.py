import json
import glob
import re
from pathlib import Path

BASE_DIR = Path("/Users/clawbot/350-layout-fork")
with open(BASE_DIR / "data" / "ocr_ground_truth_raw.json") as f:
    ocr_data = json.load(f)

layouts = []
for f in sorted(glob.glob(str(BASE_DIR / "data/layouts/*.json"))):
    with open(f) as fp:
        layouts.append(json.load(fp))

def clean_cn(text):
    return "".join(re.findall(r"[\u4e00-\u9fff]+", text))

def clean_en(text):
    return "".join(c.upper() for c in text if c.isalnum())

cat_map = []
for item in layouts:
    cn_full = item["name"]
    cn_core = cn_full.replace("构图", "").replace("原则", "").replace("版式", "").replace("布局", "").replace("法", "")
    en_full = item.get("name_en", "")
    en_clean = clean_en(en_full)
    en_words = [clean_en(w) for w in en_full.split() if len(clean_en(w)) >= 3]
    cat_map.append({
        "item": item,
        "cn_full": cn_full,
        "cn_core": cn_core,
        "en_full": en_full,
        "en_clean": en_clean,
        "en_words": en_words
    })

# Pass 1: OCR matching
matches = {}
for fname, raw_text in ocr_data.items():
    cn_raw = clean_cn(raw_text)
    en_raw = clean_en(raw_text)
    
    best_item = None
    best_score = 0
    best_reason = ""
    
    for c in cat_map:
        score = 0
        reasons = []
        
        # 1. Chinese match
        if c["cn_full"] in cn_raw:
            score += 100
            reasons.append("CN exact: " + c["cn_full"])
        elif len(c["cn_core"]) >= 2 and c["cn_core"] in cn_raw:
            score += 80
            reasons.append("CN core: " + c["cn_core"])
        else:
            common_cn = sum(1 for ch in c["cn_core"] if ch in cn_raw)
            if common_cn >= 3 and len(c["cn_core"]) <= 4:
                score += 65
                reasons.append("CN partial: " + c["cn_core"])
            
        # 2. English match
        if c["en_clean"] and len(c["en_clean"]) >= 6:
            if c["en_clean"] in en_raw:
                score += 100
                reasons.append("EN exact: " + c["en_clean"])
            else:
                matched_words = []
                for w in c["en_words"]:
                    root = w[:5] if len(w) >= 5 else w
                    if root in en_raw:
                        matched_words.append(w)
                if len(matched_words) >= 2:
                    score += 85
                    reasons.append("EN roots: " + " ".join(matched_words[:2]))
                elif len(matched_words) == 1 and len(matched_words[0]) >= 7:
                    score += 55
                    reasons.append("EN key: " + matched_words[0])

        if score > best_score:
            best_score = score
            best_item = c["item"]
            best_reason = " + ".join(reasons)
            
    if best_score >= 70:
        matches[fname] = {
            "source_file": fname,
            "target_id": best_item["id"].zfill(3),
            "target_name": best_item["name"],
            "target_en": best_item.get("name_en", ""),
            "score": best_score,
            "reason": best_reason
        }

# Resolve conflicts (highest score wins)
id_to_source = {}
for fname, m in matches.items():
    tid = m["target_id"]
    if tid not in id_to_source or m["score"] > id_to_source[tid]["score"]:
        id_to_source[tid] = m

used_files = {m["source_file"] for m in id_to_source.values()}
all_files = set(ocr_data.keys())
unused_files = all_files - used_files

print(f"Unique layout IDs calibrated via OCR: {len(id_to_source)} / 350")
print(f"Unused image files: {len(unused_files)}")

# Build final ground truth
ground_truth = []
for item in layouts:
    tid = item["id"].zfill(3)
    if tid in id_to_source:
        entry = {
            "id": tid,
            "name": item["name"],
            "name_en": item.get("name_en", ""),
            "category": item.get("category", ""),
            "original_image_file": id_to_source[tid]["source_file"],
            "calibration_status": "ocr_verified",
            "calibration_reason": id_to_source[tid]["reason"]
        }
    else:
        # Check nominal file
        nominal = f"{tid}_{item['name']}.jpg"
        if nominal in unused_files:
            entry = {
                "id": tid,
                "name": item["name"],
                "name_en": item.get("name_en", ""),
                "category": item.get("category", ""),
                "original_image_file": nominal,
                "calibration_status": "nominal_uncontested",
                "calibration_reason": "Nominal filename matching and uncontested"
            }
            used_files.add(nominal)
            unused_files.remove(nominal)
        else:
            entry = {
                "id": tid,
                "name": item["name"],
                "name_en": item.get("name_en", ""),
                "category": item.get("category", ""),
                "original_image_file": nominal if (BASE_DIR / "assets/original_thumbnails" / nominal).exists() else None,
                "calibration_status": "nominal_fallback",
                "calibration_reason": "Nominal fallback"
            }
    ground_truth.append(entry)

with open(BASE_DIR / "data/catalog_ground_truth.json", "w", encoding="utf-8") as f:
    json.dump(ground_truth, f, ensure_ascii=False, indent=2)

print("Saved catalog_ground_truth.json successfully!")
verified_cnt = sum(1 for x in ground_truth if x["calibration_status"] in ["ocr_verified", "nominal_uncontested"])
print(f"Total verified/uncontested: {verified_cnt} / 350")

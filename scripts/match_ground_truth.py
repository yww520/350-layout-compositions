import json
import glob
import re
from difflib import SequenceMatcher

with open("data/ocr_ground_truth_raw.json") as f:
    ocr_data = json.load(f)

layouts = []
for f in sorted(glob.glob("data/layouts/*.json")):
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
            # Overlap of at least 3 Chinese chars
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
                # Check root word matches (e.g. CONTAINER and QUERY in CONTAINERQUERIESLAYOUT)
                matched_words = []
                for w in c["en_words"]:
                    # Root word prefix (e.g. QUER for QUERY/QUERIES)
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

print("High-confidence matched:", len(matches), "/", len(ocr_data))

for test_file in ["051_螺旋构图.jpg", "217_纵中横排.jpg", "350_全图页幻灯片版式.jpg", "335_标题幻灯片幻灯片版式.jpg"]:
    if test_file in matches:
        m = matches[test_file]
        tid = m["target_id"]
        tname = m["target_name"]
        ten = m["target_en"]
        treason = m["reason"]
        print(f"  {test_file} --> TRUE CONTENT: #{tid} {tname} ({ten}) [{treason}]")
    else:
        print(f"  {test_file} --> not in matches")

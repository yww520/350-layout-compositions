#!/usr/bin/env python3
"""
Generate complete 350 layout visual gallery markdown tables with CDN thumbnails.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CATALOG_PATH = DATA_DIR / "catalog.json"
README_PATH = BASE_DIR / "README.md"

def build_gallery_markdown():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # Group by category and subcategory
    cats = {}
    for item in catalog:
        c = item["category"]
        sc = item["subcategory"]
        if c not in cats:
            cats[c] = {}
        if sc not in cats[c]:
            cats[c][sc] = []
        cats[c][sc].append(item)

    lines = []
    lines.append("## 350 种构图与排版全量视觉画廊 (Full Visual Gallery)\n")
    lines.append("> 涵盖 8 个一级分类与 33 个二级主题。点击任意示意图可直接打开对应的原生高清大图。\n")

    for cat_name, subcats in cats.items():
        total_in_cat = sum(len(items) for items in subcats.values())
        lines.append(f"<details open>\n<summary><h3>📌 {cat_name} ({total_in_cat} 种)</h3></summary>\n")

        for subcat_name, items in subcats.items():
            lines.append(f"#### {subcat_name} ({len(items)} 种 · 编号 {items[0]['id']}–{items[-1]['id']})\n")
            
            # Format into 4-column tables like 350 project
            row_items = []
            for item in items:
                img_url = item["thumbnail"]
                high_url = item["image"]
                cell_img = f'<a href="{high_url}"><img src="{img_url}" width="200" alt="{item["id"]} {item["name"]}"></a>'
                cell_text = f"**{item['id']}**<br>{item['name']}"
                row_items.append((cell_img, cell_text))

            # Chunk into 4 items per row
            for i in range(0, len(row_items), 4):
                chunk = row_items[i:i+4]
                # Pad to 4
                while len(chunk) < 4:
                    chunk.append(("&nbsp;", "&nbsp;"))

                img_row = "| " + " | ".join(c[0] for c in chunk) + " |"
                header_row = "| :---: | :---: | :---: | :---: |"
                text_row = "| " + " | ".join(c[1] for c in chunk) + " |"

                lines.append(img_row)
                lines.append(header_row)
                lines.append(text_row)
                lines.append("")

        lines.append("</details>\n<br>\n")

    return "\n".join(lines)

if __name__ == "__main__":
    gallery_md = build_gallery_markdown()
    
    # Read existing README
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Split before 致敬与致谢 or append
    marker = "## 致敬与致谢"
    if marker in content:
        parts = content.split(marker)
        new_content = parts[0].strip() + "\n\n---\n\n" + gallery_md + "\n\n---\n\n" + marker + parts[1]
    else:
        new_content = content + "\n\n---\n\n" + gallery_md

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✓ Successfully updated README.md with full 350 visual gallery!")

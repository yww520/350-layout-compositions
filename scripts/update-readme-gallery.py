#!/usr/bin/env python3
"""
Updates README.md with the full 350 master gallery pointing directly to ./dist/*.png
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
README_PATH = BASE_DIR / "README.md"
CATALOG_PATH = BASE_DIR / "data" / "catalog.json"
DIST_DIR = BASE_DIR / "dist"


def main():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # Group by category and subcategory
    grouped = {}
    for item in catalog:
        c = item["category"]
        sc = item["subcategory"]
        grouped.setdefault(c, {}).setdefault(sc, []).append(item)

    # Build Top Showcase Section
    showcase_html = """## 🌟 核心金标效果展示 (1:1 纯代码与真实景深母版)

本技能采用瑞士国际主义设计母版与参数化矢量解构体系，**0.5 秒在本地极速导出 1086 × 1448 绝对平直、结构严密的印刷级海报**。绝无空壳，每一张构图均配有专属的几何约束、视线动势向量与 AI 生图提示词：

| 001 三分法构图 | 002 黄金比例构图 | 003 黄金螺旋构图 |
| :---: | :---: | :---: |
| <a href="./dist/001_三分法构图.png"><img src="./dist/001_三分法构图.png" width="300" alt="001 三分法构图"></a> | <a href="./dist/002_黄金比例构图.png"><img src="./dist/002_黄金比例构图.png" width="300" alt="002 黄金比例构图"></a> | <a href="./dist/003_黄金螺旋构图.png"><img src="./dist/003_黄金螺旋构图.png" width="300" alt="003 黄金螺旋构图"></a> |
| 经典空间留白 · 湖面日出九宫交点 | 1.618 标尺 · 黄金分割矩形与大小色块 | 斐波那契方格 · 深空星海螺旋汇聚 |

| 004 黄金三角构图 | 084 深焦构图 | 134 多栏版式 |
| :---: | :---: | :---: |
| <a href="./dist/004_黄金三角构图.png"><img src="./dist/004_黄金三角构图.png" width="300" alt="004 黄金三角构图"></a> | <a href="./dist/084_深焦构图.png"><img src="./dist/084_深焦构图.png" width="300" alt="084 深焦构图"></a> | <a href="./dist/134_多栏版式.png"><img src="./dist/134_多栏版式.png" width="300" alt="134 多栏版式"></a> |
| 动态向量张力 · 折纸雪山与航海帆船 | 真实 3 层景深 · 雪山石桥与栅栏花草 | 四栏瑞士排版 · 栅格模块与密度秩序 |

---
"""

    # Build Full 350 Gallery Section
    gallery_md = """## 📚 350 种构图与排版全量视觉画廊 (Full 350 Gallery)

> 全量 350 张印刷级海报（1086 × 1448 PNG）已全部在本地生成并同步至仓库 `dist/` 目录。点击任意缩略图即可直接在 GitHub 中查看超清无损大图与排版参数。

"""

    for cat_name, subcats in grouped.items():
        total_in_cat = sum(len(items) for items in subcats.values())
        gallery_md += f"\n<details open>\n<summary><h3>📌 {cat_name} ({total_in_cat} 种)</h3></summary>\n\n"

        for subcat_name, items in subcats.items():
            gallery_md += f"#### {subcat_name} ({len(items)} 种 · 编号 {items[0]['id']}–{items[-1]['id']})\n\n"

            # 4 items per row
            for i in range(0, len(items), 4):
                row = items[i:i+4]
                # Image row
                img_cells = []
                for it in row:
                    lid = it["id"].zfill(3)
                    nm = it["name"]
                    png_rel = f"./dist/{lid}_{nm}.png"
                    img_cells.append(f'<a href="{png_rel}"><img src="{png_rel}" width="200" alt="{lid} {nm}"></a>')
                while len(img_cells) < 4:
                    img_cells.append("&nbsp;")

                gallery_md += "| " + " | ".join(img_cells) + " |\n"
                gallery_md += "| " + " | ".join([":---:"] * 4) + "\n"

                # Title row
                title_cells = []
                for it in row:
                    lid = it["id"].zfill(3)
                    nm = it["name"]
                    title_cells.append(f"**{lid}**<br>{nm}")
                while len(title_cells) < 4:
                    title_cells.append("&nbsp;")

                gallery_md += "| " + " | ".join(title_cells) + " |\n\n"

        gallery_md += "</details>\n\n"

    # Read existing README header and instructions
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Split before "## 核心效果展示" or "## 350 种构图与排版全量视觉画廊"
    split_marker = "## 核心效果展示"
    if split_marker in content:
        top_part = content.split(split_marker)[0]
    else:
        top_part = content[:500]

    new_readme = top_part.strip() + "\n\n" + showcase_html + "\n" + gallery_md
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

    print(f"✓ Successfully generated rich gallery in {README_PATH}")


if __name__ == "__main__":
    main()

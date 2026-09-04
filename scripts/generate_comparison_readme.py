#!/usr/bin/env python3
"""
Generate comprehensive README.md with 1-to-1 comparison tables for all 350 layouts:
350 Source Project Original vs New Bespoke Swiss Master Card.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
README_PATH = BASE_DIR / "README.md"
CATALOG_PATH = BASE_DIR / "data" / "catalog.json"
LAYOUTS_DIR = BASE_DIR / "data" / "layouts"

def load_layout_meta(lid):
    json_p = LAYOUTS_DIR / f"{lid}.json"
    if json_p.exists():
        try:
            return json.loads(json_p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

def main():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # Group by category and subcategory
    grouped = {}
    for item in catalog:
        c = item["category"]
        sc = item["subcategory"]
        grouped.setdefault(c, {}).setdefault(sc, []).append(item)

    header_section = """# 350 Layout Architect · 视觉构图与排版全能 Agent 技能

`350-layout-skill` 是一套专为 AI Agent（如 Claude Code, OpenClaw, OpenAI Codex, Cursor 等）打造的**生产级全媒介构图与视觉排版系统**。

基于开源著名的「350 种排版」体系，本项目将其从“静态图鉴”升级为**可计算、可编译、可执行的标准化 Agent 技能**：支持智能构图推荐、AI生图构图约束编译 (Midjourney/Flux)、前端响应式网格生成，并能**离线秒级渲染出 1086 × 1448 印刷级瑞士设计排版海报**。

---

## 一键安装与使用

把下面这段话发给支持 Skills 的 AI Agent：

```text
请安装这个仓库里的全部 Skills：https://github.com/yww520/350-layout-compositions
```

安装后即可直接调用：

```text
Use $layout-350 ...
```

---

## 🌟 核心金标效果对比展示 (1:1 原版 vs 全新重构)

本项目采用瑞士国际主义设计母版与参数化矢量解构体系，将原版低清模糊、甚至结构失衡的示意图，**彻底升级为 1086 × 1448 印刷级绝对平直矢量图鉴海报**。绝无空壳，每一张构图均配有专属的几何约束、视线动势向量与精准设计语义：

| 编号与核心版式 | 350 源项目原版 (Original) | 本项目全新重构图鉴 (New Bespoke) | 核心对比与重构升级亮点 |
| :---: | :---: | :---: | :--- |
| **001 三分法构图**<br><sub>RULE OF THIRDS</sub> | <a href="./assets/original_thumbnails/001_三分法构图.jpg"><img src="./assets/original_thumbnails/001_三分法构图.jpg" width="240" alt="001 原版"></a> | <a href="./dist/001_三分法构图.png"><img src="./dist/001_三分法构图.png" width="240" alt="001 新版"></a> | **修正地平线失衡**：原版湖面地平线倾斜且主体交点偏移；重构版严格按九宫 1/3 黄金交点定位，构筑呼吸空间留白。 |
| **002 黄金比例构图**<br><sub>GOLDEN RATIO</sub> | <a href="./assets/original_thumbnails/002_黄金比例构图.jpg"><img src="./assets/original_thumbnails/002_黄金比例构图.jpg" width="240" alt="002 原版"></a> | <a href="./dist/002_黄金比例构图.png"><img src="./dist/002_黄金比例构图.png" width="240" alt="002 新版"></a> | **精准 1:1.618 数学标尺**：构建严密的外接矩形、主副色块比例与动势线，彻底消除原版手工绘图的几何误差。 |
| **003 黄金螺旋构图**<br><sub>GOLDEN SPIRAL</sub> | <a href="./assets/original_thumbnails/003_黄金螺旋构图.jpg"><img src="./assets/original_thumbnails/003_黄金螺旋构图.jpg" width="240" alt="003 原版"></a> | <a href="./dist/003_黄金螺旋构图.png"><img src="./dist/003_黄金螺旋构图.png" width="240" alt="003 新版"></a> | **斐波那契螺旋精确方程**：解决原版螺旋线起笔生硬断裂问题，连续曲率自然收束于极坐标核心焦点。 |
| **004 黄金三角构图**<br><sub>GOLDEN TRIANGLE</sub> | <a href="./assets/original_thumbnails/004_黄金三角构图.jpg"><img src="./assets/original_thumbnails/004_黄金三角构图.jpg" width="240" alt="004 原版"></a> | <a href="./dist/004_黄金三角构图.png"><img src="./dist/004_黄金三角构图.png" width="240" alt="004 新版"></a> | **对角垂直垂足结构**：主对角线与两顶点垂直垂足精确相交，三层三角受力场平衡稳固，动感强烈。 |
| **084 深焦构图**<br><sub>DEEP FOCUS</sub> | <a href="./assets/original_thumbnails/084_深焦构图.jpg"><img src="./assets/original_thumbnails/084_深焦构图.jpg" width="240" alt="084 原版"></a> | <a href="./dist/084_深焦构图.png"><img src="./dist/084_深焦构图.png" width="240" alt="084 新版"></a> | **真实三层超焦景深**：原版仅为粗糙实景截图；新版打造前景植物门框、中景叙事建筑、远景雪山天际线全域 f/11 锐利清晰。 |
| **134 多栏版式**<br><sub>MULTI-COLUMN</sub> | <a href="./assets/original_thumbnails/134_多栏版式.jpg"><img src="./assets/original_thumbnails/134_多栏版式.jpg" width="240" alt="134 原版"></a> | <a href="./dist/134_多栏版式.png"><img src="./dist/134_多栏版式.png" width="240" alt="134 新版"></a> | **瑞士国际主义分栏范式**：精准 4 栏基准线与栏间距约束，跨栏大标与图文穿插秩序分明，解决原版排版杂乱。 |

---

## 📚 350 种构图与排版全量一对一画廊对比 (Full 350 1-on-1 Comparison Gallery)

> 全量 350 套构图在此以 **1:1 左右对照形式平铺展开**：左侧为 **350 源项目原版示意图（Original）**，右侧为 **本项目全新矢量重构的高清印刷级海报（New Bespoke）**。
> 点击任意卡片图片即可直接打开查看超清细节与排版参数。本地也可直接在浏览器中打开 `compare.html` 查看支持实时搜索与拖拽滑块对比的交互界面。

"""

    gallery_parts = [header_section]

    for cat_name, subcats in grouped.items():
        total_in_cat = sum(len(items) for items in subcats.values())
        gallery_parts.append(f"\n### 📌 {cat_name} ({total_in_cat} 种)\n\n")

        for subcat_name, items in subcats.items():
            start_id = items[0]["id"].zfill(3)
            end_id = items[-1]["id"].zfill(3)
            gallery_parts.append(f"#### {subcat_name} ({len(items)} 种 · 编号 {start_id}–{end_id})\n\n")

            table_lines = [
                "| 编号与版式名称 | 350 源项目原版 (Original) | 本项目全新重构图鉴 (New Bespoke) |",
                "| :---: | :---: | :---: |"
            ]

            for it in items:
                lid = it["id"].zfill(3)
                nm = it["name"]
                meta = load_layout_meta(lid)
                name_en = meta.get("name_en", "")
                tagline = meta.get("tagline", "")

                orig_rel = f"./assets/original_thumbnails/{lid}_{nm}.jpg"
                new_rel = f"./dist/{lid}_{nm}.png"

                title_cell = f"**{lid} {nm}**"
                if name_en:
                    title_cell += f"<br><sub>{name_en}</sub>"
                if tagline:
                    title_cell += f"<br><small>{tagline}</small>"

                orig_cell = f'<a href="{orig_rel}"><img src="{orig_rel}" width="250" alt="{lid} {nm} 原图"></a>'
                new_cell = f'<a href="{new_rel}"><img src="{new_rel}" width="250" alt="{lid} {nm} 新图"></a>'

                table_lines.append(f"| {title_cell} | {orig_cell} | {new_cell} |")

            gallery_parts.append("\n".join(table_lines) + "\n\n")

    full_readme = "".join(gallery_parts)
    README_PATH.write_text(full_readme, encoding="utf-8")
    print(f"✓ Generated comparison README with 350 1-on-1 pairs at {README_PATH}")

if __name__ == "__main__":
    main()

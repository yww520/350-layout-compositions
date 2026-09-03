#!/usr/bin/env python3
"""
350 Layout Composition & Prompt Compiler
Automatically deduces professional design parameters, geometric directives,
and AI image generation prompts for all 350 layout types.
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


CATEGORY_KNOWLEDGE = {
    "经典法则与空间留白": {
        "theme": "warm-ivory",
        "focus_type": "classic_rule",
        "default_subject": "A majestic minimalist landscape with a solitary traveler or natural landmark",
        "keywords": ["平衡", "留白", "比例", "黄金分割"],
        "keywords_en": ["Balance", "Negative Space", "Ratio", "Golden Ratio"]
    },
    "视点、景深与空间感": {
        "theme": "forest-green",
        "focus_type": "depth_perspective",
        "default_subject": "A multi-layered scenery with rich foreground, detailed architectural midground, and expansive horizon background",
        "keywords": ["景深", "层级", "透视", "空间感"],
        "keywords_en": ["Depth of Field", "Layers", "Perspective", "Spatial Sense"]
    },
    "几何形与放射结构": {
        "theme": "obsidian-black",
        "focus_type": "geometric_radial",
        "default_subject": "Dynamic geometric forces, radiating beams and stark architectural lines converging at a focal nexus",
        "keywords": ["几何", "放射", "力场", "汇聚"],
        "keywords_en": ["Geometry", "Radial", "Force Field", "Convergence"]
    },
    "字母形与曲线": {
        "theme": "warm-ivory",
        "focus_type": "curved_flow",
        "default_subject": "A winding scenic road, meandering river valley or dynamic flowing ribbon gracefully curving across space",
        "keywords": ["曲线", "流线", "韵律", "引导"],
        "keywords_en": ["Curve", "Flowline", "Rhythm", "Guidance"]
    },
    "重心、线条与轴线": {
        "theme": "cobalt-blue",
        "focus_type": "axial_linear",
        "default_subject": "Soaring bridges, diagonal architectural rafters or stark diagonal horizon creating powerful kinetic tension",
        "keywords": ["轴线", "重力", "张力", "对角线"],
        "keywords_en": ["Axis", "Gravity", "Tension", "Diagonal"]
    },
    "阵列、层叠与组群": {
        "theme": "obsidian-black",
        "focus_type": "array_pattern",
        "default_subject": "Rhythmic repetition of repeating architectural arches, modular windows or patterned geometric elements",
        "keywords": ["阵列", "层叠", "韵律", "秩序"],
        "keywords_en": ["Array", "Stacking", "Rhythm", "Order"]
    },
    "分栏、跨页与出血": {
        "theme": "forest-green",
        "focus_type": "editorial_columns",
        "default_subject": "Swiss modern editorial grid design with multi-column rhythm, balanced gutters, and bold typographic blocks",
        "keywords": ["分栏", "网格", "行长", "跨栏"],
        "keywords_en": ["Columns", "Grid", "Line Length", "Span"]
    },
    "网格系统": {
        "theme": "cobalt-blue",
        "focus_type": "modular_grid",
        "default_subject": "Precision baseline and modular grid system, structural alignment guides, mathematical typographic harmony",
        "keywords": ["模块", "基准线", "栅格", "秩序"],
        "keywords_en": ["Modular", "Baseline", "Grid", "Order"]
    },
    "响应式重排模式": {
        "theme": "cobalt-blue",
        "focus_type": "ui_responsive",
        "default_subject": "Modern responsive UI cards, bento box modular layout with rounded corners and high-contrast micro-interactions",
        "keywords": ["响应式", "便当盒", "流式", "模块化"],
        "keywords_en": ["Responsive", "Bento Box", "Fluid", "Modular"]
    },
    "视角与镜头覆盖": {
        "theme": "obsidian-black",
        "focus_type": "cinematography_lens",
        "default_subject": "Cinematic widescreen film frame, dramatic chiaroscuro lighting, dynamic camera angle and intense atmosphere",
        "keywords": ["景别", "视点", "光比", "镜头"],
        "keywords_en": ["Framing", "Angle", "Chiaroscuro", "Lens"]
    },
    "留白、虚实与章法": {
        "theme": "warm-ivory",
        "focus_type": "chinese_zen",
        "default_subject": "Traditional East Asian poetic landscape, misty mountain silhouette with generous breathing negative space",
        "keywords": ["留白", "虚实", "气韵", "意境"],
        "keywords_en": ["Negative Space", "Void & Solid", "Vital Energy", "Zen Poetics"]
    },
    "三远、透视与游观": {
        "theme": "warm-ivory",
        "focus_type": "chinese_perspective",
        "default_subject": "Three distances classical Chinese shan shui landscape, towering vertical cliffs, deep gorges and expansive valleys",
        "keywords": ["高远", "深远", "平远", "游观"],
        "keywords_en": ["High Distance", "Deep Distance", "Level Distance", "Roaming Vision"]
    }
}


def compile_layout_data(item):
    """Compiles professional design parameters and image prompt for a single layout entry."""
    lid = item["id"]
    name = item["name"]
    category = item["category"]
    cat_slug = item.get("category_slug", "")
    subcategory = item["subcategory"]

    # Match knowledge rule
    kinfo = CATEGORY_KNOWLEDGE.get(subcategory)
    if not kinfo:
        for k, v in CATEGORY_KNOWLEDGE.items():
            if k in subcategory or k in category:
                kinfo = v
                break
    if not kinfo:
        kinfo = {
            "theme": "warm-ivory" if int(lid) % 2 == 1 else "cobalt-blue",
            "focus_type": "general_composition",
            "default_subject": f"Masterful visual composition demonstrating {name} principle",
            "keywords": ["平衡", "焦点", "节奏", "引导"],
            "keywords_en": ["Balance", "Focus", "Rhythm", "Guide"]
        }

    theme = kinfo["theme"]
    subject_desc = kinfo["default_subject"]

    # Generate tailored prompt
    prompt = (
        f"Professional editorial illustration demonstrating {name} (350 Layouts series #{lid}), "
        f"{subject_desc}. "
        f"Art style: clean graphic design poster aesthetic, Swiss International Typographic influence, "
        f"harmonious color palette matching {theme} tone, fine vector linework, clear spatial hierarchy, "
        f"3:4 aspect ratio, ultra-high resolution, zero chaotic clutter."
    )

    features = [
        {
            "icon": "target",
            "title": f"{name[:2]}核心锚点",
            "title_en": "Focal Anchor",
            "desc": f"确立画面第一视觉据点，使主体在{name}框架中获得最强烈的视觉重力与识别度。"
        },
        {
            "icon": "compass",
            "title": "视线引导流线",
            "title_en": "Leading Flow",
            "desc": f"依据{name}的内在几何规律构建能量流动线，牵引视线从入口自然游弋至核心。"
        },
        {
            "icon": "layers",
            "title": "负空间与呼吸感",
            "title_en": "Negative Space",
            "desc": f"精准掌控实形体块与留白比例，消除压抑局促，赋予整体版式通透的呼吸节拍。"
        }
    ]

    tips = [
        {
            "label": "构图基准",
            "content": f"在应用{name}时，先确立骨架辅助参考线，避免元素偏离核心几何轴心。"
        },
        {
            "label": "图文呼应",
            "content": "文字标题与说明应落在视觉留白区或沿构图次导引线排列，实现图文一体化。"
        }
    ]

    checklist = [
        f"{name}核心主体位置明确无歧义",
        "引导线与视觉流向顺畅自然",
        "留白空间充足，无视觉拥挤感",
        "明暗与色彩反差符合层级逻辑",
        "信息传达准确，整体秩序严密"
    ]

    kw_list = []
    for cn, en in zip(kinfo["keywords"], kinfo["keywords_en"]):
        kw_list.append({"name": cn, "name_en": en, "icon": "check"})

    compiled = {
        "id": lid,
        "name": name,
        "name_en": f"{name} COMPOSITION".upper(),
        "category": f"{category} / {subcategory}",
        "category_slug": cat_slug,
        "subcategory": subcategory,
        "tagline": f"{name}设计法则与空间建构",
        "description": f"经典视觉架构第 {lid} 号：{name}。建立画面的几何秩序与视觉张力，平衡主体叙事与空间留白。",
        "theme": theme,
        "columns_ratio": "530px 380px",
        "visual_height": "660px",
        "ai_prompt": prompt,
        "features": features,
        "tips": tips,
        "keywords": kw_list,
        "checklist": checklist
    }
    return compiled


def compile_single(lid, update_json=False):
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)
    
    target = None
    for item in catalog:
        if item["id"].zfill(3) == lid.zfill(3):
            target = item
            break
            
    if not target:
        print(f"Error: Layout ID {lid} not found in catalog.")
        return None

    data = compile_layout_data(target)
    
    if update_json:
        target_path = LAYOUTS_DIR / f"{lid.zfill(3)}.json"
        with open(target_path, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        print(f"✓ Updated layout JSON: {target_path}")

    return data


def compile_all():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    LAYOUTS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    # Keep 001, 004, 084 custom handcrafted data intact
    skip_ids = {"001", "004", "084"}

    for item in catalog:
        lid = item["id"].zfill(3)
        if lid in skip_ids:
            continue
        data = compile_layout_data(item)
        target_path = LAYOUTS_DIR / f"{lid}.json"
        with open(target_path, "w", encoding="utf-8") as out:
            json.dump(data, out, ensure_ascii=False, indent=2)
        count += 1

    print(f"✓ Compiled and upgraded {count} layouts with professional parameters & prompts.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="350 Layout Prompt & Directive Compiler")
    parser.add_argument("--id", type=str, help="Single layout ID to compile (e.g. 134)")
    parser.add_argument("--all", action="store_true", help="Compile and upgrade all 350 layouts")
    parser.add_argument("--update", action="store_true", help="Write compiled data directly to data/layouts/{id}.json")
    args = parser.parse_args()

    if args.all:
        compile_all()
    elif args.id:
        res = compile_single(args.id, update_json=args.update)
        if res:
            print("\n=== AI Image Generation Prompt ===")
            print(res["ai_prompt"])
            print("\n=== Geometric & Design Directives ===")
            print(json.dumps({
                "theme": res["theme"],
                "features": res["features"],
                "checklist": res["checklist"]
            }, ensure_ascii=False, indent=2))
    else:
        parser.print_help()

"""
Procedural SVG Engine for 350 Layout Compositions.
Synthesizes high-fidelity, customized Swiss design SVGs for any layout ID,
guaranteeing ZERO fallback to generic dashed boxes.
"""

import json
import re
from pathlib import Path
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

# Import dedicated generators
from .cat01_composition import CAT01_SVGS
from .cat02_principles import CAT02_SVGS
from .cat03_editorial import CAT03_SVGS
from .cat04_typography import CAT04_SVGS
from .cat05_web_ui import CAT05_SVGS
from .cat06_cinema_art import CAT06_SVGS
from .cat07_presentations import CAT07_SVGS

BASE_DIR = Path(__file__).resolve().parent.parent.parent
LAYOUTS_DIR = BASE_DIR / "data" / "layouts"

# Aggregate all bespoke generators
BESPOKE_MAP = {}
BESPOKE_MAP.update(CAT01_SVGS)
BESPOKE_MAP.update(CAT02_SVGS)
BESPOKE_MAP.update(CAT03_EDITORIAL_SVGS if 'CAT03_EDITORIAL_SVGS' in globals() else CAT03_SVGS)
BESPOKE_MAP.update(CAT04_SVGS)
BESPOKE_MAP.update(CAT05_SVGS)
BESPOKE_MAP.update(CAT06_SVGS)
BESPOKE_MAP.update(CAT07_SVGS)

def synthesize_procedural_svg(layout_id, data):
    """
    Synthesize an authentic, geometrically accurate Swiss design SVG
    based on subcategory archetype and layout metadata.
    """
    name = data.get("name", "版式构图")
    name_en = data.get("name_en", "LAYOUT COMPOSITION")
    subcat = data.get("subcategory", "经典法则与空间留白")
    theme_key = data.get("theme", "warm-ivory")
    t = get_theme(theme_key)

    # Subcategory visual styles
    if "网格" in subcat or "栏" in subcat or "字体" in subcat or "对齐" in subcat:
        # Typographic & Grid System Archetype
        cols = 6 if "16" not in name else 8
        col_w = int(400 / cols)
        lines = []
        for i in range(cols + 1):
            x = 75 + i * col_w
            lines.append(f'<line x1="{x}" y1="80" x2="{x}" y2="520" stroke="{t["accent"]}" stroke-width="1.2" stroke-dasharray="4,4" opacity="0.4"/>')
        for y in range(80, 530, 44):
            lines.append(f'<line x1="75" y1="{y}" x2="{75 + cols*col_w}" y2="{y}" stroke="{t["guide"]}" stroke-width="0.8"/>')
        
        inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="6"/>
  <!-- Grid Matrix -->
  {''.join(lines)}
  <!-- Active Field Modules -->
  <rect x="{75 + col_w}" y="124" width="{col_w*3}" height="132" fill="{t['accent']}" rx="4" fill-opacity="0.9"/>
  <rect x="{75 + col_w*2}" y="300" width="{col_w*2}" height="88" fill="{t['danger']}" rx="4"/>
  <circle cx="{75 + col_w*3}" cy="344" r="14" fill="#FFFFFF"/>
  <text x="{75 + col_w*2.5}" y="195" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:18]}</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}
"""

    elif "CSS" in subcat or "原语" in subcat or "框架" in subcat or "产品" in subcat or "响应式" in subcat:
        # Web, UI & Component Archetype
        inner = f"""
  <!-- Browser / UI Viewport Shell -->
  <rect x="40" y="50" width="470" height="520" rx="10" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- UI Header Bar -->
  <rect x="40" y="50" width="470" height="42" rx="10" fill="{t['bg']}"/>
  <circle cx="65" cy="71" r="5" fill="#FF5F56"/>
  <circle cx="82" cy="71" r="5" fill="#FFBD2E"/>
  <circle cx="99" cy="71" r="5" fill="#27C93F"/>
  <rect x="130" y="60" width="280" height="22" rx="5" fill="{t['bg_surface']}"/>
  <text x="270" y="75" fill="{t['text_dim']}" font-size="10" font-family="Montserrat" text-anchor="middle">https://ui.system/{layout_id}</text>
  <!-- Main UI Component Canvas -->
  <rect x="65" y="115" width="260" height="200" rx="8" fill="{t['accent']}" fill-opacity="0.2" stroke="{t['accent']}" stroke-width="1.8"/>
  <circle cx="195" cy="185" r="32" fill="{t['accent']}"/>
  <circle cx="195" cy="185" r="8" fill="#FFFFFF"/>
  <text x="195" y="250" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:18]}</text>
  <!-- Flanking Sidebar Card -->
  <rect x="345" y="115" width="140" height="200" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <line x1="365" y1="145" x2="465" y2="145" stroke="{t['accent_alt']}" stroke-width="3" stroke-linecap="round"/>
  <line x1="365" y1="175" x2="445" y2="175" stroke="{t['text_dim']}" stroke-width="2"/>
  <line x1="365" y1="195" x2="455" y2="195" stroke="{t['text_dim']}" stroke-width="2"/>
  <!-- Bottom Full-Width Strip -->
  <rect x="65" y="335" width="420" height="110" rx="8" fill="{t['stroke']}"/>
  <line x1="90" y1="390" x2="460" y2="390" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="6,4"/>
  {badge(185, 490, name, t['accent'], t['text'], 180, 28)}
"""

    elif "三远" in subcat or "取景" in subcat or "留白" in subcat or "东亚" in subcat:
        # Traditional East Asian / Zen Composition Archetype
        inner = f"""
  <!-- Traditional Scroll Canvas -->
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Mountain Silhouette Strata -->
  <path d="M 80 340 Q 200 240 290 320 T 470 290 L 470 520 L 80 520 Z" fill="{t['stroke']}" opacity="0.6"/>
  <path d="M 60 410 Q 180 320 275 390 T 490 360 L 490 540 L 60 540 Z" fill="{t['bg']}"/>
  <!-- Floating Mist Bands -->
  <path d="M 100 320 Q 275 300 450 320" fill="none" stroke="#FFFFFF" stroke-width="12" opacity="0.3" stroke-linecap="round"/>
  <!-- Poetic Vertical Hanzi Inscription -->
  <text x="120" y="130" fill="{t['accent']}" font-size="24" font-weight="900" font-family="Kaiti, STKaiti, serif">{name[:2]}</text>
  <text x="120" y="165" fill="{t['accent']}" font-size="24" font-weight="900" font-family="Kaiti, STKaiti, serif">{name[2:4] if len(name)>2 else '构'}</text>
  <!-- Red Seal Mark -->
  <rect x="105" y="195" width="30" height="30" fill="{t['danger']}" rx="2"/>
  <text x="120" y="215" fill="#FFFFFF" font-size="12" font-family="Songti, serif" text-anchor="middle">印</text>
  <!-- Minimalist Solar Void -->
  <circle cx="370" cy="160" r="38" fill="{t['accent']}" opacity="0.4"/>
  <circle cx="370" cy="160" r="16" fill="{t['accent']}"/>
  {badge(185, 510, name, t['accent'], t['bg'], 180, 28)}
"""

    elif "幻灯片" in subcat or "演示" in subcat or "叙事" in subcat or "数据" in subcat:
        # Presentation & Information Design Archetype
        inner = f"""
  <!-- 16:9 Presentation Slide Card -->
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="70" y="130" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" letter-spacing="3">EXECUTIVE BRIEFING</text>
  <text x="70" y="180" fill="#FFFFFF" font-size="28" font-weight="900" font-family="Montserrat">{name_en[:22]}</text>
  <!-- 3 Impact Cards / Graph Blocks -->
  <rect x="70" y="220" width="120" height="160" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.2"/>
  <text x="130" y="280" fill="{t['accent_alt']}" font-size="24" font-weight="900" font-family="Montserrat" text-anchor="middle">85%</text>
  <rect x="215" y="200" width="120" height="180" rx="8" fill="{t['accent']}"/>
  <text x="275" y="280" fill="{t['bg']}" font-size="28" font-weight="900" font-family="Montserrat" text-anchor="middle">98.4%</text>
  <rect x="360" y="220" width="120" height="160" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.2"/>
  <text x="420" y="280" fill="{t['accent_alt']}" font-size="24" font-weight="900" font-family="Montserrat" text-anchor="middle">4.9★</text>
  <!-- Horizon Line -->
  <line x1="70" y1="420" x2="480" y2="420" stroke="{t['guide']}" stroke-width="1.5"/>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}
"""

    elif "人物" in subcat or "镜头" in subcat or "调度" in subcat or "视点" in subcat:
        # Cinema, Camera & Mise-en-scène Archetype
        inner = f"""
  <!-- Cinematic Widescreen Viewfinder Frame -->
  <rect x="40" y="100" width="470" height="420" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="4"/>
  <!-- Viewfinder Crosshairs & Rule-of-Thirds Grid -->
  <line x1="40" y1="240" x2="510" y2="240" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="40" y1="380" x2="510" y2="380" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="196" y1="100" x2="196" y2="520" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="353" y1="100" x2="353" y2="520" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <!-- Corner Viewfinder Brackets -->
  <path d="M 60 140 L 60 120 L 80 120 M 470 120 L 490 120 L 490 140 M 60 480 L 60 500 L 80 500 M 470 500 L 490 500 L 490 480" fill="none" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Character / Focus Subject Blocking -->
  <circle cx="196" cy="240" r="44" fill="{t['accent']}" opacity="0.25"/>
  <circle cx="196" cy="240" r="22" fill="{t['accent']}"/>
  <circle cx="196" cy="240" r="6" fill="#FFFFFF"/>
  <path d="M 150 360 Q 196 310 242 360 L 250 500 L 140 500 Z" fill="{t['stroke']}"/>
  <!-- REC Icon & Meta -->
  <circle cx="65" cy="75" r="7" fill="{t['danger']}"/>
  <text x="80" y="79" fill="{t['danger']}" font-size="12" font-weight="900" font-family="Montserrat">REC</text>
  <text x="490" y="79" fill="{t['text_dim']}" font-size="11" font-family="Montserrat" text-anchor="end">4K RAW · 24FPS</text>
  {badge(185, 470, name, t['accent'], t['bg'], 180, 28)}
"""

    else:
        # General Composition Geometry Archetype (Clean Geometric Swiss Vectors)
        inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="6"/>
  <!-- Geometric Diagonals and Symmetry Axes -->
  <line x1="50" y1="60" x2="500" y2="560" stroke="{t['guide']}" stroke-width="1.2" stroke-dasharray="6,4"/>
  <line x1="500" y1="60" x2="50" y2="560" stroke="{t['guide']}" stroke-width="1.2" stroke-dasharray="6,4"/>
  <line x1="275" y1="60" x2="275" y2="560" stroke="{t['accent_alt']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <line x1="50" y1="310" x2="500" y2="310" stroke="{t['accent_alt']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <!-- Primary Geometric Field -->
  <polygon points="275,130 440,310 275,490 110,310" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5"/>
  <!-- Focal Node Center -->
  {focal_point(275, 310, 24, t['accent'], crosshair=True)}
  <!-- Subtitle Meta -->
  <text x="275" y="240" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:24]}</text>
  {badge(185, 510, name, t['accent'], t['bg'], 180, 28)}
"""

    return wrap_svg(inner, t['bg'])

def get_svg_for_layout(layout_id):
    """
    Returns high-fidelity SVG string for any layout ID (001-350).
    Prioritizes bespoke handcrafted SVGs, falls back to intelligent procedural generator.
    """
    lid = str(layout_id).zfill(3)

    # 1. Dedicated handcrafted function
    if lid in BESPOKE_MAP:
        return BESPOKE_MAP[lid]()

    # 2. Check if already generated in data/svgs/{lid}.svg
    svg_file = BASE_DIR / "data" / "svgs" / f"{lid}.svg"
    if svg_file.exists():
        content = svg_file.read_text(encoding="utf-8").strip()
        if content and "<svg" in content:
            return content

    # 3. Load layout JSON data and synthesize procedurally
    json_path = LAYOUTS_DIR / f"{lid}.json"
    if json_path.exists():
        data = json.loads(json_path.read_text(encoding="utf-8"))
        return synthesize_procedural_svg(lid, data)

    # Fallback dummy data
    return synthesize_procedural_svg(lid, {"name": f"构图 #{lid}", "name_en": f"COMPOSITION #{lid}"})


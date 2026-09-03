#!/usr/bin/env python3
"""
350 Layout Card Renderer (Upgraded)
Compiles structured layout metadata and optional AI artwork into high-fidelity 1086x1448 Swiss posters.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"
TEMPLATES_DIR = BASE_DIR / "templates"
LAYOUTS_DIR = DATA_DIR / "layouts"
MASTER_TEMPLATE = TEMPLATES_DIR / "card-master.html"


def get_default_svg(layout_id, name, theme):
    """Generates clean parametric SVG geometry based on composition rule."""
    if layout_id == "001":
        # Rule of Thirds SVG with mountains & sun
        return """
        <svg viewBox="0 0 530 690" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="sunGlow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#E03E2D" stop-opacity="0.35"/>
              <stop offset="100%" stop-color="#E03E2D" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="530" height="690" fill="#F8F6EF" />
          <polygon points="0,690 120,490 280,690" fill="#2E3036" />
          <polygon points="100,690 240,430 380,690" fill="#4B4E58" opacity="0.9" />
          <polygon points="220,690 340,540 460,690" fill="#6B707B" opacity="0.75" />
          <path d="M 20 620 Q 80 625 140 620 T 260 620 T 380 620 T 500 620" stroke="#E03E2D" stroke-width="1.2" fill="none" opacity="0.4" />
          <path d="M 50 645 Q 110 650 170 645 T 290 645 T 410 645 T 510 645" stroke="#E03E2D" stroke-width="1.2" fill="none" opacity="0.3" />
          <line x1="176.67" y1="0" x2="176.67" y2="690" stroke="#E03E2D" stroke-width="1.6" stroke-dasharray="6,6" opacity="0.8" />
          <line x1="353.33" y1="0" x2="353.33" y2="690" stroke="#E03E2D" stroke-width="1.6" stroke-dasharray="6,6" opacity="0.8" />
          <line x1="0" y1="230" x2="530" y2="230" stroke="#E03E2D" stroke-width="1.6" stroke-dasharray="6,6" opacity="0.8" />
          <line x1="0" y1="460" x2="530" y2="460" stroke="#E03E2D" stroke-width="1.6" stroke-dasharray="6,6" opacity="0.8" />
          <circle cx="353.33" cy="230" r="7" fill="#E03E2D" />
          <circle cx="176.67" cy="460" r="7" fill="#E03E2D" />
          <circle cx="353.33" cy="460" r="7" fill="#E03E2D" />
          <circle cx="176.67" cy="230" r="64" fill="url(#sunGlow)" />
          <circle cx="176.67" cy="230" r="44" stroke="#E03E2D" stroke-width="1" fill="none" stroke-dasharray="4,4" opacity="0.6" />
          <circle cx="176.67" cy="230" r="18" fill="#E03E2D" />
          <line x1="176.67" y1="206" x2="176.67" y2="254" stroke="#FFFFFF" stroke-width="1.5" />
          <line x1="152.67" y1="230" x2="200.67" y2="230" stroke="#FFFFFF" stroke-width="1.5" />
          <rect x="38" y="140" width="124" height="32" rx="6" fill="#1A1A1A" />
          <text x="100" y="161" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="PingFang SC" text-anchor="middle">视觉焦点 · 主体</text>
        </svg>
        """
    elif layout_id == "004":
        # Golden Triangle SVG with sailboat & mountain peaks
        return """
        <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="sunGold" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#FFD000" stop-opacity="0.8"/>
              <stop offset="40%" stop-color="#FFD000" stop-opacity="0.25"/>
              <stop offset="100%" stop-color="#FFD000" stop-opacity="0"/>
            </radialGradient>
            <linearGradient id="mountGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#8BB6F9"/>
              <stop offset="100%" stop-color="#1B428A"/>
            </linearGradient>
          </defs>
          <rect width="550" height="620" fill="#071E4D"/>
          <line x1="0" y1="520" x2="550" y2="520" stroke="#1C448D" stroke-width="1.5" />
          <line x1="20" y1="550" x2="530" y2="550" stroke="#1C448D" stroke-width="1.2" stroke-dasharray="8,8" />
          <polygon points="120,530 260,330 400,530" fill="#133674" />
          <polygon points="40,530 180,380 320,530" fill="url(#mountGrad)" opacity="0.9" />
          <polygon points="140,430 180,380 220,430" fill="#FFFFFF" opacity="0.9" />
          <polygon points="200,530 330,280 460,530" fill="#3A6EC7" />
          <polygon points="280,360 330,280 375,360" fill="#FFFFFF" />
          <g transform="translate(380, 460)">
            <polygon points="20,0 20,-48 44,0" fill="#FFFFFF"/>
            <polygon points="16,0 16,-40 -2,0" fill="#D6E4FF"/>
            <polygon points="-8,3 48,3 38,12 2,12" fill="#FFD000"/>
          </g>
          <line x1="30" y1="530" x2="480" y2="90" stroke="#FFD000" stroke-width="3.5" stroke-linecap="round"/>
          <polygon points="480,90 462,108 478,114" fill="#FFD000"/>
          <line x1="480" y1="530" x2="365" y2="205" stroke="#FFD000" stroke-width="3" stroke-linecap="round"/>
          <rect x="30" y="90" width="450" height="440" stroke="rgba(255, 208, 0, 0.4)" stroke-width="1.2" stroke-dasharray="4,4" fill="none"/>
          <circle cx="365" cy="205" r="64" fill="url(#sunGold)"/>
          <circle cx="365" cy="205" r="22" stroke="#FFFFFF" stroke-width="2" fill="#FFFFFF"/>
          <line x1="365" y1="180" x2="365" y2="230" stroke="#0B2B68" stroke-width="2"/>
          <line x1="340" y1="205" x2="390" y2="205" stroke="#0B2B68" stroke-width="2"/>
          <text x="140" y="290" fill="#FFD000" font-size="12" font-weight="600" font-family="PingFang SC" transform="rotate(-44 140 290)">
            主对角动态引导线 · 牵引视线自下而上
          </text>
        </svg>
        """
    elif layout_id == "134":
        # Multi-Column Layout Swiss Editorial Grid Vector
        return """
        <svg viewBox="0 0 530 660" xmlns="http://www.w3.org/2000/svg">
          <rect width="530" height="660" fill="#09241C" rx="6"/>
          <!-- Column 1 -->
          <rect x="40" y="60" width="130" height="400" rx="4" fill="none" stroke="#D4E751" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
          <rect x="48" y="70" width="114" height="60" rx="4" fill="#D4E751" opacity="0.25"/>
          <line x1="48" y1="150" x2="162" y2="150" stroke="#FFFFFF" stroke-width="3"/>
          <line x1="48" y1="165" x2="140" y2="165" stroke="#A3B8AD" stroke-width="2"/>
          <line x1="48" y1="178" x2="155" y2="178" stroke="#A3B8AD" stroke-width="2"/>
          <line x1="48" y1="191" x2="130" y2="191" stroke="#A3B8AD" stroke-width="2"/>

          <!-- Column 2 (Spanning) -->
          <rect x="195" y="60" width="130" height="400" rx="4" fill="none" stroke="#D4E751" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
          <rect x="203" y="70" width="270" height="140" rx="4" fill="#D4E751" opacity="0.35"/>
          <text x="338" y="145" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">SPANNED HERO</text>
          
          <!-- Column 3 -->
          <rect x="350" y="60" width="130" height="400" rx="4" fill="none" stroke="#D4E751" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
          <line x1="358" y1="230" x2="472" y2="230" stroke="#FFFFFF" stroke-width="3"/>
          <line x1="358" y1="245" x2="450" y2="245" stroke="#A3B8AD" stroke-width="2"/>
          <line x1="358" y1="258" x2="465" y2="258" stroke="#A3B8AD" stroke-width="2"/>

          <!-- Gutter dimension brackets -->
          <line x1="170" y1="480" x2="195" y2="480" stroke="#D4E751" stroke-width="1.5"/>
          <text x="182" y="475" fill="#D4E751" font-size="10" font-weight="bold" font-family="Montserrat" text-anchor="middle">GUTTER</text>

          <!-- Reading path curve -->
          <path d="M 105 100 Q 260 90 338 140 T 105 280 T 260 320 T 415 320" fill="none" stroke="#D4E751" stroke-width="2.5" stroke-dasharray="6,4"/>
          <polygon points="423,320 412,314 412,326" fill="#D4E751"/>
          
          <text x="265" y="550" fill="#D4E751" font-size="15" font-weight="bold" font-family="PingFang SC" text-anchor="middle">
            多栏网格骨架 (Multi-Column Grid Architecture)
          </text>
          <text x="265" y="575" fill="#A3B8AD" font-size="12" font-family="Montserrat" text-anchor="middle">
            EQUAL COLUMNS · 25px GUTTER · HIERARCHICAL SPANNING
          </text>
        </svg>
        """
    else:
        # Parametric Grid Wireframe
        accent_color = "#FFD700" if theme in ["obsidian-black", "forest-green"] else "#E03E2D"
        return f"""
        <svg viewBox="0 0 530 650" xmlns="http://www.w3.org/2000/svg">
          <rect width="530" height="650" fill="none" />
          <rect x="30" y="40" width="470" height="570" stroke="{accent_color}" stroke-width="2" fill="none" opacity="0.6"/>
          <line x1="30" y1="392" x2="500" y2="392" stroke="{accent_color}" stroke-width="1.5" stroke-dasharray="6,6"/>
          <line x1="321" y1="40" x2="321" y2="610" stroke="{accent_color}" stroke-width="1.5" stroke-dasharray="6,6"/>
          <circle cx="321" cy="392" r="16" fill="{accent_color}" />
          <circle cx="321" cy="392" r="32" stroke="{accent_color}" stroke-width="1" fill="none" stroke-dasharray="4,4"/>
          <text x="265" y="325" fill="{accent_color}" font-size="18" font-weight="bold" font-family="PingFang SC" text-anchor="middle">{name}</text>
          <text x="265" y="350" fill="currentColor" font-size="12" font-family="Montserrat" text-anchor="middle" opacity="0.7">COMPOSITION SCHEMATIC</text>
        </svg>
        """


def load_card_data(layout_id):
    """Loads card data from JSON or falls back to catalog index."""
    json_file = LAYOUTS_DIR / f"{layout_id}.json"
    if json_file.exists():
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)

    # Fallback to catalog.json
    catalog_file = DATA_DIR / "catalog.json"
    if catalog_file.exists():
        with open(catalog_file, "r", encoding="utf-8") as f:
            catalog = json.load(f)
            for item in catalog:
                if item["id"].zfill(3) == layout_id.zfill(3):
                    from compile_prompt import compile_layout_data
                    return compile_layout_data(item)
    return None


def render_card(layout_id, output_dir=None, theme=None, output_format="both", image_path=None):
    layout_id = str(layout_id).zfill(3)
    data = load_card_data(layout_id)
    if not data:
        print(f"Error: Could not load layout {layout_id}")
        return None, None

    if not output_dir:
        output_dir = BASE_DIR / "dist"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    theme = theme or data.get("theme", "warm-ivory")
    columns_ratio = data.get("columns_ratio", "530px 380px")

    with open(MASTER_TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    # Check for custom image
    resolved_img = None
    if image_path and os.path.exists(image_path):
        resolved_img = Path(image_path).resolve()
    else:
        for candidate in [
            ASSETS_DIR / f"{layout_id}_landscape.png",
            ASSETS_DIR / f"{layout_id}_artwork.png",
            BASE_DIR / f"{layout_id}_full.png"
        ]:
            if candidate.exists():
                resolved_img = candidate.resolve()
                break

    if resolved_img:
        svg_content = f"""
        <div style="position: relative; width: 100%; height: 100%; border-radius: 6px; overflow: hidden; border: 1px solid rgba(212, 231, 81, 0.25);">
          <img src="file://{resolved_img}" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
          <svg viewBox="0 0 530 660" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;">
            <line x1="0" y1="120" x2="270" y2="120" stroke="#D4E751" stroke-width="2" stroke-dasharray="5,4" />
            <circle cx="270" cy="120" r="14" fill="rgba(212,231,81,0.3)" />
            <circle cx="270" cy="120" r="6" fill="none" stroke="#D4E751" stroke-width="2" />
            <circle cx="270" cy="120" r="2.5" fill="#D4E751" />

            <line x1="0" y1="365" x2="230" y2="365" stroke="#D4E751" stroke-width="2" stroke-dasharray="5,4" />
            <circle cx="230" cy="365" r="14" fill="rgba(212,231,81,0.3)" />
            <circle cx="230" cy="365" r="6" fill="none" stroke="#D4E751" stroke-width="2" />
            <circle cx="230" cy="365" r="2.5" fill="#D4E751" />

            <line x1="0" y1="580" x2="245" y2="580" stroke="#D4E751" stroke-width="2" stroke-dasharray="5,4" />
            <circle cx="245" cy="580" r="14" fill="rgba(212,231,81,0.3)" />
            <circle cx="245" cy="580" r="6" fill="none" stroke="#D4E751" stroke-width="2" />
            <circle cx="245" cy="580" r="2.5" fill="#D4E751" />
          </svg>
        </div>
        """
    else:
        svg_content = get_default_svg(layout_id, data["name"], theme)

    # Build Features HTML
    features_html = '<div class="feature-list">'
    for feat in data.get("features", []):
        features_html += f"""
        <div class="feature-card">
          <div class="feature-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <line x1="12" y1="8" x2="12" y2="12"/>
              <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
          </div>
          <div class="feature-text">
            <div class="feature-title-row">
              <span class="feature-title">{feat['title']}</span>
              <span class="feature-tag">{feat.get('title_en', '').upper()}</span>
            </div>
            <p class="feature-desc">{feat['desc']}</p>
          </div>
        </div>
        """
    features_html += '</div>'

    # Build Tips HTML
    tips_html = """
    <div class="tips-card">
      <div class="tips-header">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
          <path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"></path>
          <path d="M9 18h6"></path>
          <path d="M10 22h4"></path>
        </svg>
        <span>实战应用建议 (TIPS)</span>
      </div>
      <ul class="tips-list">
    """
    for tip in data.get("tips", []):
        tips_html += f"<li><strong>{tip['label']}：</strong>{tip['content']}</li>"
    tips_html += '<div class="tips-bottom-bar"></div></ul></div>'

    # Assemble Main Content HTML
    columns_ratio = "600px 345px" if not columns_ratio.startswith("3") else "345px 600px"
    if columns_ratio.startswith("345px"):
        main_content_html = f"""
        <div class="feature-column">{features_html}{tips_html}</div>
        <div class="visual-box">{svg_content}</div>
        """
    else:
        main_content_html = f"""
        <div class="visual-box">{svg_content}</div>
        <div class="feature-column">{features_html}{tips_html}</div>
        """

    # Build Keywords HTML
    keywords_html = ""
    for kw in data.get("keywords", []):
        keywords_html += f"""
        <div class="kw-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="8"/>
          </svg>
          <div class="kw-text">
            <span class="kw-cn">{kw['name']}</span>
            <span class="kw-en">{kw.get('name_en', '').upper()}</span>
          </div>
        </div>
        """

    compiled_html = template
    replacements = {
      "{{THEME}}": theme,
      "{{CARD_ID}}": data["id"],
      "{{TITLE}}": data["name"],
      "{{SUBTITLE_EN}}": data["name_en"],
      "{{CATEGORY}}": data["category"].split(" / ")[0] if " / " in data["category"] else data["category"],
      "{{CATEGORY_EN}}": "COMPOSITION PRINCIPLES",
      "{{TAGLINE}}": data.get("tagline", "用严谨的设计原则，构建画面的力量。"),
      "{{DESCRIPTION}}": data["description"],
      "{{COLUMNS_RATIO}}": columns_ratio,
      "{{MAIN_CONTENT_HTML}}": main_content_html,
      "{{KEYWORDS_HTML}}": keywords_html
    }

    for k, v in replacements.items():
        compiled_html = compiled_html.replace(k, v)

    html_file = output_dir / f"{data['id']}_{data['name']}.html"
    png_file = output_dir / f"{data['id']}_{data['name']}.png"

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(compiled_html)
    print(f"✓ Compiled HTML: {html_file}")

    if output_format in ["png", "both"]:
        chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(chrome_bin):
            import tempfile, shutil
            tmp_user_dir = tempfile.mkdtemp(prefix="chrome_render_")
            cmd = [
                chrome_bin,
                "--headless",
                "--disable-gpu",
                f"--user-data-dir={tmp_user_dir}",
                f"--screenshot={png_file}",
                "--window-size=1086,1448",
                f"file://{html_file.resolve()}"
            ]
            try:
                subprocess.run(cmd, timeout=15, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"✓ Rendered PNG: {png_file} (1086x1448)")
            except Exception as e:
                print(f"! Warning: Failed to render PNG with Chrome: {e}")
            finally:
                shutil.rmtree(tmp_user_dir, ignore_errors=True)
        else:
            print("! Chrome not found, skipping PNG export.")

    return html_file, png_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render 350 Layout Composition Card")
    parser.add_argument("--id", type=str, default="001", help="Layout ID (e.g. 001)")
    parser.add_argument("--theme", type=str, default=None, choices=["warm-ivory", "forest-green", "obsidian-black", "cobalt-blue"], help="Color theme override")
    parser.add_argument("--output", type=str, default=str(BASE_DIR / "dist"), help="Output directory")
    parser.add_argument("--format", type=str, default="both", choices=["html", "png", "both"], help="Output format")
    parser.add_argument("--image", type=str, default=None, help="Custom illustration/photo path to embed")
    args = parser.parse_args()

    render_card(args.id.zfill(3), args.output, args.theme, args.format, args.image)

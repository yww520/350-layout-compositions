#!/usr/bin/env python3
"""
350 Layout Card Renderer (Standard Swiss Master Quality)
Compiles layout metadata and bespoke vector illustrations into high-fidelity 1086x1448 Swiss posters.
"""

import argparse
import base64
import json
import os
import subprocess
import sys
import tempfile
import shutil
import time
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
TEMPLATES_DIR = BASE_DIR / "templates"
LAYOUTS_DIR = DATA_DIR / "layouts"
MASTER_TEMPLATE = TEMPLATES_DIR / "card-master.html"
SVGS_DIR = DATA_DIR / "svgs"
ASSETS_DIR = BASE_DIR / "assets"
ILLUSTRATIONS_DIR = ASSETS_DIR / "illustrations"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import svg_library


def format_image_element(img_path, name=""):
    """Format an image into a self-contained base64 data URI HTML element."""
    img_path = Path(img_path).resolve()
    try:
        suffix = img_path.suffix.lower().lstrip(".")
        mime_type = "image/jpeg" if suffix in ["jpg", "jpeg"] else f"image/{suffix}"
        with open(img_path, "rb") as f:
            b64_data = base64.b64encode(f.read()).decode("utf-8")
        return f'<img src="data:{mime_type};base64,{b64_data}" alt="{name}" style="width:100%;height:100%;object-fit:cover;display:block;border-radius:12px;" />'
    except Exception as e:
        return f'<img src="file://{img_path}" alt="{name}" style="width:100%;height:100%;object-fit:cover;display:block;border-radius:12px;" />'


def get_default_svg(layout_id, name, theme, image_path=None):
    """
    Multi-tier visual resolution:
    1. Explicit image_path passed to renderer
    2. External SVG file in data/svgs/{layout_id}.svg
    3. External illustration in assets/illustrations/{layout_id}.{png,jpg,jpeg,webp}
    4. Bespoke SVG from svg_library.py
    5. Fallback parametric grid
    """
    layout_id = str(layout_id).zfill(3)

    # 1. Explicit image_path override
    if image_path:
        img_p = Path(image_path)
        if img_p.exists():
            return format_image_element(img_p, name)

    # 2. External SVG file (data/svgs/{layout_id}.svg)
    svg_file = SVGS_DIR / f"{layout_id}.svg"
    if svg_file.exists():
        try:
            return svg_file.read_text(encoding="utf-8").strip()
        except Exception as e:
            print(f"! Warning: Failed to read {svg_file}: {e}")

    # 3. External illustration file (assets/illustrations/{layout_id}.ext)
    for ext in ["png", "jpg", "jpeg", "webp"]:
        illu_file = ILLUSTRATIONS_DIR / f"{layout_id}.{ext}"
        if illu_file.exists():
            return format_image_element(illu_file, name)

    # 4. Bespoke library function
    bespoke = svg_library.get_bespoke_svg(layout_id)
    if bespoke:
        return bespoke

    # 5. Fallback to intelligent procedural SVG engine
    try:
        from scripts.svg_generators.procedural_engine import get_svg_for_layout
        return get_svg_for_layout(layout_id)
    except Exception as e:
        print(f"! Warning: Procedural SVG generation failed: {e}")
        accent_color = "#FFD700" if theme in ["obsidian-black", "forest-green"] else "#E03E2D"
        return f"""
        <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
          <rect width="550" height="620" fill="none" />
          <rect x="35" y="45" width="480" height="530" stroke="{accent_color}" stroke-width="2" fill="none" opacity="0.7"/>
          <line x1="35" y1="372" x2="515" y2="372" stroke="{accent_color}" stroke-width="1.8" stroke-dasharray="6,6"/>
          <line x1="331" y1="45" x2="331" y2="575" stroke="{accent_color}" stroke-width="1.8" stroke-dasharray="6,6"/>
          <circle cx="331" cy="372" r="18" fill="{accent_color}" />
          <text x="275" y="300" fill="{accent_color}" font-size="20" font-weight="900" font-family="PingFang SC" text-anchor="middle">{name}</text>
        </svg>
        """


def load_card_data(layout_id):
    json_file = LAYOUTS_DIR / f"{layout_id}.json"
    if json_file.exists():
        with open(json_file, "r", encoding="utf-8") as f:
            return json.load(f)
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

    theme = theme or data.get("theme", "forest-green")
    columns_ratio = data.get("columns_ratio", "345px 600px")

    with open(MASTER_TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    # Visual box content: prioritize bespoke SVG or cropped landscape image
    svg_content = get_default_svg(layout_id, data["name"], theme, image_path=image_path)

    # Build Features HTML (Restoring the 004 exact format: feature-row + feature-icon-circle)
    features_html = '<div class="feature-list">'
    for feat in data.get("features", []):
        features_html += f"""
        <div class="feature-row">
          <div class="feature-icon-circle">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3">
              <circle cx="12" cy="12" r="7"/>
              <circle cx="12" cy="12" r="2" fill="currentColor"/>
              <line x1="12" y1="2" x2="12" y2="5"/>
              <line x1="12" y1="19" x2="12" y2="22"/>
              <line x1="2" y1="12" x2="5" y2="12"/>
              <line x1="19" y1="12" x2="22" y2="12"/>
            </svg>
          </div>
          <div class="feature-text-block">
            <div class="feature-title">{feat['title']}</div>
            <div class="feature-desc">{feat['desc']}</div>
            <div class="feature-tag-en">{feat.get('title_en', '')}</div>
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
        <span>应用建议</span>
      </div>
      <ul class="tips-list">
    """
    for tip in data.get("tips", []):
        tips_html += f"<li><strong>{tip['label']}：</strong>{tip['content']}</li>"
    tips_html += '<div class="tips-bottom-bar"></div></ul></div>'

    # Assemble Main Content HTML
    main_content_html = f"""
    <div class="feature-column">{features_html}{tips_html}</div>
    <div class="visual-box">{svg_content}</div>
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
            tmp_user_dir = tempfile.mkdtemp(prefix="chrome_render_")
            cmd = [
                chrome_bin,
                "--headless=new",
                "--disable-gpu",
                "--no-first-run",
                "--no-default-browser-check",
                "--disable-background-networking",
                "--disable-sync",
                "--disable-extensions",
                f"--user-data-dir={tmp_user_dir}",
                f"--screenshot={png_file}",
                "--window-size=1086,1448",
                f"file://{html_file.resolve()}"
            ]
            try:
                if png_file.exists():
                    try:
                        png_file.unlink()
                    except Exception:
                        pass
                # Launch Chrome headless and poll until screenshot file is generated
                proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                start_t = time.time()
                rendered_ok = False
                while time.time() - start_t < 15:
                    if png_file.exists() and png_file.stat().st_size > 50000:
                        rendered_ok = True
                        break
                    time.sleep(0.25)
                proc.terminate()
                try:
                    proc.wait(timeout=1.5)
                except Exception:
                    proc.kill()
                if rendered_ok:
                    print(f"✓ Rendered PNG: {png_file} (1086x1448)")
                else:
                    print(f"! Warning: Screenshot file not generated within timeout")
            except Exception as e:
                print(f"! Warning: Failed to render PNG with Chrome: {e}")
            finally:
                shutil.rmtree(tmp_user_dir, ignore_errors=True)
        else:
            print("! Chrome not found, skipping PNG export.")

    return html_file, png_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render 350 Layout Composition Card")
    parser.add_argument("--id", type=str, default="002", help="Layout ID (e.g. 002)")
    parser.add_argument("--theme", type=str, default=None, help="Color theme override")
    parser.add_argument("--output", type=str, default=str(BASE_DIR / "dist"), help="Output directory")
    parser.add_argument("--format", type=str, default="both", choices=["html", "png", "both"], help="Output format")
    parser.add_argument("--image", type=str, default=None, help="Custom illustration or bitmap image path")
    args = parser.parse_args()

    render_card(args.id.zfill(3), args.output, args.theme, args.format, image_path=args.image)

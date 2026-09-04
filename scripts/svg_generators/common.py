"""
Common utilities and constants for modular SVG generation in 350-layout series.
Strictly adheres to Swiss design aesthetics:
- ViewBox: 0 0 550 620
- High-contrast background canvases
- Precise vector geometry, guides, annotations, and focal anchors
"""

THEMES = {
    "obsidian-black": {
        "bg": "#12141A",
        "bg_surface": "#1A1D26",
        "accent": "#FFD700",
        "accent_alt": "#00E5FF",
        "danger": "#FF3D00",
        "text": "#FFFFFF",
        "text_dim": "#718096",
        "guide": "#333C4E",
        "stroke": "#4A5568",
    },
    "forest-green": {
        "bg": "#082018",
        "bg_surface": "#0E2D23",
        "accent": "#D4E751",
        "accent_alt": "#26A69A",
        "danger": "#FF7043",
        "text": "#FFFFFF",
        "text_dim": "#80988E",
        "guide": "#163E32",
        "stroke": "#285848",
    },
    "warm-ivory": {
        "bg": "#1F1B18",
        "bg_surface": "#2B2622",
        "accent": "#E25238",
        "accent_alt": "#FFB300",
        "danger": "#D32F2F",
        "text": "#FAF7F2",
        "text_dim": "#8A827A",
        "guide": "#3B342F",
        "stroke": "#524A44",
    },
    "cobalt-blue": {
        "bg": "#081630",
        "bg_surface": "#0E2248",
        "accent": "#448AFF",
        "accent_alt": "#00E5FF",
        "danger": "#FF5252",
        "text": "#FFFFFF",
        "text_dim": "#7C92B5",
        "guide": "#162E58",
        "stroke": "#2A4B82",
    },
}

def get_theme(theme_name=None):
    if theme_name in THEMES:
        return THEMES[theme_name]
    return THEMES["obsidian-black"]

def wrap_svg(inner_content, bg="#12141A", defs=""):
    defs_block = f"<defs>\n{defs}\n</defs>" if defs else ""
    return f"""<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
{defs_block}
  <rect width="550" height="620" fill="{bg}" rx="8"/>
{inner_content}
</svg>"""

def focal_point(cx, cy, r=16, color="#FFD700", glow_id=None, crosshair=True):
    res = []
    if glow_id:
        res.append(f'  <circle cx="{cx}" cy="{cy}" r="{r*3.5}" fill="url(#{glow_id})"/>')
    res.append(f'  <circle cx="{cx}" cy="{cy}" r="{r*1.8}" fill="none" stroke="{color}" stroke-width="1.2" stroke-dasharray="4,3" opacity="0.7"/>')
    res.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>')
    res.append(f'  <circle cx="{cx}" cy="{cy}" r="{max(3, int(r*0.25))}" fill="#FFFFFF"/>')
    if crosshair:
        l = r * 2.4
        res.append(f'  <line x1="{cx-l}" y1="{cy}" x2="{cx+l}" y2="{cy}" stroke="{color}" stroke-width="1.2" stroke-dasharray="2,2" opacity="0.6"/>')
        res.append(f'  <line x1="{cx}" y1="{cy-l}" x2="{cx}" y2="{cy+l}" stroke="{color}" stroke-width="1.2" stroke-dasharray="2,2" opacity="0.6"/>')
    return "\n".join(res)

def badge(x, y, text, bg="#FFD700", text_color="#12141A", w=160, h=30, rx=5, font_size=11):
    return f"""  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg}"/>
  <text x="{x + w/2}" y="{y + h*0.62}" fill="{text_color}" font-size="{font_size}" font-weight="900" font-family="PingFang SC, -apple-system, sans-serif" text-anchor="middle">{text}</text>"""

def dimension_h(x1, x2, y, label, color="#718096", text_color="#FFFFFF"):
    mid = (x1 + x2) / 2
    return f"""  <line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="1.2"/>
  <line x1="{x1}" y1="{y-5}" x2="{x1}" y2="{y+5}" stroke="{color}" stroke-width="1.2"/>
  <line x1="{x2}" y1="{y-5}" x2="{x2}" y2="{y+5}" stroke="{color}" stroke-width="1.2"/>
  <rect x="{mid-24}" y="{y-9}" width="48" height="18" fill="#12141A" rx="3"/>
  <text x="{mid}" y="{y+4}" fill="{text_color}" font-size="10" font-weight="bold" font-family="Montserrat, monospace" text-anchor="middle">{label}</text>"""

def dimension_v(y1, y2, x, label, color="#718096", text_color="#FFFFFF"):
    mid = (y1 + y2) / 2
    return f"""  <line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1.2"/>
  <line x1="{x-5}" y1="{y1}" x2="{x+5}" y2="{y1}" stroke="{color}" stroke-width="1.2"/>
  <line x1="{x-5}" y1="{y2}" x2="{x+5}" y2="{y2}" stroke="{color}" stroke-width="1.2"/>
  <rect x="{x-24}" y="{mid-9}" width="48" height="18" fill="#12141A" rx="3"/>
  <text x="{x}" y="{mid+4}" fill="{text_color}" font-size="10" font-weight="bold" font-family="Montserrat, monospace" text-anchor="middle">{label}</text>"""


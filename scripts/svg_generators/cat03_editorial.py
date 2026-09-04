"""
SVG generators for Category 03: 出版与编辑版式 (132-167).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_132(): # 单栏经典版式 (Single Column Classical)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Classical Book Margins (Tschichold Canon 2:3:4:6) -->
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <!-- Elegant Centered Text Block -->
  <rect x="130" y="110" width="290" height="380" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5" rx="3"/>
  <!-- Simulated Text Lines -->
  <g fill="{t['text_dim']}">
    <rect x="150" y="140" width="250" height="8" rx="2" fill="{t['accent']}"/>
    <rect x="150" y="165" width="250" height="5" rx="1"/>
    <rect x="150" y="180" width="250" height="5" rx="1"/>
    <rect x="150" y="195" width="220" height="5" rx="1"/>
    <rect x="150" y="225" width="250" height="5" rx="1"/>
    <rect x="150" y="240" width="250" height="5" rx="1"/>
    <rect x="150" y="255" width="180" height="5" rx="1"/>
    <rect x="150" y="285" width="250" height="5" rx="1"/>
    <rect x="150" y="300" width="240" height="5" rx="1"/>
    <rect x="150" y="315" width="250" height="5" rx="1"/>
    <rect x="150" y="330" width="200" height="5" rx="1"/>
  </g>
  <!-- Classical Folio Page Number -->
  <text x="275" y="460" fill="{t['accent']}" font-size="12" font-family="Montserrat" text-anchor="middle">· 42 ·</text>
  {dimension_h(50, 130, 80, "INNER", t['accent'], t['accent'])}
  {dimension_h(420, 500, 80, "OUTER", t['accent'], t['accent'])}
  {badge(185, 520, "中世纪手抄本黄金比例", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_133(): # 双栏学术版式 (Two Column Academic)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <!-- Column 1 -->
  <rect x="90" y="120" width="165" height="380" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.2" rx="3"/>
  <!-- Column 2 -->
  <rect x="295" y="120" width="165" height="380" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.2" rx="3"/>
  <!-- Gutter Dimension -->
  {dimension_h(255, 295, 95, "40px", t['accent'], t['accent'])}
  <!-- Header Banner spanning both columns -->
  <rect x="90" y="80" width="370" height="24" fill="{t['accent']}" rx="3"/>
  <text x="275" y="97" fill="{t['bg']}" font-size="11" font-weight="900" font-family="Montserrat" text-anchor="middle">ACADEMIC TWO-COLUMN SPREAD</text>
  <!-- Column Text Simulation -->
  <g fill="{t['text_dim']}">
    <rect x="105" y="140" width="135" height="4" rx="1"/>
    <rect x="105" y="152" width="135" height="4" rx="1"/>
    <rect x="105" y="164" width="110" height="4" rx="1"/>
    <rect x="105" y="184" width="135" height="4" rx="1"/>
    <rect x="105" y="196" width="135" height="4" rx="1"/>
    <rect x="310" y="140" width="135" height="4" rx="1"/>
    <rect x="310" y="152" width="135" height="4" rx="1"/>
    <rect x="310" y="164" width="125" height="4" rx="1"/>
  </g>
  {badge(185, 520, "严谨双栏与中缝控制", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_138(): # 跨页全景 (Double Page Spread DPS)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Left Page -->
  <rect x="40" y="80" width="225" height="460" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Right Page -->
  <rect x="285" y="80" width="225" height="460" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Central Book Gutter / Seam -->
  <line x1="275" y1="50" x2="275" y2="570" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="275" y="40" fill="{t['danger']}" font-size="11" font-family="Montserrat" text-anchor="middle">GUTTER SEAM</text>
  <!-- Spanning Hero Panorama Banner crossing the spine -->
  <rect x="70" y="180" width="410" height="180" fill="{t['accent']}" opacity="0.85" rx="4"/>
  <circle cx="200" cy="270" r="32" fill="#FFFFFF"/>
  <circle cx="360" cy="270" r="45" fill="{t['accent_alt']}"/>
  <text x="275" y="390" fill="{t['text']}" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">跨页贯通大图全景</text>
  {badge(185, 480, "跨页连贯规避中缝", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_148(): # 俄国构成主义 (Russian Constructivism)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Dynamic Angled Constructivist Bars (El Lissitzky style) -->
  <g transform="rotate(-18 275 310)">
    <!-- Heavy Solid Black & Crimson Red Wedges -->
    <polygon points="50,200 450,140 450,240 50,280" fill="#FF3D00"/>
    <polygon points="120,290 520,230 520,360 120,400" fill="#FFFFFF"/>
    <polygon points="20,80 320,30 320,130 20,170" fill="#2A3040"/>
    <!-- Diagonal Slogan Typography -->
    <text x="250" y="220" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Montserrat">CONSTRUCTIVISM</text>
    <text x="320" y="310" fill="#000000" font-size="28" font-weight="900" font-family="Montserrat">1920 · BEAT THE WHITES</text>
    <circle cx="420" cy="180" r="26" fill="#000000"/>
    <circle cx="420" cy="180" r="10" fill="#FF3D00"/>
  </g>
  <!-- Red Star Graphic -->
  <polygon points="90,490 97,508 116,508 101,520 106,538 90,526 74,538 79,520 64,508 83,508" fill="#FF3D00"/>
  {badge(185, 80, "斜角红色楔形冲击", "#FF3D00", "#FFFFFF", 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_149(): # 瑞士国际主义 (Swiss Style Strict Grid)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Mathematical Strict 4-Column Asymmetrical Grid -->
  <g stroke="{t['accent']}" stroke-width="1.2" stroke-dasharray="4,4" opacity="0.6">
    <line x1="60" y1="50" x2="60" y2="570"/>
    <line x1="160" y1="50" x2="160" y2="570"/>
    <line x1="260" y1="50" x2="260" y2="570"/>
    <line x1="360" y1="50" x2="360" y2="570"/>
    <line x1="460" y1="50" x2="460" y2="570"/>
    <!-- Horizontal Modules -->
    <line x1="60" y1="120" x2="460" y2="120"/>
    <line x1="60" y1="230" x2="460" y2="230"/>
    <line x1="60" y1="340" x2="460" y2="340"/>
    <line x1="60" y1="450" x2="460" y2="450"/>
  </g>
  <!-- Helvetica Asymmetric Bold Block -->
  <rect x="160" y="120" width="200" height="110" fill="{t['accent']}"/>
  <text x="180" y="175" fill="#FFFFFF" font-size="28" font-weight="900" font-family="Helvetica, Arial, sans-serif">ZÜRICH</text>
  <text x="180" y="205" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Helvetica, Arial, sans-serif">1957 · SWISS TYPOGRAPHY</text>
  <!-- Asymmetric Secondary Anchor -->
  <rect x="260" y="340" width="100" height="110" fill="{t['danger']}"/>
  <circle cx="310" cy="395" r="16" fill="#FFFFFF"/>
  {badge(185, 520, "理性客观网格法则", t['accent'], t['text'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_153(): # 便当网格模块 (Bento Grid Module)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Asymmetric Bento Box Cards (Apple / Modern Web standard) -->
  <!-- Box 1: Hero Large Card (Top Left) -->
  <rect x="50" y="70" width="270" height="220" rx="16" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="80" y="100" width="40" height="40" rx="8" fill="{t['accent']}"/>
  <text x="80" y="180" fill="#FFFFFF" font-size="18" font-weight="900" font-family="Montserrat">CORE STAT</text>
  <text x="80" y="210" fill="{t['text_dim']}" font-size="12" font-family="Montserrat">99.8% Efficiency</text>
  <!-- Box 2: Tall Vertical Card (Right) -->
  <rect x="340" y="70" width="160" height="350" rx="16" fill="{t['accent']}" opacity="0.9"/>
  <circle cx="420" cy="150" r="34" fill="#FFFFFF"/>
  <text x="420" y="260" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">INTEGRATION</text>
  <!-- Box 3: Small Card (Bottom Left A) -->
  <rect x="50" y="310" width="125" height="180" rx="16" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="112" cy="370" r="20" fill="{t['danger']}"/>
  <!-- Box 4: Small Card (Bottom Left B) -->
  <rect x="195" y="310" width="125" height="180" rx="16" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="257" cy="370" r="20" fill="{t['accent_alt']}"/>
  <!-- Box 5: Wide Bottom Span -->
  <rect x="50" y="510" width="450" height="60" rx="14" fill="{t['stroke']}"/>
  {badge(185, 525, "便当盒模块化容器", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_154(): # 圣杯三栏版式 (Holy Grail 3-Box)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Holy Grail Layout Wireframe -->
  <!-- 1. Header (Span 100%) -->
  <rect x="50" y="60" width="450" height="60" rx="6" fill="{t['accent']}"/>
  <text x="275" y="96" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">HEADER · FULL SPAN</text>
  <!-- 2. Left Nav Sidebar -->
  <rect x="50" y="140" width="95" height="320" rx="6" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="97" y="290" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">NAV</text>
  <!-- 3. Center Main Body Content (Fluid Flexible) -->
  <rect x="160" y="140" width="230" height="320" rx="6" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="275" cy="240" r="36" fill="{t['accent_alt']}"/>
  <text x="275" y="310" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">MAIN CONTENT</text>
  <!-- 4. Right Aside Sidebar -->
  <rect x="405" y="140" width="95" height="320" rx="6" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="452" y="290" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">ASIDE</text>
  <!-- 5. Footer (Span 100%) -->
  <rect x="50" y="480" width="450" height="60" rx="6" fill="{t['stroke']}"/>
  <text x="275" y="515" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">FOOTER</text>
  {badge(185, 410, "经典圣杯三栏骨架", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_160(): # 扉页仪式感 (Book Title Page)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="60" y="60" width="430" height="500" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="4"/>
  <!-- Elegant Thin Double Border Rule -->
  <rect x="75" y="75" width="400" height="470" fill="none" stroke="{t['accent']}" stroke-width="0.8" stroke-dasharray="4,2"/>
  <!-- Subtitle -->
  <text x="275" y="150" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle" letter-spacing="4">ESSAYS ON ARCHITECTURE</text>
  <!-- Monumental Title -->
  <text x="275" y="230" fill="{t['accent']}" font-size="36" font-weight="900" font-family="Georgia, serif" text-anchor="middle">MODULOR</text>
  <!-- Author / Signature Rule -->
  <line x1="210" y1="265" x2="340" y2="265" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="275" y="300" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Georgia, serif" text-anchor="middle">LE CORBUSIER</text>
  <!-- Printer / Publisher Imprint Mark -->
  <circle cx="275" cy="420" r="28" fill="none" stroke="{t['accent']}" stroke-width="1.5"/>
  <polygon points="275,405 285,425 265,425" fill="{t['accent']}"/>
  <text x="275" y="475" fill="{t['text_dim']}" font-size="10" font-family="Montserrat" text-anchor="middle">PARIS · MCML</text>
  {badge(185, 520, "典籍扉页仪式秩序", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat03
CAT03_SVGS = {
    "132": gen_132, "133": gen_133, "138": gen_138, "148": gen_148, "149": gen_149,
    "153": gen_153, "154": gen_154, "160": gen_160
}


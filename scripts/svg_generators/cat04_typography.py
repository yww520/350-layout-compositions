"""
SVG generators for Category 04: 字体与网格系统 (168-221).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_170(): # 模块化网格 (Modular Grid Matrix)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- 4x5 Modular Grid Matrix -->
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <!-- Module Cells -->
  <g fill="none" stroke="{t['accent']}" stroke-width="1.2">
    <!-- Row 1 -->
    <rect x="70" y="80" width="85" height="75" rx="3"/>
    <rect x="175" y="80" width="85" height="75" rx="3"/>
    <rect x="280" y="80" width="85" height="75" rx="3"/>
    <rect x="385" y="80" width="85" height="75" rx="3"/>
    <!-- Row 2 (Spanned Cell) -->
    <rect x="70" y="175" width="190" height="170" rx="4" fill="{t['accent']}" fill-opacity="0.85"/>
    <rect x="280" y="175" width="85" height="75" rx="3"/>
    <rect x="385" y="175" width="85" height="75" rx="3"/>
    <!-- Row 3 -->
    <rect x="280" y="270" width="190" height="75" rx="4" fill="{t['danger']}"/>
    <!-- Row 4 -->
    <rect x="70" y="365" width="85" height="75" rx="3"/>
    <rect x="175" y="365" width="85" height="75" rx="3"/>
    <rect x="280" y="365" width="85" height="75" rx="3"/>
    <rect x="385" y="365" width="85" height="75" rx="3"/>
  </g>
  <text x="165" y="265" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">2x2 SPAN</text>
  <text x="375" y="315" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">2x1 SPAN</text>
  {badge(185, 480, "模块矩阵与跨单元合并", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_171(): # 基准线网格 (Baseline Grid 8pt Rhythm)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Equidistant 8pt Baseline Grid Lines -->
  <g stroke="#FF4081" stroke-width="0.8" opacity="0.6">
""" + "\n".join([f'    <line x1="50" y1="{y}" x2="500" y2="{y}"/>' for y in range(80, 520, 24)]) + f"""
  </g>
  <!-- Cap-Height & X-Height Guide Bands -->
  <rect x="70" y="128" width="410" height="48" fill="{t['accent']}" fill-opacity="0.15"/>
  <line x1="70" y1="128" x2="480" y2="128" stroke="{t['accent_alt']}" stroke-width="1.5"/>
  <line x1="70" y1="152" x2="480" y2="152" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="70" y1="176" x2="480" y2="176" stroke="{t['danger']}" stroke-width="2"/>
  <!-- Typography Samples aligned on baseline -->
  <text x="80" y="176" fill="#FFFFFF" font-size="52" font-weight="900" font-family="Helvetica, Arial, sans-serif">Ag9</text>
  <text x="210" y="176" fill="{t['accent_alt']}" font-size="28" font-weight="bold" font-family="Helvetica">Baseline 24pt</text>
  <!-- Second Typography block -->
  <text x="80" y="272" fill="#FFFFFF" font-size="36" font-weight="900" font-family="Helvetica">Rhythm</text>
  <text x="80" y="320" fill="{t['text_dim']}" font-size="18" font-family="Helvetica">Consistent vertical cadence throughout</text>
  <text x="80" y="344" fill="{t['text_dim']}" font-size="18" font-family="Helvetica">every typographic element.</text>
  <!-- Labels -->
  <text x="495" y="128" fill="{t['accent_alt']}" font-size="9" font-family="Montserrat">CAP</text>
  <text x="495" y="152" fill="{t['accent_alt']}" font-size="9" font-family="Montserrat">MEAN</text>
  <text x="495" y="176" fill="{t['danger']}" font-size="9" font-family="Montserrat">BASE</text>
  {badge(185, 480, "严格对齐基准垂直律动", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_182(): # 首字下沉 (Drop Cap Monogram)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <!-- Massive 3-line Drop Cap "T" -->
  <rect x="80" y="100" width="130" height="140" fill="{t['accent']}" rx="6"/>
  <text x="145" y="220" fill="{t['bg']}" font-size="130" font-weight="900" font-family="Georgia, serif" text-anchor="middle">T</text>
  <!-- Text lines wrapping around Drop Cap -->
  <g fill="{t['text']}">
    <rect x="230" y="110" width="230" height="10" rx="2"/>
    <rect x="230" y="135" width="230" height="7" rx="2" fill="{t['text_dim']}"/>
    <rect x="230" y="155" width="230" height="7" rx="2" fill="{t['text_dim']}"/>
    <rect x="230" y="175" width="210" height="7" rx="2" fill="{t['text_dim']}"/>
    <rect x="230" y="195" width="230" height="7" rx="2" fill="{t['text_dim']}"/>
    <rect x="230" y="215" width="190" height="7" rx="2" fill="{t['text_dim']}"/>
  </g>
  <!-- Subsequent full-width text lines below Drop Cap -->
  <g fill="{t['text_dim']}">
    <rect x="80" y="260" width="380" height="7" rx="2"/>
    <rect x="80" y="280" width="380" height="7" rx="2"/>
    <rect x="80" y="300" width="360" height="7" rx="2"/>
    <rect x="80" y="320" width="380" height="7" rx="2"/>
    <rect x="80" y="340" width="240" height="7" rx="2"/>
  </g>
  {badge(185, 480, "首字下沉视觉锚定", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_195(): # 奇肖尔德黄金分割网格 (Tschichold 2:3 Golden Canon)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Canonical Page Outline (2:3 Ratio) -->
  <rect x="60" y="50" width="430" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="4"/>
  <!-- Construction Diagonals (Tschichold Canon) -->
  <g stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,4">
    <line x1="60" y1="50" x2="490" y2="570"/>
    <line x1="490" y1="50" x2="60" y2="570"/>
    <!-- Page 1/9 divisions -->
    <line x1="60" y1="223" x2="490" y2="223"/>
    <line x1="203" y1="50" x2="203" y2="570"/>
  </g>
  <!-- Constructed Text Area (Golden Canon Proportions 2:3:4:6) -->
  <rect x="132" y="108" width="286" height="347" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5" rx="3"/>
  <!-- Circle intersection nodes of canon -->
  <circle cx="275" cy="310" r="8" fill="{t['danger']}"/>
  <circle cx="132" cy="108" r="6" fill="{t['accent']}"/>
  <circle cx="418" cy="455" r="6" fill="{t['accent']}"/>
  <text x="275" y="270" fill="{t['accent']}" font-size="16" font-weight="900" font-family="Georgia, serif" text-anchor="middle">TEXT AREA 2:3</text>
  <text x="275" y="295" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">1/9 PAGE MARGIN CANON</text>
  {badge(185, 490, "奇肖尔德九等分网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_199(): # 约瑟夫·米勒-布罗克曼32格网格 (Josef Müller-Brockmann 32-Field Grid)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- 4 Columns x 8 Rows = 32 Field Grid -->
  <rect x="40" y="50" width="470" height="520" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <g stroke="#3A4050" stroke-width="1" stroke-dasharray="3,3">
""" + "\n".join([f'    <line x1="{x}" y1="50" x2="{x}" y2="570"/>' for x in [145, 255, 365]]) + "\n" + "\n".join([f'    <line x1="40" y1="{y}" x2="510" y2="{y}"/>' for y in [108, 166, 224, 282, 340, 398, 456]]) + f"""
  </g>
  <!-- Iconic Bold Red Accent Modules (Müller-Brockmann Zurich Concert Poster style) -->
  <rect x="150" y="112" width="210" height="110" fill="{t['accent']}"/>
  <text x="165" y="165" fill="{t['bg']}" font-size="28" font-weight="900" font-family="Helvetica, Arial, sans-serif">musica</text>
  <text x="165" y="195" fill="{t['bg']}" font-size="28" font-weight="900" font-family="Helvetica, Arial, sans-serif">viva</text>
  <!-- Secondary Field Accent -->
  <rect x="260" y="345" width="100" height="105" fill="#FF3D00"/>
  <circle cx="310" cy="397" r="24" fill="#FFFFFF"/>
  <text x="275" y="515" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Helvetica, sans-serif" text-anchor="middle">32-FIELD RATIONAL SWISS ORDER</text>
  {badge(185, 535, "32 格理性网格系统", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_202(): # 12栏响应式网格 (12-Column Responsive Layout Grid)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="60" width="470" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="6"/>
  <!-- 12 Equal Columns (Col width = 28px, Gutter = 8px) -->
  <g fill="{t['accent']}" fill-opacity="0.2" stroke="{t['accent']}" stroke-width="1">
""" + "\n".join([f'    <rect x="{60 + i*36}" y="80" width="28" height="420" rx="2"/>' for i in range(12)]) + f"""
  </g>
  <!-- Responsive Layout Components Spanning Columns -->
  <!-- Component 1: 12-Col Full Header -->
  <rect x="60" y="100" width="424" height="60" rx="4" fill="{t['accent']}"/>
  <text x="272" y="136" fill="#FFFFFF" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">COL 1–12 (100% FULL SPAN)</text>
  <!-- Component 2: 8-Col Main Body -->
  <rect x="60" y="180" width="280" height="180" rx="4" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="2"/>
  <text x="200" y="275" fill="{t['accent_alt']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">COL 1–8 (MAIN)</text>
  <!-- Component 3: 4-Col Aside -->
  <rect x="348" y="180" width="136" height="180" rx="4" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <text x="416" y="275" fill="{t['danger']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">COL 9–12 (SIDEBAR)</text>
  <!-- Component 4: 3x 4-Col Cards -->
  <rect x="60" y="380" width="136" height="80" rx="4" fill="{t['stroke']}"/>
  <rect x="204" y="380" width="136" height="80" rx="4" fill="{t['stroke']}"/>
  <rect x="348" y="380" width="136" height="80" rx="4" fill="{t['stroke']}"/>
  {badge(185, 520, "12 栏响应式流式布局", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_212(): # 中文竖排古典版式 (Vertical Chinese Traditional Tategaki)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <!-- Right-to-Left Vertical Column Guidelines -->
  <g stroke="{t['accent']}" stroke-width="1" stroke-dasharray="4,4" opacity="0.5">
    <line x1="410" y1="90" x2="410" y2="480"/>
    <line x1="340" y1="90" x2="340" y2="480"/>
    <line x1="270" y1="90" x2="270" y2="480"/>
    <line x1="200" y1="90" x2="200" y2="480"/>
    <line x1="130" y1="90" x2="130" y2="480"/>
  </g>
  <!-- Vertical Calligraphic Column Text Simulation -->
  <!-- Col 1 (Rightmost Title) -->
  <text x="410" y="140" fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, STKaiti, serif" text-anchor="middle">天</text>
  <text x="410" y="180" fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, STKaiti, serif" text-anchor="middle">地</text>
  <text x="410" y="220" fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, STKaiti, serif" text-anchor="middle">玄</text>
  <text x="410" y="260" fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, STKaiti, serif" text-anchor="middle">黄</text>
  <!-- Col 2 -->
  <text x="340" y="140" fill="{t['text']}" font-size="22" font-family="Kaiti, STKaiti, serif" text-anchor="middle">宇</text>
  <text x="340" y="175" fill="{t['text']}" font-size="22" font-family="Kaiti, STKaiti, serif" text-anchor="middle">宙</text>
  <text x="340" y="210" fill="{t['text']}" font-size="22" font-family="Kaiti, STKaiti, serif" text-anchor="middle">洪</text>
  <text x="340" y="245" fill="{t['text']}" font-size="22" font-family="Kaiti, STKaiti, serif" text-anchor="middle">荒</text>
  <!-- Traditional Red Cinnabar Seal (Bottom Left) -->
  <rect x="110" y="400" width="40" height="40" fill="{t['danger']}" rx="2"/>
  <rect x="114" y="404" width="32" height="32" fill="none" stroke="#FFFFFF" stroke-width="1.2"/>
  <text x="130" y="425" fill="#FFFFFF" font-size="14" font-family="Songti, STSong, serif" text-anchor="middle">文印</text>
  {badge(185, 520, "右起竖排直行书写", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat04
CAT04_SVGS = {
    "170": gen_170, "171": gen_171, "182": gen_182, "195": gen_195, "199": gen_199,
    "202": gen_202, "212": gen_212
}


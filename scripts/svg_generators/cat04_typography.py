"""
SVG generators for Category 04: 字体与网格系统 (168-221).
"""
import math
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

def gen_168(): # 轴线系统 (Axial System)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Main Vertical Axial Spine -->
  <line x1="230" y1="80" x2="230" y2="520" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Elements hung to the left -->
  <rect x="80" y="130" width="135" height="60" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="200" y="165" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="end">BRANCH 01</text>
  <line x1="215" y1="160" x2="230" y2="160" stroke="{t['accent']}" stroke-width="2"/>

  <rect x="70" y="310" width="145" height="90" rx="4" fill="{t['stroke']}"/>
  <text x="200" y="355" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="end">BRANCH 03</text>
  <line x1="215" y1="355" x2="230" y2="355" stroke="{t['accent']}" stroke-width="2"/>

  <!-- Elements hung to the right -->
  <rect x="245" y="210" width="210" height="75" rx="4" fill="{t['accent']}" fill-opacity="0.85"/>
  <text x="260" y="255" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat">BRANCH 02 (HERO)</text>
  <line x1="230" y1="247" x2="245" y2="247" stroke="{t['accent']}" stroke-width="2"/>

  <rect x="245" y="420" width="170" height="55" rx="4" fill="{t['accent_alt']}" opacity="0.7"/>
  <text x="260" y="452" fill="{t['bg']}" font-size="13" font-weight="bold" font-family="Montserrat">BRANCH 04</text>
  {badge(185, 520, "单轴基准左右依附系统", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_169(): # 放射系统 (Radial System)
    t = get_theme("warm-ivory")
    rays = "".join([f'<line x1="275" y1="290" x2="{275 + 200*math.cos(i*math.pi/6):.1f}" y2="{290 + 200*math.sin(i*math.pi/6):.1f}" stroke="{t["accent"] if i%3==0 else t["guide"]}" stroke-width="{2 if i%3==0 else 1}" stroke-dasharray="{4 if i%3!=0 else 0},{4 if i%3!=0 else 0}"/>' for i in range(12)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  {rays}
  <!-- Concentric ripple guides -->
  <circle cx="275" cy="290" r="80" fill="none" stroke="{t['accent_alt']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  <circle cx="275" cy="290" r="150" fill="none" stroke="{t['accent_alt']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  <!-- Radial Core -->
  <circle cx="275" cy="290" r="42" fill="{t['danger']}"/>
  <circle cx="275" cy="290" r="14" fill="#FFFFFF"/>
  <text x="275" y="110" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">CENTRIFUGAL EXPLOSION</text>
  {badge(185, 520, "放射离心文字组织", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_172(): # 网格系统 (Swiss 12-Column Grid System)
    t = get_theme("cobalt-blue")
    # 12 columns with pink gutter guides
    col_w = 26
    gut_w = 8
    cols = "".join([f'<rect x="{70 + i*(col_w+gut_w)}" y="100" width="{col_w}" height="380" fill="#FF4081" opacity="0.15" stroke="#FF4081" stroke-width="0.8" stroke-dasharray="4,4"/>' for i in range(12)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  {cols}
  <!-- Content spanning 4 columns -->
  <rect x="70" y="130" width="{col_w*4 + gut_w*3}" height="140" rx="4" fill="{t['accent']}" fill-opacity="0.9"/>
  <text x="135" y="205" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">4 COLS</text>
  <!-- Content spanning 8 columns -->
  <rect x="{70 + 4*(col_w+gut_w)}" y="130" width="{col_w*8 + gut_w*7}" height="140" rx="4" fill="{t['stroke']}"/>
  <text x="345" y="205" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">8 COLS (HERO)</text>
  <!-- Content spanning 12 columns -->
  <rect x="70" y="300" width="{col_w*12 + gut_w*11}" height="120" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="270" y="365" fill="{t['accent']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">FULL 12-COLUMN MODULE</text>
  {badge(185, 520, "瑞士国际主义12栏网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_173(): # 模块系统 (Modular Rectangle System)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 5x4 Grid of Modules with span -->
  <g stroke="{t['guide']}" stroke-width="1">
    {''.join([f'<rect x="{75 + (i%4)*95}" y="{100 + (i//4)*85}" width="85" height="75" rx="4" fill="{t["stroke"]}" opacity="0.3"/>' for i in range(16)])}
  </g>
  <!-- Merged 2x2 module -->
  <rect x="75" y="100" width="180" height="160" rx="6" fill="{t['accent']}" fill-opacity="0.9"/>
  <text x="165" y="185" fill="{t['bg']}" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">MODULE 2x2</text>
  <!-- Merged 2x1 module -->
  <rect x="265" y="270" width="180" height="75" rx="6" fill="{t['danger']}"/>
  <text x="355" y="315" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">MODULE 2x1</text>
  {badge(185, 510, "二维模块化矩阵单元", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_174(): # 过渡系统 (Transitional Fluid Grid)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Top rigid grid transitioning into bottom fluid waves -->
  <line x1="80" y1="120" x2="470" y2="120" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="80" y1="180" x2="470" y2="180" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Transitional undulating wave lines -->
  <path d="M 80 250 Q 200 210 320 270 T 470 250" fill="none" stroke="{t['accent_alt']}" stroke-width="2.5"/>
  <path d="M 80 320 Q 180 380 300 290 T 470 330" fill="none" stroke="{t['accent_alt']}" stroke-width="3"/>
  <path d="M 80 400 Q 220 460 350 360 T 470 410" fill="none" stroke="{t['danger']}" stroke-width="3.5"/>
  <text x="275" y="95" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">RIGID ORTHOGONAL → FLUID ORGANIC</text>
  {badge(185, 480, "刚性网格向流体渐变过渡", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_175(): # 双边系统 (Bilateral Symmetry System)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Central Vertical Mirror Axis -->
  <line x1="275" y1="80" x2="275" y2="500" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Bilaterally centered text lines -->
  <g fill="{t['accent_alt']}">
    <rect x="175" y="130" width="200" height="16" rx="3"/>
    <rect x="145" y="165" width="260" height="14" rx="3"/>
    <rect x="195" y="200" width="160" height="14" rx="3"/>
    <rect x="125" y="235" width="300" height="18" rx="3" fill="{t['accent']}"/>
    <rect x="165" y="275" width="220" height="14" rx="3"/>
    <rect x="215" y="310" width="120" height="14" rx="3"/>
  </g>
  <circle cx="275" cy="380" r="24" fill="{t['danger']}"/>
  <circle cx="275" cy="380" r="8" fill="#FFFFFF"/>
  {badge(185, 460, "古典中轴双侧对称系统", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_176(): # 左对齐右参差 (Flush Left Ragged Right)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Strict Left Margin Baseline Guide -->
  <line x1="90" y1="90" x2="90" y2="480" stroke="{t['accent']}" stroke-width="3.5"/>
  <g fill="{t['accent']}">
    <rect x="110" y="120" width="310" height="12" rx="2"/>
    <rect x="110" y="145" width="240" height="12" rx="2"/>
    <rect x="110" y="170" width="280" height="12" rx="2"/>
    <rect x="110" y="195" width="190" height="12" rx="2"/>
    <rect x="110" y="220" width="325" height="12" rx="2"/>
    <rect x="110" y="245" width="265" height="12" rx="2"/>
    <rect x="110" y="270" width="220" height="12" rx="2"/>
    <rect x="110" y="295" width="295" height="12" rx="2"/>
  </g>
  <!-- Ragged right curve guideline -->
  <path d="M 420 126 Q 340 200 435 226 T 405 301" fill="none" stroke="{t['danger']}" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="445" y="220" fill="{t['danger']}" font-size="11" font-family="Montserrat">RAGGED</text>
  {badge(185, 480, "齐左参差自然阅读行宽", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_177(): # 右对齐左参差 (Flush Right Ragged Left)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Strict Right Margin Baseline Guide -->
  <line x1="460" y1="90" x2="460" y2="480" stroke="{t['accent']}" stroke-width="3.5"/>
  <g fill="{t['accent']}">
    <rect x="150" y="120" width="290" height="12" rx="2"/>
    <rect x="220" y="145" width="220" height="12" rx="2"/>
    <rect x="170" y="170" width="270" height="12" rx="2"/>
    <rect x="260" y="195" width="180" height="12" rx="2"/>
    <rect x="135" y="220" width="305" height="12" rx="2"/>
    <rect x="200" y="245" width="240" height="12" rx="2"/>
  </g>
  <text x="110" y="190" fill="{t['danger']}" font-size="11" font-family="Montserrat">RAGGED</text>
  {badge(185, 480, "齐右参差边栏特异排版", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_178(): # 居中排版 (Centered Poetry)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Center Axis Line -->
  <line x1="275" y1="80" x2="275" y2="480" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <g fill="{t['accent']}">
    <rect x="175" y="130" width="200" height="12" rx="2"/>
    <rect x="125" y="160" width="300" height="12" rx="2"/>
    <rect x="155" y="190" width="240" height="12" rx="2"/>
    <rect x="195" y="220" width="160" height="12" rx="2"/>
    <rect x="145" y="250" width="260" height="12" rx="2"/>
    <rect x="185" y="280" width="180" height="12" rx="2"/>
  </g>
  <circle cx="275" cy="350" r="20" fill="{t['danger']}"/>
  <circle cx="275" cy="350" r="6" fill="#FFFFFF"/>
  {badge(185, 480, "诗歌庄严中轴居中", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_179(): # 两端对齐 (Justified Rectilinear Block)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Rigid Left and Right Bounds -->
  <line x1="90" y1="90" x2="90" y2="480" stroke="{t['accent']}" stroke-width="3"/>
  <line x1="460" y1="90" x2="460" y2="480" stroke="{t['accent']}" stroke-width="3"/>
  <g fill="{t['accent']}">
    {''.join([f'<rect x="105" y="{120 + i*24}" width="340" height="12" rx="2"/>' for i in range(10)])}
    <!-- Last line shorter (Quad left) -->
    <rect x="105" y="360" width="180" height="12" rx="2" fill="{t['accent_alt']}"/>
  </g>
  <text x="275" y="420" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">PERFECT RECTILINEAR BLOCK</text>
  {badge(185, 480, "严格两端对齐矩形文字块", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_180(): # 强制两端对齐 (Force Justified Last Line)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <line x1="90" y1="90" x2="90" y2="480" stroke="{t['danger']}" stroke-width="3"/>
  <line x1="460" y1="90" x2="460" y2="480" stroke="{t['danger']}" stroke-width="3"/>
  <g fill="{t['accent']}">
    {''.join([f'<rect x="105" y="{120 + i*24}" width="340" height="12" rx="2"/>' for i in range(8)])}
    <!-- Last line forced to stretch edge to edge with huge gaps -->
    <rect x="105" y="312" width="70" height="12" rx="2" fill="{t['danger']}"/>
    <rect x="235" y="312" width="80" height="12" rx="2" fill="{t['danger']}"/>
    <rect x="375" y="312" width="70" height="12" rx="2" fill="{t['danger']}"/>
  </g>
  <text x="275" y="370" fill="{t['danger']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">FORCED FULL-WIDTH LAST LINE</text>
  {badge(185, 480, "末行强制满宽两端对齐", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_181(): # 非对称字体排版 (Asymmetrical Typography)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Constructivist Dynamic Angled Layout (El Lissitzky style) -->
  <g transform="rotate(-20 275 280)">
    <rect x="120" y="200" width="320" height="36" fill="{t['accent']}"/>
    <text x="280" y="226" fill="{t['bg']}" font-size="22" font-weight="900" font-family="Impact, Montserrat" text-anchor="middle">BAUHAUS 1923</text>
    <rect x="80" y="250" width="220" height="18" fill="{t['stroke']}"/>
    <circle cx="360" cy="270" r="35" fill="{t['danger']}"/>
  </g>
  <line x1="70" y1="100" x2="70" y2="500" stroke="{t['accent_alt']}" stroke-width="4"/>
  {badge(185, 520, "构成主义非对称动态排版", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_183(): # 矩形绕排 (Rectangular Contour Wrap)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Center Image Block -->
  <rect x="190" y="190" width="170" height="160" rx="6" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
  <circle cx="275" cy="270" r="32" fill="{t['bg']}"/>
  <!-- Surrounding Wrapped Text Lines -->
  <g fill="{t['stroke']}">
    <rect x="80" y="110" width="390" height="10" rx="2"/>
    <rect x="80" y="135" width="390" height="10" rx="2"/>
    <rect x="80" y="160" width="390" height="10" rx="2"/>
    <!-- Left of image -->
    <rect x="80" y="205" width="95" height="10" rx="2"/><rect x="375" y="205" width="95" height="10" rx="2"/>
    <rect x="80" y="235" width="95" height="10" rx="2"/><rect x="375" y="235" width="95" height="10" rx="2"/>
    <rect x="80" y="265" width="95" height="10" rx="2"/><rect x="375" y="265" width="95" height="10" rx="2"/>
    <rect x="80" y="295" width="95" height="10" rx="2"/><rect x="375" y="295" width="95" height="10" rx="2"/>
    <rect x="80" y="325" width="95" height="10" rx="2"/><rect x="375" y="325" width="95" height="10" rx="2"/>
    <!-- Below image -->
    <rect x="80" y="370" width="390" height="10" rx="2"/>
    <rect x="80" y="395" width="340" height="10" rx="2"/>
  </g>
  {badge(185, 480, "矩形嵌入环绕排版", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_184(): # 跨栏标题 (Spanning Headline)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Colossal Spanning Headline Banner across full width -->
  <rect x="80" y="110" width="390" height="70" rx="6" fill="{t['accent']}"/>
  <text x="275" y="155" fill="{t['bg']}" font-size="26" font-weight="900" font-family="Montserrat" text-anchor="middle">SPANNING HEADLINE</text>
  <!-- 3 Text Columns Below -->
  <g fill="{t['stroke']}">
    <rect x="80" y="210" width="115" height="220" rx="4"/>
    <rect x="217" y="210" width="115" height="220" rx="4"/>
    <rect x="355" y="210" width="115" height="220" rx="4"/>
  </g>
  {badge(185, 480, "横跨多栏通栏大标", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_185(): # 悬挂缩进 (Hanging Indent)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Outdented hanging bullets outside text column -->
  <line x1="140" y1="90" x2="140" y2="480" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <!-- Item 1 -->
  <circle cx="110" cy="145" r="10" fill="{t['danger']}"/>
  <rect x="150" y="140" width="300" height="12" rx="2" fill="{t['accent']}"/>
  <rect x="150" y="160" width="260" height="10" rx="2" fill="{t['text_dim']}"/>
  <!-- Item 2 -->
  <circle cx="110" cy="225" r="10" fill="{t['danger']}"/>
  <rect x="150" y="220" width="280" height="12" rx="2" fill="{t['accent']}"/>
  <rect x="150" y="240" width="240" height="10" rx="2" fill="{t['text_dim']}"/>
  <!-- Item 3 -->
  <circle cx="110" cy="305" r="10" fill="{t['danger']}"/>
  <rect x="150" y="300" width="290" height="12" rx="2" fill="{t['accent']}"/>
  <rect x="150" y="320" width="250" height="10" rx="2" fill="{t['text_dim']}"/>
  {badge(185, 480, "标识外悬挂凸排结构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_186(): # 首行缩进 (First-Line Indent)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Paragraph 1 with 2em indent -->
  <rect x="140" y="130" width="310" height="12" rx="2" fill="{t['accent']}"/>
  <rect x="90" y="155" width="360" height="12" rx="2" fill="{t['stroke']}"/>
  <rect x="90" y="180" width="360" height="12" rx="2" fill="{t['stroke']}"/>
  <rect x="90" y="205" width="240" height="12" rx="2" fill="{t['stroke']}"/>
  <!-- Paragraph 2 with 2em indent -->
  <rect x="140" y="250" width="310" height="12" rx="2" fill="{t['accent']}"/>
  <rect x="90" y="275" width="360" height="12" rx="2" fill="{t['stroke']}"/>
  <rect x="90" y="300" width="360" height="12" rx="2" fill="{t['stroke']}"/>
  <rect x="90" y="325" width="280" height="12" rx="2" fill="{t['stroke']}"/>
  <!-- Dimension bracket for indent width -->
  {dimension_h(90, 140, 110, "2 EM", t['danger'], t['danger'])}
  {badge(185, 480, "中文传统两字首行缩进", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_187(): # 凸排标点 (Hanging Punctuation)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Strict Optical Text Margin -->
  <line x1="130" y1="90" x2="130" y2="480" stroke="{t['danger']}" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- Hanging Quote Mark outside text margin -->
  <text x="85" y="190" fill="{t['danger']}" font-size="72" font-family="Georgia, serif">“</text>
  <rect x="135" y="150" width="310" height="14" rx="2" fill="{t['accent']}"/>
  <rect x="135" y="180" width="310" height="14" rx="2" fill="{t['accent']}"/>
  <rect x="135" y="210" width="260" height="14" rx="2" fill="{t['accent']}"/>
  <text x="405" y="230" fill="{t['danger']}" font-size="72" font-family="Georgia, serif">”</text>
  <text x="275" y="340" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">PUNCTUATION OUTSIDE OPTICAL MARGIN</text>
  {badge(185, 480, "标点外挂平整视觉边缘", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_188(): # 基线对齐 (Baseline Alignment)
    t = get_theme("cobalt-blue")
    lines = "".join([f'<line x1="70" y1="{y}" x2="480" y2="{y}" stroke="#FF4081" stroke-width="1" opacity="0.6"/>' for y in range(120, 440, 28)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  {lines}
  <text x="80" y="148" fill="#FFFFFF" font-size="36" font-weight="900" font-family="Montserrat">BASELINE 28PT</text>
  <text x="80" y="204" fill="{t['accent']}" font-size="22" font-weight="bold" font-family="PingFang SC">多栏文字严格对齐网格</text>
  <text x="80" y="232" fill="{t['text_dim']}" font-size="16" font-family="Montserrat">Strict vertical cadence lock</text>
  <text x="80" y="260" fill="{t['text_dim']}" font-size="16" font-family="Montserrat">across all independent columns</text>
  {badge(185, 480, "跨栏基准线精准咬合", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_189(): # 形状文字 (Shaped Text)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Heart or Circular Contour shape containing text -->
  <circle cx="275" cy="280" r="150" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4"/>
  <g fill="{t['accent_alt']}">
    <rect x="235" y="160" width="80" height="10" rx="2"/>
    <rect x="185" y="190" width="180" height="10" rx="2"/>
    <rect x="155" y="220" width="240" height="10" rx="2"/>
    <rect x="135" y="250" width="280" height="10" rx="2"/>
    <rect x="135" y="280" width="280" height="10" rx="2"/>
    <rect x="155" y="310" width="240" height="10" rx="2"/>
    <rect x="185" y="340" width="180" height="10" rx="2"/>
    <rect x="235" y="370" width="80" height="10" rx="2"/>
  </g>
  {badge(185, 500, "具象轮廓填充形状文字", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_190(): # 图形诗排版 (Calligramme / Concrete Poetry)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Hourglass shaped concrete poetry text -->
  <g fill="{t['accent']}">
    <rect x="125" y="120" width="300" height="12" rx="2"/>
    <rect x="155" y="150" width="240" height="12" rx="2"/>
    <rect x="185" y="180" width="180" height="12" rx="2"/>
    <rect x="225" y="210" width="100" height="12" rx="2"/>
    <!-- Waist node -->
    <circle cx="275" cy="255" r="12" fill="{t['danger']}"/>
    <!-- Bottom flare -->
    <rect x="225" y="285" width="100" height="12" rx="2"/>
    <rect x="185" y="315" width="180" height="12" rx="2"/>
    <rect x="155" y="345" width="240" height="12" rx="2"/>
    <rect x="125" y="375" width="300" height="12" rx="2"/>
  </g>
  {badge(185, 480, "图象诗形意相通构建", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_191(): # 路径文字 (Text on Path)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <path id="wavePath191" d="M 70 320 C 140 160 220 160 275 300 C 330 440 410 440 480 280" fill="none" stroke="{t['accent']}" stroke-width="3" stroke-dasharray="6,4"/>
  <text fill="#FFFFFF" font-size="20" font-weight="900" font-family="Montserrat">
    <textPath href="#wavePath191" startOffset="10%">TYPOGRAPHY FLOWING ALONG BEZIER SPLINE</textPath>
  </text>
  <circle cx="170" cy="220" r="10" fill="{t['danger']}"/>
  <circle cx="380" cy="380" r="10" fill="{t['danger']}"/>
  {badge(185, 520, "样条曲线路径贴合编排", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_192(): # 垂直文字排版 (Vertical CJK Typography)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical guideline columns right-to-left -->
  <g stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4">
    <line x1="410" y1="100" x2="410" y2="460"/>
    <line x1="330" y1="100" x2="330" y2="460"/>
    <line x1="250" y1="100" x2="250" y2="460"/>
    <line x1="170" y1="100" x2="170" y2="460"/>
  </g>
  <!-- Hanzi characters reading down -->
  <g fill="{t['accent']}" font-size="32" font-weight="900" font-family="Kaiti, STKaiti, serif" text-anchor="middle">
    <text x="410" y="150">汉</text><text x="410" y="200">字</text><text x="410" y="250">直</text><text x="410" y="300">排</text>
    <text x="330" y="150">古</text><text x="330" y="200">典</text><text x="330" y="250">风</text><text x="330" y="300">骨</text>
  </g>
  <!-- Red Seal Mark -->
  <rect x="85" y="390" width="36" height="36" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, "东亚传统右起纵书行气", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_193(): # 水平文字排版 (Horizontal LTR Typography)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Horizontal LTR text tracks -->
  <g fill="{t['accent']}">
    <rect x="90" y="130" width="370" height="20" rx="4"/>
    <rect x="90" y="170" width="330" height="14" rx="3" fill="{t['stroke']}"/>
    <rect x="90" y="200" width="350" height="14" rx="3" fill="{t['stroke']}"/>
    <rect x="90" y="230" width="280" height="14" rx="3" fill="{t['stroke']}"/>
  </g>
  <!-- Arrow showing LTR flow direction -->
  <line x1="90" y1="290" x2="460" y2="290" stroke="{t['danger']}" stroke-width="3"/>
  <polygon points="460,290 440,280 440,300" fill="{t['danger']}"/>
  <text x="275" y="340" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">MODERN HORIZONTAL LTR FLOW</text>
  {badge(185, 480, "现代横排左起高效阅读", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_194(): # 手稿网格 (Manuscript Grid / Van de Graaf Canon)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Golden Diagonal diagonals of Van de Graaf canon -->
  <line x1="50" y1="60" x2="500" y2="560" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="500" y1="60" x2="50" y2="560" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <!-- Classical text block (2:3:4:6 margin ratio) -->
  <rect x="130" y="140" width="290" height="340" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5" rx="4"/>
  <text x="275" y="280" fill="{t['accent']}" font-size="18" font-weight="900" font-family="Georgia, serif" text-anchor="middle">VAN DE GRAAF CANON</text>
  <text x="275" y="310" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">MARGIN RATIO 2 : 3 : 4 : 6</text>
  {badge(185, 510, "中世纪手抄本黄金范式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_196(): # 模块化网格 (Modular Grid)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Uniform square module array -->
  <g stroke="{t['guide']}" stroke-width="1.2">
    {''.join([f'<rect x="{80 + (i%4)*92}" y="{110 + (i//4)*85}" width="80" height="75" rx="4" fill="{t["accent"] if i in [2,5,6] else t["bg"]}" fill-opacity="{0.85 if i in [2,5,6] else 1}"/>' for i in range(16)])}
  </g>
  <text x="275" y="90" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">4x4 EQUAL MODULAR UNITS</text>
  {badge(185, 520, "均质模块单元矩阵编排", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_197(): # 层级网格 (Hierarchical Web News Grid)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Hero Primary Lead Story (Top Left 60%) -->
  <rect x="75" y="90" width="250" height="220" rx="6" fill="{t['accent']}" fill-opacity="0.9"/>
  <circle cx="200" cy="180" r="36" fill="#FFFFFF"/>
  <text x="200" y="250" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">PRIMARY LEAD (HERO)</text>
  <!-- Secondary Stack (Top Right 40%) -->
  <rect x="340" y="90" width="135" height="105" rx="6" fill="{t['stroke']}"/>
  <rect x="340" y="205" width="135" height="105" rx="6" fill="{t['accent_alt']}"/>
  <!-- 3 Tertiary Cards Bottom -->
  <rect x="75" y="325" width="125" height="120" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="212" y="325" width="125" height="120" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="350" y="325" width="125" height="120" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  {badge(185, 520, "新闻门户层级权重网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_198(): # 基线网格 (Notebook Ruled Baseline Grid)
    t = get_theme("forest-green")
    lines = "".join([f'<line x1="65" y1="{y}" x2="485" y2="{y}" stroke="{t["accent"]}" stroke-width="1" opacity="0.5"/>' for y in range(110, 480, 22)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical margin red rule -->
  <line x1="130" y1="60" x2="130" y2="560" stroke="{t['danger']}" stroke-width="2"/>
  {lines}
  <text x="145" y="154" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Helvetica">Typography</text>
  <text x="145" y="198" fill="{t['accent_alt']}" font-size="18" font-family="Helvetica">Snapping strictly to baseline</text>
  {badge(185, 510, "横线记事簿基线锁死", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_200(): # 非对称网格 (Asymmetric Ratio Grid)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 1/3 Narrow Column Left -->
  <rect x="75" y="90" width="120" height="410" rx="6" fill="{t['stroke']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="135" y="130" fill="{t['accent']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">1/3 ASIDE</text>
  <!-- 2/3 Expansive Body Column Right -->
  <rect x="210" y="90" width="265" height="410" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="342" y="130" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">2/3 MAIN BODY</text>
  <circle cx="342" cy="260" r="50" fill="{t['accent']}"/>
  <circle cx="342" cy="260" r="16" fill="#FFFFFF"/>
  {badge(185, 520, "1:2 非对称黄金权重比", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_201(): # 方格网格 (Square Manuscript Grid / 原稿用紙)
    t = get_theme("warm-ivory")
    cells = "".join([f'<rect x="{75 + (i%8)*46}" y="{110 + (i//8)*46}" width="42" height="42" fill="none" stroke="{t["accent"]}" stroke-width="1" opacity="0.6"/>' for i in range(56)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  {cells}
  <text x="275" y="95" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="Kaiti, serif" text-anchor="middle">东亚经典方格原稿纸网格</text>
  {badge(185, 520, "字字独立等距方格原稿", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_203(): # 放射网格 (Radial Polar Grid)
    t = get_theme("cobalt-blue")
    rings = "".join([f'<circle cx="275" cy="290" r="{40 + i*35}" fill="none" stroke="{t["accent_alt"]}" stroke-width="1" stroke-dasharray="4,4"/>' for i in range(5)])
    spokes = "".join([f'<line x1="275" y1="290" x2="{275 + 190*math.cos(i*math.pi/4):.1f}" y2="{290 + 190*math.sin(i*math.pi/4):.1f}" stroke="{t["accent"]}" stroke-width="1.5"/>' for i in range(8)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  {rings}
  {spokes}
  <circle cx="275" cy="290" r="20" fill="{t['danger']}"/>
  <circle cx="275" cy="290" r="6" fill="#FFFFFF"/>
  {badge(185, 520, "蜘蛛网极坐标同心放射", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_204(): # 极坐标网格 (Polar Radar Grid)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Radar circles -->
  <circle cx="275" cy="280" r="160" fill="none" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="275" cy="280" r="110" fill="none" stroke="{t['accent_alt']}" stroke-width="1.2" stroke-dasharray="6,4"/>
  <circle cx="275" cy="280" r="60" fill="none" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
  <!-- Angle crosshairs -->
  <line x1="115" y1="280" x2="435" y2="280" stroke="{t['accent']}" stroke-width="1.5"/>
  <line x1="275" y1="120" x2="275" y2="440" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- Radar sweep wedge -->
  <path d="M 275 280 L 388 167 A 160 160 0 0 0 275 120 Z" fill="{t['accent']}" opacity="0.35"/>
  <circle cx="350" cy="200" r="8" fill="{t['danger']}"/>
  {badge(185, 480, "雷达极坐标方位角网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_205(): # 嵌套网格 (Nested Grid)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Outer Master Grid Cards -->
  <rect x="75" y="90" width="185" height="390" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="285" y="90" width="185" height="390" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Nested Sub-grids inside Card 1 -->
  <g fill="{t['stroke']}" stroke="#FFFFFF" stroke-width="1">
    <rect x="90" y="140" width="70" height="60" rx="3"/>
    <rect x="175" y="140" width="70" height="60" rx="3"/>
    <rect x="90" y="215" width="70" height="60" rx="3"/>
    <rect x="175" y="215" width="70" height="60" rx="3"/>
    <rect x="90" y="290" width="155" height="150" rx="4" fill="{t['accent']}"/>
  </g>
  <text x="275" y="515" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">MASTER GRID &gt; CHILD SUB-GRIDS</text>
  {badge(185, 460, "父子容器嵌套微型网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_206(): # 子网格 (CSS Subgrid)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Horizontal shared track lines spanning across both cards -->
  <line x1="60" y1="140" x2="490" y2="140" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="60" y1="260" x2="490" y2="260" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="60" y1="440" x2="490" y2="440" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <!-- Card A -->
  <rect x="75" y="90" width="180" height="360" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="90" y="105" width="150" height="28" rx="4" fill="{t['accent']}"/>
  <rect x="90" y="155" width="150" height="95" rx="4" fill="{t['stroke']}"/>
  <!-- Card B (Subgrid aligns with Card A's rows perfectly) -->
  <rect x="295" y="90" width="180" height="360" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="310" y="105" width="150" height="28" rx="4" fill="{t['accent']}"/>
  <rect x="310" y="155" width="150" height="95" rx="4" fill="{t['stroke']}"/>
  <text x="275" y="490" fill="{t['danger']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">grid-template-rows: subgrid</text>
  {badge(185, 520, "跨父子共享轨道子网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_207(): # 固定网格 (Fixed 960px Desktop Grid)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Outer viewport with empty side gutters -->
  <rect x="110" y="90" width="330" height="420" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5" rx="4"/>
  {dimension_h(110, 440, 75, "FIXED 960px", t['accent'], t['accent'])}
  <rect x="130" y="120" width="290" height="120" rx="4" fill="{t['accent']}" fill-opacity="0.8"/>
  <rect x="130" y="260" width="135" height="180" rx="4" fill="{t['stroke']}"/>
  <rect x="285" y="260" width="135" height="180" rx="4" fill="{t['stroke']}"/>
  {badge(185, 480, "固定像素居中版心网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_208(): # 流体网格 (Fluid Percentage Grid)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Elastic Columns with percentage labels -->
  <rect x="75" y="120" width="180" height="320" rx="6" fill="{t['accent']}" fill-opacity="0.85"/>
  <text x="165" y="285" fill="{t['bg']}" font-size="24" font-weight="900" font-family="Montserrat" text-anchor="middle">40%</text>
  <rect x="285" y="120" width="190" height="320" rx="6" fill="{t['accent_alt']}" fill-opacity="0.85"/>
  <text x="380" y="285" fill="{t['bg']}" font-size="24" font-weight="900" font-family="Montserrat" text-anchor="middle">60%</text>
  <!-- Expanding stretch arrows -->
  <line x1="65" y1="95" x2="485" y2="95" stroke="#FFFFFF" stroke-width="2.5"/>
  <polygon points="65,95 75,90 75,100" fill="#FFFFFF"/>
  <polygon points="485,95 475,90 475,100" fill="#FFFFFF"/>
  <text x="275" y="85" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">100% FLUID WIDTH</text>
  {badge(185, 480, "百分比弹性伸缩网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_209(): # 响应式网格 (Responsive Multi-Device Grid)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Desktop Layout (Top) -->
  <rect x="75" y="90" width="400" height="150" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="90" y="110" width="80" height="110" rx="4" fill="{t['accent']}"/>
  <rect x="180" y="110" width="80" height="110" rx="4" fill="{t['accent_alt']}"/>
  <rect x="270" y="110" width="80" height="110" rx="4" fill="{t['stroke']}"/>
  <rect x="360" y="110" width="100" height="110" rx="4" fill="{t['stroke']}"/>
  <!-- Arrow Down to Mobile Breakpoint -->
  <line x1="275" y1="255" x2="275" y2="285" stroke="{t['danger']}" stroke-width="3"/>
  <polygon points="275,285 268,275 282,275" fill="{t['danger']}"/>
  <!-- Mobile Stacking Wireframe (Bottom) -->
  <rect x="185" y="295" width="180" height="180" rx="8" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <rect x="200" y="310" width="150" height="35" rx="4" fill="{t['accent']}"/>
  <rect x="200" y="350" width="150" height="35" rx="4" fill="{t['accent_alt']}"/>
  <rect x="200" y="390" width="150" height="35" rx="4" fill="{t['stroke']}"/>
  {badge(185, 520, "断点自适应跨端重排", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_210(): # 破格网格 (Breaking the Grid)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Orderly Grid Box -->
  <rect x="110" y="120" width="330" height="360" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="2" rx="6" stroke-dasharray="6,6"/>
  <!-- Colossal element bursting out of grid bounds -->
  <circle cx="140" cy="200" r="90" fill="{t['danger']}" opacity="0.9"/>
  <circle cx="140" cy="200" r="30" fill="#FFFFFF"/>
  <rect x="180" y="280" width="310" height="90" rx="6" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
  <text x="335" y="335" fill="{t['bg']}" font-size="20" font-weight="900" font-family="Montserrat" text-anchor="middle">BURSTING OUT</text>
  {badge(185, 520, "突破框架冲破边界", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_211(): # 解构网格 (Deconstructed Grid)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Fractured, rotated overlapping grid planes David Carson style -->
  <g transform="rotate(12 240 220)">
    <rect x="90" y="130" width="180" height="200" fill="{t['stroke']}" stroke="{t['accent']}" stroke-width="2" rx="4"/>
    <line x1="90" y1="180" x2="270" y2="180" stroke="{t['accent']}" stroke-width="1.5"/>
  </g>
  <g transform="rotate(-18 310 290)">
    <rect x="220" y="180" width="210" height="210" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2.5" rx="4"/>
    <text x="325" y="295" fill="{t['danger']}" font-size="22" font-weight="900" font-family="Montserrat" text-anchor="middle">FRACTURE</text>
  </g>
  <line x1="60" y1="450" x2="480" y2="110" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="8,6"/>
  {badge(185, 520, "后现代解构解体网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_213(): # 横排右起 (RTL Horizontal)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- RTL Arrow -->
  <line x1="460" y1="140" x2="90" y2="140" stroke="{t['danger']}" stroke-width="3"/>
  <polygon points="90,140 110,130 110,150" fill="{t['danger']}"/>
  <!-- Signboard Plaque -->
  <rect x="80" y="180" width="390" height="140" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="3"/>
  <g fill="{t['accent']}" font-size="48" font-weight="900" font-family="Kaiti, STKaiti, serif">
    <text x="400" y="270">门</text><text x="320" y="270">安</text><text x="240" y="270">天</text>
  </g>
  <text x="275" y="380" fill="{t['text_dim']}" font-size="14" font-family="Kaiti, serif" text-anchor="middle">传统匾额题字 · 自右向左横书</text>
  {badge(185, 480, "古典右起横排匾额制式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_214(): # 直排右起 (Vertical RTL Scroll)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Columns 1 to 4 right to left -->
  <g fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, STKaiti, serif" text-anchor="middle">
    <text x="420" y="140">千</text><text x="420" y="180">山</text><text x="420" y="220">鸟</text><text x="420" y="260">飞</text><text x="420" y="300">绝</text>
    <text x="340" y="140">万</text><text x="340" y="180">径</text><text x="340" y="220">人</text><text x="340" y="260">踪</text><text x="340" y="300">灭</text>
    <text x="260" y="140">孤</text><text x="260" y="180">舟</text><text x="260" y="220">蓑</text><text x="260" y="260">笠</text><text x="260" y="300">翁</text>
    <text x="180" y="140">独</text><text x="180" y="180">钓</text><text x="180" y="220">寒</text><text x="180" y="260">江</text><text x="180" y="300">雪</text>
  </g>
  <!-- Right to left column progression arrow -->
  <line x1="430" y1="350" x2="170" y2="350" stroke="{t['danger']}" stroke-width="2.5"/>
  <polygon points="170,350 185,342 185,358" fill="{t['danger']}"/>
  {badge(185, 480, "古典右起直排线装书卷", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_215(): # 直排左起 (Vertical LTR Script)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical columns progressing Left to Right (e.g. Mongolian script) -->
  <g fill="{t['accent_alt']}" font-size="24" font-family="Montserrat" text-anchor="middle">
    <text x="150" y="150">A</text><text x="150" y="190">B</text><text x="150" y="230">C</text>
    <text x="230" y="150">D</text><text x="230" y="190">E</text><text x="230" y="230">F</text>
    <text x="310" y="150">G</text><text x="310" y="190">H</text><text x="310" y="230">I</text>
    <text x="390" y="150">J</text><text x="390" y="190">K</text><text x="390" y="230">L</text>
  </g>
  <!-- LTR arrow -->
  <line x1="140" y1="300" x2="400" y2="300" stroke="{t['accent']}" stroke-width="2.5"/>
  <polygon points="400,300 385,292 385,308" fill="{t['accent']}"/>
  <text x="275" y="350" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">VERTICAL LTR COLUMN SEQUENCE</text>
  {badge(185, 480, "蒙古文回鹘式左起纵书", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_216(): # 横直混排 (Mixed Horizontal & Vertical)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical Title / Callout Column on Right -->
  <rect x="350" y="90" width="120" height="410" rx="6" fill="{t['accent']}" fill-opacity="0.9"/>
  <g fill="{t['bg']}" font-size="32" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">
    <text x="410" y="160">横</text><text x="410" y="210">直</text><text x="410" y="260">交</text><text x="410" y="310">汇</text>
  </g>
  <!-- Horizontal Body Text Columns on Left -->
  <rect x="75" y="90" width="255" height="20" rx="4" fill="{t['stroke']}"/>
  <rect x="75" y="130" width="255" height="16" rx="3" fill="{t['stroke']}"/>
  <rect x="75" y="160" width="235" height="16" rx="3" fill="{t['stroke']}"/>
  <rect x="75" y="190" width="255" height="16" rx="3" fill="{t['stroke']}"/>
  <rect x="75" y="240" width="255" height="160" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="202" cy="320" r="32" fill="{t['accent_alt']}"/>
  {badge(185, 520, "现代日式杂志横直混排", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_217(): # 纵中横排 (Tate-chu-yoko)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical column line -->
  <line x1="275" y1="80" x2="275" y2="500" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="6,6"/>
  <g font-family="Kaiti, STKaiti, serif" font-size="42" font-weight="900" fill="{t['accent']}" text-anchor="middle">
    <text x="275" y="140">第</text>
  </g>
  <!-- Horizontal 2-digit number '99' embedded seamlessly in vertical text -->
  <rect x="235" y="175" width="80" height="50" rx="6" fill="{t['danger']}"/>
  <text x="275" y="212" fill="#FFFFFF" font-size="32" font-weight="900" font-family="Montserrat" text-anchor="middle">99</text>
  <g font-family="Kaiti, STKaiti, serif" font-size="42" font-weight="900" fill="{t['accent']}" text-anchor="middle">
    <text x="275" y="285">期</text>
    <text x="275" y="345">专</text>
    <text x="275" y="405">刊</text>
  </g>
  {badge(185, 480, "纵中横排双位数字正置", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_218(): # 直排中西文转向 (Vertical Western Rotated 90°)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical Chinese Characters -->
  <text x="275" y="150" fill="{t['accent']}" font-size="36" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">解</text>
  <text x="275" y="195" fill="{t['accent']}" font-size="36" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">读</text>
  <!-- Western word 'DESIGN' rotated 90 degrees clockwise -->
  <g transform="translate(275, 300) rotate(90)">
    <rect x="-70" y="-20" width="140" height="40" rx="4" fill="{t['danger']}"/>
    <text x="0" y="8" fill="#FFFFFF" font-size="22" font-weight="900" font-family="Montserrat" text-anchor="middle">DESIGN</text>
  </g>
  <text x="275" y="420" fill="{t['accent']}" font-size="36" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">美</text>
  <text x="275" y="465" fill="{t['accent']}" font-size="36" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">学</text>
  {badge(185, 520, "直排中西文顺时针旋转90°", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_219(): # 直排中西文直立 (Vertical Western Upright Stacking)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Western acronym letters stacked upright one by one -->
  <g font-size="38" font-weight="900" font-family="Montserrat" text-anchor="middle" fill="{t['accent']}">
    <text x="275" y="150">A</text>
    <text x="275" y="195">G</text>
    <text x="275" y="240">E</text>
    <text x="275" y="285">N</text>
    <text x="275" y="330">T</text>
  </g>
  <g font-size="38" font-weight="900" font-family="Kaiti, serif" text-anchor="middle" fill="{t['accent_alt']}">
    <text x="275" y="390">体</text>
    <text x="275" y="440">系</text>
  </g>
  {badge(185, 480, "中西文字母逐一正立直排", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_220(): # 双向文字排版 (BiDi Layout)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- RTL Arabic / Hebrew band -->
  <rect x="80" y="140" width="390" height="80" rx="6" fill="{t['danger']}" opacity="0.85"/>
  <text x="440" y="190" fill="#FFFFFF" font-size="24" font-weight="bold" font-family="Arial" text-anchor="end">مرحبا بالعالم (RTL)</text>
  <!-- LTR English band -->
  <rect x="80" y="250" width="390" height="80" rx="6" fill="{t['accent']}"/>
  <text x="110" y="300" fill="{t['bg']}" font-size="24" font-weight="900" font-family="Montserrat">HELLO WORLD (LTR)</text>
  <!-- Opposing flow vectors -->
  <line x1="430" y1="120" x2="110" y2="120" stroke="{t['danger']}" stroke-width="3"/>
  <polygon points="110,120 125,112 125,128" fill="{t['danger']}"/>
  <line x1="110" y1="350" x2="430" y2="350" stroke="{t['accent']}" stroke-width="3"/>
  <polygon points="430,350 415,342 415,358" fill="{t['accent']}"/>
  {badge(185, 480, "阿文英文双向文字混合", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_221(): # 旁注（Ruby）排版 (Ruby / Furigana Annotation)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Main Hanzi Character -->
  <text x="275" y="290" fill="{t['accent']}" font-size="140" font-weight="900" font-family="Kaiti, STKaiti, serif" text-anchor="middle">排</text>
  <!-- Tiny Ruby / Furigana characters floating above hanzi -->
  <rect x="185" y="110" width="180" height="36" rx="6" fill="{t['danger']}"/>
  <text x="275" y="134" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">pái (RUBY)</text>
  <line x1="185" y1="160" x2="365" y2="160" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="275" y="410" fill="{t['text_dim']}" font-size="14" font-family="PingFang SC" text-anchor="middle">汉字上方注音/振假名对齐系统</text>
  {badge(185, 480, "汉字正上方注音旁注", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

CAT04_SVGS = {
    "168": gen_168, "169": gen_169, "172": gen_172, "173": gen_173, "174": gen_174,
    "175": gen_175, "176": gen_176, "177": gen_177, "178": gen_178, "179": gen_179,
    "180": gen_180, "181": gen_181, "183": gen_183, "184": gen_184, "185": gen_185,
    "186": gen_186, "187": gen_187, "188": gen_188, "189": gen_189, "190": gen_190,
    "191": gen_191, "192": gen_192, "193": gen_193, "194": gen_194, "196": gen_196,
    "197": gen_197, "198": gen_198, "200": gen_200, "201": gen_201, "203": gen_203,
    "204": gen_204, "205": gen_205, "206": gen_206, "207": gen_207, "208": gen_208,
    "209": gen_209, "210": gen_210, "211": gen_211, "213": gen_213, "214": gen_214,
    "215": gen_215, "216": gen_216, "217": gen_217, "218": gen_218, "219": gen_219,
    "220": gen_220, "221": gen_221,
    "170": gen_170, "171": gen_171, "182": gen_182, "195": gen_195, "199": gen_199,
    "202": gen_202, "212": gen_212
}


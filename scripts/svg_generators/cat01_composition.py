"""
SVG generators for Category 01: 构图逻辑 (001-086).
"""
import math
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_006(): # 矩形折入法构图 (Rectangle Inset)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Outer Frame -->
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2" rx="4"/>
  <!-- Golden Inset Rectangle (Ratio 0.618) -->
  <rect x="135" y="155" width="280" height="310" fill="#2E2822" stroke="{t['accent']}" stroke-width="2.5" rx="4"/>
  <!-- Fold Corner Accents -->
  <line x1="50" y1="60" x2="135" y2="155" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="500" y1="60" x2="415" y2="155" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="50" y1="560" x2="135" y2="465" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="500" y1="560" x2="415" y2="465" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <!-- Focal Core -->
  <circle cx="275" cy="310" r="40" fill="{t['accent']}" opacity="0.15"/>
  <circle cx="275" cy="310" r="16" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="4" fill="#FFFFFF"/>
  {badge(195, 490, "内嵌折入 · 景深聚合", t['accent'], t['bg'], 160, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_007(): # 奇数法则构图 (Rule of Odds)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Odd triad grouping (3 primary elements vs awkward even pair) -->
  <g stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="5,5">
    <line x1="160" y1="280" x2="275" y2="200"/>
    <line x1="275" y1="200" x2="390" y2="320"/>
    <line x1="160" y1="280" x2="390" y2="320"/>
  </g>
  <!-- Node 1 (Left) -->
  <circle cx="160" cy="280" r="42" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="160" cy="280" r="12" fill="{t['stroke']}"/>
  <text x="160" y="285" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">01</text>
  <!-- Node 2 (Apex Hero) -->
  <circle cx="275" cy="200" r="54" fill="{t['accent']}" opacity="0.2"/>
  <circle cx="275" cy="200" r="38" fill="{t['accent']}"/>
  <circle cx="275" cy="200" r="10" fill="#FFFFFF"/>
  <text x="275" y="205" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">02</text>
  <!-- Node 3 (Right) -->
  <circle cx="390" cy="320" r="46" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="390" cy="320" r="14" fill="{t['stroke']}"/>
  <text x="390" y="325" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">03</text>
  <!-- Triangle Tension Badge -->
  {badge(185, 450, "奇数组群 · 动态平衡", t['accent'], t['bg'], 180, 32)}
"""
    return wrap_svg(inner, t['bg'])

def gen_008(): # 空间法则构图 (Space Principle)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Vast Void Negative Space Field (80%) -->
  <rect x="40" y="50" width="470" height="520" fill="none" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <!-- Tension Arc Vector -->
  <path d="M 400 440 Q 200 420 120 150" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4" opacity="0.7"/>
  <polygon points="120,150 135,160 125,170" fill="{t['accent']}"/>
  <!-- Minimalist Micro Focal Element at Lower Right Third -->
  <circle cx="400" cy="440" r="32" fill="{t['accent']}"/>
  <circle cx="400" cy="440" r="8" fill="#FFFFFF"/>
  <!-- Negative Space Label -->
  <text x="220" y="260" fill="{t['text_dim']}" font-size="28" font-weight="900" font-family="Montserrat" opacity="0.4">NEGATIVE SPACE</text>
  <text x="220" y="295" fill="{t['text_dim']}" font-size="14" font-family="PingFang SC" opacity="0.5">留白即空间 · 气韵自然流淌</text>
  {badge(310, 500, "80% 呼吸留白", t['accent'], t['bg'], 150, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_009(): # 视线空间构图 (Gaze Space)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Portrait Profile on Left -->
  <path d="M 120 380 Q 150 260 150 200 Q 150 160 180 150 Q 200 150 190 190 Q 210 195 200 220 Q 185 240 190 260 L 160 380 Z" fill="{t['stroke']}"/>
  <circle cx="170" cy="200" r="6" fill="{t['accent']}"/>
  <!-- Gaze Trajectory Beam to Right Void -->
  <line x1="176" y1="200" x2="480" y2="200" stroke="{t['accent']}" stroke-width="3" stroke-linecap="round"/>
  <line x1="176" y1="180" x2="480" y2="180" stroke="{t['accent']}" stroke-width="1.2" stroke-dasharray="6,4" opacity="0.5"/>
  <line x1="176" y1="220" x2="480" y2="220" stroke="{t['accent']}" stroke-width="1.2" stroke-dasharray="6,4" opacity="0.5"/>
  <polygon points="485,200 465,190 465,210" fill="{t['accent']}"/>
  <!-- Open Field on Right -->
  <rect x="260" y="120" width="220" height="160" fill="{t['bg_surface']}" rx="6" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="370" y="195" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="PingFang SC" text-anchor="middle">视线开放空间</text>
  <text x="370" y="220" fill="{t['text_dim']}" font-size="11" font-family="Montserrat" text-anchor="middle">GAZE LEAD SPACE</text>
  {badge(100, 420, "主体前侧留白", t['accent'], t['bg'], 140, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_010(): # 运动空间构图 (Action / Lead Space)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- High velocity kinetic wedge moving right -->
  <polygon points="100,270 180,310 100,350 130,310" fill="{t['accent']}"/>
  <!-- Motion Trail Speed Lines -->
  <line x1="40" y1="290" x2="90" y2="290" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="20" y1="310" x2="110" y2="310" stroke="{t['accent']}" stroke-width="3.5"/>
  <line x1="50" y1="330" x2="90" y2="330" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Vast Forward Trajectory Field -->
  <line x1="190" y1="310" x2="490" y2="310" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="8,6"/>
  <polygon points="500,310 480,300 480,320" fill="{t['guide']}"/>
  <!-- Safe Runway Box -->
  <rect x="220" y="190" width="280" height="240" fill="none" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="6,4" rx="6"/>
  <text x="360" y="295" fill="{t['accent']}" font-size="16" font-weight="900" font-family="PingFang SC" text-anchor="middle">运动前方预留空间</text>
  <text x="360" y="325" fill="{t['text_dim']}" font-size="11" font-family="Montserrat" text-anchor="middle">LEAD ROOM / BUFFER</text>
  {badge(185, 480, "消除撞壁感 · 释放动势", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_011(): # 头部空间构图 (Headroom)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Viewfinder Frame -->
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2" rx="4"/>
  <!-- Headroom Dimension Guide -->
  {dimension_v(60, 180, 110, "HEADROOM", t['accent'], t['accent'])}
  <!-- Golden Upper Boundary -->
  <line x1="50" y1="180" x2="500" y2="180" stroke="{t['accent']}" stroke-width="1.8" stroke-dasharray="6,6"/>
  <!-- Portrait Silhouette -->
  <ellipse cx="275" cy="270" rx="65" ry="85" fill="{t['stroke']}"/>
  <path d="M 175 420 Q 275 370 375 420 L 390 560 L 160 560 Z" fill="{t['stroke']}"/>
  <!-- Calibrated Eye Line -->
  <line x1="200" y1="260" x2="350" y2="260" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="275" cy="260" r="4" fill="{t['accent']}"/>
  {badge(185, 95, "舒适顶空 1/4 - 1/3", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_012(): # 填满画面构图 (Fill the Frame)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Massive Macro Geometric Burst Overflowing Edges -->
  <rect x="30" y="40" width="490" height="540" fill="none" stroke="{t['accent']}" stroke-width="3" rx="4"/>
  <polygon points="-20,120 280,30 580,160 520,580 40,640" fill="{t['bg_surface']}" stroke="{t['stroke']}" stroke-width="2"/>
  <circle cx="275" cy="310" r="190" fill="{t['accent']}" opacity="0.15"/>
  <circle cx="275" cy="310" r="130" fill="{t['accent']}" opacity="0.3"/>
  <circle cx="275" cy="310" r="70" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="18" fill="#FFFFFF"/>
  <!-- Edge Burst Bleed Indicators -->
  <line x1="10" y1="310" x2="50" y2="310" stroke="{t['accent']}" stroke-width="3"/>
  <line x1="500" y1="310" x2="540" y2="310" stroke="{t['accent']}" stroke-width="3"/>
  <line x1="275" y1="20" x2="275" y2="60" stroke="{t['accent']}" stroke-width="3"/>
  <line x1="275" y1="560" x2="275" y2="600" stroke="{t['accent']}" stroke-width="3"/>
  {badge(185, 480, "无留白 · 满幅张力", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_013(): # 负空间构图 (Negative Space)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Interlocking Gestalt Figure-Ground -->
  <rect x="50" y="80" width="450" height="460" fill="{t['stroke']}" rx="6"/>
  <!-- Negative Space Carve Cutout -->
  <path d="M 275 80 C 200 180 200 240 230 300 C 250 340 250 400 180 540 L 370 540 C 300 400 300 340 320 300 C 350 240 350 180 275 80 Z" fill="{t['bg']}"/>
  <!-- Central White Nexus inside Void -->
  <circle cx="275" cy="270" r="18" fill="{t['accent']}"/>
  <circle cx="275" cy="270" r="5" fill="#FFFFFF"/>
  <text x="275" y="440" fill="{t['accent']}" font-size="16" font-weight="900" font-family="PingFang SC" text-anchor="middle">虚实相生 · 意在形外</text>
  {badge(195, 120, "正负形双重视觉", t['accent'], t['bg'], 160, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_014(): # 框中框构图 (Frame in Frame)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Heavy Outer Architectural Wall -->
  <rect x="40" y="50" width="470" height="520" fill="{t['stroke']}" rx="6"/>
  <!-- Inner Arch Frame Cutout -->
  <path d="M 120 570 L 120 250 A 155 155 0 0 1 430 250 L 430 570 Z" fill="{t['bg']}"/>
  <!-- Distant Scene Revealed Inside Frame -->
  <polygon points="150,520 275,340 400,520" fill="{t['bg_surface']}"/>
  <circle cx="275" cy="250" r="36" fill="{t['accent']}"/>
  <circle cx="275" cy="250" r="8" fill="#FFFFFF"/>
  <!-- Arch Frame Contour Line -->
  <path d="M 120 570 L 120 250 A 155 155 0 0 1 430 250 L 430 570" fill="none" stroke="{t['accent']}" stroke-width="3.5"/>
  {badge(185, 120, "次级几何边框聚焦", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_015(): # 引导线构图 (Leading Lines)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Vanishing convergence path from bottom corners to focal sun -->
  <polygon points="50,570 500,570 275,190" fill="{t['bg_surface']}"/>
  <line x1="50" y1="570" x2="275" y2="190" stroke="{t['accent']}" stroke-width="4"/>
  <line x1="160" y1="570" x2="275" y2="190" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="8,6"/>
  <line x1="275" y1="570" x2="275" y2="190" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="10,6"/>
  <line x1="390" y1="570" x2="275" y2="190" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="8,6"/>
  <line x1="500" y1="570" x2="275" y2="190" stroke="{t['accent']}" stroke-width="4"/>
  <!-- Horizon Line -->
  <line x1="30" y1="190" x2="520" y2="190" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <!-- Destination Anchor -->
  <circle cx="275" cy="190" r="50" fill="{t['accent']}" opacity="0.2"/>
  <circle cx="275" cy="190" r="22" fill="{t['accent']}"/>
  <circle cx="275" cy="190" r="6" fill="#FFFFFF"/>
  {badge(185, 110, "线条牵引 · 视线终点", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_020(): # 镜像构图 (Mirror / Reflection)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Waterline Divider at y=310 -->
  <line x1="30" y1="310" x2="520" y2="310" stroke="{t['accent']}" stroke-width="2.5"/>
  <!-- Upper Real Scene -->
  <polygon points="120,310 275,140 430,310" fill="{t['accent']}" opacity="0.85"/>
  <circle cx="275" cy="140" r="24" fill="{t['accent_alt']}"/>
  <circle cx="275" cy="140" r="6" fill="#FFFFFF"/>
  <!-- Lower Mirror Reflection Scene -->
  <polygon points="120,310 275,480 430,310" fill="{t['accent']}" opacity="0.35"/>
  <circle cx="275" cy="480" r="24" fill="{t['accent_alt']}" opacity="0.4"/>
  <!-- Water Distortion Ripples -->
  <line x1="160" y1="350" x2="390" y2="350" stroke="{t['accent_alt']}" stroke-width="1.5" stroke-dasharray="8,6" opacity="0.7"/>
  <line x1="200" y1="390" x2="350" y2="390" stroke="{t['accent_alt']}" stroke-width="1.5" stroke-dasharray="6,4" opacity="0.6"/>
  <line x1="230" y1="430" x2="320" y2="430" stroke="{t['accent_alt']}" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.5"/>
  {badge(185, 70, "水线对称 · 上实下虚", t['accent'], t['text'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_028(): # 偏轴构图 (Off-Axis)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Vertical Off-Axis Line at x=190 (Shifted Left 1/3) -->
  <line x1="190" y1="50" x2="190" y2="570" stroke="{t['accent']}" stroke-width="3"/>
  <line x1="275" y1="50" x2="275" y2="570" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <!-- Heavy Cantilevered Blocks on Right Field -->
  <rect x="230" y="140" width="260" height="110" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="4"/>
  <rect x="230" y="280" width="220" height="150" fill="{t['accent']}" opacity="0.8" rx="4"/>
  <!-- Primary Anchor Point on Off-Axis -->
  <circle cx="190" cy="200" r="22" fill="{t['danger']}"/>
  <circle cx="190" cy="200" r="6" fill="#FFFFFF"/>
  <text x="340" y="365" fill="#FFFFFF" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">悬臂色块平衡</text>
  {badge(80, 480, "偏轴杠杆平衡", t['accent'], t['text'], 150, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_029(): # 双轴构图 (Dual-Axis)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Dual Axes Intersecting at (275, 310) -->
  <line x1="40" y1="310" x2="510" y2="310" stroke="{t['accent']}" stroke-width="2.5"/>
  <line x1="275" y1="50" x2="275" y2="570" stroke="{t['accent']}" stroke-width="2.5"/>
  <!-- 4 Energetic Quadrants -->
  <rect x="70" y="90" width="170" height="180" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <rect x="310" y="90" width="170" height="180" fill="{t['accent']}" opacity="0.2" rx="4"/>
  <rect x="70" y="350" width="170" height="180" fill="{t['accent']}" opacity="0.2" rx="4"/>
  <rect x="310" y="350" width="170" height="180" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <!-- Central Axis Intersection Nexus -->
  <circle cx="275" cy="310" r="36" fill="{t['danger']}"/>
  <circle cx="275" cy="310" r="10" fill="#FFFFFF"/>
  {badge(195, 296, "十字双轴", t['danger'], "#FFFFFF", 160, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_031(): # X形构图 (X-Shape)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Dynamic X Diagonals Crossing at Center -->
  <line x1="60" y1="80" x2="490" y2="540" stroke="{t['accent']}" stroke-width="5" stroke-linecap="round"/>
  <line x1="490" y1="80" x2="60" y2="540" stroke="{t['accent']}" stroke-width="5" stroke-linecap="round"/>
  <!-- 4 Corner Terminal Nodes -->
  <circle cx="60" cy="80" r="16" fill="{t['stroke']}"/>
  <circle cx="490" cy="80" r="16" fill="{t['stroke']}"/>
  <circle cx="60" cy="540" r="16" fill="{t['stroke']}"/>
  <circle cx="490" cy="540" r="16" fill="{t['stroke']}"/>
  <!-- Central Intersection Epicenter -->
  <circle cx="275" cy="310" r="50" fill="{t['accent']}" opacity="0.25"/>
  <circle cx="275" cy="310" r="26" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="8" fill="#FFFFFF"/>
  {badge(185, 450, "X 型对角交汇", t['accent'], t['bg'], 180, 32)}
"""
    return wrap_svg(inner, t['bg'])

def gen_032(): # T形构图 (T-Shape)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Horizontal Lintel Crossbeam -->
  <rect x="50" y="100" width="450" height="70" fill="{t['accent']}" rx="6"/>
  <!-- Vertical Supportive Column Pillar -->
  <rect x="235" y="170" width="80" height="390" fill="{t['stroke']}" rx="4"/>
  <!-- Open Side Bays -->
  <rect x="50" y="190" width="165" height="370" fill="none" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6" rx="4"/>
  <rect x="335" y="190" width="165" height="370" fill="none" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6" rx="4"/>
  <!-- Focal Node at T Junction (275, 170) -->
  <circle cx="275" cy="170" r="28" fill="{t['accent_alt']}"/>
  <circle cx="275" cy="170" r="8" fill="#FFFFFF"/>
  {badge(195, 280, "T 型横梁支柱", t['accent'], t['bg'], 160, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_033(): # L形构图 (L-Shape)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Vertical Left Mast -->
  <rect x="60" y="70" width="90" height="470" fill="{t['accent']}" rx="6"/>
  <!-- Bottom Horizontal Base -->
  <rect x="60" y="450" width="430" height="90" fill="{t['accent']}" rx="6"/>
  <!-- Sheltered Open Arena at Upper Right -->
  <rect x="180" y="70" width="310" height="350" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,4" rx="6"/>
  <!-- Focal Element in L Corner -->
  <circle cx="220" cy="380" r="32" fill="{t['accent_alt']}"/>
  <circle cx="220" cy="380" r="10" fill="#FFFFFF"/>
  <text x="335" y="240" fill="{t['text_dim']}" font-size="16" font-family="PingFang SC" text-anchor="middle">L 型半包围主场</text>
  {badge(245, 480, "L 构架基底", t['bg'], t['text'], 160, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_034(): # V形构图 (V-Shape)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- V Shape Inward Funnel Wedge -->
  <polygon points="60,90 275,510 490,90 400,90 275,370 150,90" fill="{t['accent']}"/>
  <!-- Downward Guiding Vector Lines -->
  <line x1="80" y1="120" x2="275" y2="510" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="6,4" opacity="0.7"/>
  <line x1="470" y1="120" x2="275" y2="510" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="6,4" opacity="0.7"/>
  <!-- Bottom Apex Anchor -->
  <circle cx="275" cy="510" r="30" fill="{t['accent_alt']}"/>
  <circle cx="275" cy="510" r="8" fill="#FFFFFF"/>
  {badge(185, 250, "V 型下倾汇聚", t['accent_alt'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_036(): # C形构图 (C-Shape)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Sweeping C Crescent Path -->
  <path d="M 400 110 A 210 210 0 1 0 400 510" fill="none" stroke="{t['accent']}" stroke-width="32" stroke-linecap="round"/>
  <!-- Focal Harbor Nexus inside C Bay -->
  <circle cx="260" cy="310" r="50" fill="{t['accent_alt']}" opacity="0.2"/>
  <circle cx="260" cy="310" r="26" fill="{t['accent_alt']}"/>
  <circle cx="260" cy="310" r="8" fill="#FFFFFF"/>
  <text x="260" y="380" fill="{t['text']}" font-size="14" font-weight="bold" font-family="PingFang SC" text-anchor="middle">内弯视觉港湾</text>
  {badge(175, 450, "C 形环抱包围", t['accent'], t['bg'], 170, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_038(): # 曲线构图 (Curved Line)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Sinuous Meandering River / Path -->
  <path d="M 100 560 C 280 500 80 340 275 290 C 450 240 200 120 420 70" fill="none" stroke="{t['accent']}" stroke-width="14" stroke-linecap="round"/>
  <path d="M 100 560 C 280 500 80 340 275 290 C 450 240 200 120 420 70" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="8,6"/>
  <!-- Stepping Milestone Nodes along curve -->
  <circle cx="100" cy="560" r="14" fill="{t['accent_alt']}"/>
  <circle cx="275" cy="290" r="20" fill="{t['accent_alt']}"/>
  <circle cx="420" cy="70" r="26" fill="{t['accent']}"/>
  <circle cx="420" cy="70" r="8" fill="#FFFFFF"/>
  {badge(185, 450, "蜿蜒纵深游弋", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_039(): # 波浪形构图 (Wave Form)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Harmonic Repeating Sine Waves -->
  <path d="M 40 240 Q 110 160 180 240 T 320 240 T 460 240 T 520 240" fill="none" stroke="{t['accent']}" stroke-width="6" stroke-linecap="round"/>
  <path d="M 40 330 Q 110 250 180 330 T 320 330 T 460 330 T 520 330" fill="none" stroke="{t['accent_alt']}" stroke-width="4" stroke-linecap="round"/>
  <path d="M 40 420 Q 110 340 180 420 T 320 420 T 460 420 T 520 420" fill="none" stroke="{t['stroke']}" stroke-width="3" stroke-linecap="round"/>
  <!-- Crest and Trough Amplitude Markers -->
  <circle cx="110" cy="200" r="10" fill="{t['accent']}"/>
  <circle cx="250" cy="200" r="10" fill="{t['accent']}"/>
  <circle cx="390" cy="200" r="10" fill="{t['accent']}"/>
  {badge(185, 480, "波浪律动韵律", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_040(): # 螺旋形构图 (Spiral Form)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Archimedean / Inward Vortex Curve -->
  <path d="M 275 310 A 30 30 0 0 1 295 340 A 60 60 0 0 1 235 370 A 100 100 0 0 1 175 260 A 150 150 0 0 1 355 190 A 210 210 0 0 1 450 420" fill="none" stroke="{t['accent']}" stroke-width="4.5" stroke-linecap="round"/>
  <!-- Central Inward Epicenter -->
  <circle cx="275" cy="310" r="40" fill="{t['accent']}" opacity="0.2"/>
  <circle cx="275" cy="310" r="18" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="5" fill="#FFFFFF"/>
  {badge(185, 490, "螺旋向心吸入", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])


def gen_042(): # 金字塔构图 (Pyramid)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Monumental Stepped Pyramid -->
  <polygon points="275,110 90,490 460,490" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2.5"/>
  <!-- Tier Horizontal Strata -->
  <line x1="220" y1="220" x2="330" y2="220" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="165" y1="330" x2="385" y2="330" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="120" y1="420" x2="430" y2="420" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Radiant Apex Crown -->
  <circle cx="275" cy="110" r="38" fill="{t['accent']}" opacity="0.2"/>
  <circle cx="275" cy="110" r="18" fill="{t['accent']}"/>
  <circle cx="275" cy="110" r="5" fill="#FFFFFF"/>
  <!-- Apex Rays -->
  <line x1="275" y1="50" x2="275" y2="80" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="220" y1="70" x2="245" y2="90" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="330" y1="70" x2="305" y2="90" stroke="{t['accent']}" stroke-width="2"/>
  {badge(185, 520, "金字塔稳固基座", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_043(): # 倒三角构图 (Inverted Triangle)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Inverted Triangular Wedge balancing on bottom apex -->
  <polygon points="60,110 490,110 275,510" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Unstable Balance Fulcrum Point (275, 510) -->
  <circle cx="275" cy="510" r="30" fill="{t['danger']}" opacity="0.25"/>
  <circle cx="275" cy="510" r="16" fill="{t['danger']}"/>
  <circle cx="275" cy="510" r="4" fill="#FFFFFF"/>
  <!-- Center of Mass Tension Line -->
  <line x1="275" y1="110" x2="275" y2="510" stroke="{t['accent_alt']}" stroke-width="1.8" stroke-dasharray="6,4"/>
  <!-- Mass Top Load Blocks -->
  <rect x="140" y="150" width="270" height="70" fill="{t['accent']}" opacity="0.8" rx="4"/>
  <text x="275" y="192" fill="{t['bg']}" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">顶重底尖 · 极端张力</text>
  {badge(185, 540, "临界平衡点", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_044(): # 菱形构图 (Diamond / Rhombus)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Diamond Rhombus 4 Vertices -->
  <polygon points="275,70 480,310 275,550 70,310" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Inner Rhombus Grid -->
  <line x1="275" y1="70" x2="275" y2="550" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <line x1="70" y1="310" x2="480" y2="310" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <!-- 4 Acute Point Nodes -->
  <circle cx="275" cy="70" r="12" fill="{t['accent']}"/>
  <circle cx="480" cy="310" r="12" fill="{t['accent']}"/>
  <circle cx="275" cy="550" r="12" fill="{t['accent']}"/>
  <circle cx="70" cy="310" r="12" fill="{t['accent']}"/>
  <!-- Central Diamond Core -->
  <polygon points="275,220 355,310 275,400 195,310" fill="{t['accent']}" opacity="0.3"/>
  <circle cx="275" cy="310" r="14" fill="#FFFFFF"/>
  {badge(185, 300, "菱形聚气", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_045(): # 梯形构图 (Trapezoid)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Perspective Architectural Trapezoid -->
  <polygon points="170,120 380,120 480,520 70,520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2.5"/>
  <!-- Internal Horizontal Tiers -->
  <line x1="145" y1="220" x2="405" y2="220" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="120" y1="320" x2="430" y2="320" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="95" y1="420" x2="455" y2="420" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <!-- Skyward Vanishing Vectors -->
  <line x1="70" y1="520" x2="275" y2="30" stroke="{t['accent_alt']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  <line x1="480" y1="520" x2="275" y2="30" stroke="{t['accent_alt']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  {badge(185, 470, "梯形纵深延伸", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_046(): # 矩形构图 (Rectangle)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Harmonic Golden Rectangles Nested -->
  <rect x="60" y="80" width="430" height="460" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2.5" rx="4"/>
  <rect x="110" y="130" width="330" height="360" fill="none" stroke="{t['accent_alt']}" stroke-width="1.8" stroke-dasharray="6,4" rx="4"/>
  <rect x="160" y="180" width="230" height="260" fill="{t['accent']}" opacity="0.2" rx="4"/>
  <!-- Center Core -->
  <circle cx="275" cy="310" r="16" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="4" fill="#FFFFFF"/>
  {dimension_h(60, 490, 60, "430 px", t['accent'], t['accent'])}
  {dimension_v(80, 540, 510, "460 px", t['accent'], t['accent'])}
  {badge(185, 360, "矩形比例模度", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_048(): # 椭圆构图 (Ellipse)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Tilted Orbital Ellipse (Keplerian Orbit) -->
  <g transform="rotate(-25 275 310)">
    <ellipse cx="275" cy="310" rx="220" ry="120" fill="none" stroke="{t['accent']}" stroke-width="3"/>
    <!-- Major & Minor Axes -->
    <line x1="55" y1="310" x2="495" y2="310" stroke="{t['guide']}" stroke-width="1.2" stroke-dasharray="6,6"/>
    <line x1="275" y1="190" x2="275" y2="430" stroke="{t['guide']}" stroke-width="1.2" stroke-dasharray="6,6"/>
    <!-- Twin Orbital Foci -->
    <circle cx="160" cy="310" r="14" fill="{t['danger']}"/>
    <circle cx="160" cy="310" r="4" fill="#FFFFFF"/>
    <circle cx="390" cy="310" r="14" fill="{t['accent_alt']}"/>
    <circle cx="390" cy="310" r="4" fill="#FFFFFF"/>
    <!-- Satellite Element -->
    <circle cx="440" cy="230" r="18" fill="{t['accent']}"/>
  </g>
  {badge(185, 520, "开普勒双焦点轨道", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_049(): # 弧形构图 (Arc)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Dynamic Vaulting Parabolic Bridge Arc -->
  <path d="M 50 510 Q 275 90 500 510" fill="none" stroke="{t['accent']}" stroke-width="6" stroke-linecap="round"/>
  <!-- Arc Supportive Ribs -->
  <line x1="140" y1="370" x2="140" y2="510" stroke="{t['stroke']}" stroke-width="2"/>
  <line x1="210" y1="240" x2="210" y2="510" stroke="{t['stroke']}" stroke-width="2"/>
  <line x1="275" y1="195" x2="275" y2="510" stroke="{t['accent_alt']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <line x1="340" y1="240" x2="340" y2="510" stroke="{t['stroke']}" stroke-width="2"/>
  <line x1="410" y1="370" x2="410" y2="510" stroke="{t['stroke']}" stroke-width="2"/>
  <!-- Keystone Apex Anchor (275, 195) -->
  <circle cx="275" cy="195" r="24" fill="{t['accent']}"/>
  <circle cx="275" cy="195" r="6" fill="#FFFFFF"/>
  {badge(185, 470, "跨度飞拱结构", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_050(): # 环形构图 (Ring / Torus)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Donut Ring Geometry -->
  <circle cx="275" cy="310" r="180" fill="none" stroke="{t['stroke']}" stroke-width="40"/>
  <circle cx="275" cy="310" r="180" fill="none" stroke="{t['accent']}" stroke-width="6"/>
  <!-- Inner Ring Void Center -->
  <circle cx="275" cy="310" r="130" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <!-- Ring Orbit Beads -->
  <circle cx="275" cy="130" r="16" fill="{t['accent_alt']}"/>
  <circle cx="455" cy="310" r="16" fill="{t['accent']}"/>
  <circle cx="275" cy="490" r="16" fill="{t['accent_alt']}"/>
  <circle cx="95" cy="310" r="16" fill="{t['danger']}"/>
  {badge(185, 295, "环形周转 · 中心虚空", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_051(): # 螺旋构图 (Archimedean Spiral)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Equidistant Coil Archimedean Spiral -->
  <path d="M 275 310 A 25 25 0 0 1 275 360 A 50 50 0 0 1 225 310 A 75 75 0 0 1 275 235 A 100 100 0 0 1 375 310 A 130 130 0 0 1 275 440 A 165 165 0 0 1 110 310 A 200 200 0 0 1 275 110" fill="none" stroke="{t['accent']}" stroke-width="3.5" stroke-linecap="round"/>
  <!-- Radial Ray Degree Guides -->
  <line x1="75" y1="310" x2="475" y2="310" stroke="{t['guide']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  <line x1="275" y1="110" x2="275" y2="510" stroke="{t['guide']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  <circle cx="275" cy="310" r="14" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="4" fill="#FFFFFF"/>
  {badge(185, 480, "阿基米德匀速展开", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_052(): # 放射构图 (Radial / Burst)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Radial Ray Beam Burst from Epicenter (275, 310) -->
  <g stroke="{t['accent']}" stroke-width="2">
    <line x1="275" y1="310" x2="50" y2="80"/>
    <line x1="275" y1="310" x2="275" y2="50"/>
    <line x1="275" y1="310" x2="500" y2="80"/>
    <line x1="275" y1="310" x2="520" y2="310"/>
    <line x1="275" y1="310" x2="500" y2="540"/>
    <line x1="275" y1="310" x2="275" y2="570"/>
    <line x1="275" y1="310" x2="50" y2="540"/>
    <line x1="275" y1="310" x2="30" y2="310"/>
    <!-- Interstitial Fine Beams -->
    <line x1="275" y1="310" x2="160" y2="60" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="275" y1="310" x2="390" y2="60" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="275" y1="310" x2="520" y2="200" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="275" y1="310" x2="520" y2="420" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="275" y1="310" x2="390" y2="560" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="275" y1="310" x2="160" y2="560" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="275" y1="310" x2="30" y2="420" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="275" y1="310" x2="30" y2="200" stroke="{t['accent_alt']}" stroke-width="1" stroke-dasharray="4,4"/>
  </g>
  <!-- Solar Burst Core -->
  <circle cx="275" cy="310" r="50" fill="{t['accent']}" opacity="0.25"/>
  <circle cx="275" cy="310" r="26" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="8" fill="#FFFFFF"/>
  {badge(185, 470, "全向放射爆发", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_053(): # 向心构图 (Centripetal)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Inward Converging Arrows Pointing to Epicenter (275, 310) -->
  <line x1="80" y1="120" x2="220" y2="260" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="225,265 210,250 230,245" fill="{t['accent']}"/>
  <line x1="470" y1="120" x2="330" y2="260" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="325,265 340,245 320,250" fill="{t['accent']}"/>
  <line x1="80" y1="500" x2="220" y2="360" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="225,355 210,370 230,375" fill="{t['accent']}"/>
  <line x1="470" y1="500" x2="330" y2="360" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="325,355 340,375 320,370" fill="{t['accent']}"/>
  <!-- Concentric Rings Contracted Inward -->
  <circle cx="275" cy="310" r="160" fill="none" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <circle cx="275" cy="310" r="90" fill="none" stroke="{t['accent_alt']}" stroke-width="1.8" stroke-dasharray="4,4"/>
  <!-- Dense Inward Singularity Core -->
  <circle cx="275" cy="310" r="32" fill="{t['danger']}"/>
  <circle cx="275" cy="310" r="8" fill="#FFFFFF"/>
  {badge(185, 470, "向心引力坍缩", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_054(): # 离心构图 (Centrifugal)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Elements flying outward past frame boundaries -->
  <circle cx="275" cy="310" r="40" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2"/>
  <!-- Outward Kinetic Vectors -->
  <line x1="275" y1="270" x2="275" y2="70" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="275,60 265,80 285,80" fill="{t['accent']}"/>
  <line x1="310" y1="310" x2="510" y2="310" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="520,310 500,300 500,320" fill="{t['accent']}"/>
  <line x1="275" y1="350" x2="275" y2="550" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="275,560 265,540 285,540" fill="{t['accent']}"/>
  <line x1="240" y1="310" x2="40" y2="310" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="30,310 50,300 50,320" fill="{t['accent']}"/>
  <!-- Flying Particle Rectangles -->
  <rect x="360" y="160" width="40" height="40" fill="{t['accent_alt']}" transform="rotate(25 380 180)"/>
  <rect x="140" y="420" width="35" height="35" fill="{t['accent_alt']}" transform="rotate(-15 157 437)"/>
  {badge(185, 295, "离心向外发散", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_055(): # 同心式构图 (Concentric Circles)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Calibrated Concentric Target Rings -->
  <circle cx="275" cy="310" r="220" fill="none" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="275" cy="310" r="165" fill="none" stroke="{t['stroke']}" stroke-width="2" stroke-dasharray="6,6"/>
  <circle cx="275" cy="310" r="110" fill="none" stroke="{t['accent_alt']}" stroke-width="2.5"/>
  <circle cx="275" cy="310" r="55" fill="{t['accent']}" opacity="0.3"/>
  <!-- Center Bullseye -->
  <circle cx="275" cy="310" r="22" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="6" fill="#FFFFFF"/>
  <!-- Crosshair Radial Lines -->
  <line x1="55" y1="310" x2="495" y2="310" stroke="{t['accent']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  <line x1="275" y1="90" x2="275" y2="530" stroke="{t['accent']}" stroke-width="1.2" stroke-dasharray="4,4"/>
  {badge(185, 480, "等距同心波纹", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_056(): # 四象限构图 (Four Quadrants)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Cartesian Coordinate Cross (x=275, y=310) -->
  <line x1="40" y1="310" x2="510" y2="310" stroke="{t['accent']}" stroke-width="2.5"/>
  <line x1="275" y1="50" x2="275" y2="570" stroke="{t['accent']}" stroke-width="2.5"/>
  <!-- Axis Arrowheads -->
  <polygon points="515,310 500,302 500,318" fill="{t['accent']}"/>
  <polygon points="275,45 267,60 283,60" fill="{t['accent']}"/>
  <!-- Quadrant Panels -->
  <!-- Q1 Top Right -->
  <rect x="295" y="80" width="190" height="210" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <circle cx="390" cy="185" r="28" fill="{t['accent']}"/>
  <text x="390" y="240" fill="{t['accent']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">QUADRANT I</text>
  <!-- Q2 Top Left -->
  <rect x="65" y="80" width="190" height="210" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <rect x="135" y="155" width="50" height="50" fill="{t['accent_alt']}" rx="4"/>
  <text x="160" y="240" fill="{t['accent_alt']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">QUADRANT II</text>
  <!-- Q3 Bottom Left -->
  <rect x="65" y="330" width="190" height="210" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <polygon points="160,390 190,440 130,440" fill="{t['stroke']}"/>
  <text x="160" y="490" fill="{t['text_dim']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">QUADRANT III</text>
  <!-- Q4 Bottom Right -->
  <rect x="295" y="330" width="190" height="210" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <circle cx="390" cy="425" r="22" fill="{t['danger']}"/>
  <text x="390" y="490" fill="{t['danger']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">QUADRANT IV</text>
  <!-- Center Origin Marker -->
  <circle cx="275" cy="310" r="10" fill="#FFFFFF"/>
"""
    return wrap_svg(inner, t['bg'])

def gen_058(): # 阶梯构图 (Stepped)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Ascending Geometric Terraced Steps -->
  <path d="M 60 520 L 170 520 L 170 420 L 280 420 L 280 320 L 390 320 L 390 220 L 490 220 L 490 520 Z" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2.5"/>
  <!-- Step Highlights -->
  <rect x="60" y="490" width="110" height="30" fill="{t['stroke']}"/>
  <rect x="170" y="390" width="110" height="30" fill="{t['accent_alt']}" opacity="0.6"/>
  <rect x="280" y="290" width="110" height="30" fill="{t['accent']}" opacity="0.8"/>
  <rect x="390" y="190" width="100" height="30" fill="{t['accent']}"/>
  <!-- Upward Progression Vector -->
  <line x1="80" y1="460" x2="460" y2="150" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="6,4"/>
  <polygon points="465,145 445,150 455,165" fill="#FFFFFF"/>
  <!-- Apex Summit Anchor -->
  <circle cx="440" cy="190" r="20" fill="{t['accent']}"/>
  <circle cx="440" cy="190" r="6" fill="#FFFFFF"/>
  {badge(185, 470, "阶梯递进上扬", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_059(): # 层叠构图 (Overlapping)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Staggered Overlapping Translucent Cards -->
  <rect x="70" y="100" width="260" height="320" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2"/>
  <rect x="145" y="160" width="260" height="320" rx="8" fill="#1E2330" stroke="{t['accent_alt']}" stroke-width="2" opacity="0.9"/>
  <rect x="220" y="220" width="260" height="320" rx="8" fill="{t['accent']}" opacity="0.85" rx="8"/>
  <!-- Drop Shadow Accent Lines -->
  <line x1="220" y1="220" x2="220" y2="480" stroke="#000000" stroke-width="4" opacity="0.4"/>
  <line x1="145" y1="160" x2="145" y2="420" stroke="#000000" stroke-width="4" opacity="0.4"/>
  <circle cx="350" cy="380" r="28" fill="#FFFFFF"/>
  <circle cx="350" cy="380" r="8" fill="{t['bg']}"/>
  {badge(185, 70, "多重景深层叠", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_060(): # 级联构图 (Cascade)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Waterfall Cascading Panels -->
  <g stroke="{t['accent']}" stroke-width="2">
    <rect x="60" y="80" width="280" height="110" rx="6" fill="{t['bg_surface']}"/>
    <rect x="130" y="210" width="280" height="110" rx="6" fill="{t['bg_surface']}"/>
    <rect x="200" y="340" width="280" height="110" rx="6" fill="{t['accent']}" fill-opacity="0.2"/>
  </g>
  <!-- Connecting Waterfall Curves -->
  <path d="M 200 190 Q 200 210 230 210" fill="none" stroke="{t['accent_alt']}" stroke-width="3"/>
  <path d="M 270 320 Q 270 340 300 340" fill="none" stroke="{t['accent_alt']}" stroke-width="3"/>
  <!-- Cascade Milestone Nodes -->
  <circle cx="200" cy="135" r="14" fill="{t['stroke']}"/>
  <circle cx="270" cy="265" r="16" fill="{t['accent_alt']}"/>
  <circle cx="340" cy="395" r="22" fill="{t['accent']}"/>
  <circle cx="340" cy="395" r="6" fill="#FFFFFF"/>
  {badge(185, 480, "级联错位跌落", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_061(): # 聚类构图 (Cluster)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Dense Planetary Cluster of Varied Circles -->
  <circle cx="250" cy="290" r="65" fill="{t['accent']}"/>
  <circle cx="250" cy="290" r="16" fill="#FFFFFF"/>
  <circle cx="340" cy="240" r="42" fill="{t['accent_alt']}"/>
  <circle cx="180" cy="230" r="34" fill="{t['stroke']}"/>
  <circle cx="310" cy="380" r="48" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="190" cy="360" r="36" fill="{t['stroke']}"/>
  <circle cx="380" cy="330" r="24" fill="{t['danger']}"/>
  <circle cx="260" cy="190" r="20" fill="{t['accent_alt']}"/>
  <!-- Vast Void Negative Perimeter -->
  <rect x="50" y="60" width="450" height="500" fill="none" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6" rx="6"/>
  {badge(185, 490, "群聚密实 · 外围虚空", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_062(): # 分散构图 (Dispersed)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Controlled Harmonic Dispersal of Elements -->
  <g fill="{t['accent']}">
    <circle cx="110" cy="130" r="20"/>
    <circle cx="430" cy="110" r="16"/>
    <circle cx="260" cy="170" r="14" fill="{t['accent_alt']}"/>
    <circle cx="140" cy="280" r="24" fill="{t['stroke']}"/>
    <circle cx="410" cy="270" r="28"/>
    <circle cx="230" cy="380" r="18"/>
    <circle cx="360" cy="420" r="16" fill="{t['accent_alt']}"/>
    <circle cx="120" cy="480" r="22" fill="{t['danger']}"/>
    <circle cx="450" cy="490" r="18"/>
  </g>
  <!-- Delicate Connecting Tension Lines -->
  <line x1="110" y1="130" x2="260" y2="170" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="260" y1="170" x2="430" y2="110" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="140" y1="280" x2="410" y2="270" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="230" y1="380" x2="360" y2="420" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  {badge(185, 70, "离散平衡 · 呼吸间距", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_063(): # 分支构图 (Branching)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Dendritic Tree Branching System -->
  <path d="M 275 560 L 275 360 L 160 220 L 100 110 M 160 220 L 220 110 M 275 360 L 390 220 L 340 110 M 390 220 L 450 110" fill="none" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <!-- Leaf Endpoint Nodes -->
  <circle cx="100" cy="110" r="16" fill="{t['accent_alt']}"/>
  <circle cx="220" cy="110" r="16" fill="{t['accent']}"/>
  <circle cx="340" cy="110" r="16" fill="{t['accent_alt']}"/>
  <circle cx="450" cy="110" r="16" fill="{t['danger']}"/>
  <!-- Trunk Solid Base -->
  <rect x="255" y="520" width="40" height="60" fill="{t['stroke']}"/>
  {badge(185, 460, "树状分支递解", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_064(): # 网络构图 (Network)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Constellation Mesh Network -->
  <g stroke="{t['accent_alt']}" stroke-width="1.5" opacity="0.6">
    <line x1="120" y1="150" x2="275" y2="110"/>
    <line x1="275" y1="110" x2="430" y2="160"/>
    <line x1="120" y1="150" x2="180" y2="280"/>
    <line x1="275" y1="110" x2="275" y2="290"/>
    <line x1="430" y1="160" x2="370" y2="290"/>
    <line x1="180" y1="280" x2="275" y2="290"/>
    <line x1="275" y1="290" x2="370" y2="290"/>
    <line x1="180" y1="280" x2="140" y2="440"/>
    <line x1="275" y1="290" x2="275" y2="450"/>
    <line x1="370" y1="290" x2="410" y2="430"/>
    <line x1="140" y1="440" x2="275" y2="450"/>
    <line x1="275" y1="450" x2="410" y2="430"/>
  </g>
  <!-- Network Graph Nodes -->
  <circle cx="120" cy="150" r="12" fill="{t['stroke']}"/>
  <circle cx="275" cy="110" r="16" fill="{t['accent_alt']}"/>
  <circle cx="430" cy="160" r="12" fill="{t['stroke']}"/>
  <circle cx="180" cy="280" r="14" fill="{t['stroke']}"/>
  <!-- Central Hub Nexus -->
  <circle cx="275" cy="290" r="32" fill="{t['accent']}" opacity="0.25"/>
  <circle cx="275" cy="290" r="18" fill="{t['accent']}"/>
  <circle cx="275" cy="290" r="5" fill="#FFFFFF"/>
  <circle cx="370" cy="290" r="14" fill="{t['stroke']}"/>
  <circle cx="140" cy="440" r="14" fill="{t['stroke']}"/>
  <circle cx="275" cy="450" r="16" fill="{t['danger']}"/>
  <circle cx="410" cy="430" r="14" fill="{t['stroke']}"/>
  {badge(185, 520, "网状拓扑节点", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_068(): # 线性透视 (Linear Perspective)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Floor Perspective Grid Receding to Vanishing Point (275, 230) -->
  <polygon points="40,570 510,570 275,230" fill="{t['bg_surface']}"/>
  <g stroke="{t['accent']}" stroke-width="1.8">
    <line x1="40" y1="570" x2="275" y2="230"/>
    <line x1="130" y1="570" x2="275" y2="230"/>
    <line x1="220" y1="570" x2="275" y2="230"/>
    <line x1="275" y1="570" x2="275" y2="230" stroke="#FFFFFF" stroke-dasharray="6,4"/>
    <line x1="330" y1="570" x2="275" y2="230"/>
    <line x1="420" y1="570" x2="275" y2="230"/>
    <line x1="510" y1="570" x2="275" y2="230"/>
  </g>
  <!-- Transverse Perspective Floor Transverses -->
  <line x1="75" y1="520" x2="475" y2="520" stroke="{t['accent']}" stroke-width="1.5"/>
  <line x1="115" y1="460" x2="435" y2="460" stroke="{t['accent']}" stroke-width="1.5"/>
  <line x1="160" y1="390" x2="390" y2="390" stroke="{t['accent']}" stroke-width="1.2"/>
  <line x1="210" y1="310" x2="340" y2="310" stroke="{t['accent']}" stroke-width="1"/>
  <!-- Horizon Line -->
  <line x1="30" y1="230" x2="520" y2="230" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="6,6"/>
  <!-- Vanishing Point Sun -->
  <circle cx="275" cy="230" r="36" fill="{t['accent']}" opacity="0.25"/>
  <circle cx="275" cy="230" r="14" fill="{t['accent']}"/>
  <circle cx="275" cy="230" r="4" fill="#FFFFFF"/>
  {badge(185, 120, "一点单灭点透视", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_071(): # 等轴测构图 (Isometric)
    t = get_theme("forest-green")
    inner = f"""
  <!-- 30-Degree Axonometric Isometric Cubes -->
  <!-- Cube 1 (Center) -->
  <g transform="translate(275, 290)">
    <!-- Top Face -->
    <polygon points="0,-70 60,-35 0,0 -60,-35" fill="{t['accent']}"/>
    <!-- Left Face -->
    <polygon points="-60,-35 0,0 0,70 -60,35" fill="{t['accent_alt']}"/>
    <!-- Right Face -->
    <polygon points="0,0 60,-35 60,35 0,70" fill="{t['stroke']}"/>
  </g>
  <!-- Cube 2 (Left Lower) -->
  <g transform="translate(175, 410)">
    <polygon points="0,-50 45,-25 0,0 -45,-25" fill="{t['accent']}" opacity="0.7"/>
    <polygon points="-45,-25 0,0 0,50 -45,25" fill="{t['accent_alt']}" opacity="0.7"/>
    <polygon points="0,0 45,-25 45,25 0,50" fill="{t['stroke']}" opacity="0.7"/>
  </g>
  <!-- Cube 3 (Right Lower) -->
  <g transform="translate(375, 410)">
    <polygon points="0,-50 45,-25 0,0 -45,-25" fill="{t['accent']}" opacity="0.7"/>
    <polygon points="-45,-25 0,0 0,50 -45,25" fill="{t['accent_alt']}" opacity="0.7"/>
    <polygon points="0,0 45,-25 45,25 0,50" fill="{t['stroke']}" opacity="0.7"/>
  </g>
  <!-- Isometric 30-deg grid guidelines -->
  <line x1="50" y1="440" x2="500" y2="180" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="6,6"/>
  <line x1="50" y1="180" x2="500" y2="440" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="6,6"/>
  {badge(185, 80, "30° 等轴测无衰减", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_077(): # 俯瞰/上帝视角 (Bird's Eye)
    t = get_theme("forest-green")
    inner = f"""
  <!-- 90-Degree Orthogonal Map Plan View -->
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2" rx="6"/>
  <!-- Street / Corridor Grid Lines -->
  <rect x="100" y="110" width="140" height="170" fill="{t['stroke']}" rx="4"/>
  <rect x="280" y="110" width="170" height="170" fill="{t['stroke']}" rx="4"/>
  <rect x="100" y="320" width="140" height="190" fill="{t['stroke']}" rx="4"/>
  <rect x="280" y="320" width="170" height="190" fill="{t['stroke']}" rx="4"/>
  <!-- Crossroad Intersection (x=260, y=300) -->
  <circle cx="260" cy="300" r="32" fill="{t['accent']}" opacity="0.25"/>
  <circle cx="260" cy="300" r="16" fill="{t['accent']}"/>
  <circle cx="260" cy="300" r="4" fill="#FFFFFF"/>
  <!-- Top-down view compass -->
  <polygon points="460,90 455,110 465,110" fill="{t['danger']}"/>
  <text x="460" y="85" fill="{t['danger']}" font-size="10" font-weight="900" text-anchor="middle">N</text>
  {badge(185, 490, "90° 垂直俯瞰全景", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_078(): # 仰视/巨像视角 (Worm's Eye)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Towering Monolith converging into sky zenith -->
  <polygon points="70,570 480,570 340,90 210,90" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Vertical Soaring Grid Lines -->
  <line x1="160" y1="570" x2="245" y2="90" stroke="{t['accent_alt']}" stroke-width="1.8"/>
  <line x1="275" y1="570" x2="275" y2="90" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="6,4"/>
  <line x1="390" y1="570" x2="305" y2="90" stroke="{t['accent_alt']}" stroke-width="1.8"/>
  <!-- Sky Zenith Apex Beacon -->
  <circle cx="275" cy="90" r="30" fill="{t['accent']}" opacity="0.3"/>
  <circle cx="275" cy="90" r="14" fill="{t['accent']}"/>
  <circle cx="275" cy="90" r="4" fill="#FFFFFF"/>
  {badge(185, 520, "低机位巨像仰角", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_080(): # 荷兰角倾斜 (Dutch Angle)
    t = get_theme("forest-green")
    inner = f"""
  <!-- 15-Degree Tilted Frame -->
  <g transform="rotate(15 275 310)">
    <rect x="60" y="90" width="430" height="440" fill="{t['bg_surface']}" stroke="{t['danger']}" stroke-width="3" rx="6"/>
    <!-- Horizon Canted -->
    <line x1="40" y1="310" x2="510" y2="310" stroke="{t['accent']}" stroke-width="3"/>
    <circle cx="275" cy="250" r="28" fill="{t['danger']}"/>
    <circle cx="275" cy="250" r="8" fill="#FFFFFF"/>
  </g>
  <!-- True Level Reference Dashed Line -->
  <line x1="30" y1="310" x2="520" y2="310" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="8,6" opacity="0.5"/>
  <text x="440" y="300" fill="#FFFFFF" font-size="11" font-family="Montserrat" opacity="0.7">HORIZON 0°</text>
  {badge(185, 480, "15° 倾斜失衡心理张力", t['danger'], "#FFFFFF", 190, 30)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat01
CAT01_SVGS = {
    "006": gen_006, "007": gen_007, "008": gen_008, "009": gen_009, "010": gen_010,
    "011": gen_011, "012": gen_012, "013": gen_013, "014": gen_014, "015": gen_015,
    "020": gen_020, "028": gen_028, "029": gen_029, "031": gen_031, "032": gen_032,
    "033": gen_033, "034": gen_034, "036": gen_036, "038": gen_038, "039": gen_039,
    "040": gen_040, "042": gen_042, "043": gen_043, "044": gen_044, "045": gen_045,
    "046": gen_046, "048": gen_048, "049": gen_049, "050": gen_050, "051": gen_051,
    "052": gen_052, "053": gen_053, "054": gen_054, "055": gen_055, "056": gen_056,
    "058": gen_058, "059": gen_059, "060": gen_060, "061": gen_061, "062": gen_062,
    "063": gen_063, "064": gen_064, "068": gen_068, "071": gen_071, "077": gen_077,
    "078": gen_078, "080": gen_080
}


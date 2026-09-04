"""
SVG generators for Category 02: 视觉原则与格式塔 (087-133).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_087(): # 对称平衡 (Symmetrical Balance)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Fulcrum balance beam on center axis (x=275, y=360) -->
  <line x1="100" y1="360" x2="450" y2="360" stroke="{t['accent']}" stroke-width="3"/>
  <polygon points="275,360 255,410 295,410" fill="{t['stroke']}"/>
  <!-- Left Weight Block -->
  <rect x="120" y="240" width="100" height="120" fill="{t['accent']}" rx="6"/>
  <circle cx="170" cy="300" r="16" fill="#FFFFFF"/>
  <!-- Right Identical Weight Block -->
  <rect x="330" y="240" width="100" height="120" fill="{t['accent']}" rx="6"/>
  <circle cx="380" cy="300" r="16" fill="#FFFFFF"/>
  <!-- Center Vertical Axis Guide -->
  <line x1="275" y1="80" x2="275" y2="520" stroke="{t['guide']}" stroke-width="1.8" stroke-dasharray="6,6"/>
  {badge(185, 470, "均等对称静态平衡", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_088(): # 非对称平衡 (Asymmetrical Balance)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Fulcrum at center x=275, y=360 -->
  <line x1="70" y1="360" x2="480" y2="360" stroke="{t['accent']}" stroke-width="3"/>
  <polygon points="275,360 255,410 295,410" fill="{t['stroke']}"/>
  <!-- Large Light Low-Density Area on Left (Close to fulcrum) -->
  <rect x="110" y="160" width="140" height="200" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2" rx="6"/>
  <text x="180" y="265" fill="{t['text_dim']}" font-size="14" font-family="Montserrat" text-anchor="middle">LARGE / LIGHT</text>
  <!-- Small Dense High-Contrast Red Anchor on Right (Far out on arm) -->
  <rect x="400" y="290" width="70" height="70" fill="{t['accent']}" rx="6"/>
  <circle cx="435" cy="325" r="14" fill="#FFFFFF"/>
  <!-- Distance leverage indicators -->
  <line x1="180" y1="380" x2="275" y2="380" stroke="{t['accent']}" stroke-width="1.2"/>
  <line x1="275" y1="380" x2="435" y2="380" stroke="{t['accent']}" stroke-width="1.2"/>
  {badge(185, 470, "杠杆力矩非对称平衡", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_095(): # 尺寸极差对比 (Scale Disparity 10:1)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Colossal Monolithic Display Number (10:1 ratio) -->
  <text x="60" y="380" fill="{t['accent']}" font-size="280" font-weight="900" font-family="Montserrat, sans-serif" opacity="0.95">8</text>
  <!-- Micro Detail Card in Upper Right -->
  <rect x="300" y="100" width="200" height="130" fill="{t['bg_surface']}" stroke="{t['accent_alt']}" stroke-width="1.5" rx="6"/>
  <circle cx="330" cy="130" r="12" fill="{t['danger']}"/>
  <line x1="355" y1="130" x2="470" y2="130" stroke="#FFFFFF" stroke-width="2"/>
  <line x1="330" y1="160" x2="470" y2="160" stroke="{t['text_dim']}" stroke-width="1.5"/>
  <line x1="330" y1="180" x2="440" y2="180" stroke="{t['text_dim']}" stroke-width="1.5"/>
  <line x1="330" y1="200" x2="460" y2="200" stroke="{t['text_dim']}" stroke-width="1.5"/>
  <!-- Scale Ratio Callout -->
  <text x="300" y="270" fill="{t['accent_alt']}" font-size="16" font-weight="900" font-family="Montserrat">SCALE RATIO 10:1</text>
  {badge(185, 520, "极限体量反差张力", t['accent'], t['text'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_096(): # 明暗黑白极差 (High Contrast Noir)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Split Light and Shadow Field -->
  <rect x="50" y="60" width="225" height="490" fill="#000000"/>
  <rect x="275" y="60" width="225" height="490" fill="#FFFFFF"/>
  <!-- Intersecting Inverted Elements -->
  <!-- White element inside pure black field -->
  <circle cx="160" cy="305" r="55" fill="#FFFFFF"/>
  <circle cx="160" cy="305" r="16" fill="#000000"/>
  <!-- Black element inside pure white field -->
  <circle cx="390" cy="305" r="55" fill="#000000"/>
  <circle cx="390" cy="305" r="16" fill="#FFFFFF"/>
  <!-- Central Razor Border -->
  <line x1="275" y1="60" x2="275" y2="550" stroke="{t['danger']}" stroke-width="3"/>
  {badge(185, 490, "黑白极高反差", t['danger'], "#FFFFFF", 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_098(): # 冷暖色彩对抗 (Color Temperature Clash)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Icy Cold Cyan vs Molten Hot Crimson -->
  <path d="M 50 60 L 320 60 L 180 550 L 50 550 Z" fill="#00E5FF" opacity="0.9"/>
  <path d="M 320 60 L 500 60 L 500 550 L 180 550 Z" fill="#FF3D00" opacity="0.9"/>
  <!-- Clash Boundary Lightning Vector -->
  <line x1="320" y1="60" x2="180" y2="550" stroke="#FFFFFF" stroke-width="4"/>
  <!-- Thermal Core Nodes -->
  <circle cx="160" cy="200" r="28" fill="#081630"/>
  <circle cx="160" cy="200" r="8" fill="#00E5FF"/>
  <circle cx="340" cy="410" r="28" fill="#FFFFFF"/>
  <circle cx="340" cy="410" r="8" fill="#FF3D00"/>
  {badge(185, 290, "冷暖极致对撞", "#FFFFFF", "#12141A", 180, 32)}
"""
    return wrap_svg(inner, t['bg'])

def gen_107(): # 韵律重复 (Rhythmic Repetition)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Equalizer Pulse Wave Repeats -->
  <g fill="{t['accent']}">
    <rect x="70" y="360" width="22" height="150" rx="4"/>
    <rect x="110" y="280" width="22" height="230" rx="4"/>
    <rect x="150" y="200" width="22" height="310" rx="4"/>
    <rect x="190" y="140" width="22" height="370" rx="4" fill="{t['danger']}"/>
    <rect x="230" y="240" width="22" height="270" rx="4"/>
    <rect x="270" y="320" width="22" height="190" rx="4"/>
    <rect x="310" y="180" width="22" height="330" rx="4"/>
    <rect x="350" y="110" width="22" height="400" rx="4" fill="{t['danger']}"/>
    <rect x="390" y="220" width="22" height="290" rx="4"/>
    <rect x="430" y="340" width="22" height="170" rx="4"/>
  </g>
  <!-- Baseline Line -->
  <line x1="50" y1="510" x2="490" y2="510" stroke="{t['guide']}" stroke-width="2"/>
  <!-- Harmonic Wave Guide -->
  <path d="M 80 360 Q 190 100 270 320 T 350 110 T 440 340" fill="none" stroke="{t['accent_alt']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  {badge(185, 70, "周期律动频段共振", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_116(): # 临近原则 (Proximity)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Proximity grouping: 2 distinct islands of 3x3 dots -->
  <!-- Left Island (x=100..200, y=180..380) -->
  <g fill="{t['accent']}">
    <circle cx="110" cy="200" r="16"/>
    <circle cx="160" cy="200" r="16"/>
    <circle cx="210" cy="200" r="16"/>
    <circle cx="110" cy="280" r="16"/>
    <circle cx="160" cy="280" r="16"/>
    <circle cx="210" cy="280" r="16"/>
    <circle cx="110" cy="360" r="16"/>
    <circle cx="160" cy="360" r="16"/>
    <circle cx="210" cy="360" r="16"/>
  </g>
  <rect x="85" y="170" width="150" height="220" fill="none" stroke="{t['accent']}" stroke-width="1.8" stroke-dasharray="6,4" rx="8"/>
  <text x="160" y="420" fill="{t['accent']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">GROUP A (PROXIMITY)</text>

  <!-- Right Island (x=340..440, y=180..380) -->
  <g fill="{t['accent_alt']}">
    <circle cx="340" cy="200" r="16"/>
    <circle cx="390" cy="200" r="16"/>
    <circle cx="440" cy="200" r="16"/>
    <circle cx="340" cy="280" r="16"/>
    <circle cx="390" cy="280" r="16"/>
    <circle cx="440" cy="280" r="16"/>
    <circle cx="340" cy="360" r="16"/>
    <circle cx="390" cy="360" r="16"/>
    <circle cx="440" cy="360" r="16"/>
  </g>
  <rect x="315" y="170" width="150" height="220" fill="none" stroke="{t['accent_alt']}" stroke-width="1.8" stroke-dasharray="6,4" rx="8"/>
  <text x="390" y="420" fill="{t['accent_alt']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">GROUP B (PROXIMITY)</text>

  <!-- Large Inter-Group Distance Void -->
  {dimension_h(235, 315, 280, "GAP", t['danger'], "#FFFFFF")}
  {badge(185, 480, "距离临近凝聚为组群", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_117(): # 闭合原则 (Closure)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Incomplete Arc Circle (Mental Closure) -->
  <path d="M 275 130 A 150 150 0 0 1 425 280" fill="none" stroke="{t['accent']}" stroke-width="16" stroke-linecap="round"/>
  <path d="M 390 380 A 150 150 0 0 1 200 450" fill="none" stroke="{t['accent']}" stroke-width="16" stroke-linecap="round"/>
  <path d="M 130 360 A 150 150 0 0 1 180 180" fill="none" stroke="{t['accent']}" stroke-width="16" stroke-linecap="round"/>
  <!-- Virtual Missing Gap Lines (Dashed mental closure) -->
  <circle cx="275" cy="290" r="150" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="6,6" opacity="0.4"/>
  <!-- Central Focus Completed by Mind -->
  <circle cx="275" cy="290" r="28" fill="{t['accent_alt']}"/>
  <circle cx="275" cy="290" r="8" fill="#FFFFFF"/>
  <text x="275" y="490" fill="{t['accent']}" font-size="15" font-weight="900" font-family="PingFang SC" text-anchor="middle">视觉知觉自动补全闭合</text>
  {badge(185, 70, "完形闭合认知", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_118(): # 连续原则 (Continuity)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Smooth intersecting continuous curves -->
  <path d="M 60 460 C 180 460 200 160 480 160" fill="none" stroke="{t['accent']}" stroke-width="6" stroke-linecap="round"/>
  <path d="M 60 160 C 180 160 200 460 480 460" fill="none" stroke="{t['accent_alt']}" stroke-width="6" stroke-linecap="round"/>
  <!-- Intersection Nexus Point -->
  <circle cx="270" cy="310" r="26" fill="{t['danger']}"/>
  <circle cx="270" cy="310" r="8" fill="#FFFFFF"/>
  <!-- Directional Guiding Arrows -->
  <polygon points="490,160 470,150 470,170" fill="{t['accent']}"/>
  <polygon points="490,460 470,450 470,470" fill="{t['accent_alt']}"/>
  <text x="275" y="400" fill="{t['text']}" font-size="14" font-weight="bold" font-family="PingFang SC" text-anchor="middle">平滑轨迹视线惯性延展</text>
  {badge(185, 80, "顺滑连续性", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_119(): # 图底反转 (Figure-Ground / Rubin Vase)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Rubin Vase Profile Geometry -->
  <rect x="60" y="80" width="430" height="440" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2" rx="6"/>
  <!-- Central Goblet Silhouette in Gold -->
  <path d="M 160 100 Q 275 110 390 100 C 330 160 310 230 350 300 C 370 340 330 420 370 480 L 180 480 C 220 420 180 340 200 300 C 240 230 220 160 160 100 Z" fill="{t['accent']}"/>
  <!-- Negative Space Flanking Profile Heads -->
  <circle cx="120" cy="220" r="8" fill="{t['accent_alt']}"/>
  <circle cx="430" cy="220" r="8" fill="{t['accent_alt']}"/>
  <text x="275" y="300" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">VASE</text>
  <text x="120" y="300" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">FACE A</text>
  <text x="430" y="300" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">FACE B</text>
  {badge(185, 500, "正负形图底交替反转", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_121(): # 连通原则 (Connectedness)
    t = get_theme("forest-green")
    inner = f"""
  <!-- 4 Distant Nodes Connected in pairs creating dominant unity -->
  <!-- Pair 1 Linked -->
  <line x1="120" y1="200" x2="330" y2="200" stroke="{t['accent']}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="120" cy="200" r="28" fill="{t['accent']}"/>
  <circle cx="120" cy="200" r="8" fill="#FFFFFF"/>
  <circle cx="330" cy="200" r="28" fill="{t['accent']}"/>
  <circle cx="330" cy="200" r="8" fill="#FFFFFF"/>
  <text x="225" y="240" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">CONNECTED UNIT 1</text>

  <!-- Pair 2 Linked diagonally -->
  <line x1="180" y1="380" x2="430" y2="380" stroke="{t['accent_alt']}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="180" cy="380" r="28" fill="{t['accent_alt']}"/>
  <circle cx="180" cy="380" r="8" fill="#FFFFFF"/>
  <circle cx="430" cy="380" r="28" fill="{t['accent_alt']}"/>
  <circle cx="430" cy="380" r="8" fill="#FFFFFF"/>
  <text x="305" y="420" fill="{t['accent_alt']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">CONNECTED UNIT 2</text>

  {badge(185, 480, "连线强力覆盖临近", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_126(): # 格式塔异质焦点 (Gestalt Focal Point)
    t = get_theme("forest-green")
    inner = f"""
  <!-- 4x4 Grid of Identical Gray Circles -->
  <g fill="{t['stroke']}">
    <circle cx="130" cy="160" r="18"/><circle cx="210" cy="160" r="18"/><circle cx="290" cy="160" r="18"/><circle cx="370" cy="160" r="18"/>
    <circle cx="130" cy="240" r="18"/><circle cx="210" cy="240" r="18"/><circle cx="290" cy="240" r="18"/><circle cx="370" cy="240" r="18"/>
    <circle cx="130" cy="320" r="18"/><circle cx="210" cy="320" r="18"/>
    <!-- (290, 320) is the EXTREME ANOMALY FOCAL POINT -->
    <circle cx="370" cy="320" r="18"/>
    <circle cx="130" cy="400" r="18"/><circle cx="210" cy="400" r="18"/><circle cx="290" cy="400" r="18"/><circle cx="370" cy="400" r="18"/>
  </g>
  <!-- Heterogeneous Hero Focal Anchor -->
  <rect x="265" y="295" width="50" height="50" fill="{t['danger']}" rx="6" transform="rotate(45 290 320)"/>
  <circle cx="290" cy="320" r="38" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="4,4"/>
  <circle cx="290" cy="320" r="8" fill="#FFFFFF"/>
  <line x1="290" y1="230" x2="290" y2="280" stroke="{t['accent']}" stroke-width="2"/>
  <polygon points="290,285 285,270 295,270" fill="{t['accent']}"/>
  <text x="290" y="215" fill="{t['accent']}" font-size="13" font-weight="900" font-family="PingFang SC" text-anchor="middle">特异形态强焦点</text>
  {badge(185, 480, "同质背景破局点", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

def gen_127(): # Z型阅读动线 (Z-Pattern)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Canonical Z-Pattern Path for Landing Pages -->
  <!-- 1. Top Left Anchor (Logo) -->
  <rect x="60" y="90" width="70" height="40" fill="{t['accent']}" rx="4"/>
  <text x="95" y="115" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">LOGO</text>
  <!-- 2. Top Right Anchor (Action / Nav) -->
  <rect x="380" y="90" width="110" height="40" fill="{t['stroke']}" rx="4"/>
  <text x="435" y="115" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">NAV / CTA</text>
  <!-- 3. Bottom Left Anchor (Supporting Visual) -->
  <rect x="60" y="440" width="140" height="70" fill="{t['stroke']}" rx="4"/>
  <text x="130" y="480" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">BENEFIT</text>
  <!-- 4. Bottom Right Anchor (Final Conversion CTA) -->
  <rect x="340" y="440" width="150" height="70" fill="{t['accent']}" rx="6"/>
  <text x="415" y="480" fill="{t['bg']}" font-size="15" font-weight="900" font-family="Montserrat" text-anchor="middle">CONVERT</text>
  <!-- Bold Z Vector Flow Path -->
  <path d="M 95 110 L 435 110 L 130 475 L 415 475" fill="none" stroke="{t['accent']}" stroke-width="4.5" stroke-dasharray="8,6" stroke-linecap="round"/>
  <polygon points="425,475 410,465 410,485" fill="{t['accent']}"/>
  {badge(185, 270, "经典 Z 型扫描流", t['accent'], t['bg'], 180, 32)}
"""
    return wrap_svg(inner, t['bg'])

def gen_128(): # F型阅读动线 (F-Pattern)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Canonical F-Pattern Eyetracking Heatmap Path -->
  <!-- Top Horizontal Bar 1 (Full width reading) -->
  <rect x="60" y="90" width="430" height="35" fill="{t['accent']}" rx="4"/>
  <!-- Middle Horizontal Bar 2 (Half width reading) -->
  <rect x="60" y="190" width="280" height="30" fill="{t['accent_alt']}" rx="4"/>
  <!-- Lower Horizontal Bar 3 (Shorter scan) -->
  <rect x="60" y="280" width="180" height="25" fill="{t['stroke']}" rx="4"/>
  <!-- Vertical Left Scan Corridor -->
  <rect x="60" y="90" width="40" height="420" fill="{t['accent']}" opacity="0.6" rx="4"/>
  <!-- Eyetracking heatmap flow vectors -->
  <line x1="80" y1="105" x2="480" y2="105" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="80" y1="205" x2="330" y2="205" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
  <line x1="80" y1="292" x2="230" y2="292" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
  <line x1="80" y1="105" x2="80" y2="500" stroke="{t['danger']}" stroke-width="4" stroke-dasharray="6,4"/>
  {badge(185, 450, "F 型眼动热区模型", t['accent'], t['bg'], 180, 30)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat02

def gen_089(): # 静态构图 (Static Composition)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Ground Baseline Anchor -->
  <line x1="70" y1="440" x2="480" y2="440" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <!-- Perfectly centered solid monolith -->
  <rect x="185" y="200" width="180" height="240" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5" rx="4"/>
  <circle cx="275" cy="300" r="36" fill="{t['accent']}"/>
  <circle cx="275" cy="300" r="10" fill="#FFFFFF"/>
  <!-- Symmetry Axis -->
  <line x1="275" y1="80" x2="275" y2="500" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <text x="275" y="160" fill="{t['text_dim']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">STATIC EQUILIBRIUM</text>
  {badge(185, 480, "绝对对称 · 庄穆安定", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_090(): # 动态构图 (Dynamic Composition)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Slanted 45-degree dynamic thrust vectors -->
  <line x1="60" y1="520" x2="440" y2="100" stroke="{t['accent']}" stroke-width="4"/>
  <polygon points="440,100 400,120 420,140" fill="{t['accent']}"/>
  <!-- Velocity speed bands -->
  <line x1="110" y1="540" x2="460" y2="150" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="12,8"/>
  <line x1="70" y1="450" x2="390" y2="90" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="8,6"/>
  <!-- Dynamic tilted blocks -->
  <g transform="rotate(-35 275 310)">
    <rect x="215" y="240" width="120" height="140" rx="6" fill="{t['danger']}" opacity="0.9"/>
    <circle cx="275" cy="310" r="24" fill="#FFFFFF"/>
  </g>
  <text x="275" y="120" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">DYNAMIC VELOCITY</text>
  {badge(185, 520, "倾斜动势 · 破画张力", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_091(): # 开放式构图 (Open Composition)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Elements bleeding past frame edges -->
  <circle cx="50" cy="200" r="90" fill="{t['accent']}" opacity="0.4"/>
  <circle cx="500" cy="420" r="110" fill="{t['accent_alt']}" opacity="0.4"/>
  <rect x="200" y="40" width="150" height="120" rx="6" fill="{t['stroke']}" opacity="0.8"/>
  <!-- Outward expansion vectors -->
  <line x1="275" y1="310" x2="80" y2="160" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="6,4"/>
  <line x1="275" y1="310" x2="470" y2="450" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="6,4"/>
  <line x1="275" y1="310" x2="275" y2="80" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="6,4"/>
  <circle cx="275" cy="310" r="16" fill="{t['danger']}"/>
  <text x="275" y="350" fill="{t['text']}" font-size="12" font-family="Montserrat" text-anchor="middle">EXPANDING BEYOND CANVAS</text>
  {badge(185, 520, "画外延展 · 开放视界", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_092(): # 封闭式构图 (Closed Composition)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Heavy Enclosing Border -->
  <rect x="80" y="90" width="390" height="420" rx="10" fill="none" stroke="{t['accent']}" stroke-width="4"/>
  <!-- Centripetal Arrows pointing inward -->
  <line x1="110" y1="130" x2="230" y2="260" stroke="{t['accent_alt']}" stroke-width="2.5"/>
  <polygon points="230,260 215,245 235,240" fill="{t['accent_alt']}"/>
  <line x1="440" y1="130" x2="320" y2="260" stroke="{t['accent_alt']}" stroke-width="2.5"/>
  <polygon points="320,260 335,245 315,240" fill="{t['accent_alt']}"/>
  <!-- Contained Core -->
  <circle cx="275" cy="300" r="45" fill="{t['accent']}"/>
  <circle cx="275" cy="300" r="16" fill="#FFFFFF"/>
  <text x="275" y="380" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">CENTRIPETAL FOCUS</text>
  {badge(185, 460, "向心内聚封闭结构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_093(): # 单一焦点构图 (Single Focus)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Matrix of 36 muted dots -->
  <g fill="{t['stroke']}" opacity="0.4">
    {''.join([f'<circle cx="{115 + (i%6)*64}" cy="{130 + (i//6)*60}" r="8"/>' for i in range(36) if i != 14])}
  </g>
  <!-- Single High-Intensity Focal Star at index 14 (cx=243, cy=250) -->
  <circle cx="243" cy="250" r="55" fill="{t['danger']}" opacity="0.2"/>
  <circle cx="243" cy="250" r="35" fill="none" stroke="{t['accent']}" stroke-width="1.8" stroke-dasharray="4,3"/>
  <circle cx="243" cy="250" r="18" fill="{t['accent']}"/>
  <circle cx="243" cy="250" r="6" fill="#FFFFFF"/>
  <text x="275" y="450" fill="{t['accent']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">THE SINGULAR EYE DESTINATION</text>
  {badge(185, 520, "万绿丛中一点红", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_094(): # 多重焦点构图 (Multiple Foci)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Interconnecting Tension Triangle -->
  <polygon points="170,200 380,240 250,420" fill="none" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="6,6"/>
  <!-- Focus Node 1 (Alpha) -->
  <circle cx="170" cy="200" r="34" fill="{t['accent']}"/>
  <circle cx="170" cy="200" r="10" fill="#FFFFFF"/>
  <text x="170" y="150" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">FOCUS α</text>
  <!-- Focus Node 2 (Beta) -->
  <circle cx="380" cy="240" r="26" fill="{t['accent_alt']}"/>
  <circle cx="380" cy="240" r="8" fill="#FFFFFF"/>
  <text x="380" y="195" fill="{t['accent_alt']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">FOCUS β</text>
  <!-- Focus Node 3 (Gamma) -->
  <circle cx="250" cy="420" r="22" fill="{t['danger']}"/>
  <circle cx="250" cy="420" r="6" fill="#FFFFFF"/>
  <text x="250" y="470" fill="{t['danger']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">FOCUS γ</text>
  {badge(185, 520, "多重焦点视线巡游", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_097(): # 平衡原则 (Balance Principle)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Fulcrum balance triangle -->
  <polygon points="275,340 245,410 305,410" fill="{t['stroke']}" stroke="{t['guide']}" stroke-width="2"/>
  <!-- Balance beam -->
  <line x1="80" y1="340" x2="470" y2="340" stroke="{t['accent']}" stroke-width="3.5"/>
  <!-- Left visual mass -->
  <rect x="110" y="220" width="120" height="120" rx="6" fill="{t['accent']}"/>
  <circle cx="170" cy="280" r="20" fill="#FFFFFF"/>
  <!-- Right equal counterweight -->
  <circle cx="390" cy="280" r="60" fill="{t['accent_alt']}"/>
  <circle cx="390" cy="280" r="16" fill="#FFFFFF"/>
  <!-- Center equilibrium line -->
  <line x1="275" y1="100" x2="275" y2="340" stroke="{t['danger']}" stroke-width="1.8" stroke-dasharray="4,4"/>
  {badge(185, 480, "视觉重力动态均势", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_099(): # 尺度对比原则 (Scale Contrast)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Colossal Monolith on Right -->
  <rect x="230" y="100" width="230" height="410" rx="6" fill="{t['accent']}"/>
  <text x="345" y="320" fill="{t['bg']}" font-size="36" font-weight="900" font-family="Montserrat" text-anchor="middle">100X</text>
  <!-- Tiny Human Scale Dot on Left -->
  <circle cx="130" cy="490" r="12" fill="{t['danger']}"/>
  <circle cx="130" cy="490" r="4" fill="#FFFFFF"/>
  <text x="130" y="460" fill="{t['text']}" font-size="12" font-family="Montserrat" text-anchor="middle">1X (SCALE)</text>
  <!-- Disparity line -->
  <line x1="130" y1="490" x2="230" y2="490" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  {badge(185, 520, "极端尺度比例张力", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_100(): # 明暗对比原则 (Chiaroscuro / Light & Dark)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Split field: Deep Black Left, Pure Light Right -->
  <rect x="50" y="60" width="225" height="500" fill="#111111"/>
  <rect x="275" y="60" width="225" height="500" fill="#FAF7F2"/>
  <!-- Light element inside dark field -->
  <circle cx="160" cy="300" r="52" fill="#FAF7F2"/>
  <circle cx="160" cy="300" r="14" fill="#111111"/>
  <!-- Dark element inside light field -->
  <circle cx="390" cy="300" r="52" fill="#111111"/>
  <circle cx="390" cy="300" r="14" fill="#FAF7F2"/>
  <line x1="275" y1="60" x2="275" y2="560" stroke="{t['danger']}" stroke-width="3"/>
  {badge(185, 500, "明暗对立 · 虚实分明", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_101(): # 色彩对比原则 (Color Contrast)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Saturated Cyan Field Left -->
  <rect x="80" y="120" width="180" height="340" rx="6" fill="#00E5FF" fill-opacity="0.85"/>
  <circle cx="170" cy="290" r="38" fill="#FF3D00"/>
  <circle cx="170" cy="290" r="10" fill="#FFFFFF"/>
  <!-- Saturated Red-Orange Field Right -->
  <rect x="290" y="120" width="180" height="340" rx="6" fill="#FF3D00" fill-opacity="0.85"/>
  <circle cx="380" cy="290" r="38" fill="#00E5FF"/>
  <circle cx="380" cy="290" r="10" fill="#FFFFFF"/>
  <text x="275" y="95" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">COMPLEMENTARY CLASH</text>
  {badge(185, 500, "互补色彩心理张力", "#FF3D00", "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_102(): # 形状对比原则 (Shape Contrast)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Soft Organic Round Circle on Left -->
  <circle cx="180" cy="300" r="85" fill="{t['accent_alt']}" opacity="0.7"/>
  <circle cx="180" cy="300" r="30" fill="#FFFFFF"/>
  <!-- Sharp Aggressive Jagged Polygon on Right Piercing Space -->
  <polygon points="290,140 450,260 380,450 250,370" fill="{t['danger']}"/>
  <polygon points="260,250 360,300 280,360" fill="{t['bg']}"/>
  <text x="275" y="100" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">ORGANIC CURVE VS JAGGED ANGLE</text>
  {badge(185, 500, "方圆尖钝形态碰撞", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_103(): # 质感对比原则 (Texture Contrast)
    t = get_theme("warm-ivory")
    # Generate halftone stippled dot pattern for left, sleek smooth for right
    dots = "".join([f'<circle cx="{95 + (i%9)*18}" cy="{160 + (i//9)*18}" r="{2 + (i%3)*1.5}" fill="{t["accent"]}"/>' for i in range(144)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Left: Coarse Halftone Grain Surface -->
  <rect x="80" y="120" width="180" height="340" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <g>{dots}</g>
  <text x="170" y="490" fill="{t['accent']}" font-size="12" font-family="Montserrat" text-anchor="middle">ROUGH / STIPPLE</text>
  <!-- Right: Sleek Mirror Smooth Surface -->
  <rect x="290" y="120" width="180" height="340" rx="6" fill="#FFFFFF" opacity="0.85"/>
  <circle cx="380" cy="290" r="45" fill="{t['accent']}"/>
  <text x="380" y="490" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">SMOOTH / GLOSS</text>
  {badge(185, 75, "肌理质感触觉反差", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_104(): # 动静对比原则 (Motion vs Stillness)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Motion Blur Streamers rushing past -->
  <line x1="60" y1="200" x2="320" y2="200" stroke="{t['danger']}" stroke-width="6" stroke-linecap="round" opacity="0.4"/>
  <line x1="120" y1="250" x2="440" y2="250" stroke="{t['danger']}" stroke-width="10" stroke-linecap="round" opacity="0.8"/>
  <line x1="80" y1="300" x2="360" y2="300" stroke="{t['accent_alt']}" stroke-width="4" stroke-linecap="round" opacity="0.5"/>
  <line x1="140" y1="350" x2="480" y2="350" stroke="{t['danger']}" stroke-width="8" stroke-linecap="round" opacity="0.7"/>
  <!-- Solid Immovable Anchor Rock Pillar -->
  <rect x="240" y="140" width="70" height="320" fill="#FFFFFF" rx="4" stroke="{t['accent']}" stroke-width="3"/>
  <circle cx="275" cy="300" r="16" fill="{t['bg']}"/>
  <text x="275" y="115" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">STEADY VS VELOCITY</text>
  {badge(185, 510, "疾速动线与静止基石", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_105(): # 并置原则 (Juxtaposition)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Split Dual Panels -->
  <!-- Concept A (Classical Column / Order) -->
  <rect x="75" y="110" width="180" height="350" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="105" y1="160" x2="225" y2="160" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="120" y1="160" x2="120" y2="400" stroke="{t['accent_alt']}" stroke-width="3"/>
  <line x1="165" y1="160" x2="165" y2="400" stroke="{t['accent_alt']}" stroke-width="3"/>
  <line x1="210" y1="160" x2="210" y2="400" stroke="{t['accent_alt']}" stroke-width="3"/>
  <text x="165" y="435" fill="{t['text']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">CLASSICAL</text>
  <!-- Concept B (Digital Abstract / Glitch) -->
  <rect x="295" y="110" width="180" height="350" rx="6" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <rect x="315" y="160" width="140" height="40" fill="{t['danger']}" opacity="0.7"/>
  <rect x="335" y="220" width="120" height="50" fill="{t['accent']}" opacity="0.8"/>
  <circle cx="385" cy="330" r="32" fill="#00E5FF"/>
  <text x="385" y="435" fill="{t['text']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">AVANT-GARDE</text>
  {badge(185, 510, "双重视野概念并置", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_106(): # 隔离原则 (Isolation Principle)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Dense Cluster of 16 shapes huddled in bottom-left -->
  <g fill="{t['stroke']}">
    <circle cx="100" cy="380" r="16"/><circle cx="130" cy="360" r="14"/><circle cx="160" cy="390" r="18"/>
    <circle cx="120" cy="420" r="15"/><circle cx="150" cy="440" r="16"/><circle cx="180" cy="410" r="14"/>
    <circle cx="110" cy="460" r="12"/><circle cx="140" cy="480" r="15"/><circle cx="170" cy="460" r="16"/>
  </g>
  <!-- Vast Void (85% of space) -->
  <!-- Single Isolated Beacon in Top Right -->
  <circle cx="390" cy="180" r="42" fill="{t['accent']}" opacity="0.2"/>
  <circle cx="390" cy="180" r="24" fill="{t['accent']}"/>
  <circle cx="390" cy="180" r="8" fill="#FFFFFF"/>
  <text x="390" y="235" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">ISOLATED NODE</text>
  {badge(185, 520, "离群独置产生绝对聚焦", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_108(): # 图案组织 (Pattern Organization)
    t = get_theme("warm-ivory")
    # Modular repeating geometric tile
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <g stroke="{t['guide']}" stroke-width="1">
    {''.join([f'<rect x="{80 + (i%4)*95}" y="{100 + (i//4)*95}" width="80" height="80" rx="6" fill="{t["accent"] if i in [5,10] else (t["stroke"] if i%2==0 else t["bg"])}" opacity="{0.9 if i in [5,10] else 0.6}"/>' for i in range(16)])}
  </g>
  <circle cx="275" cy="290" r="32" fill="{t['accent']}"/>
  <circle cx="275" cy="290" r="10" fill="#FFFFFF"/>
  {badge(185, 520, "周期图案纹样组织", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_109(): # 节奏组织 (Rhythm Organization)
    t = get_theme("cobalt-blue")
    # Musical beat waveforms
    bars = "".join([f'<rect x="{80 + i*16}" y="{310 - (20 + (i*13)%140)}" width="10" height="{(40 + (i*13)%140)*2}" rx="3" fill="{t["accent"] if i%4==0 else t["accent_alt"]}" opacity="{1.0 if i%4==0 else 0.6}"/>' for i in range(24)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <line x1="70" y1="310" x2="480" y2="310" stroke="{t['danger']}" stroke-width="2" stroke-dasharray="4,4"/>
  {bars}
  <text x="275" y="110" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">METRIC PULSE & TEMPO</text>
  {badge(185, 520, "视觉节拍波形韵律", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_110(): # 渐变组织 (Gradation Organization)
    t = get_theme("forest-green")
    # Concentric or scale stepped bars
    steps = "".join([f'<rect x="{80 + i*36}" y="{380 - i*28}" width="28" height="{60 + i*28}" rx="4" fill="{t["accent"]}" opacity="{0.2 + i*0.08}"/>' for i in range(10)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  {steps}
  <path d="M 80 380 Q 250 260 430 100" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="6,4"/>
  <circle cx="430" cy="100" r="12" fill="{t['danger']}"/>
  {badge(185, 500, "尺度色阶梯级渐变", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_111(): # 交替节奏组织 (Alternating Rhythm)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- ABABAB Cadence: Square, Circle, Square, Circle -->
  <g transform="translate(15, 0)">
    <rect x="70" y="240" width="60" height="60" rx="4" fill="{t['accent']}"/>
    <circle cx="190" cy="270" r="30" fill="{t['accent_alt']}"/>
    <rect x="250" y="240" width="60" height="60" rx="4" fill="{t['accent']}"/>
    <circle cx="370" cy="270" r="30" fill="{t['accent_alt']}"/>
  </g>
  <text x="275" y="160" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">A - B - A - B ALTERNATING CADENCE</text>
  {badge(185, 480, "交替起伏规整节律", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_112(): # 渐进节奏组织 (Progressive Rhythm)
    t = get_theme("warm-ivory")
    # Fibonacci growth squares
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Progressive exponential elements -->
  <circle cx="90" cy="350" r="8" fill="{t['accent']}"/>
  <circle cx="130" cy="350" r="13" fill="{t['accent']}"/>
  <circle cx="185" cy="350" r="21" fill="{t['accent']}"/>
  <circle cx="260" cy="350" r="34" fill="{t['accent']}"/>
  <circle cx="370" cy="350" r="55" fill="{t['accent']}"/>
  <!-- Connecting Fibonacci growth arc -->
  <path d="M 90 350 C 150 250 260 180 370 295" fill="none" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="275" y="130" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">EXPONENTIAL GROWTH SEQUENCE</text>
  {badge(185, 480, "斐波那契渐进扩张", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_113(): # 流动节奏组织 (Flowing Rhythm)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Sinusoidal undulating ribbons -->
  <path d="M 60 220 Q 160 140 275 220 T 490 220" fill="none" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <path d="M 60 280 Q 160 200 275 280 T 490 280" fill="none" stroke="{t['accent_alt']}" stroke-width="5" stroke-linecap="round"/>
  <path d="M 60 340 Q 160 260 275 340 T 490 340" fill="none" stroke="{t['danger']}" stroke-width="3" stroke-linecap="round"/>
  <circle cx="275" cy="280" r="16" fill="#FFFFFF"/>
  <text x="275" y="120" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">ORGANIC STREAMLINE FLOW</text>
  {badge(185, 480, "流体曲线连续动势", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_114(): # 随机节奏组织 (Random Rhythm)
    t = get_theme("cobalt-blue")
    # Generative scattered confetti with dynamic tension
    import random
    rng = random.Random(114)
    elements = "".join([f'<circle cx="{rng.randint(90, 460)}" cy="{rng.randint(110, 450)}" r="{rng.randint(6, 26)}" fill="{t["accent"] if i%3==0 else (t["accent_alt"] if i%3==1 else t["danger"])}" opacity="{rng.uniform(0.5, 0.95):.2f}"/>' for i in range(28)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  {elements}
  <text x="275" y="95" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">STOCHASTIC CHAOS DYNAMICS</text>
  {badge(185, 520, "随机散落受控无序", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_122(): # 简化构图原则 (Simplification Principle)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Extreme Minimalism: 1 Line + 1 Circle (Less is More) -->
  <line x1="100" y1="310" x2="450" y2="310" stroke="{t['accent']}" stroke-width="3"/>
  <circle cx="275" cy="220" r="26" fill="{t['accent']}"/>
  <circle cx="275" cy="220" r="8" fill="#FFFFFF"/>
  <text x="275" y="420" fill="{t['text_dim']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">LESS IS MORE</text>
  {badge(185, 500, "奥卡姆剃刀极限简化", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_123(): # 裁切构图 (Cropping)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Massive Circle dramatically cropped by top-right corner -->
  <clipPath id="cropFrame123"><rect x="50" y="60" width="450" height="500" rx="8"/></clipPath>
  <g clip-path="url(#cropFrame123)">
    <circle cx="480" cy="80" r="240" fill="{t['accent']}" opacity="0.9"/>
    <circle cx="480" cy="80" r="160" fill="{t['accent_alt']}" opacity="0.6"/>
    <circle cx="480" cy="80" r="80" fill="#FFFFFF"/>
  </g>
  <!-- Frame corner brackets showing cropping tension -->
  <line x1="500" y1="60" x2="500" y2="200" stroke="{t['danger']}" stroke-width="4"/>
  <line x1="360" y1="60" x2="500" y2="60" stroke="{t['danger']}" stroke-width="4"/>
  <text x="160" y="380" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat">DRAMATIC CROPPING</text>
  {badge(185, 520, "边框破损剧烈裁切", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_124(): # 满幅构图 (Full-Bleed)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- 100% Edge-to-Edge immersion, zero white borders -->
  <rect x="0" y="0" width="550" height="620" fill="{t['accent']}" fill-opacity="0.85"/>
  <circle cx="275" cy="270" r="120" fill="{t['bg']}"/>
  <circle cx="275" cy="270" r="40" fill="#FFFFFF"/>
  <rect x="40" y="460" width="470" height="90" rx="8" fill="{t['bg']}" fill-opacity="0.9"/>
  <text x="275" y="515" fill="#FFFFFF" font-size="20" font-weight="900" font-family="Montserrat" text-anchor="middle">FULL BLEED ZERO MARGINS</text>
  {badge(185, 580, "满幅出血无界视野", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_125(): # 疏密对比原则 (Density Contrast)
    t = get_theme("forest-green")
    dots = "".join([f'<circle cx="{75 + (i%8)*16}" cy="{90 + (i//8)*16}" r="5" fill="{t["accent"]}"/>' for i in range(64)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Dense Cluster in Top Left (20% space, 90% elements) -->
  <rect x="65" y="80" width="140" height="140" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <g>{dots}</g>
  <!-- Vast Void (80% space, 1 single element) -->
  <circle cx="380" cy="360" r="36" fill="{t['danger']}"/>
  <circle cx="380" cy="360" r="12" fill="#FFFFFF"/>
  <line x1="185" y1="200" x2="344" y2="324" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="380" y="430" fill="{t['text_dim']}" font-size="14" font-family="Kaiti, serif" text-anchor="middle">密不通风 · 疏可走马</text>
  {badge(185, 520, "聚散疏密强烈反差", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_129(): # 古腾堡图式 (Gutenberg Diagram)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Z-Path Reading Vector -->
  <path d="M 120 140 L 430 140 L 120 440 L 430 440" fill="none" stroke="{t['accent']}" stroke-width="4" stroke-dasharray="8,6"/>
  <!-- Primary Optical Area (POA) Top Left -->
  <circle cx="120" cy="140" r="32" fill="{t['accent']}"/>
  <text x="120" y="145" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">POA</text>
  <!-- Strong Fallow Area Top Right -->
  <circle cx="430" cy="140" r="22" fill="{t['stroke']}"/>
  <!-- Weak Fallow Area Bottom Left -->
  <circle cx="120" cy="440" r="22" fill="{t['stroke']}"/>
  <!-- Terminal Area (TA) Bottom Right Hero Callout -->
  <circle cx="430" cy="440" r="32" fill="{t['danger']}"/>
  <text x="430" y="445" fill="#FFFFFF" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">TA</text>
  <text x="275" y="290" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">READING GRAVITY (Z-FLOW)</text>
  {badge(185, 520, "古腾堡对角线阅读流", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_130(): # 层蛋糕扫描模式 (Layer Cake Scanning)
    t = get_theme("cobalt-blue")
    # Horizontal scanning shelves alternating with skipped text
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Cake Layer 1 (Heading Scanned) -->
  <rect x="80" y="110" width="390" height="36" rx="6" fill="{t['accent']}"/>
  <line x1="60" y1="128" x2="500" y2="128" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <!-- Skipped Body Lines -->
  <rect x="100" y="160" width="320" height="10" rx="2" fill="{t['stroke']}" opacity="0.4"/>
  <rect x="100" y="180" width="280" height="10" rx="2" fill="{t['stroke']}" opacity="0.4"/>
  <!-- Cake Layer 2 (Subheading Scanned) -->
  <rect x="80" y="220" width="340" height="32" rx="6" fill="{t['accent_alt']}"/>
  <line x1="60" y1="236" x2="460" y2="236" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <!-- Skipped Body Lines -->
  <rect x="100" y="270" width="310" height="10" rx="2" fill="{t['stroke']}" opacity="0.4"/>
  <rect x="100" y="290" width="250" height="10" rx="2" fill="{t['stroke']}" opacity="0.4"/>
  <!-- Cake Layer 3 (CTA Button Scanned) -->
  <rect x="80" y="330" width="260" height="36" rx="6" fill="{t['accent']}"/>
  <line x1="60" y1="348" x2="370" y2="348" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="275" y="430" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">EYE FIXATES ON HEADINGS ONLY</text>
  {badge(185, 480, "千层糕标题跳跃扫描", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_131(): # 斑点扫描模式 (Spotted Pattern)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Faint body text lines -->
  <g fill="{t['stroke']}" opacity="0.35">
    {''.join([f'<rect x="80" y="{110 + i*22}" width="390" height="8" rx="2"/>' for i in range(16)])}
  </g>
  <!-- Saccade Gaze Leap Vector connecting spotted fixation clusters -->
  <path d="M 140 132 L 380 176 L 190 264 L 410 330 L 220 418" fill="none" stroke="{t['danger']}" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Spotted Fixation Heatmaps -->
  <circle cx="140" cy="132" r="28" fill="{t['accent']}" opacity="0.4"/><circle cx="140" cy="132" r="12" fill="{t['accent']}"/>
  <circle cx="380" cy="176" r="34" fill="{t['danger']}" opacity="0.4"/><circle cx="380" cy="176" r="14" fill="{t['danger']}"/>
  <circle cx="190" cy="264" r="26" fill="{t['accent_alt']}" opacity="0.4"/><circle cx="190" cy="264" r="10" fill="{t['accent_alt']}"/>
  <circle cx="410" cy="330" r="38" fill="{t['accent']}" opacity="0.4"/><circle cx="410" cy="330" r="16" fill="{t['accent']}"/>
  <circle cx="220" cy="418" r="30" fill="{t['danger']}" opacity="0.4"/><circle cx="220" cy="418" r="12" fill="{t['danger']}"/>
  {badge(185, 520, "关键词散点凝视跳跃", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

CAT02_SVGS = {
    "089": gen_089, "090": gen_090, "091": gen_091, "092": gen_092, "093": gen_093,
    "094": gen_094, "097": gen_097, "099": gen_099, "100": gen_100, "101": gen_101,
    "102": gen_102, "103": gen_103, "104": gen_104, "105": gen_105, "106": gen_106,
    "108": gen_108, "109": gen_109, "110": gen_110, "111": gen_111, "112": gen_112,
    "113": gen_113, "114": gen_114, "122": gen_122, "123": gen_123, "124": gen_124,
    "125": gen_125, "129": gen_129, "130": gen_130, "131": gen_131,
    "087": gen_087, "088": gen_088, "095": gen_095, "096": gen_096, "098": gen_098,
    "107": gen_107, "116": gen_116, "117": gen_117, "118": gen_118, "119": gen_119,
    "121": gen_121, "126": gen_126, "127": gen_127, "128": gen_128
}


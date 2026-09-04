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
CAT02_SVGS = {
    "087": gen_087, "088": gen_088, "095": gen_095, "096": gen_096, "098": gen_098,
    "107": gen_107, "116": gen_116, "117": gen_117, "118": gen_118, "119": gen_119,
    "121": gen_121, "126": gen_126, "127": gen_127, "128": gen_128
}


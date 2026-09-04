"""
SVG generators for Category 05: 网页与 UI 系统 (222-300).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_224(): # 绝对定位钉死 (Absolute Positioning Pin)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Relative Parent Container -->
  <rect x="50" y="70" width="450" height="480" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4" rx="8"/>
  <text x="80" y="105" fill="{t['accent_alt']}" font-size="12" font-family="Montserrat">position: relative;</text>
  <!-- Absolute Pinned Card (top: 40px, right: 40px) -->
  <rect x="290" y="130" width="180" height="130" fill="{t['accent']}" rx="8"/>
  <circle cx="330" cy="170" r="16" fill="#FFFFFF"/>
  <text x="360" y="175" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat">PINNED</text>
  <text x="300" y="210" fill="{t['bg']}" font-size="11" font-family="Montserrat">top: 60px; right: 30px;</text>
  <!-- Coordinate Offset Dimension Vectors -->
  <line x1="290" y1="70" x2="290" y2="130" stroke="{t['danger']}" stroke-width="2"/>
  <line x1="470" y1="130" x2="500" y2="130" stroke="{t['danger']}" stroke-width="2"/>
  <!-- Target Pin Marker -->
  <circle cx="470" cy="130" r="8" fill="{t['danger']}"/>
  {badge(185, 490, "脱离普通流 · 精准锚定", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_230(): # CSS 网格系统 (CSS Grid Template Columns)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="6"/>
  <!-- Grid track definitions: 1fr 2fr 1fr -->
  <text x="100" y="90" fill="{t['accent_alt']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">1fr</text>
  <text x="275" y="90" fill="{t['accent']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">2fr</text>
  <text x="450" y="90" fill="{t['accent_alt']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">1fr</text>
  <!-- Grid Cells -->
  <g stroke="{t['accent']}" stroke-width="1.5">
    <!-- Row 1 -->
    <rect x="70" y="110" width="80" height="100" rx="4" fill="{t['bg']}"/>
    <rect x="170" y="110" width="210" height="100" rx="4" fill="{t['accent']}" fill-opacity="0.8"/>
    <rect x="400" y="110" width="80" height="100" rx="4" fill="{t['bg']}"/>
    <!-- Row 2 -->
    <rect x="70" y="230" width="80" height="140" rx="4" fill="{t['bg']}"/>
    <rect x="170" y="230" width="210" height="140" rx="4" fill="{t['bg_surface']}"/>
    <circle cx="275" cy="300" r="32" fill="{t['accent_alt']}"/>
    <rect x="400" y="230" width="80" height="140" rx="4" fill="{t['bg']}"/>
    <!-- Row 3 -->
    <rect x="70" y="390" width="410" height="70" rx="4" fill="{t['stroke']}"/>
  </g>
  <text x="275" y="432" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">grid-column: 1 / -1 (FULL ROW)</text>
  {badge(185, 500, "二维二维网格精确排版", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_243(): # 堆叠原语 (Stack Primitive)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="70" y="60" width="410" height="500" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="8"/>
  <!-- Vertical Stack Item 1 -->
  <rect x="100" y="90" width="350" height="80" rx="6" fill="{t['accent']}"/>
  <text x="275" y="136" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">STACK ITEM 1</text>
  <!-- Gap Token 1 -->
  {dimension_v(170, 200, 465, "gap", t['danger'], "#FFFFFF")}
  <!-- Vertical Stack Item 2 -->
  <rect x="100" y="200" width="350" height="110" rx="6" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="2"/>
  <circle cx="150" cy="255" r="22" fill="{t['accent_alt']}"/>
  <text x="275" y="260" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">STACK ITEM 2</text>
  <!-- Gap Token 2 -->
  {dimension_v(310, 340, 465, "gap", t['danger'], "#FFFFFF")}
  <!-- Vertical Stack Item 3 -->
  <rect x="100" y="340" width="350" height="80" rx="6" fill="{t['stroke']}"/>
  <text x="275" y="386" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">STACK ITEM 3</text>
  {badge(185, 480, "等距一维垂直流", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_255(): # 经典圣杯后台 (Holy Grail Dashboard Shell)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Full App Shell Wireframe -->
  <rect x="40" y="50" width="470" height="520" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Top Navigation Header -->
  <rect x="40" y="50" width="470" height="50" rx="8" fill="{t['accent']}"/>
  <circle cx="70" cy="75" r="12" fill="#FFFFFF"/>
  <text x="100" y="80" fill="#FFFFFF" font-size="13" font-weight="900" font-family="Montserrat">ENTERPRISE CLOUD</text>
  <circle cx="470" cy="75" r="14" fill="{t['danger']}"/>
  <!-- Left Side Navigation Bar -->
  <rect x="40" y="100" width="110" height="470" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <rect x="55" y="125" width="80" height="24" rx="4" fill="{t['accent']}" opacity="0.3"/>
  <rect x="55" y="160" width="80" height="20" rx="4" fill="{t['stroke']}"/>
  <rect x="55" y="190" width="80" height="20" rx="4" fill="{t['stroke']}"/>
  <rect x="55" y="220" width="80" height="20" rx="4" fill="{t['stroke']}"/>
  <!-- Main Workspace Area -->
  <!-- Breadcrumb bar -->
  <text x="175" y="130" fill="{t['text_dim']}" font-size="11" font-family="Montserrat">Home / Dashboard / Overview</text>
  <!-- 2x2 Metric KPI Widget Cards -->
  <rect x="170" y="150" width="150" height="90" rx="6" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="1.5"/>
  <text x="185" y="180" fill="{t['text_dim']}" font-size="10" font-family="Montserrat">ACTIVE USERS</text>
  <text x="185" y="215" fill="{t['accent_alt']}" font-size="22" font-weight="900" font-family="Montserrat">24,580</text>

  <rect x="340" y="150" width="150" height="90" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="355" y="180" fill="{t['text_dim']}" font-size="10" font-family="Montserrat">REVENUE</text>
  <text x="355" y="215" fill="{t['accent']}" font-size="22" font-weight="900" font-family="Montserrat">$184.2K</text>

  <!-- Big Data Graph Card -->
  <rect x="170" y="260" width="320" height="200" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <path d="M 190 420 L 240 370 L 290 390 L 350 320 L 410 340 L 460 280" fill="none" stroke="{t['accent']}" stroke-width="3"/>
  <circle cx="460" cy="280" r="6" fill="{t['danger']}"/>
  {badge(240, 500, "后台控制台框架", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_273(): # KPI数据大指标 (KPI Metric Stat Counter)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Big Stat KPI Dashboard Card -->
  <rect x="50" y="80" width="450" height="460" rx="16" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- KPI Label -->
  <text x="90" y="140" fill="{t['text_dim']}" font-size="14" font-weight="bold" font-family="Montserrat" letter-spacing="2">NET CONVERSION RATE</text>
  <!-- Colossal Headline Stat Number -->
  <text x="90" y="240" fill="#FFFFFF" font-size="76" font-weight="900" font-family="Montserrat">48.6%</text>
  <!-- Growth Badge -->
  <rect x="360" y="185" width="100" height="36" rx="18" fill="{t['accent']}"/>
  <text x="410" y="208" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">+14.2% ↑</text>
  <!-- Ambient Trend Vector Line -->
  <path d="M 90 420 Q 200 440 275 350 T 450 310" fill="none" stroke="{t['accent']}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="450" cy="310" r="16" fill="{t['accent']}"/>
  <circle cx="450" cy="310" r="5" fill="#FFFFFF"/>
  <text x="90" y="470" fill="{t['text_dim']}" font-size="12" font-family="Montserrat">Updated 2 minutes ago · Benchmark 32.0%</text>
  {badge(185, 490, "核心 KPI 视觉压强", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_275(): # 3阶定价矩阵 (Pricing 3-Tier Matrix)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- 3-Tier Pricing Matrix (Starter, Pro [Hero Highlight], Enterprise) -->
  <!-- Card 1: Starter -->
  <rect x="40" y="120" width="135" height="380" rx="10" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="107" y="160" fill="{t['text_dim']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">STARTER</text>
  <text x="107" y="205" fill="#FFFFFF" font-size="26" font-weight="900" font-family="Montserrat" text-anchor="middle">$0</text>

  <!-- Card 2: PRO (HERO POPPED ELEVATED) -->
  <rect x="195" y="80" width="160" height="430" rx="12" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Popular Tag -->
  <rect x="235" y="65" width="80" height="24" rx="12" fill="{t['danger']}"/>
  <text x="275" y="81" fill="#FFFFFF" font-size="10" font-weight="900" font-family="Montserrat" text-anchor="middle">POPULAR</text>
  <text x="275" y="130" fill="{t['accent']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">PRO PLAN</text>
  <text x="275" y="185" fill="#FFFFFF" font-size="38" font-weight="900" font-family="Montserrat" text-anchor="middle">$29</text>
  <rect x="220" y="440" width="110" height="40" rx="6" fill="{t['accent']}"/>
  <text x="275" y="465" fill="#FFFFFF" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">GET PRO</text>

  <!-- Card 3: Enterprise -->
  <rect x="375" y="120" width="135" height="380" rx="10" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="442" y="160" fill="{t['text_dim']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">ENTERPRISE</text>
  <text x="442" y="205" fill="#FFFFFF" font-size="26" font-weight="900" font-family="Montserrat" text-anchor="middle">$99</text>

  {badge(185, 530, "突出高转化核心档位", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_281(): # 看板列式泳道 (Kanban 3-Column Board)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Col 1: TO DO -->
  <rect x="60" y="90" width="125" height="440" rx="6" fill="{t['bg']}"/>
  <text x="122" y="120" fill="{t['text_dim']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">TODO (3)</text>
  <rect x="70" y="140" width="105" height="60" rx="4" fill="{t['stroke']}"/>
  <rect x="70" y="215" width="105" height="60" rx="4" fill="{t['stroke']}"/>

  <!-- Col 2: IN PROGRESS (HERO) -->
  <rect x="210" y="90" width="130" height="440" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.8"/>
  <text x="275" y="120" fill="{t['accent']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">PROGRESS (2)</text>
  <rect x="220" y="140" width="110" height="85" rx="6" fill="{t['accent']}" fill-opacity="0.2" stroke="{t['accent']}" stroke-width="1.5"/>
  <circle cx="240" cy="165" r="10" fill="{t['danger']}"/>
  <text x="240" y="205" fill="#FFFFFF" font-size="11" font-weight="bold" font-family="Montserrat">Feature v2.0</text>

  <!-- Col 3: DONE -->
  <rect x="365" y="90" width="125" height="440" rx="6" fill="{t['bg']}"/>
  <text x="427" y="120" fill="{t['accent_alt']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">DONE (5)</text>
  <rect x="375" y="140" width="105" height="50" rx="4" fill="{t['stroke']}"/>
  <rect x="375" y="205" width="105" height="50" rx="4" fill="{t['stroke']}"/>
  {badge(185, 520, "看板泳道任务流转", t['accent'], t['text'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat05
CAT05_SVGS = {
    "224": gen_224, "230": gen_230, "243": gen_243, "255": gen_255, "273": gen_273,
    "275": gen_275, "281": gen_281
}


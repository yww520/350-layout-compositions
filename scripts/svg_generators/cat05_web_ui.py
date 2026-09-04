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

def gen_222(): # 普通流布局 (Normal Flow)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical Block Stacking -->
  <rect x="80" y="100" width="390" height="60" rx="6" fill="{t['accent']}"/>
  <text x="275" y="135" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">BLOCK 1 (100% WIDTH)</text>
  <!-- Inline Elements flowing horizontally -->
  <g transform="translate(80, 180)">
    <rect x="0" y="0" width="110" height="40" rx="4" fill="{t['stroke']}"/>
    <text x="55" y="25" fill="#FFFFFF" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">INLINE 1</text>
    <rect x="125" y="0" width="130" height="40" rx="4" fill="{t['stroke']}"/>
    <text x="190" y="25" fill="#FFFFFF" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">INLINE 2</text>
    <rect x="270" y="0" width="120" height="40" rx="4" fill="{t['stroke']}"/>
    <text x="330" y="25" fill="#FFFFFF" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">INLINE 3</text>
  </g>
  <rect x="80" y="245" width="390" height="120" rx="6" fill="{t['accent_alt']}" fill-opacity="0.85"/>
  <text x="275" y="310" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">BLOCK 2 (VERTICAL CASCADE)</text>
  {badge(185, 480, "块级向下行内横向标准流", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_223(): # 块级布局 (Block-Level Layout)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Stacking Block boxes with margins -->
  <rect x="80" y="100" width="390" height="75" rx="6" fill="{t['accent']}"/>
  <text x="275" y="145" fill="{t['bg']}" font-size="15" font-weight="900" font-family="Montserrat" text-anchor="middle">BLOCK BOX A (margin-bottom: 24px)</text>
  <line x1="80" y1="190" x2="470" y2="190" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <rect x="80" y="205" width="390" height="100" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="275" y="260" fill="#FFFFFF" font-size="15" font-weight="900" font-family="Montserrat" text-anchor="middle">BLOCK BOX B (display: block)</text>
  <rect x="80" y="330" width="390" height="75" rx="6" fill="{t['accent_alt']}"/>
  <text x="275" y="375" fill="{t['bg']}" font-size="15" font-weight="900" font-family="Montserrat" text-anchor="middle">BLOCK BOX C</text>
  {badge(185, 500, "块级独占单行垂直堆砌", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_225(): # 流根布局 (Block Formatting Context BFC)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Outer Container with BFC Isolation boundary -->
  <rect x="75" y="90" width="400" height="390" rx="8" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="95" y="120" fill="{t['danger']}" font-size="12" font-weight="bold" font-family="Montserrat">BFC CONTAINER (overflow: hidden)</text>
  <!-- Contained Float Box inside BFC -->
  <rect x="95" y="140" width="130" height="110" rx="6" fill="{t['accent']}"/>
  <text x="160" y="200" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">FLOAT: LEFT</text>
  <!-- Sibling text avoiding float overlap -->
  <rect x="245" y="140" width="210" height="20" rx="3" fill="{t['stroke']}"/>
  <rect x="245" y="170" width="190" height="20" rx="3" fill="{t['stroke']}"/>
  <rect x="245" y="200" width="210" height="20" rx="3" fill="{t['stroke']}"/>
  <rect x="95" y="270" width="360" height="100" rx="6" fill="{t['accent_alt']}" opacity="0.8"/>
  <text x="275" y="325" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">NO MARGIN COLLAPSE ACROSS BFC</text>
  {badge(185, 520, "块格式化上下文BFC隔离", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_227(): # 网格布局 (Grid Layout 2D Tracks)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Numbered Grid Lines 1 to 4 -->
  <g stroke="#FF5252" stroke-width="1.2" stroke-dasharray="4,4">
    <line x1="80" y1="90" x2="80" y2="450"/><line x1="210" y1="90" x2="210" y2="450"/>
    <line x1="340" y1="90" x2="340" y2="450"/><line x1="470" y1="90" x2="470" y2="450"/>
    <line x1="70" y1="100" x2="480" y2="100"/><line x1="70" y1="210" x2="480" y2="210"/>
    <line x1="70" y1="320" x2="480" y2="320"/><line x1="70" y1="430" x2="480" y2="430"/>
  </g>
  <!-- Line Numbers -->
  <text x="80" y="85" fill="#FF5252" font-size="11" font-family="Montserrat" text-anchor="middle">1</text>
  <text x="210" y="85" fill="#FF5252" font-size="11" font-family="Montserrat" text-anchor="middle">2</text>
  <text x="340" y="85" fill="#FF5252" font-size="11" font-family="Montserrat" text-anchor="middle">3</text>
  <text x="470" y="85" fill="#FF5252" font-size="11" font-family="Montserrat" text-anchor="middle">4</text>
  <!-- Grid area spanned cell -->
  <rect x="85" y="105" width="250" height="100" rx="6" fill="{t['accent']}"/>
  <text x="210" y="160" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">grid-column: 1 / 3</text>
  <rect x="345" y="105" width="120" height="210" rx="6" fill="{t['accent_alt']}"/>
  <text x="405" y="215" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">grid-row: 1 / 3</text>
  <rect x="85" y="215" width="120" height="100" rx="6" fill="{t['stroke']}"/>
  <rect x="215" y="215" width="120" height="100" rx="6" fill="{t['stroke']}"/>
  {badge(185, 490, "CSS Grid 二维轨道布局", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_228(): # 子网格布局 (CSS Subgrid)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Shared Grid Row Tracks across multiple cards -->
  <line x1="60" y1="150" x2="490" y2="150" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="60" y1="250" x2="490" y2="250" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="60" y1="430" x2="490" y2="430" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <!-- Card A -->
  <rect x="75" y="100" width="180" height="340" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="90" y="110" width="150" height="30" rx="4" fill="{t['accent']}"/>
  <rect x="90" y="160" width="150" height="80" rx="4" fill="{t['stroke']}"/>
  <!-- Card B (Header & content row heights align perfectly via subgrid) -->
  <rect x="295" y="100" width="180" height="340" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="310" y="110" width="150" height="30" rx="4" fill="{t['accent']}"/>
  <rect x="310" y="160" width="150" height="80" rx="4" fill="{t['stroke']}"/>
  <text x="275" y="475" fill="{t['danger']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">grid-template-rows: subgrid</text>
  {badge(185, 510, "卡片行对齐无缝子网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_229(): # 多栏布局 (Multi-Column Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="100" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">column-count: 3; column-gap: 24px;</text>
  <!-- 3 Text Columns with column-rule dividers -->
  <line x1="195" y1="120" x2="195" y2="450" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="355" y1="120" x2="355" y2="450" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <g fill="{t['stroke']}">
    <rect x="75" y="130" width="105" height="310" rx="4"/>
    <rect x="210" y="130" width="130" height="310" rx="4" fill="{t['accent_alt']}" opacity="0.7"/>
    <rect x="370" y="130" width="105" height="310" rx="4"/>
  </g>
  {badge(185, 490, "报章多栏流动分栏", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_231(): # 浮动布局 (Float & Clearfix)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Floated Image Box Left -->
  <rect x="80" y="110" width="150" height="140" rx="6" fill="{t['accent']}"/>
  <circle cx="155" cy="180" r="32" fill="{t['bg']}"/>
  <text x="155" y="140" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">float: left;</text>
  <!-- Text lines wrapping around float -->
  <g fill="{t['stroke']}">
    <rect x="245" y="110" width="220" height="12" rx="2"/>
    <rect x="245" y="135" width="220" height="12" rx="2"/>
    <rect x="245" y="160" width="220" height="12" rx="2"/>
    <rect x="245" y="185" width="200" height="12" rx="2"/>
    <rect x="245" y="210" width="220" height="12" rx="2"/>
    <rect x="245" y="235" width="180" height="12" rx="2"/>
    <!-- Text resumed below float -->
    <rect x="80" y="270" width="385" height="12" rx="2"/>
    <rect x="80" y="295" width="385" height="12" rx="2"/>
  </g>
  <!-- Clearfix indicator bar -->
  <line x1="80" y1="330" x2="465" y2="330" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="275" y="360" fill="{t['danger']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">clear: both; (CLEARFIX BARRIER)</text>
  {badge(185, 500, "经典图文浮动与闭合", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_232(): # 相对定位布局 (Relative Positioning)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Original Reserved Space (Dashed Ghost Box) -->
  <rect x="110" y="160" width="200" height="150" rx="6" fill="none" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="210" y="240" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">ORIGINAL FLOW SPACE</text>
  <!-- Shifted Relative Box (top: 40px, left: 60px) -->
  <rect x="170" y="200" width="200" height="150" rx="6" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
  <circle cx="270" cy="275" r="28" fill="{t['bg']}"/>
  <!-- Offset displacement vectors -->
  <line x1="110" y1="160" x2="170" y2="160" stroke="{t['danger']}" stroke-width="2"/>
  <line x1="170" y1="160" x2="170" y2="200" stroke="{t['danger']}" stroke-width="2"/>
  <text x="270" y="390" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">top: 40px; left: 60px;</text>
  {badge(185, 480, "相对原位偏移保留占位", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_233(): # 绝对定位布局 (Absolute Positioning)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Relative Parent Container -->
  <rect x="80" y="90" width="390" height="410" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="100" y="120" fill="{t['text_dim']}" font-size="12" font-family="Montserrat">parent {{ position: relative; }}</text>
  <!-- Absolute Box pinned to bottom right -->
  <rect x="260" y="320" width="190" height="160" rx="8" fill="{t['danger']}"/>
  <circle cx="355" cy="400" r="24" fill="#FFFFFF"/>
  <text x="355" y="360" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">ABSOLUTE</text>
  <line x1="450" y1="320" x2="470" y2="320" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2,2"/>
  <line x1="260" y1="480" x2="260" y2="500" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="2,2"/>
  {badge(185, 520, "脱离文档流精准绝对锚定", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_234(): # 固定定位布局 (Fixed Positioning Viewport)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Scrolling Page Content in background -->
  <g fill="{t['stroke']}" opacity="0.4">
    {''.join([f'<rect x="80" y="{140 + i*40}" width="390" height="22" rx="4"/>' for i in range(8)])}
  </g>
  <!-- Fixed Navbar pinned to viewport top -->
  <rect x="50" y="60" width="450" height="60" rx="8" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
  <circle cx="90" cy="90" r="14" fill="{t['bg']}"/>
  <text x="275" y="96" fill="{t['bg']}" font-size="15" font-weight="900" font-family="Montserrat" text-anchor="middle">FIXED NAVBAR (position: fixed; top: 0)</text>
  {badge(185, 480, "视口钉死固定不随滚动", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_235(): # 粘性定位布局 (Sticky Positioning)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Top scrolled-out content -->
  <rect x="80" y="80" width="390" height="50" rx="4" fill="{t['stroke']}" opacity="0.4"/>
  <!-- Sticky Header Bar Pinning to Top: 20px -->
  <rect x="70" y="150" width="410" height="55" rx="6" fill="{t['danger']}" stroke="#FFFFFF" stroke-width="2"/>
  <text x="275" y="184" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">STICKY SECTION HEADER (top: 0)</text>
  <!-- Pinned Pin Marker -->
  <circle cx="450" cy="177" r="8" fill="#FFD600"/>
  <!-- Body rows scrolling underneath -->
  <rect x="80" y="225" width="390" height="60" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="80" y="300" width="390" height="60" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="80" y="375" width="390" height="60" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  {badge(185, 490, "滚动触顶吸附粘性定位", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_236(): # 瀑布流布局 (Masonry Staggered Columns)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Column 1 -->
  <rect x="75" y="90" width="115" height="140" rx="6" fill="{t['accent']}"/>
  <rect x="75" y="245" width="115" height="190" rx="6" fill="{t['stroke']}"/>
  <!-- Column 2 -->
  <rect x="205" y="90" width="115" height="200" rx="6" fill="{t['stroke']}"/>
  <rect x="205" y="305" width="115" height="130" rx="6" fill="{t['accent_alt']}"/>
  <!-- Column 3 -->
  <rect x="335" y="90" width="115" height="120" rx="6" fill="{t['accent_alt']}"/>
  <rect x="335" y="225" width="115" height="210" rx="6" fill="{t['danger']}"/>
  {badge(185, 520, "错落紧凑垂直瀑布流", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_237(): # 覆盖布局 (Modal Overlay Backdrop)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Dimmed Backdrop -->
  <rect x="50" y="60" width="450" height="500" fill="#000000" fill-opacity="0.7" rx="8"/>
  <!-- Elevated Modal Window Dialog -->
  <rect x="110" y="160" width="330" height="280" rx="10" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5"/>
  <rect x="110" y="160" width="330" height="40" rx="10" fill="{t['accent']}"/>
  <circle cx="135" cy="180" r="6" fill="#FF5F56"/>
  <text x="275" y="186" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">MODAL DIALOG</text>
  <circle cx="275" cy="270" r="32" fill="{t['accent_alt']}"/>
  <rect x="175" y="350" width="200" height="36" rx="6" fill="{t['accent']}"/>
  <text x="275" y="373" fill="{t['bg']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">CONFIRM ACTION</text>
  {badge(185, 520, "模态弹窗遮罩层级", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_238(): # 固定宽度布局 (Fixed-Width Centered 1200px)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Left Gutter -->
  <rect x="50" y="60" width="65" height="500" fill="{t['stroke']}" opacity="0.3"/>
  <!-- Right Gutter -->
  <rect x="435" y="60" width="65" height="500" fill="{t['stroke']}" opacity="0.3"/>
  <!-- Fixed 320px Canvas Center -->
  <rect x="115" y="90" width="320" height="420" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="135" y="120" width="280" height="120" rx="4" fill="{t['accent']}"/>
  <text x="275" y="290" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">max-width: 1200px; margin: auto;</text>
  {badge(185, 480, "固定版心居中留白", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_239(): # 流体布局 (Fluid Layout 100vw)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="60" y="110" width="430" height="340" rx="8" fill="{t['accent']}" fill-opacity="0.2" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Elastic arrows indicating 100% width stretching -->
  <line x1="70" y1="280" x2="480" y2="280" stroke="#FFFFFF" stroke-width="3"/>
  <polygon points="70,280 85,272 85,288" fill="#FFFFFF"/>
  <polygon points="480,280 465,272 465,288" fill="#FFFFFF"/>
  <text x="275" y="250" fill="#FFFFFF" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">100% FLUID RESPONSIVENESS</text>
  {badge(185, 480, "全视口无界自适应流动", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_240(): # 响应式布局 (Responsive Breakpoint Cascade)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Desktop Wireframe -->
  <rect x="75" y="90" width="400" height="130" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="90" y="110" width="100" height="90" rx="4" fill="{t['accent']}"/>
  <rect x="205" y="110" width="170" height="90" rx="4" fill="{t['stroke']}"/>
  <text x="435" y="160" fill="{t['accent']}" font-size="11" font-family="Montserrat">1200px</text>
  <!-- Tablet -->
  <rect x="115" y="240" width="320" height="100" rx="6" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="1.5"/>
  <rect x="130" y="255" width="80" height="70" rx="4" fill="{t['accent_alt']}"/>
  <rect x="225" y="255" width="190" height="70" rx="4" fill="{t['stroke']}"/>
  <text x="390" y="370" fill="{t['accent_alt']}" font-size="11" font-family="Montserrat">768px</text>
  <!-- Mobile -->
  <rect x="185" y="360" width="180" height="100" rx="6" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="1.5"/>
  <rect x="200" y="375" width="150" height="30" rx="3" fill="{t['danger']}"/>
  <rect x="200" y="415" width="150" height="30" rx="3" fill="{t['stroke']}"/>
  {badge(185, 520, "多端断点级联响应式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_241(): # 自适应布局 (Adaptive Stepped Layout)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Stepped discrete device profiles -->
  <rect x="80" y="120" width="390" height="90" rx="6" fill="{t['accent']}" fill-opacity="0.9"/>
  <text x="275" y="170" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">DESKTOP PROFILE (FIXED 1024px)</text>
  <rect x="110" y="230" width="330" height="80" rx="6" fill="{t['accent_alt']}" fill-opacity="0.9"/>
  <text x="275" y="275" fill="{t['bg']}" font-size="15" font-weight="900" font-family="Montserrat" text-anchor="middle">TABLET PROFILE (FIXED 768px)</text>
  <rect x="155" y="330" width="240" height="80" rx="6" fill="{t['danger']}"/>
  <text x="275" y="375" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">MOBILE PROFILE (375px)</text>
  {badge(185, 480, "阶梯自适应离散模版", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_242(): # 容器查询布局 (Container Queries @container)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Wide Container Parent -->
  <rect x="70" y="100" width="410" height="160" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="90" y="125" fill="{t['accent']}" font-size="11" font-family="Montserrat">@container (min-width: 350px) -> HORIZONTAL</text>
  <rect x="90" y="140" width="120" height="100" rx="6" fill="{t['accent']}"/>
  <rect x="230" y="150" width="220" height="20" rx="4" fill="{t['stroke']}"/>
  <rect x="230" y="185" width="180" height="16" rx="3" fill="{t['stroke']}"/>
  <!-- Narrow Container Parent -->
  <rect x="145" y="280" width="260" height="200" rx="8" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <text x="160" y="305" fill="{t['danger']}" font-size="11" font-family="Montserrat">@container (max-width: 300px) -> STACK</text>
  <rect x="165" y="320" width="220" height="60" rx="4" fill="{t['danger']}"/>
  <rect x="165" y="395" width="220" height="16" rx="3" fill="{t['stroke']}"/>
  <rect x="165" y="420" width="180" height="16" rx="3" fill="{t['stroke']}"/>
  {badge(185, 520, "父容器尺寸驱动组件重构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])


def gen_244(): # 盒子原语 (The Box Model)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}"/>
  <!-- Margin (Orange) -->
  <rect x="70" y="90" width="410" height="410" rx="8" fill="none" stroke="#FF9800" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="90" y="115" fill="#FF9800" font-size="12" font-weight="bold" font-family="Montserrat">MARGIN</text>
  <!-- Border (Yellow) -->
  <rect x="100" y="130" width="350" height="330" rx="6" fill="none" stroke="#FFD600" stroke-width="2.5"/>
  <text x="120" y="155" fill="#FFD600" font-size="12" font-weight="bold" font-family="Montserrat">BORDER</text>
  <!-- Padding (Green) -->
  <rect x="130" y="170" width="290" height="250" rx="6" fill="none" stroke="#00E676" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="150" y="195" fill="#00E676" font-size="12" font-weight="bold" font-family="Montserrat">PADDING</text>
  <!-- Content (Blue) -->
  <rect x="160" y="210" width="230" height="170" rx="6" fill="{t['accent']}"/>
  <text x="275" y="300" fill="#FFFFFF" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">CONTENT</text>
  {badge(185, 470, "同心盒模型四层架构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_245(): # 居中器原语 (The Center)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <line x1="50" y1="310" x2="500" y2="310" stroke="{t['accent']}" stroke-width="1.8" stroke-dasharray="6,6"/>
  <line x1="275" y1="60" x2="275" y2="560" stroke="{t['accent']}" stroke-width="1.8" stroke-dasharray="6,6"/>
  <circle cx="275" cy="310" r="80" fill="{t['accent']}" fill-opacity="0.15"/>
  <circle cx="275" cy="310" r="42" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="12" fill="#FFFFFF"/>
  <text x="275" y="430" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">place-items: center (50% / 50%)</text>
  {badge(185, 490, "绝对几何居中原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_246(): # 簇群原语 (The Cluster)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Flex-wrap chip cluster flowing naturally -->
  <g transform="translate(75, 140)">
    <rect x="0" y="0" width="90" height="36" rx="18" fill="{t['accent']}"/>
    <rect x="105" y="0" width="130" height="36" rx="18" fill="{t['accent_alt']}"/>
    <rect x="250" y="0" width="110" height="36" rx="18" fill="{t['stroke']}"/>
    <rect x="0" y="50" width="150" height="36" rx="18" fill="{t['stroke']}"/>
    <rect x="165" y="50" width="100" height="36" rx="18" fill="{t['accent']}"/>
    <rect x="280" y="50" width="90" height="36" rx="18" fill="{t['danger']}"/>
    <rect x="0" y="100" width="120" height="36" rx="18" fill="{t['accent_alt']}"/>
    <rect x="135" y="100" width="160" height="36" rx="18" fill="{t['stroke']}"/>
  </g>
  <text x="275" y="340" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">flex-wrap: wrap; gap: 1rem;</text>
  {badge(185, 480, "自然换行簇群流原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_247(): # 侧栏原语 (The Sidebar)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Sidebar Fixed Basis 120px -->
  <rect x="75" y="100" width="120" height="380" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="135" y="140" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">SIDEBAR</text>
  <!-- Main Growing Body -->
  <rect x="210" y="100" width="265" height="380" rx="6" fill="{t['stroke']}"/>
  <circle cx="342" cy="260" r="42" fill="{t['accent']}"/>
  <text x="342" y="350" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">MAIN (flex-grow: 1)</text>
  {badge(185, 520, "弹性侧栏主次原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_248(): # 切换器原语 (The Switcher)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Horizontal Row Mode (Above Threshold) -->
  <rect x="75" y="110" width="390" height="120" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="90" y="130" width="110" height="80" rx="4" fill="{t['accent']}"/>
  <rect x="215" y="130" width="110" height="80" rx="4" fill="{t['accent_alt']}"/>
  <rect x="340" y="130" width="110" height="80" rx="4" fill="{t['stroke']}"/>
  <!-- Switch Arrow -->
  <line x1="275" y1="245" x2="275" y2="275" stroke="{t['danger']}" stroke-width="3"/>
  <polygon points="275,275 268,265 282,265" fill="{t['danger']}"/>
  <!-- Vertical Stack Mode (Below Threshold) -->
  <rect x="145" y="285" width="260" height="170" rx="8" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <rect x="160" y="300" width="230" height="35" rx="4" fill="{t['accent']}"/>
  <rect x="160" y="345" width="230" height="35" rx="4" fill="{t['accent_alt']}"/>
  <rect x="160" y="390" width="230" height="35" rx="4" fill="{t['stroke']}"/>
  {badge(185, 500, "断点行列突变切换原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_249(): # 封面原语 (The Cover)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Header Top Pinned -->
  <rect x="80" y="90" width="390" height="40" rx="6" fill="{t['stroke']}"/>
  <text x="275" y="115" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">HEADER (PINNED TOP)</text>
  <!-- Centered Hero Principal (margin-block: auto) -->
  <rect x="110" y="210" width="330" height="160" rx="8" fill="{t['accent']}"/>
  <text x="275" y="280" fill="{t['bg']}" font-size="24" font-weight="900" font-family="Montserrat" text-anchor="middle">HERO (CENTERED)</text>
  <text x="275" y="310" fill="{t['bg']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">margin-block: auto;</text>
  <!-- Footer Bottom Pinned -->
  <rect x="80" y="460" width="390" height="40" rx="6" fill="{t['stroke']}"/>
  <text x="275" y="485" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">FOOTER (PINNED BOTTOM)</text>
  {badge(185, 520, "满屏首尾锚定封面原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_250(): # 自适应网格原语 (Auto-Grid / repeat(auto-fit))
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="100" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">repeat(auto-fit, minmax(110px, 1fr))</text>
  <g fill="{t['stroke']}">
    <rect x="75" y="125" width="115" height="130" rx="6" fill="{t['accent']}"/>
    <rect x="210" y="125" width="115" height="130" rx="6" fill="{t['accent_alt']}"/>
    <rect x="345" y="125" width="115" height="130" rx="6"/>
    <rect x="75" y="275" width="115" height="130" rx="6"/>
    <rect x="210" y="275" width="115" height="130" rx="6"/>
    <rect x="345" y="275" width="115" height="130" rx="6" fill="{t['danger']}"/>
  </g>
  {badge(185, 480, "无需媒体查询自动卡片网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_251(): # 比例框原语 (The Frame / Aspect Ratio)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 16:9 Video Box -->
  <rect x="75" y="160" width="390" height="220" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5"/>
  <polygon points="255,245 255,295 305,270" fill="{t['danger']}"/>
  {dimension_h(75, 465, 140, "16 UNIT WIDTH", t['accent'], t['accent'])}
  {dimension_v(160, 380, 485, "9", t['accent'], t['accent'])}
  <text x="275" y="430" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">aspect-ratio: 16 / 9;</text>
  {badge(185, 490, "等比缩放比例框原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_252(): # 横向卷轴原语 (The Reel)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Horizontal Scrolling Reel Cards overflowing canvas -->
  <rect x="75" y="170" width="130" height="180" rx="8" fill="{t['accent']}"/>
  <rect x="220" y="170" width="130" height="180" rx="8" fill="{t['accent_alt']}"/>
  <rect x="365" y="170" width="130" height="180" rx="8" fill="{t['stroke']}"/>
  <!-- Scroll Snapping Arrow -->
  <line x1="90" y1="390" x2="450" y2="390" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="8,6"/>
  <polygon points="450,390 435,382 435,398" fill="#FFFFFF"/>
  <text x="275" y="430" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">overflow-x: auto; scroll-snap-type: x mandatory;</text>
  {badge(185, 490, "平滑吸附横向走马灯原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_253(): # 悬浮层原语 (Floating Action Button & Tooltip)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Base background card -->
  <rect x="80" y="100" width="380" height="380" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Tooltip Popover Layer -->
  <rect x="130" y="160" width="210" height="60" rx="6" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <polygon points="235,220 245,235 255,220" fill="{t['accent']}"/>
  <text x="235" y="195" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">POPOVER TOOLTIP</text>
  <!-- Floating Action Button (FAB) Bottom Right -->
  <circle cx="400" cy="420" r="32" fill="{t['danger']}"/>
  <line x1="385" y1="420" x2="415" y2="420" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
  <line x1="400" y1="405" x2="400" y2="435" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
  {badge(185, 520, "悬浮交互提升原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_254(): # 图标文字对齐原语 (Icon + Text Baseline Alignment)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Alignment Baseline Red Rule -->
  <line x1="70" y1="280" x2="480" y2="280" stroke="{t['danger']}" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- Icon SVG Square Optical Center -->
  <rect x="90" y="220" width="60" height="60" rx="10" fill="{t['accent']}"/>
  <circle cx="120" cy="250" r="14" fill="#FFFFFF"/>
  <!-- Typography baseline snapped -->
  <text x="170" y="280" fill="#FFFFFF" font-size="42" font-weight="900" font-family="Montserrat">Settings</text>
  <text x="275" y="370" fill="{t['text_dim']}" font-size="13" font-family="Montserrat" text-anchor="middle">display: inline-flex; align-items: center;</text>
  {badge(185, 480, "图标文字光学垂直对齐", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])


def gen_256(): # 双列页面 (Two-Column Page)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Column 1 (Left 50%) -->
  <rect x="75" y="100" width="185" height="390" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="167" cy="220" r="36" fill="{t['accent']}"/>
  <text x="167" y="320" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">COLUMN 01</text>
  <!-- Column 2 (Right 50%) -->
  <rect x="285" y="100" width="185" height="390" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="377" cy="220" r="36" fill="{t['accent_alt']}"/>
  <text x="377" y="320" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">COLUMN 02</text>
  {badge(185, 520, "双列等宽经典分栏", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_257(): # 三列页面 (Three-Column Page)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Left Nav (20%) -->
  <rect x="70" y="100" width="80" height="390" rx="4" fill="{t['stroke']}"/>
  <text x="110" y="140" fill="{t['accent']}" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">NAV</text>
  <!-- Center Main Feed (55%) -->
  <rect x="165" y="100" width="215" height="390" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="272" cy="240" r="38" fill="{t['accent']}"/>
  <text x="272" y="340" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">MAIN FEED</text>
  <!-- Right Widgets (25%) -->
  <rect x="395" y="100" width="85" height="390" rx="4" fill="{t['stroke']}"/>
  <text x="437" y="140" fill="{t['accent_alt']}" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">WIDGETS</text>
  {badge(185, 520, "经典三栏左右护持布局", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_258(): # 侧边栏页面 (Sidebar Page with Collapsed Rail)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Collapsed Icon Rail Left -->
  <rect x="65" y="90" width="55" height="410" rx="4" fill="{t['stroke']}"/>
  <circle cx="92" cy="130" r="12" fill="{t['accent']}"/>
  <circle cx="92" cy="170" r="12" fill="{t['accent_alt']}"/>
  <!-- Expandable Menu Sidebar -->
  <rect x="130" y="90" width="130" height="410" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="195" y="130" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">SIDEBAR</text>
  <!-- Main Workspace Right -->
  <rect x="270" y="90" width="215" height="410" rx="6" fill="{t['stroke']}" opacity="0.5"/>
  <circle cx="377" cy="260" r="42" fill="{t['accent']}"/>
  {badge(185, 520, "双层侧栏伸缩工作台", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_259(): # 分屏布局 (Split-Screen 50/50 Layout)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Left Half: Photography / Brand Visual -->
  <rect x="65" y="85" width="200" height="420" rx="6" fill="{t['accent']}"/>
  <circle cx="165" cy="270" r="48" fill="#FFFFFF"/>
  <text x="165" y="370" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">BRAND HERO</text>
  <!-- Right Half: Clean Login Form -->
  <rect x="280" y="85" width="200" height="420" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="380" y="170" fill="#FFFFFF" font-size="16" font-weight="bold" font-family="Montserrat" text-anchor="middle">SIGN IN</text>
  <rect x="300" y="200" width="160" height="35" rx="4" fill="{t['stroke']}"/>
  <rect x="300" y="250" width="160" height="35" rx="4" fill="{t['stroke']}"/>
  <rect x="300" y="310" width="160" height="40" rx="6" fill="{t['accent']}"/>
  {badge(185, 520, "50/50 图文分屏登录页", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_260(): # 圣杯布局 (Holy Grail Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Header Top -->
  <rect x="75" y="90" width="390" height="45" rx="4" fill="{t['accent']}"/>
  <text x="270" y="118" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">HEADER (100% WIDTH)</text>
  <!-- Nav Left -->
  <rect x="75" y="145" width="85" height="240" rx="4" fill="{t['stroke']}"/>
  <text x="117" y="260" fill="{t['accent']}" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">NAV</text>
  <!-- Main Center -->
  <rect x="170" y="145" width="200" height="240" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="270" y="260" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">MAIN CONTENT</text>
  <!-- Aside Right -->
  <rect x="380" y="145" width="85" height="240" rx="4" fill="{t['stroke']}"/>
  <text x="422" y="260" fill="{t['accent']}" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">ASIDE</text>
  <!-- Footer Bottom -->
  <rect x="75" y="395" width="390" height="45" rx="4" fill="{t['accent']}"/>
  <text x="270" y="423" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">FOOTER (100% WIDTH)</text>
  {badge(185, 480, "网页经典五段圣杯架构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_261(): # 页眉—主体—页脚 (Header-Body-Footer)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Header -->
  <rect x="75" y="90" width="390" height="50" rx="6" fill="{t['accent']}"/>
  <text x="270" y="122" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">HEADER</text>
  <!-- Main Body -->
  <rect x="75" y="155" width="390" height="240" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="270" cy="270" r="42" fill="{t['accent_alt']}"/>
  <!-- Footer -->
  <rect x="75" y="410" width="390" height="50" rx="6" fill="{t['stroke']}"/>
  <text x="270" y="442" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">STICKY FOOTER</text>
  {badge(185, 490, "三段式首中尾通用骨架", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_262(): # 顶部导航布局 (Top Navigation Bar Layout)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Topnav Banner -->
  <rect x="65" y="80" width="420" height="55" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Logo -->
  <circle cx="95" cy="107" r="14" fill="{t['accent']}"/>
  <!-- Nav Links -->
  <rect x="140" y="102" width="50" height="12" rx="2" fill="#FFFFFF"/>
  <rect x="205" y="102" width="50" height="12" rx="2" fill="{t['text_dim']}"/>
  <rect x="270" y="102" width="50" height="12" rx="2" fill="{t['text_dim']}"/>
  <!-- Search Input & Avatar -->
  <rect x="350" y="97" width="80" height="22" rx="11" fill="{t['stroke']}"/>
  <circle cx="455" cy="107" r="12" fill="{t['danger']}"/>
  <!-- Hero below nav -->
  <rect x="65" y="155" width="420" height="280" rx="8" fill="{t['stroke']}" opacity="0.5"/>
  {badge(185, 480, "全局顶栏导航标杆架构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_263(): # 导航抽屉布局 (Navigation Drawer / Off-Canvas)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Dimmed Main Canvas -->
  <rect x="50" y="60" width="450" height="500" fill="#000000" fill-opacity="0.6" rx="8"/>
  <!-- Sliding Drawer extending from left edge -->
  <rect x="50" y="60" width="220" height="500" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2.5" rx="8"/>
  <circle cx="100" cy="120" r="20" fill="{t['accent']}"/>
  <g fill="{t['stroke']}">
    <rect x="80" y="170" width="150" height="35" rx="4" fill="{t['accent']}"/>
    <rect x="80" y="220" width="150" height="35" rx="4"/>
    <rect x="80" y="270" width="150" height="35" rx="4"/>
    <rect x="80" y="320" width="150" height="35" rx="4"/>
  </g>
  <!-- Slide-in Arrow -->
  <line x1="220" y1="250" x2="280" y2="250" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="6,4"/>
  <polygon points="280,250 268,242 268,258" fill="#FFFFFF"/>
  {badge(185, 520, "侧滑呼出抽屉导航", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_264(): # 底部导航布局 (Mobile Bottom Navigation)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Mobile Screen Shell -->
  <rect x="115" y="80" width="320" height="440" rx="24" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Content Area -->
  <rect x="140" y="120" width="270" height="280" rx="8" fill="{t['stroke']}" opacity="0.4"/>
  <!-- Bottom Bar with 4 Icons -->
  <rect x="115" y="430" width="320" height="60" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="160" cy="460" r="14" fill="{t['accent']}"/>
  <circle cx="225" cy="460" r="12" fill="{t['text_dim']}"/>
  <circle cx="290" cy="460" r="12" fill="{t['text_dim']}"/>
  <circle cx="355" cy="460" r="12" fill="{t['text_dim']}"/>
  <circle cx="420" cy="460" r="12" fill="{t['text_dim']}"/>
  {badge(185, 520, "移动端底部固定导航条", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_265(): # 标签页布局 (Tabbed Interface)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Tab Header Bar -->
  <g transform="translate(75, 100)">
    <!-- Active Tab (Highlight) -->
    <rect x="0" y="0" width="120" height="40" rx="6" fill="{t['accent']}"/>
    <text x="60" y="25" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">OVERVIEW</text>
    <!-- Inactive Tab 2 -->
    <rect x="130" y="0" width="120" height="40" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
    <text x="190" y="25" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">SETTINGS</text>
    <!-- Inactive Tab 3 -->
    <rect x="260" y="0" width="120" height="40" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
    <text x="320" y="25" fill="{t['text_dim']}" font-size="12" font-family="Montserrat" text-anchor="middle">METRICS</text>
  </g>
  <!-- Active Tab Panel Content -->
  <rect x="75" y="150" width="390" height="300" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="270" cy="280" r="50" fill="{t['accent_alt']}"/>
  {badge(185, 490, "多维度视窗标签页切换", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_266(): # 手风琴布局 (Accordion Collapsible List)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Accordion Item 1 (Collapsed) -->
  <rect x="75" y="100" width="390" height="50" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="100" y="132" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat">01. What is Swiss Typographic Style?</text>
  <text x="435" y="132" fill="{t['accent']}" font-size="16" font-weight="900">+</text>
  <!-- Accordion Item 2 (EXPANDED ACTIVE) -->
  <rect x="75" y="165" width="390" height="160" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="100" y="197" fill="{t['accent']}" font-size="13" font-weight="bold" font-family="Montserrat">02. How do grids establish visual rhythm?</text>
  <text x="435" y="197" fill="{t['accent']}" font-size="18" font-weight="900">−</text>
  <rect x="100" y="225" width="340" height="80" rx="4" fill="{t['stroke']}" opacity="0.5"/>
  <!-- Accordion Item 3 (Collapsed) -->
  <rect x="75" y="340" width="390" height="50" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="100" y="372" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat">03. How to manage responsive breakpoints?</text>
  <text x="435" y="372" fill="{t['accent']}" font-size="16" font-weight="900">+</text>
  {badge(185, 510, "折叠手风琴信息展开", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_267(): # 列表—详情布局 (Master-Detail Split Pane)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Left Master List (35%) -->
  <rect x="70" y="90" width="135" height="410" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="80" y="110" width="115" height="50" rx="4" fill="{t['accent']}"/>
  <rect x="80" y="170" width="115" height="50" rx="4" fill="{t['stroke']}"/>
  <rect x="80" y="230" width="115" height="50" rx="4" fill="{t['stroke']}"/>
  <rect x="80" y="290" width="115" height="50" rx="4" fill="{t['stroke']}"/>
  <!-- Right Detail Reading Pane (65%) -->
  <rect x="220" y="90" width="260" height="410" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="260" cy="135" r="20" fill="{t['accent']}"/>
  <rect x="295" y="125" width="160" height="16" rx="3" fill="#FFFFFF"/>
  <rect x="240" y="180" width="220" height="12" rx="2" fill="{t['text_dim']}"/>
  <rect x="240" y="205" width="200" height="12" rx="2" fill="{t['text_dim']}"/>
  <rect x="240" y="240" width="220" height="140" rx="6" fill="{t['stroke']}" opacity="0.5"/>
  {badge(185, 520, "主从双窗格列表详情", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_268(): # 辅助窗格布局 (Inspector Drawer Layout)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Main Canvas (70%) -->
  <rect x="70" y="90" width="270" height="410" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="205" cy="270" r="50" fill="{t['accent']}"/>
  <!-- Right Inspector Drawer (30% like Figma Properties) -->
  <rect x="350" y="90" width="130" height="410" rx="6" fill="{t['stroke']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="415" y="125" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">INSPECTOR</text>
  <rect x="365" y="150" width="100" height="24" rx="3" fill="{t['bg']}"/>
  <rect x="365" y="185" width="100" height="24" rx="3" fill="{t['bg']}"/>
  <rect x="365" y="220" width="100" height="24" rx="3" fill="{t['bg']}"/>
  {badge(185, 520, "右侧属性检视辅助窗格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])


def gen_269(): # 信息流布局 (Feed Stream Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Card 1 -->
  <rect x="80" y="90" width="390" height="120" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <circle cx="120" cy="130" r="18" fill="{t['accent']}"/>
  <line x1="150" y1="125" x2="350" y2="125" stroke="#FFFFFF" stroke-width="3"/>
  <line x1="150" y1="145" x2="280" y2="145" stroke="{t['text_dim']}" stroke-width="2"/>
  <!-- Card 2 with image snippet -->
  <rect x="80" y="230" width="390" height="210" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="120" cy="270" r="18" fill="{t['accent_alt']}"/>
  <rect x="100" y="310" width="350" height="110" rx="4" fill="{t['stroke']}"/>
  {badge(185, 480, "社交媒体无限动态信息流", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_270(): # 卡片网格布局 (Card Grid / E-Commerce Products)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 2x2 Product Card Grid -->
  <g stroke="{t['accent']}" stroke-width="1.5">
    <rect x="75" y="90" width="185" height="175" rx="8" fill="{t['bg']}"/>
    <rect x="285" y="90" width="185" height="175" rx="8" fill="{t['bg']}"/>
    <rect x="75" y="285" width="185" height="175" rx="8" fill="{t['bg']}"/>
    <rect x="285" y="285" width="185" height="175" rx="8" fill="{t['accent']}" fill-opacity="0.9"/>
  </g>
  <circle cx="167" cy="160" r="32" fill="{t['accent']}"/>
  <circle cx="377" cy="160" r="32" fill="{t['accent_alt']}"/>
  <circle cx="167" cy="355" r="32" fill="{t['stroke']}"/>
  <circle cx="377" cy="355" r="32" fill="#FFFFFF"/>
  {badge(185, 490, "电商卡片矩阵规整展陈", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_271(): # 瀑布流页面 (Masonry Content Grid)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 3 Masonry columns staggered vertically -->
  <rect x="75" y="90" width="115" height="160" rx="6" fill="{t['accent']}"/>
  <rect x="75" y="265" width="115" height="200" rx="6" fill="{t['stroke']}"/>
  <rect x="205" y="90" width="115" height="210" rx="6" fill="{t['stroke']}"/>
  <rect x="205" y="315" width="115" height="150" rx="6" fill="{t['accent_alt']}"/>
  <rect x="335" y="90" width="115" height="140" rx="6" fill="{t['accent_alt']}"/>
  <rect x="335" y="245" width="115" height="220" rx="6" fill="{t['danger']}"/>
  {badge(185, 510, "多栏相册自适应瀑布流", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_274(): # 数据表格布局 (Data Table with Striped Rows)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Table Header -->
  <rect x="70" y="90" width="410" height="40" rx="4" fill="{t['accent']}"/>
  <text x="100" y="115" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat">ID</text>
  <text x="170" y="115" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat">NAME</text>
  <text x="320" y="115" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat">STATUS</text>
  <text x="430" y="115" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat">METRIC</text>
  <!-- Striped Data Rows -->
  <rect x="70" y="135" width="410" height="35" fill="{t['bg']}"/>
  <rect x="70" y="175" width="410" height="35" fill="{t['stroke']}" opacity="0.25"/>
  <rect x="70" y="215" width="410" height="35" fill="{t['bg']}"/>
  <rect x="70" y="255" width="410" height="35" fill="{t['stroke']}" opacity="0.25"/>
  <rect x="70" y="295" width="410" height="35" fill="{t['bg']}"/>
  <rect x="70" y="335" width="410" height="35" fill="{t['stroke']}" opacity="0.25"/>
  <!-- Status Badge on Row 2 -->
  <rect x="310" y="182" width="65" height="20" rx="10" fill="#00E676"/>
  <text x="342" y="196" fill="#12141A" font-size="10" font-weight="900" text-anchor="middle">ACTIVE</text>
  {badge(185, 480, "斑马条纹规整数据报表", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_276(): # 轮播布局 (Hero Carousel Slider)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Hero Carousel Slide -->
  <rect x="70" y="100" width="410" height="320" rx="10" fill="{t['stroke']}"/>
  <circle cx="275" cy="240" r="65" fill="{t['accent']}"/>
  <!-- Left/Right Nav Arrows -->
  <circle cx="95" cy="260" r="16" fill="{t['bg']}" fill-opacity="0.8"/>
  <text x="95" y="265" fill="#FFFFFF" font-size="14" font-weight="bold" text-anchor="middle">‹</text>
  <circle cx="455" cy="260" r="16" fill="{t['bg']}" fill-opacity="0.8"/>
  <text x="455" y="265" fill="#FFFFFF" font-size="14" font-weight="bold" text-anchor="middle">›</text>
  <!-- Pagination Dots -->
  <circle cx="235" cy="390" r="5" fill="{t['guide']}"/>
  <circle cx="255" cy="390" r="7" fill="{t['danger']}"/>
  <circle cx="275" cy="390" r="5" fill="{t['guide']}"/>
  <circle cx="295" cy="390" r="5" fill="{t['guide']}"/>
  {badge(185, 480, "幻灯走马轮播组件", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_277(): # 时间线布局 (Vertical Milestone Timeline)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vertical Track Line -->
  <line x1="110" y1="100" x2="110" y2="460" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Node 1 -->
  <circle cx="110" cy="130" r="12" fill="{t['accent']}"/><circle cx="110" cy="130" r="4" fill="#FFFFFF"/>
  <rect x="145" y="110" width="315" height="60" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- Node 2 (Active Milestone) -->
  <circle cx="110" cy="230" r="16" fill="{t['danger']}"/><circle cx="110" cy="230" r="5" fill="#FFFFFF"/>
  <rect x="145" y="205" width="315" height="75" rx="6" fill="{t['accent']}"/>
  <!-- Node 3 -->
  <circle cx="110" cy="350" r="12" fill="{t['stroke']}"/>
  <rect x="145" y="330" width="315" height="60" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  {badge(185, 480, "立式时间线履历节点", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_278(): # 看板布局 (Kanban Board Columns)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Col 1: TO DO -->
  <rect x="70" y="90" width="120" height="400" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="130" y="120" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">TO DO</text>
  <rect x="80" y="140" width="100" height="70" rx="4" fill="{t['stroke']}"/>
  <rect x="80" y="225" width="100" height="70" rx="4" fill="{t['stroke']}"/>
  <!-- Col 2: IN PROGRESS -->
  <rect x="205" y="90" width="135" height="400" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="272" y="120" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">IN PROGRESS</text>
  <rect x="215" y="140" width="115" height="90" rx="4" fill="{t['accent']}"/>
  <!-- Col 3: DONE -->
  <rect x="355" y="90" width="120" height="400" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="415" y="120" fill="{t['accent_alt']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">DONE</text>
  <rect x="365" y="140" width="100" height="70" rx="4" fill="#00E676" fill-opacity="0.7"/>
  {badge(185, 520, "看板敏捷泳道任务列", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_279(): # 日历布局 (Calendar Monthly Grid)
    t = get_theme("warm-ivory")
    cells = "".join([f'<rect x="{75 + (i%7)*54}" y="{140 + (i//7)*60}" width="50" height="55" rx="4" fill="{t["accent"] if i==17 else t["bg"]}" stroke="{t["guide"]}" stroke-width="1"/>' for i in range(28)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="100" fill="#FFFFFF" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">SEPTEMBER 2026</text>
  <!-- 7x4 Calendar Days Matrix -->
  {cells}
  <circle cx="{75 + (17%7)*54 + 25}" cy="{140 + (17//7)*60 + 28}" r="10" fill="#FFFFFF"/>
  {badge(185, 480, "月历日程网格矩阵", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_280(): # 树形浏览布局 (Tree Directory Hierarchy)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Root folder -->
  <rect x="80" y="100" width="160" height="35" rx="4" fill="{t['accent']}"/>
  <text x="110" y="122" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat">📁 project-root/</text>
  <!-- Tree connector branches -->
  <line x1="110" y1="135" x2="110" y2="420" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="110" y1="180" x2="150" y2="180" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="110" y1="250" x2="150" y2="250" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="110" y1="320" x2="150" y2="320" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Sub-items -->
  <rect x="150" y="165" width="180" height="30" rx="3" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="165" y="185" fill="#FFFFFF" font-size="11" font-family="Montserrat">📁 src/components/</text>
  <rect x="150" y="235" width="200" height="30" rx="3" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="165" y="255" fill="{t['accent']}" font-size="11" font-family="Montserrat">📄 index.tsx (ACTIVE)</text>
  <rect x="150" y="305" width="150" height="30" rx="3" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="165" y="325" fill="#FFFFFF" font-size="11" font-family="Montserrat">📄 styles.css</text>
  {badge(185, 480, "目录树分支层级视图", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_282(): # 地图主导布局 (Map-Centric Interface)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['stroke']}" rx="8"/>
  <!-- Road Network Lines -->
  <path d="M 50 150 Q 200 180 320 120 T 500 200" stroke="{t['accent']}" stroke-width="6" fill="none"/>
  <path d="M 120 60 Q 180 280 180 560" stroke="#FFFFFF" stroke-width="4" fill="none"/>
  <path d="M 380 60 Q 320 300 450 560" stroke="#FFFFFF" stroke-width="4" fill="none"/>
  <!-- GPS Location Pin -->
  <circle cx="275" cy="240" r="18" fill="{t['danger']}"/>
  <circle cx="275" cy="240" r="6" fill="#FFFFFF"/>
  <!-- Floating Search Card -->
  <rect x="80" y="90" width="320" height="50" rx="25" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="110" cy="115" r="10" fill="{t['accent']}"/>
  <text x="135" y="120" fill="#FFFFFF" font-size="12" font-family="Montserrat">Search destination...</text>
  {badge(185, 480, "全屏地图浮动卡片交互", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_283(): # 画布工作区布局 (Canvas Workspace / Miro Figma)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Infinite Canvas Grid Dot background -->
  <g fill="{t['guide']}">
    {''.join([f'<circle cx="{90 + (i%8)*48}" cy="{110 + (i//8)*48}" r="1.5"/>' for i in range(48)])}
  </g>
  <!-- Floating Canvas Node 1 -->
  <rect x="100" y="150" width="130" height="90" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="230" cy="195" r="6" fill="{t['accent']}"/>
  <!-- Connector Spline -->
  <path d="M 230 195 C 290 195 280 320 320 320" fill="none" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- Floating Canvas Node 2 -->
  <rect x="320" y="270" width="140" height="100" rx="6" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <!-- Top Center Toolbar -->
  <rect x="175" y="75" width="200" height="36" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  {badge(185, 480, "无限画布无限平移编排", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_284(): # 表单布局 (Vertical Form Field Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="85" y="110" fill="#FFFFFF" font-size="20" font-weight="900" font-family="Montserrat">ACCOUNT SETUP</text>
  <!-- Field 1 -->
  <text x="85" y="150" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat">EMAIL ADDRESS</text>
  <rect x="85" y="160" width="380" height="44" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- Field 2 -->
  <text x="85" y="235" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat">PASSWORD</text>
  <rect x="85" y="245" width="380" height="44" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Submit Button -->
  <rect x="85" y="330" width="380" height="50" rx="8" fill="{t['accent']}"/>
  <text x="275" y="361" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">CONTINUE →</text>
  {badge(185, 480, "标准垂直表单字段对齐", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_285(): # 分步表单 (Multi-Step Form Wizard)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Stepper Track connecting 3 steps -->
  <line x1="110" y1="120" x2="440" y2="120" stroke="{t['guide']}" stroke-width="3"/>
  <line x1="110" y1="120" x2="275" y2="120" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Step 1 (Completed) -->
  <circle cx="110" cy="120" r="16" fill="#00E676"/><text x="110" y="125" fill="#12141A" font-size="12" font-weight="bold" text-anchor="middle">✓</text>
  <!-- Step 2 (Active) -->
  <circle cx="275" cy="120" r="20" fill="{t['accent']}"/><text x="275" y="126" fill="{t['bg']}" font-size="14" font-weight="900" text-anchor="middle">2</text>
  <!-- Step 3 (Pending) -->
  <circle cx="440" cy="120" r="16" fill="{t['stroke']}"/><text x="440" y="125" fill="#FFFFFF" font-size="12" font-weight="bold" text-anchor="middle">3</text>
  <!-- Active Step Form Container -->
  <rect x="80" y="180" width="390" height="220" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="275" y="225" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">STEP 2: PAYMENT METHOD</text>
  <rect x="110" y="255" width="330" height="40" rx="6" fill="{t['stroke']}"/>
  {badge(185, 480, "分步向导步进条指引", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_286(): # 搜索结果布局 (Search Engine Results Page SERP)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Search Input Bar -->
  <rect x="75" y="90" width="390" height="44" rx="22" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="105" cy="112" r="8" fill="{t['accent']}"/>
  <text x="130" y="117" fill="#FFFFFF" font-size="13" font-family="Montserrat">Swiss design grid system 2026</text>
  <!-- Result 1 -->
  <g transform="translate(75, 160)">
    <text x="0" y="15" fill="{t['text_dim']}" font-size="11" font-family="Montserrat">https://design.org/grid-canon</text>
    <text x="0" y="38" fill="{t['accent']}" font-size="16" font-weight="bold" font-family="Montserrat">The Definitive Guide to Swiss International Grids</text>
    <rect x="0" y="48" width="360" height="8" rx="2" fill="{t['stroke']}"/>
    <rect x="0" y="62" width="310" height="8" rx="2" fill="{t['stroke']}"/>
  </g>
  <!-- Result 2 -->
  <g transform="translate(75, 265)">
    <text x="0" y="15" fill="{t['text_dim']}" font-size="11" font-family="Montserrat">https://specs.layout.io/modern-ui</text>
    <text x="0" y="38" fill="{t['accent_alt']}" font-size="16" font-weight="bold" font-family="Montserrat">350 Layout Compositions Architecture</text>
    <rect x="0" y="48" width="370" height="8" rx="2" fill="{t['stroke']}"/>
  </g>
  {badge(185, 480, "搜索引擎标准结果列表", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_287(): # 设置页面布局 (Settings Dashboard Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Left Category List -->
  <rect x="75" y="90" width="130" height="410" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="85" y="110" width="110" height="35" rx="4" fill="{t['accent']}"/>
  <rect x="85" y="155" width="110" height="35" rx="4" fill="{t['stroke']}" opacity="0.5"/>
  <rect x="85" y="200" width="110" height="35" rx="4" fill="{t['stroke']}" opacity="0.5"/>
  <!-- Right Settings Switches Pane -->
  <rect x="220" y="90" width="255" height="410" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="240" y="130" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat">Notifications</text>
  <!-- Toggle Switch 1 (Active) -->
  <rect x="410" y="115" width="48" height="24" rx="12" fill="#00E676"/>
  <circle cx="446" cy="127" r="9" fill="#FFFFFF"/>
  <!-- Toggle Switch 2 (Inactive) -->
  <text x="240" y="185" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat">Dark Mode</text>
  <rect x="410" y="170" width="48" height="24" rx="12" fill="{t['stroke']}"/>
  <circle cx="422" cy="182" r="9" fill="#FFFFFF"/>
  {badge(185, 520, "偏好设定分类切换列表", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_288(): # 媒体对象布局 (Nicole Sullivan Media Object)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 3 Media Objects: Fixed Avatar Left, Fluid Body Right -->
  <g transform="translate(75, 110)">
    <circle cx="35" cy="35" r="28" fill="{t['accent']}"/>
    <rect x="80" y="10" width="280" height="16" rx="3" fill="#FFFFFF"/>
    <rect x="80" y="35" width="240" height="10" rx="2" fill="{t['text_dim']}"/>
    <rect x="80" y="52" width="200" height="10" rx="2" fill="{t['text_dim']}"/>
  </g>
  <g transform="translate(75, 210)">
    <circle cx="35" cy="35" r="28" fill="{t['accent_alt']}"/>
    <rect x="80" y="10" width="280" height="16" rx="3" fill="#FFFFFF"/>
    <rect x="80" y="35" width="250" height="10" rx="2" fill="{t['text_dim']}"/>
  </g>
  <g transform="translate(75, 310)">
    <circle cx="35" cy="35" r="28" fill="{t['danger']}"/>
    <rect x="80" y="10" width="280" height="16" rx="3" fill="#FFFFFF"/>
    <rect x="80" y="35" width="220" height="10" rx="2" fill="{t['text_dim']}"/>
  </g>
  {badge(185, 480, "媒体对象原子复用原语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_289(): # Hero 主视觉布局 (Hero Banner Layout)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- High Impact Hero Banner -->
  <text x="80" y="150" fill="{t['accent']}" font-size="42" font-weight="900" font-family="Montserrat">TRANSFORM</text>
  <text x="80" y="200" fill="#FFFFFF" font-size="42" font-weight="900" font-family="Montserrat">YOUR VISION</text>
  <text x="80" y="245" fill="{t['text_dim']}" font-size="14" font-family="PingFang SC">端到端工业级设计工程流，一键生成出版标准</text>
  <!-- CTA Buttons -->
  <rect x="80" y="280" width="150" height="44" rx="6" fill="{t['accent']}"/>
  <text x="155" y="307" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">GET STARTED →</text>
  <!-- Floating Device Mockup Right -->
  <rect x="260" y="250" width="210" height="180" rx="10" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="2"/>
  <circle cx="365" cy="340" r="32" fill="{t['accent_alt']}"/>
  {badge(185, 510, "强引力主视觉横幅首屏", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_290(): # 分层导航布局 (Hierarchical Navigation & Breadcrumb)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Breadcrumbs Bar -->
  <rect x="75" y="90" width="390" height="40" rx="4" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="95" y="115" fill="{t['text_dim']}" font-size="11" font-family="Montserrat">Home &gt; Products &gt; Architecture &gt; </text>
  <text x="340" y="115" fill="{t['accent']}" font-size="11" font-weight="bold" font-family="Montserrat">Layout-350</text>
  <!-- Mega-Menu Dropdown Panel below -->
  <rect x="75" y="145" width="390" height="280" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <g fill="{t['stroke']}">
    <rect x="95" y="175" width="100" height="180" rx="4"/>
    <rect x="210" y="175" width="100" height="180" rx="4"/>
    <rect x="325" y="175" width="120" height="180" rx="4" fill="{t['accent']}" fill-opacity="0.2"/>
  </g>
  {badge(185, 480, "面包屑与多级联动导航", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])


def gen_291(): # 大体流动模式 (Mostly Fluid Pattern)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Columns expanding fluidly until screen margin -->
  <rect x="75" y="100" width="185" height="180" rx="6" fill="{t['accent']}"/>
  <rect x="280" y="100" width="185" height="180" rx="6" fill="{t['accent_alt']}"/>
  <rect x="75" y="300" width="390" height="120" rx="6" fill="{t['stroke']}"/>
  <text x="275" y="365" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">FLUID GRID ON DESKTOP → COLLAPSE ON MOBILE</text>
  {badge(185, 480, "大致流动响应重排模式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_292(): # 列下落模式 (Column Drop Pattern)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 2 Columns in row 1 -->
  <rect x="75" y="100" width="185" height="160" rx="6" fill="{t['accent']}"/>
  <rect x="280" y="100" width="185" height="160" rx="6" fill="{t['accent_alt']}"/>
  <!-- Dropped 3rd Column below -->
  <line x1="372" y1="265" x2="275" y2="295" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <rect x="75" y="285" width="390" height="130" rx="6" fill="{t['danger']}"/>
  <text x="275" y="355" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">COLUMN DROPPED BELOW</text>
  {badge(185, 480, "多栏逐级下落堆叠模式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_293(): # 布局切换模式 (Layout Shifter Pattern)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Complex repositioning of elements across zones -->
  <rect x="75" y="100" width="100" height="320" rx="6" fill="{t['stroke']}"/>
  <rect x="190" y="100" width="275" height="150" rx="6" fill="{t['accent']}"/>
  <rect x="190" y="270" width="130" height="150" rx="6" fill="{t['accent_alt']}"/>
  <rect x="335" y="270" width="130" height="150" rx="6" fill="{t['danger']}"/>
  <text x="275" y="460" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">ELEMENTS SHIFT INTO NEW ZONES</text>
  {badge(185, 520, "深层结构位移重构模式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_294(): # 微调模式 (Tiny Tweaks Pattern)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Fluid font-size scaling clamp() -->
  <text x="275" y="200" fill="{t['accent']}" font-size="42" font-weight="900" font-family="Montserrat" text-anchor="middle">clamp(1rem, 5vw, 3rem)</text>
  <line x1="75" y1="250" x2="475" y2="250" stroke="{t['guide']}" stroke-width="2"/>
  <text x="275" y="320" fill="#FFFFFF" font-size="16" font-weight="bold" font-family="PingFang SC" text-anchor="middle">微调字号、间距与圆角参数</text>
  <text x="275" y="355" fill="{t['text_dim']}" font-size="13" font-family="Montserrat" text-anchor="middle">Subtle typography & margin scaling</text>
  {badge(185, 480, "流体参数无级微调模式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_295(): # 画布外模式 (Off-Canvas Pattern)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Main screen pushed right -->
  <rect x="180" y="80" width="320" height="420" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="2"/>
  <!-- Off-canvas panel appearing on left -->
  <rect x="50" y="80" width="130" height="420" rx="6" fill="{t['accent']}"/>
  <text x="115" y="290" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">OFF-CANVAS</text>
  {badge(185, 520, "画外移入视口展开模式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_296(): # 堆叠重排 (Stack Reflow)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="90" y="110" width="370" height="65" rx="6" fill="{t['accent']}"/>
  <rect x="90" y="190" width="370" height="65" rx="6" fill="{t['accent_alt']}"/>
  <rect x="90" y="270" width="370" height="65" rx="6" fill="{t['stroke']}"/>
  <rect x="90" y="350" width="370" height="65" rx="6" fill="{t['danger']}"/>
  {badge(185, 480, "水平元素垂直全宽堆叠", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_297(): # 顺序重排 (Order Reflow)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="90" y="110" width="370" height="60" rx="6" fill="{t['accent']}"/>
  <text x="275" y="146" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">ITEM B (order: -1 on mobile)</text>
  <rect x="90" y="190" width="370" height="60" rx="6" fill="{t['stroke']}"/>
  <text x="275" y="226" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">ITEM A (order: 0)</text>
  <rect x="90" y="270" width="370" height="60" rx="6" fill="{t['stroke']}"/>
  <text x="275" y="306" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">ITEM C (order: 1)</text>
  {badge(185, 480, "CSS order 属性视觉倒序", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_298(): # 折叠双窗格 (Fold Dual-Pane)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Tablet dual-pane folding into single mobile view -->
  <rect x="75" y="100" width="180" height="320" rx="6" fill="{t['accent']}"/>
  <rect x="285" y="100" width="180" height="320" rx="6" fill="{t['accent_alt']}"/>
  <!-- Fold line -->
  <line x1="270" y1="80" x2="270" y2="440" stroke="{t['danger']}" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="270" y="465" fill="{t['danger']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">FOLD SEAM</text>
  {badge(185, 520, "双屏折叠单屏自适应切换", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_299(): # 自适应网格重排 (Adaptive Grid Reflow)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <g fill="{t['stroke']}">
    <rect x="75" y="110" width="175" height="140" rx="6" fill="{t['accent']}"/>
    <rect x="280" y="110" width="175" height="140" rx="6" fill="{t['accent_alt']}"/>
    <rect x="75" y="270" width="175" height="140" rx="6" fill="{t['accent_alt']}"/>
    <rect x="280" y="270" width="175" height="140" rx="6" fill="{t['danger']}"/>
  </g>
  {badge(185, 480, "网格卡片自动流转自适应", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_300(): # 组件级响应布局 (Component-Level Responsive)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Micro Component redesigning itself in sidebar vs main -->
  <rect x="70" y="110" width="390" height="130" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="140" cy="175" r="35" fill="{t['accent']}"/>
  <rect x="200" y="150" width="230" height="18" rx="3" fill="#FFFFFF"/>
  <rect x="200" y="180" width="180" height="12" rx="2" fill="{t['text_dim']}"/>
  <rect x="145" y="270" width="240" height="170" rx="8" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="2"/>
  <circle cx="265" cy="325" r="26" fill="{t['accent_alt']}"/>
  <rect x="175" y="370" width="180" height="14" rx="3" fill="#FFFFFF"/>
  {badge(185, 500, "组件级自适应容器响应终极态", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

CAT05_SVGS = {
    "222": gen_222, "223": gen_223, "225": gen_225, "227": gen_227, "228": gen_228, "229": gen_229, "231": gen_231, "232": gen_232, "233": gen_233, "234": gen_234, "235": gen_235, "236": gen_236, "237": gen_237, "238": gen_238, "239": gen_239, "240": gen_240, "241": gen_241, "242": gen_242, "244": gen_244, "245": gen_245, "246": gen_246, "247": gen_247, "248": gen_248, "249": gen_249, "250": gen_250, "251": gen_251, "252": gen_252, "253": gen_253, "254": gen_254, "256": gen_256, "257": gen_257, "258": gen_258, "259": gen_259, "260": gen_260, "261": gen_261, "262": gen_262, "263": gen_263, "264": gen_264, "265": gen_265, "266": gen_266, "267": gen_267, "268": gen_268, "269": gen_269, "270": gen_270, "271": gen_271, "274": gen_274, "276": gen_276, "277": gen_277, "278": gen_278, "279": gen_279, "280": gen_280, "282": gen_282, "283": gen_283, "284": gen_284, "285": gen_285, "286": gen_286, "287": gen_287, "288": gen_288, "289": gen_289, "290": gen_290, "291": gen_291, "292": gen_292, "293": gen_293, "294": gen_294, "295": gen_295, "296": gen_296, "297": gen_297, "298": gen_298, "299": gen_299, "300": gen_300,
    "224": gen_224, "230": gen_230, "243": gen_243, "255": gen_255, "273": gen_273,
    "275": gen_275, "281": gen_281
}


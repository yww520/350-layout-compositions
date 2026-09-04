"""
SVG generators for Category 07: 演示文稿与信息设计 (335-350).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_335(): # 极简巨字封面 (Title Slide Minimal Giant Typo)
    t = get_theme("forest-green")
    inner = f"""
  <!-- 16:9 Presentation Frame -->
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Category Meta -->
  <text x="70" y="140" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="Montserrat" letter-spacing="4">KEYNOTE · 2026</text>
  <!-- Colossal Headline -->
  <text x="70" y="240" fill="#FFFFFF" font-size="58" font-weight="900" font-family="Helvetica, Arial, sans-serif">BEYOND</text>
  <text x="70" y="310" fill="{t['accent']}" font-size="58" font-weight="900" font-family="Helvetica, Arial, sans-serif">LIMITS.</text>
  <!-- Subtitle Paragraph -->
  <text x="70" y="370" fill="{t['text_dim']}" font-size="16" font-family="PingFang SC">重塑下一代人机协作工作流系统架构</text>
  <!-- Author / Presenter Stamp -->
  <line x1="70" y1="430" x2="480" y2="430" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="90" cy="465" r="16" fill="{t['accent']}"/>
  <text x="120" y="470" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat">DR. ALEX CHEN · PRINCIPAL RESEARCHER</text>
  {badge(185, 510, "极简巨字第一视线压强", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_338(): # 三支柱架构页 (3-Pillar Architecture Slide)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="100" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">THREE CORE PILLARS</text>
  <!-- Pillar 1 -->
  <rect x="60" y="130" width="120" height="340" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <circle cx="120" cy="180" r="24" fill="{t['accent']}"/>
  <text x="120" y="186" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">01</text>
  <text x="120" y="240" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">SPEED</text>
  <line x1="80" y1="270" x2="160" y2="270" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="120" y="310" fill="{t['text_dim']}" font-size="11" font-family="PingFang SC" text-anchor="middle">毫秒级响应</text>

  <!-- Pillar 2 (HERO HIGHLIGHT) -->
  <rect x="200" y="110" width="150" height="380" rx="10" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
  <circle cx="275" cy="170" r="28" fill="#FFFFFF"/>
  <text x="275" y="177" fill="{t['bg']}" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">02</text>
  <text x="275" y="240" fill="{t['bg']}" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">SECURITY</text>
  <line x1="230" y1="270" x2="320" y2="270" stroke="{t['bg']}" stroke-width="2"/>
  <text x="275" y="310" fill="{t['bg']}" font-size="13" font-weight="bold" font-family="PingFang SC" text-anchor="middle">零信任安全闭环</text>

  <!-- Pillar 3 -->
  <rect x="370" y="130" width="120" height="340" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <circle cx="430" cy="180" r="24" fill="{t['accent']}"/>
  <text x="430" y="186" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">03</text>
  <text x="430" y="240" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">SCALE</text>
  <line x1="390" y1="270" x2="470" y2="270" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="430" y="310" fill="{t['text_dim']}" font-size="11" font-family="PingFang SC" text-anchor="middle">弹性分布式</text>
  {badge(185, 520, "三支柱并列架构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_344(): # 时间轴里程碑 (Timeline Horizon Linear Milestones)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Central Horizontal Timeline Vector (y=310) -->
  <line x1="70" y1="310" x2="470" y2="310" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <!-- 4 Milestone Nodes -->
  <!-- Milestone 1 (Top Branch) -->
  <line x1="110" y1="310" x2="110" y2="200" stroke="{t['accent_alt']}" stroke-width="2"/>
  <circle cx="110" cy="310" r="14" fill="{t['accent_alt']}"/>
  <circle cx="110" cy="310" r="4" fill="#FFFFFF"/>
  <rect x="60" y="140" width="100" height="50" rx="6" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="1.2"/>
  <text x="110" y="165" fill="{t['accent_alt']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">Q1 · ALPHA</text>

  <!-- Milestone 2 (Bottom Branch) -->
  <line x1="220" y1="310" x2="220" y2="420" stroke="{t['accent_alt']}" stroke-width="2"/>
  <circle cx="220" cy="310" r="14" fill="{t['accent_alt']}"/>
  <circle cx="220" cy="310" r="4" fill="#FFFFFF"/>
  <rect x="170" y="430" width="100" height="50" rx="6" fill="{t['bg']}" stroke="{t['accent_alt']}" stroke-width="1.2"/>
  <text x="220" y="455" fill="{t['accent_alt']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">Q2 · BETA</text>

  <!-- Milestone 3 (Top Branch HERO) -->
  <line x1="330" y1="310" x2="330" y2="180" stroke="{t['accent']}" stroke-width="3"/>
  <circle cx="330" cy="310" r="20" fill="{t['accent']}"/>
  <circle cx="330" cy="310" r="6" fill="#FFFFFF"/>
  <rect x="270" y="110" width="120" height="60" rx="8" fill="{t['accent']}"/>
  <text x="330" y="145" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">Q3 · LAUNCH</text>

  <!-- Milestone 4 (Bottom Branch) -->
  <line x1="440" y1="310" x2="440" y2="420" stroke="{t['stroke']}" stroke-width="2"/>
  <circle cx="440" cy="310" r="14" fill="{t['stroke']}"/>
  <rect x="390" y="430" width="100" height="50" rx="6" fill="{t['bg']}" stroke="{t['stroke']}" stroke-width="1.2"/>
  <text x="440" y="455" fill="{t['text_dim']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">Q4 · SCALE</text>
  {badge(185, 520, "时间轴里程碑演进", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_345(): # 2x2战略矩阵页 (2x2 Strategy Matrix Quadrant)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="50" width="470" height="520" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Coordinate Axes (x=275, y=310) -->
  <line x1="70" y1="310" x2="480" y2="310" stroke="{t['accent']}" stroke-width="2.5"/>
  <polygon points="485,310 470,302 470,318" fill="{t['accent']}"/>
  <line x1="275" y1="540" x2="275" y2="80" stroke="{t['accent']}" stroke-width="2.5"/>
  <polygon points="275,75 267,90 283,90" fill="{t['accent']}"/>
  <!-- Axis Labels -->
  <text x="480" y="340" fill="{t['accent']}" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="end">FEASIBILITY →</text>
  <text x="275" y="65" fill="{t['accent']}" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">IMPACT ↑</text>
  <!-- Q1 (Top-Right): QUICK WINS (HERO) -->
  <rect x="295" y="95" width="190" height="200" rx="8" fill="{t['accent']}" fill-opacity="0.2" stroke="{t['accent']}" stroke-width="2"/>
  <text x="390" y="140" fill="{t['accent']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">QUICK WINS</text>
  <circle cx="350" cy="180" r="16" fill="{t['accent']}"/>
  <circle cx="430" cy="220" r="22" fill="{t['accent']}"/>
  <circle cx="390" cy="250" r="14" fill="{t['accent']}"/>

  <!-- Q2 (Top-Left): STRATEGIC BETS -->
  <rect x="65" y="95" width="190" height="200" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="160" y="140" fill="{t['text_dim']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">BIG BETS</text>
  <circle cx="160" cy="200" r="18" fill="{t['stroke']}"/>

  <!-- Q3 (Bottom-Left): LOW PRIORITY -->
  <rect x="65" y="325" width="190" height="190" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="160" y="365" fill="{t['text_dim']}" font-size="11" font-family="Montserrat" text-anchor="middle">ELIMINATE</text>

  <!-- Q4 (Bottom-Right): FILL-INS -->
  <rect x="295" y="325" width="190" height="190" rx="8" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="390" y="365" fill="{t['text_dim']}" font-size="11" font-family="Montserrat" text-anchor="middle">FILL-INS</text>
  {badge(185, 520, "2x2 战略优先级象限", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_347(): # 文氏图集合交集 (Venn Diagram Intersecting Sets)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 3 Translucent Intersecting Circles -->
  <!-- Circle A (Top) -->
  <circle cx="275" cy="220" r="120" fill="{t['accent']}" fill-opacity="0.35" stroke="{t['accent']}" stroke-width="2.5"/>
  <text x="275" y="150" fill="{t['accent']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">DESIRABLE</text>

  <!-- Circle B (Bottom Left) -->
  <circle cx="205" cy="330" r="120" fill="{t['accent_alt']}" fill-opacity="0.35" stroke="{t['accent_alt']}" stroke-width="2.5"/>
  <text x="140" y="400" fill="{t['accent_alt']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">FEASIBLE</text>

  <!-- Circle C (Bottom Right) -->
  <circle cx="345" cy="330" r="120" fill="{t['danger']}" fill-opacity="0.35" stroke="{t['danger']}" stroke-width="2.5"/>
  <text x="410" y="400" fill="{t['danger']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">VIABLE</text>

  <!-- Central Triple Intersection Nexus (SWEET SPOT) -->
  <circle cx="275" cy="295" r="26" fill="#FFFFFF"/>
  <circle cx="275" cy="295" r="8" fill="{t['bg']}"/>
  <text x="275" y="260" fill="#FFFFFF" font-size="11" font-weight="900" font-family="Montserrat" text-anchor="middle">SWEET SPOT</text>
  {badge(185, 520, "三维文氏交集甜点", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat07
CAT07_SVGS = {
    "335": gen_335, "338": gen_338, "344": gen_344, "345": gen_345, "347": gen_347
}


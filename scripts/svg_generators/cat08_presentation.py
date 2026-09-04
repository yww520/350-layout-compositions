"""
SVG generators for Category 08: 演示文稿与信息设计 (335-350).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_335(): # 极简巨字封面 (Title Slide Minimal Giant Typo)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="70" y="140" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="Montserrat" letter-spacing="4">KEYNOTE · 2026</text>
  <text x="70" y="240" fill="#FFFFFF" font-size="58" font-weight="900" font-family="Helvetica, Arial, sans-serif">BEYOND</text>
  <text x="70" y="310" fill="{t['accent']}" font-size="58" font-weight="900" font-family="Helvetica, Arial, sans-serif">LIMITS.</text>
  <text x="70" y="370" fill="{t['text_dim']}" font-size="16" font-family="PingFang SC">重塑下一代人机协作工作流系统架构</text>
  <line x1="70" y1="430" x2="480" y2="430" stroke="{t['guide']}" stroke-width="1.5"/>
  <circle cx="90" cy="465" r="16" fill="{t['accent']}"/>
  <text x="120" y="470" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat">DR. ALEX CHEN · PRINCIPAL RESEARCHER</text>
  {badge(185, 510, "极简巨字第一视线压强", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_336(): # 标题和内容幻灯片 (Title and Content Slide)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="70" y="130" fill="#FFFFFF" font-size="26" font-weight="900" font-family="Montserrat">EXECUTIVE SUMMARY</text>
  <line x1="70" y1="150" x2="480" y2="150" stroke="{t['accent']}" stroke-width="2"/>
  <!-- 3 Bullet points with accent chips -->
  <g transform="translate(70, 190)">
    <circle cx="10" cy="15" r="6" fill="{t['danger']}"/>
    <text x="30" y="20" fill="#FFFFFF" font-size="16" font-weight="bold" font-family="PingFang SC">战略协同：实现跨业务单元数据打通与无缝流转</text>
    <rect x="30" y="35" width="350" height="8" rx="2" fill="{t['text_dim']}"/>
  </g>
  <g transform="translate(70, 270)">
    <circle cx="10" cy="15" r="6" fill="{t['danger']}"/>
    <text x="30" y="20" fill="#FFFFFF" font-size="16" font-weight="bold" font-family="PingFang SC">成本控制：自动化流水线降低单次交付边际开销</text>
    <rect x="30" y="35" width="320" height="8" rx="2" fill="{t['text_dim']}"/>
  </g>
  <g transform="translate(70, 350)">
    <circle cx="10" cy="15" r="6" fill="{t['danger']}"/>
    <text x="30" y="20" fill="#FFFFFF" font-size="16" font-weight="bold" font-family="PingFang SC">价值升维：由流程跟随向技术主导决策全面转变</text>
    <rect x="30" y="35" width="370" height="8" rx="2" fill="{t['text_dim']}"/>
  </g>
  {badge(185, 480, "标准标题内容条列页", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_337(): # 节标题幻灯片 (Section Header Slide)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Giant Chapter Number -->
  <text x="70" y="220" fill="{t['accent']}" font-size="110" font-weight="900" font-family="Montserrat">02</text>
  <line x1="70" y1="260" x2="320" y2="260" stroke="{t['accent_alt']}" stroke-width="4"/>
  <text x="70" y="320" fill="#FFFFFF" font-size="32" font-weight="900" font-family="PingFang SC">核心技术实现路径</text>
  <text x="70" y="360" fill="{t['text_dim']}" font-size="16" font-family="Montserrat">Architecture & Implementation Plan</text>
  {badge(185, 480, "章节过渡转折指引", t['accent'], t['bg'], 180, 28)}
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
  <!-- Pillar 2 (HERO HIGHLIGHT) -->
  <rect x="200" y="110" width="150" height="380" rx="10" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
  <circle cx="275" cy="170" r="28" fill="#FFFFFF"/>
  <text x="275" y="177" fill="{t['bg']}" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">02</text>
  <text x="275" y="240" fill="{t['bg']}" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">SECURITY</text>
  <!-- Pillar 3 -->
  <rect x="370" y="130" width="120" height="340" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <circle cx="430" cy="180" r="24" fill="{t['accent']}"/>
  <text x="430" y="186" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">03</text>
  <text x="430" y="240" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">SCALE</text>
  {badge(185, 520, "三支柱并列架构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_339(): # 比较幻灯片 (Comparison Slide)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="110" fill="#FFFFFF" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">PROS VS CONS COMPARISON</text>
  <!-- Left Side: Option A (Green/Positive) -->
  <rect x="65" y="140" width="195" height="320" rx="8" fill="{t['bg']}" stroke="#00E676" stroke-width="2"/>
  <rect x="65" y="140" width="195" height="40" rx="8" fill="#00E676" fill-opacity="0.2"/>
  <text x="162" y="166" fill="#00E676" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">SOLUTION A (AI)</text>
  <text x="85" y="220" fill="#00E676" font-weight="bold">✓ 10x Throughput</text>
  <text x="85" y="260" fill="#00E676" font-weight="bold">✓ Zero Human Latency</text>
  <text x="85" y="300" fill="#00E676" font-weight="bold">✓ 24/7 Availability</text>
  <!-- Right Side: Option B (Red/Legacy) -->
  <rect x="290" y="140" width="195" height="320" rx="8" fill="{t['bg']}" stroke="#FF3D00" stroke-width="2"/>
  <rect x="290" y="140" width="195" height="40" rx="8" fill="#FF3D00" fill-opacity="0.2"/>
  <text x="387" y="166" fill="#FF3D00" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">SOLUTION B (LEGACY)</text>
  <text x="310" y="220" fill="#FF3D00" font-weight="bold">✕ Manual Bottlenecks</text>
  <text x="310" y="260" fill="#FF3D00" font-weight="bold">✕ Linear Cost Scaling</text>
  <text x="310" y="300" fill="#FF3D00" font-weight="bold">✕ Error-Prone Delivery</text>
  {badge(185, 490, "双方案优劣并置裁决", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_340(): # 仅标题幻灯片 (Title-Only Big Statement Slide)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Centered Massive Statement -->
  <text x="80" y="240" fill="{t['accent']}" font-size="64" font-family="Georgia, serif">“</text>
  <text x="275" y="290" fill="#FFFFFF" font-size="28" font-weight="900" font-family="PingFang SC" text-anchor="middle">简单即是终极的复杂。</text>
  <text x="275" y="335" fill="{t['text_dim']}" font-size="16" font-family="Montserrat" text-anchor="middle">Simplicity is the ultimate sophistication.</text>
  <text x="440" y="370" fill="{t['accent']}" font-size="64" font-family="Georgia, serif">”</text>
  {badge(185, 480, "金句宣言极大视听留白", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_341(): # 空白幻灯片 (Blank Whiteboard Slide)
    t = get_theme("warm-ivory")
    # Minimal subtle dot grid matrix
    dots = "".join([f'<circle cx="{90 + (i%8)*52}" cy="{130 + (i//8)*52}" r="2" fill="{t["accent"]}" opacity="0.4"/>' for i in range(48)])
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  {dots}
  <!-- Footer meta -->
  <line x1="70" y1="480" x2="480" y2="480" stroke="{t['guide']}" stroke-width="1"/>
  <text x="70" y="505" fill="{t['text_dim']}" font-size="10" font-family="Montserrat">PROJECT CODEX · CONFIDENTIAL</text>
  <text x="480" y="505" fill="{t['text_dim']}" font-size="10" font-family="Montserrat" text-anchor="end">SLIDE 42</text>
  {badge(185, 290, "点阵空白自由画布", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_342(): # 内容与标题说明 (Content with Caption Sidebar)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Main Content Showcase on Left (60%) -->
  <rect x="65" y="110" width="250" height="380" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="190" cy="280" r="55" fill="{t['accent']}"/>
  <circle cx="190" cy="280" r="16" fill="#FFFFFF"/>
  <text x="190" y="370" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">VISUAL ARTIFACT</text>
  <!-- Caption Explanation Sidebar on Right (40%) -->
  <rect x="330" y="110" width="155" height="380" rx="6" fill="{t['stroke']}" opacity="0.5"/>
  <text x="345" y="150" fill="{t['accent_alt']}" font-size="14" font-weight="900" font-family="Montserrat">METRICS</text>
  <rect x="345" y="170" width="125" height="8" rx="2" fill="#FFFFFF"/>
  <rect x="345" y="190" width="105" height="8" rx="2" fill="{t['text_dim']}"/>
  <rect x="345" y="210" width="115" height="8" rx="2" fill="{t['text_dim']}"/>
  {badge(185, 520, "图元主体与边栏释义", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_343(): # 图片与标题说明 (Image Card with Title Overlay)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Hero photo card -->
  <rect x="65" y="100" width="420" height="340" rx="8" fill="{t['stroke']}"/>
  <circle cx="275" cy="240" r="70" fill="{t['accent']}"/>
  <!-- Title card overlay floating on bottom of image -->
  <rect x="90" y="320" width="370" height="100" rx="6" fill="{t['bg']}" fill-opacity="0.95" stroke="{t['accent_alt']}" stroke-width="1.5"/>
  <text x="115" y="355" fill="#FFFFFF" font-size="18" font-weight="900" font-family="PingFang SC">新一代分布式视觉管线</text>
  <text x="115" y="385" fill="{t['text_dim']}" font-size="12" font-family="Montserrat">High-throughput deterministic rendering architecture</text>
  {badge(185, 480, "图面浮层信息卡片", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_344(): # 时间轴里程碑 (Timeline Horizon Linear Milestones)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="110" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">PROJECT MILESTONES 2026</text>
  <line x1="70" y1="300" x2="480" y2="300" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <!-- Q1 -->
  <circle cx="110" cy="300" r="16" fill="{t['stroke']}"/>
  <text x="110" y="340" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">Q1</text>
  <!-- Q2 -->
  <circle cx="215" cy="300" r="16" fill="{t['stroke']}"/>
  <text x="215" y="340" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">Q2</text>
  <!-- Q3 HERO -->
  <circle cx="330" cy="300" r="24" fill="{t['danger']}"/>
  <circle cx="330" cy="300" r="8" fill="#FFFFFF"/>
  <text x="330" y="350" fill="{t['danger']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">Q3 LAUNCH</text>
  <!-- Q4 -->
  <circle cx="440" cy="300" r="16" fill="{t['stroke']}"/>
  <text x="440" y="340" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">Q4</text>
  {badge(185, 480, "季度时间轴路标跃迁", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_345(): # 大数字冲击页 (Big Number KPI Metric Slide)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="70" y="130" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="Montserrat" letter-spacing="3">PERFORMANCE BREAKTHROUGH</text>
  <!-- Huge 100pt Number -->
  <text x="70" y="260" fill="#FFFFFF" font-size="110" font-weight="900" font-family="Montserrat">10x</text>
  <text x="70" y="320" fill="{t['accent']}" font-size="24" font-weight="900" font-family="PingFang SC">交付效率全面跃迁</text>
  <line x1="70" y1="360" x2="480" y2="360" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="70" y="400" fill="{t['text_dim']}" font-size="14" font-family="Montserrat">+94.8% Pipeline throughput reduction</text>
  {badge(185, 480, "关键指标巨数冲击", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_346(): # 时间线页幻灯片 (Timeline Slide)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="70" y="120" fill="#FFFFFF" font-size="20" font-weight="900" font-family="Montserrat">DEVELOPMENT ROADMAP</text>
  <!-- Vertical Track -->
  <line x1="110" y1="160" x2="110" y2="460" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Node 1 -->
  <circle cx="110" cy="180" r="10" fill="{t['stroke']}"/>
  <rect x="140" y="165" width="320" height="40" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="160" y="190" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat">PHASE 1 · CORE FOUNDATIONS</text>
  <!-- Node 2 (Active) -->
  <circle cx="110" cy="270" r="14" fill="{t['danger']}"/>
  <rect x="140" y="250" width="320" height="50" rx="6" fill="{t['accent']}"/>
  <text x="160" y="280" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat">PHASE 2 · ACCELERATION</text>
  <!-- Node 3 -->
  <circle cx="110" cy="370" r="10" fill="{t['stroke']}"/>
  <rect x="140" y="355" width="320" height="40" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1"/>
  <text x="160" y="380" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="Montserrat">PHASE 3 · GLOBAL SCALE</text>
  {badge(185, 490, "立式时间线进展里程碑", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_347(): # 4步流程步进页 (Process Stepper Slide)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="110" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">4-STAGE WORKFLOW ENGINE</text>
  <!-- Step 1 -->
  <rect x="70" y="140" width="370" height="60" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="110" y="176" fill="{t['accent']}" font-size="16" font-weight="900" font-family="Montserrat">01. INGESTION</text>
  <line x1="255" y1="200" x2="255" y2="220" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Step 2 -->
  <rect x="70" y="220" width="370" height="60" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="110" y="256" fill="{t['accent']}" font-size="16" font-weight="900" font-family="Montserrat">02. CURATION</text>
  <line x1="255" y1="280" x2="255" y2="300" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Step 3 HERO -->
  <rect x="70" y="300" width="370" height="65" rx="8" fill="{t['accent']}"/>
  <text x="110" y="340" fill="{t['bg']}" font-size="18" font-weight="900" font-family="Montserrat">03. SYNTHESIS</text>
  <line x1="255" y1="365" x2="255" y2="385" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Step 4 -->
  <rect x="70" y="385" width="370" height="60" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="110" y="421" fill="{t['accent']}" font-size="16" font-weight="900" font-family="Montserrat">04. DELIVERY</text>
  {badge(185, 490, "四阶段工序流程序列", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_348(): # 矩阵页幻灯片 (2x2 Strategy Matrix Slide)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="110" fill="#FFFFFF" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">BCG STRATEGY MATRIX</text>
  <!-- 2x2 Matrix Grid Lines -->
  <line x1="275" y1="140" x2="275" y2="460" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="80" y1="300" x2="470" y2="300" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Q1 (Top Right Star) -->
  <rect x="285" y="150" width="175" height="140" rx="6" fill="{t['danger']}" opacity="0.2"/>
  <text x="372" y="200" fill="{t['danger']}" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">★ STARS</text>
  <!-- Q2 (Top Left Question) -->
  <rect x="90" y="150" width="175" height="140" rx="6" fill="{t['accent']}" opacity="0.1"/>
  <text x="177" y="200" fill="{t['accent']}" font-size="16" font-weight="bold" font-family="Montserrat" text-anchor="middle">? QUESTION</text>
  <!-- Q3 (Bottom Right Cash Cow) -->
  <rect x="285" y="310" width="175" height="140" rx="6" fill="{t['accent_alt']}" opacity="0.1"/>
  <text x="372" y="360" fill="{t['accent_alt']}" font-size="16" font-weight="bold" font-family="Montserrat" text-anchor="middle">$ CASH COW</text>
  <!-- Q4 (Bottom Left Dogs) -->
  <rect x="90" y="310" width="175" height="140" rx="6" fill="{t['stroke']}" opacity="0.2"/>
  <text x="177" y="360" fill="{t['text_dim']}" font-size="16" font-family="Montserrat" text-anchor="middle">✕ DOGS</text>
  {badge(185, 490, "波士顿2x2决策象限", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_349(): # 数据图表页幻灯片 (Data Chart Dashboard Slide)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="70" width="470" height="480" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="70" y="120" fill="#FFFFFF" font-size="20" font-weight="900" font-family="Montserrat">QUARTERLY REVENUE GROWTH</text>
  <!-- Bar chart columns -->
  <rect x="80" y="360" width="45" height="100" rx="4" fill="{t['stroke']}"/>
  <rect x="150" y="300" width="45" height="160" rx="4" fill="{t['accent_alt']}"/>
  <rect x="220" y="240" width="45" height="220" rx="4" fill="{t['accent_alt']}"/>
  <rect x="290" y="180" width="45" height="280" rx="4" fill="{t['accent']}"/>
  <rect x="360" y="130" width="45" height="330" rx="4" fill="{t['danger']}"/>
  <!-- Trend line -->
  <path d="M 102 350 L 172 290 L 242 230 L 312 170 L 382 120" fill="none" stroke="#FFFFFF" stroke-width="3"/>
  <circle cx="382" cy="120" r="8" fill="#FFFFFF"/>
  <text x="382" y="100" fill="{t['danger']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">+142%</text>
  {badge(185, 490, "多维数据图表仪表盘", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_350(): # 全图页幻灯片 (Full Bleed Slide)
    t = get_theme("forest-green")
    inner = f"""
  <!-- 100% full frame immersion -->
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['stroke']}"/>
  <circle cx="275" cy="270" r="95" fill="{t['accent']}" opacity="0.85"/>
  <circle cx="275" cy="270" r="32" fill="#FFFFFF"/>
  <rect x="40" y="420" width="470" height="140" rx="8" fill="{t['bg']}" fill-opacity="0.9"/>
  <text x="70" y="470" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Montserrat">FULL-BLEED CINEMATIC IMMERSION</text>
  <text x="70" y="500" fill="{t['text_dim']}" font-size="14" font-family="PingFang SC">满幅沉浸 · 视听冲击力最大化收尾</text>
  {badge(185, 530, "满幅沉浸式高潮收尾", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat08 Presentation
CAT08_PRESENTATION_SVGS = {
    "335": gen_335, "336": gen_336, "337": gen_337, "338": gen_338, "339": gen_339,
    "340": gen_340, "341": gen_341, "342": gen_342, "343": gen_343, "344": gen_344,
    "345": gen_345, "346": gen_346, "347": gen_347, "348": gen_348, "349": gen_349,
    "350": gen_350
}

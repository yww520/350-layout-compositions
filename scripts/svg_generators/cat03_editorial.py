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

def gen_135(): # 对称跨页 (Symmetrical Spread)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Two facing pages with center spine -->
  <rect x="50" y="80" width="215" height="440" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <rect x="285" y="80" width="215" height="440" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <!-- Book Spine Gutter -->
  <line x1="275" y1="60" x2="275" y2="540" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Symmetrical Content Left -->
  <rect x="80" y="120" width="155" height="120" fill="{t['accent']}" opacity="0.85" rx="4"/>
  <rect x="80" y="260" width="155" height="18" rx="3" fill="{t['stroke']}"/>
  <rect x="80" y="290" width="135" height="10" rx="2" fill="{t['text_dim']}"/>
  <rect x="80" y="310" width="145" height="10" rx="2" fill="{t['text_dim']}"/>
  <!-- Symmetrical Content Right (Mirror) -->
  <rect x="315" y="120" width="155" height="120" fill="{t['accent']}" opacity="0.85" rx="4"/>
  <rect x="315" y="260" width="155" height="18" rx="3" fill="{t['stroke']}"/>
  <rect x="335" y="290" width="135" height="10" rx="2" fill="{t['text_dim']}"/>
  <rect x="325" y="310" width="145" height="10" rx="2" fill="{t['text_dim']}"/>
  {badge(185, 520, "中缝镜像对称跨页", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_136(): # 非对称跨页 (Asymmetrical Spread)
    t = get_theme("forest-green")
    inner = f"""
  <!-- Left Page: Full Photo Dominance -->
  <rect x="50" y="80" width="215" height="440" fill="{t['accent']}" fill-opacity="0.9" rx="4"/>
  <circle cx="157" cy="300" r="48" fill="#FFFFFF"/>
  <text x="157" y="420" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">HERO VISUAL</text>
  <!-- Center Spine -->
  <line x1="275" y1="60" x2="275" y2="540" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Right Page: 2-Column Typographic Layout -->
  <rect x="285" y="80" width="215" height="440" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <rect x="305" y="110" width="175" height="24" rx="4" fill="{t['accent_alt']}"/>
  <g fill="{t['stroke']}">
    <rect x="305" y="150" width="80" height="180" rx="3"/>
    <rect x="400" y="150" width="80" height="180" rx="3"/>
  </g>
  <rect x="305" y="350" width="175" height="70" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  {badge(185, 520, "图文非对称对偶平衡", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_137(): # 通版跨页 (Panoramic Spread)
    t = get_theme("cobalt-blue")
    inner = f"""
  <!-- Panoramic continuous hero image crossing gutter -->
  <rect x="50" y="120" width="450" height="320" rx="8" fill="{t['accent']}" fill-opacity="0.85"/>
  <circle cx="275" cy="280" r="80" fill="{t['bg']}"/>
  <circle cx="275" cy="280" r="26" fill="#FFFFFF"/>
  <!-- Spine crease indicator passing through image center -->
  <line x1="275" y1="80" x2="275" y2="480" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="8,6" opacity="0.75"/>
  <text x="275" y="95" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">GUTTER SPINE CROSSING</text>
  <!-- Caption bar spanning both pages -->
  <rect x="90" y="460" width="370" height="32" rx="6" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="275" y="481" fill="{t['text']}" font-size="12" font-family="PingFang SC" text-anchor="middle">全景无阻碍跨版通幅视觉</text>
  {badge(185, 520, "破缝通版全景震撼", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_139(): # 无出血版式 (No-Bleed Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Pure white outer sheet margin -->
  <rect x="50" y="60" width="450" height="500" fill="#FFFFFF" rx="6" stroke="{t['stroke']}" stroke-width="2"/>
  <!-- Safe Print Content Area strictly inset by 30px -->
  <rect x="90" y="100" width="370" height="420" fill="{t['bg']}" rx="4" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="110" y1="140" x2="440" y2="140" stroke="{t['accent']}" stroke-width="3"/>
  <rect x="110" y="170" width="150" height="140" rx="4" fill="{t['stroke']}"/>
  <rect x="280" y="170" width="160" height="140" rx="4" fill="{t['bg_surface']}"/>
  <!-- Dimension arrows showing safe margin -->
  {dimension_h(50, 90, 80, "30mm", t['danger'], t['danger'])}
  {dimension_h(460, 500, 80, "30mm", t['danger'], t['danger'])}
  {badge(185, 480, "安全内缩白边装帧", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_140(): # 图片主导版式 (Image-Dominant)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 85% Giant Hero Image Box -->
  <rect x="70" y="80" width="410" height="350" rx="6" fill="{t['accent']}" fill-opacity="0.85"/>
  <circle cx="275" cy="240" r="65" fill="{t['bg']}"/>
  <circle cx="275" cy="240" r="20" fill="#FFFFFF"/>
  <!-- 15% Minimal Caption Bar -->
  <line x1="70" y1="450" x2="480" y2="450" stroke="{t['accent']}" stroke-width="2"/>
  <text x="70" y="480" fill="#FFFFFF" font-size="14" font-weight="bold" font-family="Montserrat">DOMINANT IMAGE 85%</text>
  <text x="70" y="500" fill="{t['text_dim']}" font-size="11" font-family="PingFang SC">以视觉图像统领全局，文字退为微观注脚</text>
  {badge(330, 465, "巨幅图像主导", t['accent'], t['bg'], 140, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_141(): # 文字主导版式 (Text-Dominant)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Giant Initial Drop Cap -->
  <text x="80" y="190" fill="{t['accent']}" font-size="96" font-weight="900" font-family="Georgia, serif">T</text>
  <!-- Dense 3-column text columns -->
  <g fill="{t['stroke']}">
    <rect x="160" y="110" width="100" height="330" rx="3"/>
    <rect x="275" y="110" width="100" height="330" rx="3"/>
    <rect x="390" y="110" width="90" height="330" rx="3"/>
  </g>
  <text x="275" y="475" fill="{t['text']}" font-size="13" font-weight="bold" font-family="Montserrat" text-anchor="middle">ESSAY DENSITY & TYPOGRAPHY</text>
  {badge(185, 510, "纯文字学术长文架构", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_142(): # 大标题版式 (Big Headline)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Colossal Headline dominating 60% vertical space -->
  <text x="75" y="170" fill="{t['accent']}" font-size="74" font-weight="900" font-family="Montserrat" letter-spacing="-2">TYPO</text>
  <text x="75" y="245" fill="#FFFFFF" font-size="74" font-weight="900" font-family="Montserrat" letter-spacing="-2">GRAPHIC</text>
  <text x="75" y="320" fill="{t['accent_alt']}" font-size="74" font-weight="900" font-family="Montserrat" letter-spacing="-2">IMPACT</text>
  <!-- Subordinate body text footer -->
  <line x1="75" y1="360" x2="475" y2="360" stroke="{t['guide']}" stroke-width="2"/>
  <rect x="75" y="385" width="280" height="12" rx="2" fill="{t['text_dim']}"/>
  <rect x="75" y="405" width="240" height="12" rx="2" fill="{t['text_dim']}"/>
  {badge(185, 480, "标语字号震慑冲击", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_143(): # 图片窗口版式 (Image Window)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Die-cut Window Cutout Frame -->
  <rect x="110" y="110" width="330" height="330" rx="16" fill="none" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Revealed Photo Scene inside window -->
  <rect x="125" y="125" width="300" height="300" rx="10" fill="{t['stroke']}"/>
  <circle cx="275" cy="275" r="60" fill="{t['accent']}"/>
  <circle cx="275" cy="275" r="20" fill="#FFFFFF"/>
  <!-- Window framing brackets -->
  <path d="M 90 90 L 120 90 M 90 90 L 90 120" stroke="{t['danger']}" stroke-width="3" fill="none"/>
  <path d="M 460 90 L 430 90 M 460 90 L 460 120" stroke="{t['danger']}" stroke-width="3" fill="none"/>
  {badge(185, 480, "开窗漏景视觉窥探", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_144(): # 框架版式 (Frame Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Double Decorative Classical Border -->
  <rect x="75" y="85" width="400" height="450" rx="4" fill="none" stroke="{t['accent']}" stroke-width="3"/>
  <rect x="85" y="95" width="380" height="430" rx="2" fill="none" stroke="{t['accent_alt']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <!-- Center Artwork Content -->
  <rect x="145" y="160" width="260" height="220" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.8"/>
  <circle cx="275" cy="270" r="42" fill="{t['accent']}"/>
  <circle cx="275" cy="270" r="12" fill="#FFFFFF"/>
  <text x="275" y="420" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">FRAMED CLASSICISM</text>
  {badge(185, 480, "古典饰边层层嵌套", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_145(): # 多面板版式 (Multi-Panel Graphic Novel Grid)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Comic / Graphic Novel 6 Panels with thick gutters -->
  <!-- Row 1 (Wide panel + Narrow panel) -->
  <rect x="75" y="90" width="240" height="120" rx="4" fill="{t['stroke']}" stroke="#FFFFFF" stroke-width="2"/>
  <rect x="330" y="90" width="145" height="120" rx="4" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
  <!-- Row 2 (3 Equal panels) -->
  <rect x="75" y="225" width="115" height="120" rx="4" fill="{t['accent_alt']}" stroke="#FFFFFF" stroke-width="2"/>
  <rect x="205" y="225" width="140" height="120" rx="4" fill="{t['stroke']}" stroke="#FFFFFF" stroke-width="2"/>
  <rect x="360" y="225" width="115" height="120" rx="4" fill="{t['danger']}" stroke="#FFFFFF" stroke-width="2"/>
  <!-- Row 3 (Full-width climax panel) -->
  <rect x="75" y="360" width="400" height="100" rx="4" fill="{t['accent']}" fill-opacity="0.9" stroke="#FFFFFF" stroke-width="2"/>
  <circle cx="275" cy="410" r="24" fill="#FFFFFF"/>
  {badge(185, 490, "连环画分镜叙事网格", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_147(): # 马戏团版式 (Circus Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vibrant, Eclectic Mosaic of mixed font banners, stickers & tiles -->
  <rect x="75" y="90" width="200" height="80" fill="{t['danger']}" rx="4"/>
  <text x="175" y="140" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Impact, Montserrat" text-anchor="middle">EXTRA!</text>
  <circle cx="380" cy="150" r="50" fill="{t['accent']}"/>
  <text x="380" y="158" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">HOT</text>
  <rect x="75" y="190" width="300" height="90" rx="6" fill="{t['accent_alt']}"/>
  <rect x="75" y="300" width="180" height="130" rx="4" fill="{t['stroke']}"/>
  <rect x="275" y="300" width="200" height="130" rx="4" fill="{t['accent']}"/>
  <polygon points="410,210 450,250 370,250" fill="{t['danger']}"/>
  {badge(185, 470, "马戏团杂糅喧嚣版面", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_150(): # 图文谜语版式 (Rebus Layout)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Text line with embedded icon puzzle substitutions -->
  <text x="80" y="160" fill="#FFFFFF" font-size="28" font-weight="900" font-family="Montserrat">I</text>
  <circle cx="150" cy="150" r="24" fill="{t['danger']}"/>
  <text x="210" y="160" fill="#FFFFFF" font-size="28" font-weight="900" font-family="Montserrat">DESIGN</text>
  <line x1="80" y1="200" x2="470" y2="200" stroke="{t['guide']}" stroke-width="2"/>
  <text x="80" y="270" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Montserrat">WHEN</text>
  <rect x="180" y="240" width="45" height="45" rx="6" fill="{t['accent']}"/>
  <text x="250" y="270" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Montserrat">MEETS</text>
  <polygon points="380,240 410,285 350,285" fill="{t['accent_alt']}"/>
  <text x="275" y="380" fill="{t['text_dim']}" font-size="14" font-family="PingFang SC" text-anchor="middle">符号与文字互换的视觉谜题</text>
  {badge(185, 480, "以象指文图文谜语", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_151(): # 拼贴版式 (Collage Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Dadaist torn paper scraps angled dynamically -->
  <g transform="rotate(-8 240 240)">
    <polygon points="100,120 320,100 300,340 80,320" fill="{t['stroke']}" stroke="#FFFFFF" stroke-width="2"/>
    <rect x="120" y="140" width="160" height="80" fill="{t['bg']}"/>
  </g>
  <g transform="rotate(12 320 290)">
    <polygon points="220,180 430,160 410,420 200,400" fill="{t['accent']}" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="320" cy="290" r="42" fill="#FFFFFF"/>
  </g>
  <!-- Tape overlay strap -->
  <rect x="190" y="90" width="80" height="24" fill="#FFF9C4" opacity="0.75" transform="rotate(25 230 102)"/>
  {badge(185, 510, "达达撕贴异质并置", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_152(): # 蒙太奇版式 (Montage Layout)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Layered translucent photographic exposures -->
  <circle cx="220" cy="270" r="110" fill="{t['accent']}" opacity="0.4"/>
  <circle cx="330" cy="270" r="110" fill="{t['accent_alt']}" opacity="0.4"/>
  <!-- Intersection lens creating third meaning -->
  <ellipse cx="275" cy="270" rx="55" ry="90" fill="{t['danger']}" opacity="0.7"/>
  <circle cx="275" cy="270" r="14" fill="#FFFFFF"/>
  <text x="275" y="110" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">A + B = C MONTAGE DIALECTIC</text>
  {badge(185, 480, "多重叠印意义升华", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_155(): # 插页式版式 (Fold-Out Insert)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Bound magazine body -->
  <rect x="80" y="100" width="280" height="400" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <!-- Unfolded Extra Width Gatefold Page Flap Extending Out -->
  <rect x="330" y="120" width="150" height="360" fill="{t['accent']}" rx="4" stroke="#FFFFFF" stroke-width="2"/>
  <!-- Dashed Fold Crease line -->
  <line x1="330" y1="100" x2="330" y2="500" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="405" y="300" fill="{t['bg']}" font-size="13" font-weight="900" font-family="Montserrat" text-anchor="middle">GATEFOLD</text>
  {badge(185, 520, "异形拉页展开画幅", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_156(): # 侧栏版式 (Sidebar Layout)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Main Editorial Body Column Left (65%) -->
  <rect x="75" y="100" width="250" height="410" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="95" y="130" width="210" height="16" rx="3" fill="{t['accent']}"/>
  <rect x="95" y="160" width="210" height="10" rx="2" fill="{t['stroke']}"/>
  <rect x="95" y="180" width="180" height="10" rx="2" fill="{t['stroke']}"/>
  <!-- Highlight Colored Factoid Sidebar Right (35%) -->
  <rect x="345" y="100" width="130" height="410" rx="6" fill="{t['accent']}" fill-opacity="0.9"/>
  <text x="410" y="140" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">FACTS</text>
  <circle cx="410" cy="200" r="24" fill="#FFFFFF"/>
  <rect x="365" y="250" width="90" height="8" rx="2" fill="{t['bg']}"/>
  <rect x="365" y="270" width="70" height="8" rx="2" fill="{t['bg']}"/>
  {badge(185, 520, "主文侧栏辅助注记", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_157(): # 边注版式 (Marginalia)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Centered Inner Main Column -->
  <rect x="80" y="100" width="240" height="400" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5" rx="4"/>
  <g fill="{t['stroke']}">
    {''.join([f'<rect x="100" y="{130 + i*22}" width="200" height="8" rx="2"/>' for i in range(15)])}
  </g>
  <!-- Generous Outer Margin for Marginal Notes -->
  <line x1="340" y1="100" x2="340" y2="500" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <rect x="355" y="160" width="115" height="70" rx="4" fill="{t['accent']}" fill-opacity="0.2" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="412" y="195" fill="{t['accent']}" font-size="10" font-family="Montserrat" text-anchor="middle">[NOTE §1.4]</text>
  <rect x="355" y="280" width="115" height="80" rx="4" fill="{t['accent_alt']}" fill-opacity="0.2" stroke="{t['accent_alt']}" stroke-width="1.5"/>
  <text x="412" y="320" fill="{t['accent_alt']}" font-size="10" font-family="Montserrat" text-anchor="middle">[SCHOLIA]</text>
  {badge(185, 520, "留白天地边注考据", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_158(): # 环绕图版式 (Runaround / Text Wrap)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Central Organic Circular Image Cutout -->
  <circle cx="275" cy="280" r="70" fill="{t['accent']}"/>
  <circle cx="275" cy="280" r="20" fill="#FFFFFF"/>
  <!-- Text contour lines curving smoothly around circle -->
  <g fill="{t['stroke']}">
    <rect x="80" y="110" width="390" height="10" rx="2"/>
    <rect x="80" y="130" width="390" height="10" rx="2"/>
    <rect x="80" y="150" width="390" height="10" rx="2"/>
    <rect x="80" y="175" width="390" height="10" rx="2"/>
    <!-- Contoured left & right blocks -->
    <rect x="80" y="220" width="100" height="10" rx="2"/><rect x="370" y="220" width="100" height="10" rx="2"/>
    <rect x="80" y="250" width="90" height="10" rx="2"/><rect x="380" y="250" width="90" height="10" rx="2"/>
    <rect x="80" y="280" width="90" height="10" rx="2"/><rect x="380" y="280" width="90" height="10" rx="2"/>
    <rect x="80" y="310" width="100" height="10" rx="2"/><rect x="370" y="310" width="100" height="10" rx="2"/>
    <!-- Resumed full width lines -->
    <rect x="80" y="370" width="390" height="10" rx="2"/>
    <rect x="80" y="390" width="350" height="10" rx="2"/>
  </g>
  {badge(185, 480, "图文有机曲线绕排", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_159(): # 浮动块版式 (Callout Box)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Background 2-column text -->
  <g fill="{t['stroke']}" opacity="0.35">
    <rect x="80" y="100" width="180" height="390" rx="3"/>
    <rect x="290" y="100" width="180" height="390" rx="3"/>
  </g>
  <!-- Floating Pull-Quote Callout Box overlapping columns -->
  <rect x="135" y="210" width="280" height="180" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="3"/>
  <text x="165" y="255" fill="{t['accent']}" font-size="36" font-family="Georgia, serif">“</text>
  <text x="275" y="295" fill="#FFFFFF" font-size="16" font-weight="900" font-family="PingFang SC" text-anchor="middle">核心观点提炼卡片</text>
  <text x="275" y="325" fill="{t['accent']}" font-size="12" font-family="Montserrat" text-anchor="middle">HIGHLIGHTED CALLOUT</text>
  <text x="385" y="355" fill="{t['accent']}" font-size="36" font-family="Georgia, serif">”</text>
  {badge(185, 520, "跨栏浮动引述凸显", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_161(): # 章节扉页 (Chapter Opener)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Vast Generous Empty Space (65%) -->
  <text x="90" y="200" fill="{t['accent']}" font-size="64" font-weight="900" font-family="Montserrat">CHAPTER</text>
  <text x="90" y="280" fill="#FFFFFF" font-size="80" font-weight="900" font-family="Georgia, serif">04</text>
  <line x1="90" y1="320" x2="450" y2="320" stroke="{t['accent_alt']}" stroke-width="3"/>
  <text x="90" y="360" fill="{t['text']}" font-size="18" font-weight="bold" font-family="PingFang SC">字体排印与网格架构系统</text>
  <text x="90" y="390" fill="{t['text_dim']}" font-size="12" font-family="Montserrat">Typographic Grid Foundations</text>
  {badge(185, 480, "章节扉页庄重留白", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_162(): # 栏目开启页 (Department Opener)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Top Bold Category Indicator Tab -->
  <rect x="50" y="60" width="200" height="44" fill="{t['accent']}" rx="4"/>
  <text x="150" y="88" fill="{t['bg']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">SPECIAL REPORT</text>
  <!-- Main Hero Spread -->
  <rect x="80" y="140" width="390" height="200" rx="6" fill="{t['stroke']}"/>
  <circle cx="275" cy="240" r="40" fill="{t['accent_alt']}"/>
  <text x="80" y="380" fill="#FFFFFF" font-size="24" font-weight="900" font-family="PingFang SC">杂志固定栏目头牌</text>
  <line x1="80" y1="410" x2="470" y2="410" stroke="{t['guide']}" stroke-width="2"/>
  {badge(185, 480, "杂志专栏识别标签", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_163(): # 特写跨页 (Macro Detail Spread)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Giant Magnifying Zoom Ring -->
  <circle cx="275" cy="290" r="160" fill="{t['stroke']}" stroke="{t['accent']}" stroke-width="4"/>
  <circle cx="275" cy="290" r="90" fill="{t['accent']}" opacity="0.7"/>
  <circle cx="275" cy="290" r="20" fill="#FFFFFF"/>
  <!-- Crosshair Reticle lines -->
  <line x1="115" y1="290" x2="435" y2="290" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="275" y1="130" x2="275" y2="450" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="275" y="110" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">MACRO TEXTURE DETAIL 1000X</text>
  {badge(185, 520, "微观特写跨版呈现", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_164(): # 目录版式 (Table of Contents)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="80" y="120" fill="{t['accent']}" font-size="24" font-weight="900" font-family="Montserrat">CONTENTS</text>
  <!-- Dotted leader lines with page numbers -->
  <g fill="{t['text']}" font-size="13" font-family="Montserrat">
    <text x="80" y="170">01. THE SWISS CANON</text>
    <line x1="260" y1="166" x2="430" y2="166" stroke="{t['stroke']}" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="445" y="170" fill="{t['accent']}" font-weight="bold">12</text>

    <text x="80" y="220">02. GESTALT LAWS</text>
    <line x1="225" y1="216" x2="430" y2="216" stroke="{t['stroke']}" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="445" y="220" fill="{t['accent']}" font-weight="bold">48</text>

    <text x="80" y="270">03. EDITORIAL PRINT</text>
    <line x1="235" y1="266" x2="430" y2="266" stroke="{t['stroke']}" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="445" y="270" fill="{t['accent']}" font-weight="bold">96</text>

    <text x="80" y="320">04. GRID SYSTEMS</text>
    <line x1="220" y1="316" x2="430" y2="316" stroke="{t['stroke']}" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="445" y="320" fill="{t['accent']}" font-weight="bold">168</text>

    <text x="80" y="370">05. WEB & RESPONSIVE</text>
    <line x1="260" y1="366" x2="430" y2="366" stroke="{t['stroke']}" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="445" y="370" fill="{t['accent']}" font-weight="bold">222</text>
  </g>
  {badge(185, 480, "点线导引目录条理", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_165(): # 索引版式 (Index Layout)
    t = get_theme("cobalt-blue")
    # 4 compact alphabetical index columns
    cols = "".join([f'<g transform="translate({75 + i*105}, 0)"><text x="0" y="140" fill="{t["accent"]}" font-size="16" font-weight="900" font-family="Montserrat">{chr(65+i)}</text><rect x="0" y="160" width="85" height="280" rx="3" fill="{t["stroke"]}" opacity="0.4"/></g>' for i in range(4)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="80" y="105" fill="#FFFFFF" font-size="20" font-weight="900" font-family="Montserrat">SUBJECT INDEX (A-Z)</text>
  {cols}
  {badge(185, 520, "多栏紧凑检索索引", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_166(): # 图录版式 (Catalogue Grid)
    t = get_theme("forest-green")
    # 3x3 catalog items with item numbers
    items = "".join([f'<g transform="translate({80 + (i%3)*135}, {110 + (i//3)*110})"><rect x="0" y="0" width="120" height="75" rx="4" fill="{t["stroke"]}"/><circle cx="60" cy="37" r="16" fill="{t["accent"]}"/><rect x="0" y="82" width="70" height="8" rx="2" fill="{t["text_dim"]}"/><text x="120" y="88" fill="{t["accent_alt"]}" font-size="9" font-family="Montserrat" text-anchor="end">#{str(i+1).zfill(2)}</text></g>' for i in range(9)])
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="80" y="95" fill="{t['accent']}" font-size="14" font-weight="bold" font-family="Montserrat">EXHIBITION CATALOGUE</text>
  {items}
  {badge(185, 520, "艺术品展录规范矩阵", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_167(): # 引语主导版式 (Quote Dominant)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="60" width="450" height="500" fill="{t['bg_surface']}" rx="8" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Giant Colossal Quotation Marks -->
  <text x="80" y="180" fill="{t['accent']}" font-size="110" font-family="Georgia, serif" opacity="0.9">“</text>
  <text x="110" y="250" fill="#FFFFFF" font-size="24" font-weight="900" font-family="PingFang SC">形式永远服从于功能，</text>
  <text x="110" y="290" fill="{t['accent']}" font-size="24" font-weight="900" font-family="PingFang SC">这是永恒不变的自然法则。</text>
  <text x="420" y="370" fill="{t['accent']}" font-size="110" font-family="Georgia, serif" opacity="0.9">”</text>
  <line x1="110" y1="350" x2="280" y2="350" stroke="{t['guide']}" stroke-width="2"/>
  <text x="110" y="380" fill="{t['text_dim']}" font-size="12" font-family="Montserrat">— LOUIS SULLIVAN (1896)</text>
  {badge(185, 480, "巨幅语录引文破版", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

CAT03_SVGS = {
    "135": gen_135, "136": gen_136, "137": gen_137, "139": gen_139, "140": gen_140,
    "141": gen_141, "142": gen_142, "143": gen_143, "144": gen_144, "145": gen_145,
    "147": gen_147, "150": gen_150, "151": gen_151, "152": gen_152, "155": gen_155,
    "156": gen_156, "157": gen_157, "158": gen_158, "159": gen_159, "161": gen_161,
    "162": gen_162, "163": gen_163, "164": gen_164, "165": gen_165, "166": gen_166,
    "167": gen_167,
    "132": gen_132, "133": gen_133, "138": gen_138, "148": gen_148, "149": gen_149,
    "153": gen_153, "154": gen_154, "160": gen_160
}


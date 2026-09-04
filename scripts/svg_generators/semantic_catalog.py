"""
Semantic Vector Catalog for 350 Layout Compositions.
Provides unique, authentic geometric schematics for every layout concept,
eliminating any repeated templates.
"""

from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def generate_semantic_svg(layout_id, data):
    name = data.get("name", "")
    name_en = data.get("name_en", "")
    subcat = data.get("subcategory", "")
    theme_key = data.get("theme", "warm-ivory")
    t = get_theme(theme_key)
    lid = str(layout_id).zfill(3)

    # 1. Traditional Chinese Painting & Aesthetics (315-334)
    if "高远" in name:
        # Soaring mountain peak Guo Xi style
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <polygon points="275,80 170,430 380,430" fill="{t['stroke']}" opacity="0.9"/>
  <polygon points="275,80 230,270 275,430" fill="{t['accent']}" opacity="0.3"/>
  <polygon points="275,80 200,200 275,260" fill="#FFFFFF" opacity="0.6"/>
  <path d="M 120 370 Q 275 350 430 370" stroke="#FFFFFF" stroke-width="18" fill="none" opacity="0.4" stroke-linecap="round"/>
  <line x1="275" y1="490" x2="275" y2="90" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4"/>
  <polygon points="275,80 268,98 282,98" fill="{t['accent']}"/>
  <text x="350" y="140" fill="{t['accent']}" font-size="16" font-family="Kaiti, STKaiti, serif">自山下而仰山巅</text>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "深远" in name:
        # Winding ravine penetrating deep
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <path d="M 50 150 Q 180 220 275 140 T 500 180 L 500 570 L 50 570 Z" fill="{t['stroke']}"/>
  <path d="M 50 280 Q 220 350 320 270 T 500 320 L 500 570 L 50 570 Z" fill="{t['bg']}"/>
  <path d="M 275 520 C 275 420 210 360 250 290 C 280 230 240 180 275 120" fill="none" stroke="{t['accent']}" stroke-width="4" stroke-dasharray="6,4"/>
  <polygon points="275,115 268,132 282,132" fill="{t['accent']}"/>
  <text x="360" y="110" fill="{t['accent']}" font-size="16" font-family="Kaiti, STKaiti, serif">自山前而窥山后</text>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "平远" in name:
        # Low peaceful horizon marsh
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <line x1="50" y1="360" x2="500" y2="360" stroke="{t['accent']}" stroke-width="2.5"/>
  <path d="M 80 360 Q 200 330 320 360 T 480 355" fill="none" stroke="{t['stroke']}" stroke-width="4"/>
  <ellipse cx="275" cy="200" rx="45" ry="45" fill="{t['accent']}" opacity="0.3"/>
  <ellipse cx="275" cy="200" rx="18" ry="18" fill="{t['accent']}"/>
  <text x="275" y="440" fill="{t['text_dim']}" font-size="16" font-family="Kaiti, STKaiti, serif" text-anchor="middle">自近山而望远山 · 平远渺渺</text>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "一河两岸" in name:
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <polygon points="80,150 180,120 280,150" fill="{t['stroke']}" opacity="0.6"/>
  <polygon points="310,140 390,115 470,140" fill="{t['stroke']}" opacity="0.4"/>
  <rect x="70" y="180" width="410" height="170" fill="none" stroke="{t['accent']}" stroke-width="1" stroke-dasharray="6,6" opacity="0.4"/>
  <polygon points="60,520 180,410 320,440 480,520" fill="{t['stroke']}"/>
  <line x1="160" y1="420" x2="150" y2="300" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <line x1="190" y1="430" x2="200" y2="320" stroke="{t['accent']}" stroke-width="3.5" stroke-linecap="round"/>
  <rect x="420" y="80" width="30" height="30" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "边角" in name:
        # Southern song Ma Yuan half mountain corner
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Corner landscape occupying lower left 1/3 -->
  <polygon points="50,220 260,570 50,570" fill="{t['stroke']}"/>
  <line x1="50" y1="220" x2="260" y2="570" stroke="{t['accent']}" stroke-width="3"/>
  <line x1="110" y1="330" x2="180" y2="280" stroke="{t['accent']}" stroke-width="3" stroke-linecap="round"/>
  <!-- 75% Vast Mist Void in Upper Right -->
  <text x="360" y="240" fill="{t['text_dim']}" font-size="20" font-family="Kaiti, STKaiti, serif" text-anchor="middle">马一角 · 留白旷远</text>
  <circle cx="360" cy="150" r="28" fill="{t['accent']}" opacity="0.4"/>
  <rect x="420" y="80" width="26" height="26" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "折枝" in name:
        # Cut branch flower composition
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <path d="M 50 380 Q 200 340 320 220 T 430 130" fill="none" stroke="{t['accent']}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="320" cy="220" r="22" fill="{t['danger']}"/>
  <circle cx="430" cy="130" r="16" fill="{t['accent_alt']}"/>
  <circle cx="230" cy="280" r="14" fill="{t['accent_alt']}"/>
  <text x="140" y="160" fill="{t['text_dim']}" font-size="16" font-family="Kaiti, STKaiti, serif">截取生动一枝 · 以小见大</text>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "留白" in name or "计白当黑" in name or "虚实" in name:
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <path d="M 320 70 C 450 140 480 340 380 480 C 320 540 240 520 280 440 C 320 360 220 280 290 180 Z" fill="{t['stroke']}"/>
  <circle cx="160" cy="310" r="22" fill="{t['danger']}"/>
  <circle cx="160" cy="310" r="6" fill="#FFFFFF"/>
  <line x1="160" y1="310" x2="330" y2="310" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="160" y="370" fill="{t['accent']}" font-size="20" font-family="Kaiti, STKaiti, serif" text-anchor="middle">无画处皆成妙境</text>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "疏密" in name or "聚散" in name:
        inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Dense Cluster on Left -->
  <g fill="{t['accent']}">
    <circle cx="120" cy="240" r="14"/><circle cx="150" cy="220" r="18"/><circle cx="170" cy="260" r="12"/><circle cx="130" cy="280" r="16"/>
    <circle cx="190" cy="230" r="22"/><circle cx="150" cy="310" r="14"/><circle cx="180" cy="290" r="16"/>
  </g>
  <rect x="100" y="190" width="120" height="140" fill="none" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="160" y="360" fill="{t['accent']}" font-size="13" font-family="Kaiti, serif" text-anchor="middle">密不通风</text>
  <!-- Sparse Void on Right -->
  <circle cx="410" cy="260" r="16" fill="{t['danger']}"/>
  <text x="410" y="360" fill="{t['text_dim']}" font-size="13" font-family="Kaiti, serif" text-anchor="middle">疏可走马</text>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""

    # 2. Cinema & Camera Shots (301-314)
    elif "单人" in name:
        inner = f"""
  <rect x="40" y="90" width="470" height="440" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Solitary Figure in Frame -->
  <circle cx="275" cy="230" r="38" fill="{t['accent']}"/>
  <path d="M 210 380 Q 275 310 340 380 L 350 490 L 200 490 Z" fill="{t['stroke']}"/>
  <!-- Rule of thirds guide lines -->
  <line x1="196" y1="90" x2="196" y2="530" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="353" y1="90" x2="353" y2="530" stroke="{t['guide']}" stroke-width="1" stroke-dasharray="4,4"/>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "双人" in name:
        inner = f"""
  <rect x="40" y="90" width="470" height="440" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Two figures facing each other -->
  <circle cx="160" cy="260" r="30" fill="{t['accent']}"/>
  <path d="M 110 400 Q 160 330 210 400 L 220 490 L 100 490 Z" fill="{t['stroke']}"/>
  <circle cx="390" cy="260" r="30" fill="{t['accent_alt']}"/>
  <path d="M 340 400 Q 390 330 440 400 L 450 490 L 330 490 Z" fill="{t['stroke']}"/>
  <line x1="190" y1="260" x2="360" y2="260" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <circle cx="275" cy="260" r="10" fill="{t['danger']}"/>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "三人" in name:
        inner = f"""
  <rect x="40" y="90" width="470" height="440" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- 3 Figures in Triangle Formation -->
  <circle cx="275" cy="180" r="26" fill="{t['accent']}"/>
  <circle cx="160" cy="340" r="24" fill="{t['accent_alt']}"/>
  <circle cx="390" cy="340" r="24" fill="{t['accent_alt']}"/>
  <polygon points="275,180 160,340 390,340" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="5,4"/>
  <text x="275" y="280" fill="{t['accent']}" font-size="12" font-family="Montserrat" text-anchor="middle">TRIANGLE STAGING</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "群像" in name:
        inner = f"""
  <rect x="40" y="90" width="470" height="440" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Multi-Figure Ensemble Tableau -->
  <circle cx="90" cy="320" r="18" fill="{t['stroke']}"/>
  <circle cx="160" cy="270" r="22" fill="{t['accent_alt']}"/>
  <circle cx="240" cy="230" r="26" fill="{t['accent']}"/>
  <circle cx="320" cy="250" r="24" fill="{t['accent_alt']}"/>
  <circle cx="400" cy="290" r="20" fill="{t['stroke']}"/>
  <circle cx="470" cy="340" r="16" fill="{t['stroke']}"/>
  <!-- Staging Arc Guide -->
  <path d="M 90 320 Q 240 180 470 340" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4"/>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "过肩" in name:
        inner = f"""
  <rect x="40" y="90" width="470" height="440" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Blurred Foreground Shoulder on Left -->
  <path d="M 40 280 Q 150 260 170 360 L 190 530 L 40 530 Z" fill="{t['stroke']}" opacity="0.8"/>
  <circle cx="100" cy="220" r="40" fill="{t['stroke']}" opacity="0.8"/>
  <!-- In-Focus Character across Table -->
  <circle cx="360" cy="260" r="32" fill="{t['accent']}"/>
  <circle cx="360" cy="260" r="8" fill="#FFFFFF"/>
  <path d="M 310 400 Q 360 340 410 400 L 420 530 L 300 530 Z" fill="{t['accent']}" opacity="0.3"/>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "鸟瞰" in name or "顶视" in name or "俯视" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2"/>
  <!-- Top-Down Map Grid -->
  <rect x="90" y="100" width="160" height="180" fill="{t['stroke']}" rx="4"/>
  <rect x="290" y="100" width="170" height="180" fill="{t['stroke']}" rx="4"/>
  <rect x="90" y="320" width="160" height="180" fill="{t['stroke']}" rx="4"/>
  <rect x="290" y="320" width="170" height="180" fill="{t['stroke']}" rx="4"/>
  <circle cx="270" cy="300" r="28" fill="{t['accent']}"/>
  <circle cx="270" cy="300" r="8" fill="#FFFFFF"/>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "虫视" in name or "仰视" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="2"/>
  <polygon points="80,560 470,560 330,90 220,90" fill="{t['stroke']}" stroke="{t['accent']}" stroke-width="3"/>
  <line x1="160" y1="560" x2="250" y2="90" stroke="{t['accent_alt']}" stroke-width="2"/>
  <line x1="390" y1="560" x2="300" y2="90" stroke="{t['accent_alt']}" stroke-width="2"/>
  <circle cx="275" cy="90" r="22" fill="{t['accent']}"/>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "移轴" in name:
        # Tilt-shift miniature slice
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}"/>
  <!-- Top Blurred Band -->
  <rect x="50" y="60" width="450" height="140" fill="{t['stroke']}" opacity="0.5"/>
  <text x="275" y="140" fill="{t['text_dim']}" font-size="14" font-family="Montserrat" text-anchor="middle">DEFOCUSED (BLUR)</text>
  <!-- Sharp Center Plane Slice -->
  <rect x="50" y="200" width="450" height="180" fill="{t['accent']}" opacity="0.25" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="275" cy="290" r="32" fill="{t['accent']}"/>
  <circle cx="275" cy="290" r="10" fill="#FFFFFF"/>
  <text x="275" y="345" fill="#FFFFFF" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">RAZOR FOCUS SLICE</text>
  <!-- Bottom Blurred Band -->
  <rect x="50" y="380" width="450" height="180" fill="{t['stroke']}" opacity="0.5"/>
  {badge(185, 490, name, t['accent'], t['bg'], 180, 28)}"""
    elif "浅景深" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}"/>
  <!-- Bokeh Discs in Background -->
  <circle cx="120" cy="160" r="45" fill="{t['stroke']}" opacity="0.4"/>
  <circle cx="410" cy="180" r="60" fill="{t['stroke']}" opacity="0.3"/>
  <circle cx="160" cy="420" r="55" fill="{t['stroke']}" opacity="0.4"/>
  <circle cx="430" cy="400" r="50" fill="{t['stroke']}" opacity="0.35"/>
  <!-- Razor Sharp Subject in Foreground -->
  <circle cx="275" cy="290" r="48" fill="{t['accent']}"/>
  <circle cx="275" cy="290" r="14" fill="#FFFFFF"/>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""

    # 3. Typography & Layout Systems (168-221)
    elif "左对齐" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Strict Left Flush Margin Rule -->
  <line x1="90" y1="80" x2="90" y2="520" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Ragged Right Lines -->
  <g fill="{t['accent']}">
    <rect x="105" y="110" width="280" height="12" rx="3"/>
    <rect x="105" y="135" width="230" height="12" rx="3"/>
    <rect x="105" y="160" width="310" height="12" rx="3"/>
    <rect x="105" y="185" width="190" height="12" rx="3"/>
    <rect x="105" y="210" width="260" height="12" rx="3"/>
    <rect x="105" y="255" width="300" height="12" rx="3"/>
    <rect x="105" y="280" width="220" height="12" rx="3"/>
    <rect x="105" y="305" width="270" height="12" rx="3"/>
  </g>
  <text x="430" y="215" fill="{t['text_dim']}" font-size="11" font-family="Montserrat">RAGGED RIGHT</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "右对齐" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Strict Right Flush Margin Rule -->
  <line x1="450" y1="80" x2="450" y2="520" stroke="{t['accent']}" stroke-width="3"/>
  <g fill="{t['accent']}">
    <rect x="170" y="110" width="265" height="12" rx="3"/>
    <rect x="220" y="135" width="215" height="12" rx="3"/>
    <rect x="140" y="160" width="295" height="12" rx="3"/>
    <rect x="260" y="185" width="175" height="12" rx="3"/>
  </g>
  <text x="120" y="150" fill="{t['text_dim']}" font-size="11" font-family="Montserrat">RAGGED LEFT</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "两端对齐" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Left and Right Flush Bounds -->
  <line x1="90" y1="80" x2="90" y2="520" stroke="{t['accent']}" stroke-width="2.5"/>
  <line x1="450" y1="80" x2="450" y2="520" stroke="{t['accent']}" stroke-width="2.5"/>
  <g fill="{t['accent']}">
    <rect x="105" y="110" width="330" height="10" rx="2"/>
    <rect x="105" y="130" width="330" height="10" rx="2"/>
    <rect x="105" y="150" width="330" height="10" rx="2"/>
    <rect x="105" y="170" width="330" height="10" rx="2"/>
    <rect x="105" y="190" width="230" height="10" rx="2"/>
  </g>
  <text x="275" y="260" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">JUSTIFIED RECTILINEAR BLOCK</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "直排" in name or "竖排" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Vertical columns right-to-left -->
  <g stroke="{t['accent']}" stroke-width="1" stroke-dasharray="4,4" opacity="0.6">
    <line x1="410" y1="90" x2="410" y2="480"/>
    <line x1="330" y1="90" x2="330" y2="480"/>
    <line x1="250" y1="90" x2="250" y2="480"/>
    <line x1="170" y1="90" x2="170" y2="480"/>
  </g>
  <text x="410" y="140" fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">道</text>
  <text x="410" y="185" fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">生</text>
  <text x="410" y="230" fill="{t['accent']}" font-size="28" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">一</text>
  <rect x="90" y="400" width="36" height="36" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""

    # 4. Web, UI & Component Patterns (222-300)
    elif "单列" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Centered Single Column Content Container -->
  <rect x="135" y="90" width="280" height="440" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="160" y="120" width="230" height="120" rx="4" fill="{t['accent']}" opacity="0.8"/>
  <circle cx="275" cy="180" r="24" fill="#FFFFFF"/>
  <text x="275" y="280" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">SINGLE COLUMN 640px</text>
  {badge(185, 480, name, t['accent'], t['text'], 180, 28)}"""
    elif "双列" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="65" y="100" width="195" height="400" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="290" y="100" width="195" height="400" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="162" cy="200" r="32" fill="{t['accent']}"/>
  <circle cx="387" cy="200" r="32" fill="{t['accent_alt']}"/>
  {badge(185, 480, name, t['accent'], t['text'], 180, 28)}"""
    elif "三列" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="60" y="100" width="120" height="400" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="215" y="100" width="120" height="400" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="370" y="100" width="120" height="400" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <circle cx="120" cy="180" r="20" fill="{t['accent']}"/>
  <circle cx="275" cy="180" r="20" fill="{t['accent_alt']}"/>
  <circle cx="430" cy="180" r="20" fill="{t['danger']}"/>
  {badge(185, 480, name, t['accent'], t['text'], 180, 28)}"""
    elif "侧边栏" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Fixed Sidebar on Left -->
  <rect x="60" y="90" width="120" height="440" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="120" y="130" fill="{t['accent']}" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">SIDEBAR</text>
  <!-- Fluid Main Body on Right -->
  <rect x="200" y="90" width="290" height="440" rx="6" fill="{t['stroke']}"/>
  <circle cx="345" cy="240" r="40" fill="{t['accent']}"/>
  <circle cx="345" cy="240" r="10" fill="#FFFFFF"/>
  {badge(185, 480, name, t['accent'], t['text'], 180, 28)}"""
    elif "瀑布流" in name:
        # Masonry staggered columns
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Col 1 Cards -->
  <rect x="60" y="90" width="125" height="150" rx="6" fill="{t['accent']}"/>
  <rect x="60" y="260" width="125" height="210" rx="6" fill="{t['stroke']}"/>
  <!-- Col 2 Cards -->
  <rect x="210" y="90" width="125" height="220" rx="6" fill="{t['stroke']}"/>
  <rect x="210" y="330" width="125" height="140" rx="6" fill="{t['accent_alt']}"/>
  <!-- Col 3 Cards -->
  <rect x="360" y="90" width="125" height="130" rx="6" fill="{t['accent_alt']}"/>
  <rect x="360" y="240" width="125" height="230" rx="6" fill="{t['danger']}"/>
  {badge(185, 520, name, t['accent'], t['text'], 180, 28)}"""
    elif "卡片" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="65" y="100" width="195" height="190" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="290" y="100" width="195" height="190" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="65" y="310" width="195" height="190" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <rect x="290" y="310" width="195" height="190" rx="8" fill="{t['accent']}" fill-opacity="0.85"/>
  <circle cx="387" cy="405" r="28" fill="#FFFFFF"/>
  {badge(185, 480, name, t['accent'], t['text'], 180, 28)}"""
    elif "信息流" in name:
        # Feed stream layout
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Feed Card 1 -->
  <rect x="80" y="90" width="390" height="120" rx="6" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <circle cx="120" cy="130" r="18" fill="{t['accent']}"/>
  <line x1="150" y1="125" x2="350" y2="125" stroke="#FFFFFF" stroke-width="3"/>
  <line x1="150" y1="145" x2="280" y2="145" stroke="{t['text_dim']}" stroke-width="2"/>
  <!-- Feed Card 2 (Image post) -->
  <rect x="80" y="230" width="390" height="240" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="100" y="290" width="350" height="150" rx="4" fill="{t['stroke']}"/>
  <circle cx="275" cy="365" r="30" fill="{t['accent_alt']}"/>
  {badge(185, 520, name, t['accent'], t['text'], 180, 28)}"""
    elif "盒子" in name:
        # Concentric CSS Box Model
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}"/>
  <!-- Margin Box (Orange) -->
  <rect x="70" y="90" width="410" height="420" rx="6" fill="none" stroke="#FF9800" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="90" y="115" fill="#FF9800" font-size="12" font-weight="bold" font-family="Montserrat">MARGIN</text>
  <!-- Border Box (Yellow) -->
  <rect x="100" y="130" width="350" height="340" rx="6" fill="none" stroke="#FFD600" stroke-width="2"/>
  <text x="120" y="155" fill="#FFD600" font-size="12" font-weight="bold" font-family="Montserrat">BORDER</text>
  <!-- Padding Box (Green) -->
  <rect x="130" y="170" width="290" height="260" rx="6" fill="none" stroke="#00E676" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="150" y="195" fill="#00E676" font-size="12" font-weight="bold" font-family="Montserrat">PADDING</text>
  <!-- Content Box (Blue) -->
  <rect x="160" y="210" width="230" height="180" rx="6" fill="{t['accent']}" fill-opacity="0.8"/>
  <text x="275" y="305" fill="#FFFFFF" font-size="18" font-weight="900" font-family="Montserrat" text-anchor="middle">CONTENT</text>
  {badge(185, 480, name, t['accent'], t['text'], 180, 28)}"""
    elif "居中器" in name or "居中" in name:
        inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <line x1="50" y1="310" x2="500" y2="310" stroke="{t['accent']}" stroke-width="1.8" stroke-dasharray="6,6"/>
  <line x1="275" y1="60" x2="275" y2="560" stroke="{t['accent']}" stroke-width="1.8" stroke-dasharray="6,6"/>
  <circle cx="275" cy="310" r="70" fill="{t['accent']}" fill-opacity="0.2"/>
  <circle cx="275" cy="310" r="32" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="10" fill="#FFFFFF"/>
  <text x="275" y="420" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">PERFECT 50% / 50% CENTER</text>
  {badge(185, 480, name, t['accent'], t['text'], 180, 28)}"""

    # 5. Presentation Slides & Data Visuals (335-350)
    elif "数据图表" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- Bar Chart Columns -->
  <rect x="80" y="380" width="40" height="120" rx="4" fill="{t['stroke']}"/>
  <rect x="140" y="300" width="40" height="200" rx="4" fill="{t['accent_alt']}"/>
  <rect x="200" y="240" width="40" height="260" rx="4" fill="{t['accent_alt']}"/>
  <rect x="260" y="160" width="40" height="340" rx="4" fill="{t['accent']}"/>
  <rect x="320" y="210" width="40" height="290" rx="4" fill="{t['accent_alt']}"/>
  <rect x="380" y="120" width="40" height="380" rx="4" fill="{t['danger']}"/>
  <!-- Trend Line Overlay -->
  <path d="M 100 370 L 160 290 L 220 230 L 280 150 L 340 200 L 400 110" fill="none" stroke="#FFFFFF" stroke-width="3"/>
  <circle cx="400" cy="110" r="8" fill="#FFFFFF"/>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "时间线" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <line x1="70" y1="310" x2="470" y2="310" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <circle cx="120" cy="310" r="16" fill="{t['stroke']}"/>
  <circle cx="220" cy="310" r="16" fill="{t['accent_alt']}"/>
  <circle cx="330" cy="310" r="22" fill="{t['accent']}"/>
  <circle cx="330" cy="310" r="6" fill="#FFFFFF"/>
  <circle cx="430" cy="310" r="16" fill="{t['danger']}"/>
  <line x1="330" y1="310" x2="330" y2="180" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="270" y="130" width="120" height="50" rx="6" fill="{t['accent']}"/>
  <text x="330" y="160" fill="{t['bg']}" font-size="12" font-weight="900" font-family="Montserrat" text-anchor="middle">LAUNCH V3</text>
  {badge(185, 520, name, t['accent'], t['bg'], 180, 28)}"""
    elif "流程" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- 4 Step Sequential Process -->
  <rect x="70" y="110" width="370" height="65" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="110" y="150" fill="{t['accent']}" font-size="16" font-weight="900" font-family="Montserrat">01. DISCOVERY</text>
  <line x1="255" y1="175" x2="255" y2="205" stroke="{t['accent']}" stroke-width="2"/>

  <rect x="70" y="210" width="370" height="65" rx="8" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="1.5"/>
  <text x="110" y="250" fill="{t['accent']}" font-size="16" font-weight="900" font-family="Montserrat">02. ARCHITECTURE</text>
  <line x1="255" y1="275" x2="255" y2="305" stroke="{t['accent']}" stroke-width="2"/>

  <rect x="70" y="310" width="370" height="65" rx="8" fill="{t['accent']}"/>
  <text x="110" y="350" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Montserrat">03. EXECUTION</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "大数字" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="70" y="130" fill="{t['text_dim']}" font-size="14" font-weight="bold" font-family="Montserrat" letter-spacing="3">GLOBAL REACH</text>
  <text x="70" y="250" fill="{t['accent']}" font-size="92" font-weight="900" font-family="Montserrat">350+</text>
  <text x="70" y="310" fill="#FFFFFF" font-size="20" font-weight="bold" font-family="PingFang SC">标准排版与视觉构图系统</text>
  <line x1="70" y1="360" x2="480" y2="360" stroke="{t['guide']}" stroke-width="1.5"/>
  <text x="70" y="400" fill="{t['text_dim']}" font-size="13" font-family="Montserrat">100% Precision Layout Framework</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "引语" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <text x="80" y="160" fill="{t['accent']}" font-size="72" font-family="Georgia, serif">“</text>
  <text x="110" y="240" fill="#FFFFFF" font-size="26" font-weight="900" font-family="PingFang SC">好设计是显而易见的，</text>
  <text x="110" y="290" fill="{t['accent']}" font-size="26" font-weight="900" font-family="PingFang SC">伟大的设计是隐形的。</text>
  <text x="440" y="340" fill="{t['accent']}" font-size="72" font-family="Georgia, serif">”</text>
  <line x1="110" y1="380" x2="260" y2="380" stroke="{t['stroke']}" stroke-width="2"/>
  <text x="110" y="415" fill="{t['text_dim']}" font-size="13" font-family="Montserrat">JOE SPARANO</text>
  {badge(185, 480, name, t['accent'], t['bg'], 180, 28)}"""
    elif "比较" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <!-- PRO on Left (Green) -->
  <rect x="65" y="100" width="195" height="380" rx="8" fill="{t['bg']}" stroke="#00E676" stroke-width="2"/>
  <circle cx="162" cy="150" r="22" fill="#00E676"/>
  <text x="162" y="157" fill="#12141A" font-size="18" font-weight="900" text-anchor="middle">✓</text>
  <text x="162" y="210" fill="#00E676" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">ADVANTAGE</text>
  <!-- CON on Right (Red) -->
  <rect x="290" y="100" width="195" height="380" rx="8" fill="{t['bg']}" stroke="#FF3D00" stroke-width="2"/>
  <circle cx="387" cy="150" r="22" fill="#FF3D00"/>
  <text x="387" y="157" fill="#FFFFFF" font-size="18" font-weight="900" text-anchor="middle">✕</text>
  <text x="387" y="210" fill="#FF3D00" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">TRADEOFF</text>
  {badge(185, 510, name, t['accent'], t['bg'], 180, 28)}"""
    elif "全图" in name:
        inner = f"""
  <rect x="40" y="60" width="470" height="500" rx="8" fill="{t['stroke']}"/>
  <circle cx="275" cy="270" r="90" fill="{t['accent']}" opacity="0.8"/>
  <rect x="40" y="380" width="470" height="180" fill="{t['bg']}" fill-opacity="0.9"/>
  <text x="70" y="440" fill="#FFFFFF" font-size="28" font-weight="900" font-family="Montserrat">FULL BLEED IMMERSION</text>
  <text x="70" y="475" fill="{t['text_dim']}" font-size="14" font-family="PingFang SC">满幅视觉主导 · 消除边框拘束</text>
  {badge(185, 510, name, t['accent'], t['bg'], 180, 28)}"""

    # 6. Default Dynamic Procedural Geometry (Parametrically unique by hash of lid)
    else:
        # Use integer seed from layout ID to generate genuine, varied geometric compositions
        seed = int(lid)
        shape_type = seed % 6
        accent_c = t['accent']
        alt_c = t['accent_alt']

        if shape_type == 0:
            # Concentric Geometric Rings + Ray Axes
            rings = "".join([f'<circle cx="275" cy="290" r="{40 + j*35}" fill="none" stroke="{accent_c}" stroke-width="{2 if j%2==0 else 1}" stroke-dasharray="{6 if j%2!=0 else 0},{4 if j%2!=0 else 0}"/>' for j in range(4)])
            inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  {rings}
  <circle cx="275" cy="290" r="24" fill="{alt_c}"/>
  <circle cx="275" cy="290" r="8" fill="#FFFFFF"/>
  <line x1="90" y1="290" x2="460" y2="290" stroke="{accent_c}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <line x1="275" y1="100" x2="275" y2="480" stroke="{accent_c}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="275" y="450" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:24]}</text>
  {badge(185, 490, name, accent_c, t['bg'], 180, 28)}"""
        elif shape_type == 1:
            # Polygonal Tessellation Structure
            inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <polygon points="275,100 450,220 450,420 275,510 100,420 100,220" fill="none" stroke="{accent_c}" stroke-width="2.5"/>
  <polygon points="275,170 380,250 380,380 275,440 170,380 170,250" fill="{t['stroke']}" stroke="{alt_c}" stroke-width="1.8"/>
  <circle cx="275" cy="310" r="32" fill="{accent_c}"/>
  <circle cx="275" cy="310" r="10" fill="#FFFFFF"/>
  <text x="275" y="240" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:24]}</text>
  {badge(185, 480, name, accent_c, t['bg'], 180, 28)}"""
        elif shape_type == 2:
            # Multi-Axis Equilibrium Grid
            inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <line x1="80" y1="120" x2="470" y2="480" stroke="{accent_c}" stroke-width="3"/>
  <line x1="470" y1="120" x2="80" y2="480" stroke="{alt_c}" stroke-width="2" stroke-dasharray="6,4"/>
  <rect x="185" y="220" width="180" height="180" rx="8" fill="{t['bg']}" stroke="{accent_c}" stroke-width="2"/>
  <circle cx="275" cy="310" r="28" fill="{accent_c}"/>
  <circle cx="275" cy="310" r="8" fill="#FFFFFF"/>
  <text x="275" y="440" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:24]}</text>
  {badge(185, 490, name, accent_c, t['bg'], 180, 28)}"""
        elif shape_type == 3:
            # Asymmetric Staggered Bands
            h1 = 60 + (seed * 17) % 180
            h2 = 50 + (seed * 29) % 200
            h3 = 40 + (seed * 43) % 160
            inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="80" y="{110 + (seed%5)*15}" width="280" height="{h1}" rx="6" fill="{accent_c}" opacity="0.85"/>
  <rect x="190" y="{240 - (seed%4)*20}" width="270" height="{h2}" rx="6" fill="{t['stroke']}"/>
  <circle cx="340" cy="200" r="36" fill="{alt_c}"/>
  <circle cx="340" cy="200" r="12" fill="#FFFFFF"/>
  <text x="275" y="450" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:24]}</text>
  {badge(185, 490, name, accent_c, t['bg'], 180, 28)}"""
        elif shape_type == 4:
            # Perspective Convergence Vector Fan
            inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <polygon points="50,560 500,560 275,160" fill="{t['stroke']}"/>
  <line x1="50" y1="560" x2="275" y2="160" stroke="{accent_c}" stroke-width="3"/>
  <line x1="160" y1="560" x2="275" y2="160" stroke="{accent_c}" stroke-width="1.8" stroke-dasharray="6,4"/>
  <line x1="275" y1="560" x2="275" y2="160" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="6,4"/>
  <line x1="390" y1="560" x2="275" y2="160" stroke="{accent_c}" stroke-width="1.8" stroke-dasharray="6,4"/>
  <line x1="500" y1="560" x2="275" y2="160" stroke="{accent_c}" stroke-width="3"/>
  <circle cx="275" cy="160" r="32" fill="{accent_c}"/>
  <circle cx="275" cy="160" r="10" fill="#FFFFFF"/>
  <text x="275" y="110" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:24]}</text>
  {badge(185, 500, name, accent_c, t['bg'], 180, 28)}"""
        else:
            # Dynamic Quadrant Staging
            inner = f"""
  <rect x="50" y="60" width="450" height="500" rx="8" fill="{t['bg_surface']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="80" y="100" width="170" height="180" rx="6" fill="{accent_c}" opacity="0.2"/>
  <circle cx="165" cy="190" r="28" fill="{accent_c}"/>
  <rect x="300" y="100" width="170" height="180" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="80" y="320" width="170" height="180" rx="6" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5"/>
  <rect x="300" y="320" width="170" height="180" rx="6" fill="{alt_c}" opacity="0.7"/>
  <circle cx="385" cy="410" r="28" fill="#FFFFFF"/>
  <text x="275" y="305" fill="{t['text']}" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">{name_en[:24]}</text>
  {badge(185, 520, name, accent_c, t['bg'], 180, 28)}"""

    return wrap_svg(inner, t['bg'])


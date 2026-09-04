"""
SVG generators for Category 06: 影视镜头视听语言与调度 (301-314).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_301(): # 单人构图 (Solo Character)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- 2.39:1 Cinematic Letterbox -->
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <!-- Top and Bottom Mask -->
  <rect x="40" y="60" width="470" height="60" fill="#000000"/>
  <rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Solitary Subject at 1/3 vertical line -->
  <line x1="196" y1="120" x2="196" y2="500" stroke="{t['guide']}" stroke-width="1.2" stroke-dasharray="6,4"/>
  <circle cx="196" cy="260" r="38" fill="{t['accent']}"/>
  <circle cx="196" cy="260" r="10" fill="#FFFFFF"/>
  <path d="M 140 400 Q 196 340 252 400 L 260 500 L 130 500 Z" fill="{t['stroke']}"/>
  <!-- Vast Negative Space on Right (Looking Room) -->
  <line x1="215" y1="260" x2="440" y2="260" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="6,4"/>
  <polygon points="440,260 425,252 425,268" fill="{t['accent_alt']}"/>
  <text x="340" y="245" fill="{t['accent_alt']}" font-size="12" font-family="Montserrat">LOOKING ROOM</text>
  {badge(185, 520, "单人主体与视线留白", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_302(): # 双人对峙镜头 (Two-Shot Dynamic Confrontation)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Left Actor -->
  <path d="M 60 500 L 140 500 Q 180 380 180 280 Q 180 220 150 200 Q 120 200 120 240 L 60 260 Z" fill="{t['stroke']}"/>
  <circle cx="150" cy="240" r="5" fill="{t['accent']}"/>
  <!-- Right Actor -->
  <path d="M 490 500 L 410 500 Q 370 380 370 280 Q 370 220 400 200 Q 430 200 430 240 L 490 260 Z" fill="{t['stroke']}"/>
  <circle cx="400" cy="240" r="5" fill="{t['accent']}"/>
  <line x1="155" y1="240" x2="395" y2="240" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <circle cx="275" cy="240" r="14" fill="{t['danger']}"/>
  {badge(185, 520, "双人对峙张力中线", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_303(): # 三人构图 (Three-Shot Triangle Staging)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Tension Triangle connecting 3 characters -->
  <polygon points="275,200 150,380 400,380" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Character 1 Apex Authority -->
  <circle cx="275" cy="200" r="32" fill="{t['accent']}"/>
  <circle cx="275" cy="200" r="8" fill="#FFFFFF"/>
  <!-- Character 2 Left -->
  <circle cx="150" cy="380" r="26" fill="{t['accent_alt']}"/>
  <!-- Character 3 Right -->
  <circle cx="400" cy="380" r="26" fill="{t['accent_alt']}"/>
  <text x="275" y="320" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">TRIANGLE STAGING</text>
  {badge(185, 520, "三人三角权力位阶", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_304(): # 群像构图 (Ensemble Tableau)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Staging Arch Guide -->
  <path d="M 80 400 Q 275 220 470 400" fill="none" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- 7 Ensemble Characters positioned along arc -->
  <g fill="{t['stroke']}">
    <circle cx="90" cy="390" r="20"/><circle cx="150" cy="330" r="24"/>
    <circle cx="215" cy="280" r="28" fill="{t['accent_alt']}"/>
    <circle cx="275" cy="250" r="34" fill="{t['accent']}"/><circle cx="275" cy="250" r="10" fill="#FFFFFF"/>
    <circle cx="335" cy="280" r="28" fill="{t['accent_alt']}"/>
    <circle cx="400" cy="330" r="24"/><circle cx="460" cy="390" r="20"/>
  </g>
  {badge(185, 520, "群像人物多重视角排布", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_305(): # 过肩构图 (Over-The-Shoulder OTS)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Blurred Foreground Shoulder on Left -->
  <path d="M 40 320 Q 160 300 180 420 L 190 500 L 40 500 Z" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="2"/>
  <circle cx="110" cy="250" r="48" fill="{t['bg']}" stroke="{t['guide']}" stroke-width="2"/>
  <text x="110" y="380" fill="{t['text_dim']}" font-size="11" font-family="Montserrat" text-anchor="middle">FOREGROUND (DEFOCUSED)</text>
  <!-- In-Focus Conversationalist in Center-Right -->
  <circle cx="350" cy="280" r="38" fill="{t['accent']}"/>
  <circle cx="350" cy="280" r="10" fill="#FFFFFF"/>
  <path d="M 290 440 Q 350 370 410 440 L 420 500 L 280 500 Z" fill="{t['accent_alt']}" opacity="0.5"/>
  <line x1="158" y1="250" x2="340" y2="275" stroke="{t['danger']}" stroke-width="2" stroke-dasharray="6,4"/>
  {badge(185, 520, "经典过肩对话视线纵深", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_306(): # 主观视角构图 (POV Subjective Shot)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Viewfinder reticle brackets -->
  <path d="M 90 190 L 90 160 L 120 160 M 460 160 L 430 160 M 460 160 L 460 190 M 90 430 L 90 460 L 120 460 M 460 460 L 430 460 M 460 460 L 460 430" stroke="{t['danger']}" stroke-width="2.5" fill="none"/>
  <!-- Center Crosshairs -->
  <line x1="230" y1="310" x2="320" y2="310" stroke="{t['danger']}" stroke-width="1.5"/>
  <line x1="275" y1="265" x2="275" y2="355" stroke="{t['danger']}" stroke-width="1.5"/>
  <circle cx="275" cy="310" r="40" fill="none" stroke="{t['danger']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="275" cy="310" r="8" fill="{t['accent']}"/>
  <text x="275" y="200" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">FIRST-PERSON POV</text>
  {badge(185, 520, "第一人称主观代入镜头", t['danger'], "#FFFFFF", 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_307(): # 客观视角构图 (Objective Wide Shot)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Wide architectural space with detached miniature figures -->
  <line x1="40" y1="400" x2="510" y2="400" stroke="{t['accent']}" stroke-width="2"/>
  <rect x="90" y="200" width="120" height="200" fill="{t['stroke']}" opacity="0.5"/>
  <rect x="340" y="160" width="130" height="240" fill="{t['stroke']}" opacity="0.5"/>
  <!-- Neutral tiny spectators on ground -->
  <circle cx="250" cy="385" r="10" fill="{t['accent']}"/>
  <circle cx="290" cy="385" r="10" fill="{t['accent_alt']}"/>
  <text x="275" y="160" fill="{t['text_dim']}" font-size="13" font-family="Montserrat" text-anchor="middle">IMPARTIAL SPECTATOR DISTANCE</text>
  {badge(185, 520, "第三人称客观旁观视角", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_308(): # 净单人镜头 (Clean Single)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Perfectly clean frame, zero foreground intrusion -->
  <circle cx="275" cy="280" r="55" fill="{t['accent']}"/>
  <circle cx="275" cy="280" r="16" fill="#FFFFFF"/>
  <path d="M 190 450 Q 275 370 360 450 L 380 500 L 170 500 Z" fill="{t['accent_alt']}" opacity="0.6"/>
  <!-- Purity guide boundary -->
  <rect x="160" y="200" width="230" height="300" fill="none" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4,4"/>
  {badge(185, 520, "无干扰纯净单人特写", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_309(): # 脏单人镜头 (Dirty Single)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Foreground head silhouette clipping the edge (The 'Dirty' element) -->
  <path d="M 40 220 Q 140 240 150 360 L 160 500 L 40 500 Z" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <circle cx="80" cy="190" r="45" fill="{t['bg']}" stroke="{t['danger']}" stroke-width="2"/>
  <text x="100" y="460" fill="{t['danger']}" font-size="11" font-family="Montserrat">DIRTY FOREGROUND</text>
  <!-- In-focus actor in midground -->
  <circle cx="330" cy="280" r="48" fill="{t['accent']}"/>
  <circle cx="330" cy="280" r="14" fill="#FFFFFF"/>
  <path d="M 260 440 Q 330 370 400 440 L 410 500 L 250 500 Z" fill="{t['stroke']}"/>
  {badge(185, 520, "带前景干扰带肩单人镜头", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_310(): # 深度调度 (Deep Staging / Z-Axis Depth)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Z-Axis vector receding into tunnel -->
  <line x1="110" y1="480" x2="275" y2="200" stroke="{t['accent']}" stroke-width="3" stroke-dasharray="6,4"/>
  <!-- Foreground character (Large) -->
  <circle cx="110" cy="440" r="38" fill="{t['accent']}"/>
  <!-- Midground character (Medium) -->
  <circle cx="190" cy="320" r="22" fill="{t['accent_alt']}"/>
  <!-- Background character (Tiny) -->
  <circle cx="275" cy="200" r="12" fill="{t['danger']}"/>
  <text x="370" y="205" fill="{t['danger']}" font-size="12" font-family="Montserrat">BACKGROUND ACTOR</text>
  <text x="275" y="150" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">Z-AXIS DEEP CHOREOGRAPHY</text>
  {badge(185, 520, "Z轴纵深多层场面调度", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_311(): # 平面调度 (Planar Staging)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Wes Anderson Style 2D Horizontal Flat Runway -->
  <line x1="40" y1="430" x2="510" y2="430" stroke="{t['accent']}" stroke-width="3"/>
  <!-- 4 Characters strictly standing side by side on same frontal plane -->
  <g fill="{t['accent']}">
    <circle cx="120" cy="340" r="24"/><rect x="105" y="370" width="30" height="60" rx="3" fill="{t['stroke']}"/>
    <circle cx="220" cy="340" r="24" fill="{t['accent_alt']}"/><rect x="205" y="370" width="30" height="60" rx="3" fill="{t['stroke']}"/>
    <circle cx="330" cy="340" r="24" fill="{t['danger']}"/><rect x="315" y="370" width="30" height="60" rx="3" fill="{t['stroke']}"/>
    <circle cx="430" cy="340" r="24"/><rect x="415" y="370" width="30" height="60" rx="3" fill="{t['stroke']}"/>
  </g>
  <text x="275" y="180" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">WES ANDERSON 2D LATERAL TABLEAU</text>
  {badge(185, 520, "横向二维平面扁平调度", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_312(): # 三角调度 (Triangular Staging)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Dynamic Staging Triangle -->
  <polygon points="275,180 140,420 410,420" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4"/>
  <circle cx="275" cy="180" r="28" fill="{t['danger']}"/>
  <circle cx="140" cy="420" r="28" fill="{t['accent']}"/>
  <circle cx="410" cy="420" r="28" fill="{t['accent_alt']}"/>
  <text x="275" y="310" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">POWER DYNAMIC TRIANGLE</text>
  {badge(185, 520, "三角站位戏剧性张力", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_313(): # 横向调度 (Lateral Tracking Shot)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Camera Dolly Tracking Rail Line -->
  <line x1="60" y1="450" x2="490" y2="450" stroke="{t['danger']}" stroke-width="4"/>
  <!-- Motion Track Vector Arrows -->
  <line x1="120" y1="320" x2="380" y2="320" stroke="{t['accent']}" stroke-width="3" stroke-dasharray="8,6"/>
  <polygon points="380,320 365,312 365,328" fill="{t['accent']}"/>
  <circle cx="250" cy="320" r="34" fill="{t['accent']}"/>
  <circle cx="250" cy="320" r="10" fill="#FFFFFF"/>
  <text x="275" y="200" fill="{t['text']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">HORIZONTAL TRACKING DOLLY</text>
  {badge(185, 520, "横向平移轨道运动调度", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_314(): # 多层前景调度 (Multi-Layer Foreground Staging)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="40" y="120" width="470" height="380" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2" rx="6"/>
  <rect x="40" y="60" width="470" height="60" fill="#000000"/><rect x="40" y="500" width="470" height="60" fill="#000000"/>
  <!-- Deep Background Subject -->
  <circle cx="275" cy="310" r="32" fill="{t['accent']}"/>
  <circle cx="275" cy="310" r="8" fill="#FFFFFF"/>
  <!-- Foreground Venetian Blinds / Screen Slats -->
  <g fill="{t['bg']}" stroke="{t['guide']}" stroke-width="1.5">
    {''.join([f'<rect x="40" y="{140 + i*36}" width="470" height="18"/>' for i in range(10)])}
  </g>
  <text x="275" y="190" fill="{t['danger']}" font-size="14" font-weight="bold" font-family="Montserrat" text-anchor="middle">PEEKING THROUGH FOREGROUND SLATS</text>
  {badge(185, 520, "多层隔栅前景窥探调度", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat06
CAT06_SVGS = {
    "301": gen_301, "302": gen_302, "303": gen_303, "304": gen_304, "305": gen_305,
    "306": gen_306, "307": gen_307, "308": gen_308, "309": gen_309, "310": gen_310,
    "311": gen_311, "312": gen_312, "313": gen_313, "314": gen_314
}

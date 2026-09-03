"""
Rich, bespoke SVG composition visuals for 350 layout series.
Each visual features authentic geometric framing, iconic thematic illustration,
and precise composition guides.
"""

def get_svg_001():
    # Rule of Thirds (三分法)
    return """
    <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="sunGlowRed" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#E25238" stop-opacity="0.8"/>
          <stop offset="40%" stop-color="#E25238" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#E25238" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="mountGradWarm" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#555047"/>
          <stop offset="100%" stop-color="#22201D"/>
        </linearGradient>
      </defs>
      <rect width="550" height="620" fill="#24211E" rx="8"/>
      <!-- Water waves -->
      <line x1="0" y1="510" x2="550" y2="510" stroke="#3A3630" stroke-width="1.5"/>
      <path d="M 20 545 Q 90 550 160 545 T 300 545 T 440 545 T 530 545" stroke="#E25238" stroke-width="1.2" fill="none" opacity="0.3"/>
      <path d="M 40 575 Q 110 580 180 575 T 320 575 T 460 575 T 520 575" stroke="#E25238" stroke-width="1.2" fill="none" opacity="0.2"/>
      <!-- Mountain silhouettes -->
      <polygon points="60,510 190,320 320,510" fill="url(#mountGradWarm)"/>
      <polygon points="210,510 330,370 450,510" fill="#3D3A34" opacity="0.9"/>
      <polygon points="145,385 190,320 235,385" fill="#FFFFFF" opacity="0.85"/>
      <!-- Thirds Grid lines -->
      <line x1="183.3" y1="50" x2="183.3" y2="570" stroke="#E25238" stroke-width="1.8" stroke-dasharray="6,6" opacity="0.75"/>
      <line x1="366.6" y1="50" x2="366.6" y2="570" stroke="#E25238" stroke-width="1.8" stroke-dasharray="6,6" opacity="0.75"/>
      <line x1="40" y1="206.6" x2="510" y2="206.6" stroke="#E25238" stroke-width="1.8" stroke-dasharray="6,6" opacity="0.75"/>
      <line x1="40" y1="413.3" x2="510" y2="413.3" stroke="#E25238" stroke-width="1.8" stroke-dasharray="6,6" opacity="0.75"/>
      <!-- Intersection anchors -->
      <circle cx="366.6" cy="206.6" r="6" fill="#E25238"/>
      <circle cx="183.3" cy="413.3" r="6" fill="#E25238"/>
      <circle cx="366.6" cy="413.3" r="6" fill="#E25238"/>
      <!-- Primary Focal Anchor (Upper Left Third) -->
      <circle cx="183.3" cy="206.6" r="65" fill="url(#sunGlowRed)"/>
      <circle cx="183.3" cy="206.6" r="30" stroke="#E25238" stroke-width="1.5" fill="none" stroke-dasharray="4,4"/>
      <circle cx="183.3" cy="206.6" r="14" fill="#E25238"/>
      <circle cx="183.3" cy="206.6" r="4" fill="#FFFFFF"/>
      <rect x="110" y="130" width="146" height="30" rx="6" fill="#E25238"/>
      <text x="183" y="150" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">视觉主角 · 黄金交点</text>
    </svg>
    """


def get_svg_002():
    # Golden Ratio (黄金比例构图)
    return """
    <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="goldPointGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#D4AF37" stop-opacity="0.9"/>
          <stop offset="40%" stop-color="#D4AF37" stop-opacity="0.3"/>
          <stop offset="100%" stop-color="#D4AF37" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="mountGradForest" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#2D5A4C"/>
          <stop offset="100%" stop-color="#0E2E24"/>
        </linearGradient>
      </defs>
      <rect width="550" height="620" fill="#072018" rx="8"/>

      <!-- Golden Dimension top bar (1.618) -->
      <line x1="50" y1="80" x2="500" y2="80" stroke="#D4AF37" stroke-width="1.5"/>
      <line x1="50" y1="73" x2="50" y2="87" stroke="#D4AF37" stroke-width="1.5"/>
      <line x1="500" y1="73" x2="500" y2="87" stroke="#D4AF37" stroke-width="1.5"/>
      <text x="275" y="72" fill="#D4AF37" font-size="14" font-weight="800" font-family="Montserrat" text-anchor="middle">1.618</text>

      <!-- Golden Dimension right bar (1.0) -->
      <line x1="520" y1="100" x2="520" y2="480" stroke="#D4AF37" stroke-width="1.5"/>
      <line x1="513" y1="100" x2="527" y2="100" stroke="#D4AF37" stroke-width="1.5"/>
      <line x1="513" y1="480" x2="527" y2="480" stroke="#D4AF37" stroke-width="1.5"/>
      <text x="536" y="295" fill="#D4AF37" font-size="14" font-weight="800" font-family="Montserrat" text-anchor="middle">1</text>

      <!-- Main Golden Rectangle Outer Frame (450 x 380) -->
      <rect x="50" y="100" width="450" height="380" fill="none" stroke="#D4AF37" stroke-width="2.5" rx="4"/>

      <!-- Scenery inside Golden Rectangle -->
      <g clip-path="url(#goldenClip)">
        <clipPath id="goldenClip">
          <rect x="51" y="101" width="448" height="378" rx="3"/>
        </clipPath>
        <!-- Mist mountain inside -->
        <polygon points="50,480 210,250 360,480" fill="url(#mountGradForest)"/>
        <polygon points="170,310 210,250 250,310" fill="#FFFFFF" opacity="0.85"/>
        <polygon points="260,480 370,290 480,480" fill="#1A4337" opacity="0.8"/>
        <!-- Flowing river -->
        <path d="M 50 430 Q 200 450 328 335 T 500 410" stroke="#D4AF37" stroke-width="1.5" fill="none" stroke-dasharray="4,4" opacity="0.4"/>
      </g>

      <!-- Vertical Golden Divider (x = 50 + 450 * 0.618 = 328.1) -->
      <line x1="328.1" y1="100" x2="328.1" y2="480" stroke="#D4AF37" stroke-width="2" stroke-dasharray="6,5"/>

      <!-- Horizontal Golden Divider (y = 100 + 380 * 0.618 = 334.8) -->
      <line x1="50" y1="334.8" x2="500" y2="334.8" stroke="#D4AF37" stroke-width="2" stroke-dasharray="6,5"/>

      <!-- Golden Section Intersection Point (328.1, 334.8) -->
      <circle cx="328.1" cy="334.8" r="60" fill="url(#goldPointGlow)"/>
      <circle cx="328.1" cy="334.8" r="24" stroke="#FFFFFF" stroke-width="2" fill="none" stroke-dasharray="4,4"/>
      <circle cx="328.1" cy="334.8" r="14" fill="#D4AF37"/>
      <circle cx="328.1" cy="334.8" r="4" fill="#072018"/>

      <rect x="345" y="345" width="105" height="26" rx="4" fill="#0D2D23" stroke="#D4AF37" stroke-width="1"/>
      <text x="397" y="362" fill="#D4AF37" font-size="11" font-weight="bold" font-family="PingFang SC" text-anchor="middle">黄金分割点</text>

      <!-- Bottom Proportion Blocks -->
      <!-- Major 1.618 Block (Width 278, Height 70) -->
      <rect x="50" y="500" width="278" height="72" rx="4" fill="#E8DFCE"/>
      <text x="189" y="534" fill="#09241C" font-size="24" font-weight="900" font-family="Montserrat" text-anchor="middle">1.618</text>
      <text x="189" y="555" fill="#4B473F" font-size="12" font-weight="800" font-family="PingFang SC" text-anchor="middle">大部分 · MAJOR</text>

      <!-- Minor 1.0 Block (Width 172, Height 70) -->
      <rect x="328" y="500" width="172" height="72" rx="4" fill="#0E3327" stroke="#D4AF37" stroke-width="1.5"/>
      <text x="414" y="534" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Montserrat" text-anchor="middle">1</text>
      <text x="414" y="555" fill="#D4AF37" font-size="12" font-weight="800" font-family="PingFang SC" text-anchor="middle">小部分 · MINOR</text>
    </svg>
    """


def get_svg_003():
    # Golden Spiral (黄金螺旋构图)
    return """
    <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="spiralGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#FFD000" stop-opacity="0.95"/>
          <stop offset="45%" stop-color="#FFD000" stop-opacity="0.3"/>
          <stop offset="100%" stop-color="#FFD000" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <rect width="550" height="620" fill="#0A1838" rx="8"/>
      <!-- Starry sky particles -->
      <circle cx="80" cy="120" r="1.5" fill="#FFFFFF" opacity="0.7"/>
      <circle cx="210" cy="95" r="2" fill="#FFFFFF" opacity="0.8"/>
      <circle cx="480" cy="140" r="1.5" fill="#FFFFFF" opacity="0.6"/>
      <circle cx="450" cy="380" r="2" fill="#FFFFFF" opacity="0.8"/>
      <circle cx="120" cy="460" r="1.5" fill="#FFFFFF" opacity="0.7"/>

      <!-- Fibonacci Nested Rectangles -->
      <g stroke="#FFD000" stroke-width="1.5" fill="none" opacity="0.45">
        <rect x="40" y="80" width="460" height="460" rx="4"/>
        <line x1="324.3" y1="80" x2="324.3" y2="540"/>
        <line x1="324.3" y1="364.3" x2="500" y2="364.3"/>
        <line x1="391.3" y1="80" x2="391.3" y2="364.3"/>
        <line x1="324.3" y1="188.3" x2="391.3" y2="188.3"/>
      </g>

      <!-- Golden Spiral Curve -->
      <path d="M 40 540 A 460 460 0 0 1 500 80 A 284.3 284.3 0 0 1 324.3 364.3 A 175.7 175.7 0 0 1 391.3 188.3 A 108 108 0 0 1 349 230"
            stroke="#FFD000" stroke-width="4.5" fill="none" stroke-linecap="round"/>

      <!-- Secondary guide vector -->
      <line x1="40" y1="540" x2="366" y2="215" stroke="#8BB6F9" stroke-width="1.8" stroke-dasharray="6,6" opacity="0.6"/>

      <!-- Focal Whirl Center (366, 215) -->
      <circle cx="366" cy="215" r="60" fill="url(#spiralGlow)"/>
      <circle cx="366" cy="215" r="22" stroke="#FFFFFF" stroke-width="2" fill="none"/>
      <circle cx="366" cy="215" r="12" fill="#FFD000"/>
      <circle cx="366" cy="215" r="3.5" fill="#0A1838"/>

      <rect x="250" y="160" width="100" height="28" rx="4" fill="#082154" stroke="#FFD000" stroke-width="1.2"/>
      <text x="300" y="179" fill="#FFD000" font-size="11" font-weight="900" font-family="PingFang SC" text-anchor="middle">螺旋汇聚极点</text>

      <text x="275" y="575" fill="#FFD000" font-size="14" font-weight="bold" font-family="PingFang SC" text-anchor="middle">
        斐波那契黄金螺旋 · 引导视觉汇聚核心
      </text>
    </svg>
    """


def get_svg_004():
    # Golden Triangle (黄金三角构图)
    return """
    <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="sunGold" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#FFD000" stop-opacity="0.8"/>
          <stop offset="40%" stop-color="#FFD000" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#FFD000" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="mountGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#8BB6F9"/>
          <stop offset="100%" stop-color="#1B428A"/>
        </linearGradient>
      </defs>
      <rect width="550" height="620" fill="#071E4D" rx="8"/>
      <line x1="0" y1="520" x2="550" y2="520" stroke="#1C448D" stroke-width="1.5" />
      <line x1="20" y1="550" x2="530" y2="550" stroke="#1C448D" stroke-width="1.2" stroke-dasharray="8,8" />
      <polygon points="120,530 260,330 400,530" fill="#133674" />
      <polygon points="40,530 180,380 320,530" fill="url(#mountGrad)" opacity="0.9" />
      <polygon points="140,430 180,380 220,430" fill="#FFFFFF" opacity="0.9" />
      <polygon points="200,530 330,280 460,530" fill="#3A6EC7" />
      <polygon points="280,360 330,280 375,360" fill="#FFFFFF" />
      <g transform="translate(380, 460)">
        <polygon points="20,0 20,-48 44,0" fill="#FFFFFF"/>
        <polygon points="16,0 16,-40 -2,0" fill="#D6E4FF"/>
        <polygon points="-8,3 48,3 38,12 2,12" fill="#FFD000"/>
      </g>
      <line x1="30" y1="530" x2="480" y2="90" stroke="#FFD000" stroke-width="3.5" stroke-linecap="round"/>
      <polygon points="480,90 462,108 478,114" fill="#FFD000"/>
      <line x1="480" y1="530" x2="365" y2="205" stroke="#FFD000" stroke-width="3" stroke-linecap="round"/>
      <rect x="30" y="90" width="450" height="440" stroke="rgba(255, 208, 0, 0.4)" stroke-width="1.2" stroke-dasharray="4,4" fill="none"/>
      <circle cx="365" cy="205" r="64" fill="url(#sunGold)"/>
      <circle cx="365" cy="205" r="22" stroke="#FFFFFF" stroke-width="2" fill="#FFFFFF"/>
      <line x1="365" y1="180" x2="365" y2="230" stroke="#0B2B68" stroke-width="2"/>
      <line x1="340" y1="205" x2="390" y2="205" stroke="#0B2B68" stroke-width="2"/>
      <text x="140" y="290" fill="#FFD000" font-size="12" font-weight="600" font-family="PingFang SC" transform="rotate(-44 140 290)">
        主对角动态引导线 · 牵引视线自下而上
      </text>
    </svg>
    """


def get_svg_005():
    # Diagonal Method (对角线法构图)
    return """
    <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="diagSky" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#1F2A44"/>
          <stop offset="100%" stop-color="#0B132B"/>
        </linearGradient>
      </defs>
      <rect width="550" height="620" fill="url(#diagSky)" rx="8"/>
      <!-- Diagonal Perspective Road / Bridge -->
      <polygon points="0,620 550,150 550,220 0,620" fill="#E25238" opacity="0.3"/>
      <line x1="0" y1="620" x2="550" y2="150" stroke="#E25238" stroke-width="5" stroke-linecap="round"/>
      <line x1="0" y1="570" x2="550" y2="230" stroke="#E25238" stroke-width="2" stroke-dasharray="8,6"/>
      <line x1="0" y1="520" x2="550" y2="310" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.5"/>
      <!-- Diagonal speed markers -->
      <line x1="120" y1="620" x2="120" y2="520" stroke="#E25238" stroke-width="2"/>
      <line x1="250" y1="620" x2="250" y2="410" stroke="#E25238" stroke-width="2"/>
      <line x1="380" y1="620" x2="380" y2="300" stroke="#E25238" stroke-width="2"/>
      <!-- Dynamic focal element at upper right -->
      <circle cx="460" cy="225" r="28" fill="#E25238"/>
      <circle cx="460" cy="225" r="10" fill="#FFFFFF"/>
      <text x="320" y="380" fill="#FFFFFF" font-size="13" font-weight="bold" font-family="PingFang SC" transform="rotate(-38 320 380)">
        倾斜动势 · 突破水平沉闷
      </text>
    </svg>
    """


def get_svg_084():
    # Deep Focus (深焦构图)
    return """
    <div style="position: relative; width: 100%; height: 100%; border-radius: 6px; overflow: hidden; border: 1px solid rgba(212, 231, 81, 0.25);">
      <img src="file:///Users/clawbot/Projects/350-layout-skill/assets/084_landscape.png" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
      <svg viewBox="0 0 530 660" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;">
        <line x1="0" y1="120" x2="270" y2="120" stroke="#D4E751" stroke-width="2" stroke-dasharray="5,4" />
        <circle cx="270" cy="120" r="14" fill="rgba(212,231,81,0.3)" />
        <circle cx="270" cy="120" r="6" fill="none" stroke="#D4E751" stroke-width="2" />
        <circle cx="270" cy="120" r="2.5" fill="#D4E751" />

        <line x1="0" y1="365" x2="230" y2="365" stroke="#D4E751" stroke-width="2" stroke-dasharray="5,4" />
        <circle cx="230" cy="365" r="14" fill="rgba(212,231,81,0.3)" />
        <circle cx="230" cy="365" r="6" fill="none" stroke="#D4E751" stroke-width="2" />
        <circle cx="230" cy="365" r="2.5" fill="#D4E751" />

        <line x1="0" y1="580" x2="245" y2="580" stroke="#D4E751" stroke-width="2" stroke-dasharray="5,4" />
        <circle cx="245" cy="580" r="14" fill="rgba(212,231,81,0.3)" />
        <circle cx="245" cy="580" r="6" fill="none" stroke="#D4E751" stroke-width="2" />
        <circle cx="245" cy="580" r="2.5" fill="#D4E751" />
      </svg>
    </div>
    """


def get_svg_134():
    # Multi-Column Layout (多栏版式)
    return """
    <svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
      <rect width="550" height="620" fill="#0A2C21" rx="8"/>
      <!-- 4 Columns Architecture -->
      <!-- Col 1: Grid -->
      <g transform="translate(30, 60)">
        <rect width="105" height="420" rx="4" fill="none" stroke="#D4E751" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
        <text x="52" y="30" fill="#D4E751" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">栅格</text>
        <text x="52" y="46" fill="#A3B8AD" font-size="9" font-family="Montserrat" text-anchor="middle">GRID</text>
        <!-- 3x4 block grid inside -->
        <g stroke="#D4E751" stroke-width="1" fill="none" opacity="0.8">
          <rect x="12" y="70" width="80" height="100" rx="2"/>
          <line x1="12" y1="95" x2="92" y2="95"/>
          <line x1="12" y1="120" x2="92" y2="120"/>
          <line x1="12" y1="145" x2="92" y2="145"/>
          <line x1="38" y1="70" x2="38" y2="170"/>
          <line x1="65" y1="70" x2="65" y2="170"/>
        </g>
        <line x1="12" y1="210" x2="92" y2="210" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="12" y1="225" x2="80" y2="225" stroke="#A3B8AD" stroke-width="1.5"/>
        <line x1="12" y1="238" x2="88" y2="238" stroke="#A3B8AD" stroke-width="1.5"/>
      </g>

      <!-- Col 2: Module -->
      <g transform="translate(150, 60)">
        <rect width="105" height="420" rx="4" fill="none" stroke="#D4E751" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
        <text x="52" y="30" fill="#D4E751" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">模块</text>
        <text x="52" y="46" fill="#A3B8AD" font-size="9" font-family="Montserrat" text-anchor="middle">MODULE</text>
        <rect x="12" y="70" width="80" height="45" rx="3" fill="#D4E751" opacity="0.3"/>
        <circle cx="32" cy="92" r="12" fill="#D4AF37"/>
        <line x1="50" y1="88" x2="84" y2="88" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="50" y1="96" x2="75" y2="96" stroke="#A3B8AD" stroke-width="1.5"/>
        <rect x="12" y="130" width="80" height="35" rx="3" fill="#D4AF37"/>
        <line x1="12" y1="190" x2="92" y2="190" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="12" y1="205" x2="70" y2="205" stroke="#A3B8AD" stroke-width="1.5"/>
      </g>

      <!-- Col 3: Density -->
      <g transform="translate(270, 60)">
        <rect width="105" height="420" rx="4" fill="none" stroke="#D4E751" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
        <text x="52" y="30" fill="#D4E751" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">密度</text>
        <text x="52" y="46" fill="#A3B8AD" font-size="9" font-family="Montserrat" text-anchor="middle">DENSITY</text>
        <rect x="12" y="70" width="80" height="70" rx="3" fill="none" stroke="#D4E751" stroke-width="1"/>
        <circle cx="32" cy="95" r="10" fill="#133674"/>
        <line x1="48" y1="90" x2="84" y2="90" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="48" y1="100" x2="76" y2="100" stroke="#A3B8AD" stroke-width="1.5"/>
        <line x1="12" y1="170" x2="92" y2="170" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="12" y1="185" x2="80" y2="185" stroke="#A3B8AD" stroke-width="1.5"/>
      </g>

      <!-- Col 4: Organization -->
      <g transform="translate(390, 60)">
        <rect width="105" height="420" rx="4" fill="none" stroke="#D4E751" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.6"/>
        <text x="52" y="30" fill="#D4E751" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">组织</text>
        <text x="52" y="46" fill="#A3B8AD" font-size="9" font-family="Montserrat" text-anchor="middle">ORDER</text>
        <rect x="12" y="70" width="80" height="90" rx="3" fill="none" stroke="#D4AF37" stroke-width="1"/>
        <rect x="18" y="76" width="68" height="35" rx="2" fill="#D4AF37"/>
        <line x1="18" y1="122" x2="86" y2="122" stroke="#FFFFFF" stroke-width="2"/>
        <line x1="18" y1="134" x2="70" y2="134" stroke="#A3B8AD" stroke-width="1.5"/>
        <line x1="18" y1="146" x2="80" y2="146" stroke="#A3B8AD" stroke-width="1.5"/>
      </g>

      <!-- Reading Flow path -->
      <path d="M 80 150 Q 210 130 320 200 T 440 200" fill="none" stroke="#D4E751" stroke-width="2.5" stroke-dasharray="5,4"/>
      <polygon points="445,200 435,195 435,205" fill="#D4E751"/>

      <!-- Bottom Bar -->
      <rect x="30" y="520" width="465" height="46" rx="4" fill="#0F382B" stroke="#D4E751" stroke-width="1"/>
      <text x="262" y="548" fill="#D4E751" font-size="14" font-weight="900" font-family="PingFang SC" text-anchor="middle">
        模块化 · 秩序 · 灵活组合
      </text>
    </svg>
    """


def get_bespoke_svg(layout_id):
    lid = str(layout_id).zfill(3)
    if lid == "001":
        return get_svg_001()
    elif lid == "002":
        return get_svg_002()
    elif lid == "003":
        return get_svg_003()
    elif lid == "004":
        return get_svg_004()
    elif lid == "005":
        return get_svg_005()
    elif lid == "084":
        return get_svg_084()
    elif lid == "134":
        return get_svg_134()
    return None

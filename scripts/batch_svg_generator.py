#!/usr/bin/env python3
"""
Comprehensive Modular SVG Generator for 350 Layouts.
Generates authentic, bespoke Swiss design SVGs (viewBox 0 0 550 620)
and saves them directly into data/svgs/{id}.svg.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SVGS_DIR = BASE_DIR / "data" / "svgs"
SVGS_DIR.mkdir(parents=True, exist_ok=True)

SVGS = {}

# ================= 024-030 重心、线条与轴线 =================

# 024 平行线构图 (PARALLEL LINES COMPOSITION)
SVGS["024"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#181A20" rx="8"/>
  <g stroke="#3A4050" stroke-width="2" stroke-dasharray="6,6">
    <line x1="80" y1="40" x2="80" y2="580"/>
    <line x1="470" y1="40" x2="470" y2="580"/>
  </g>
  <!-- Rhythmic Parallel Bands -->
  <line x1="140" y1="80" x2="140" y2="540" stroke="#3D5AFE" stroke-width="8" stroke-linecap="round"/>
  <line x1="190" y1="120" x2="190" y2="500" stroke="#3D5AFE" stroke-width="14" stroke-linecap="round"/>
  <line x1="250" y1="60" x2="250" y2="560" stroke="#FF5252" stroke-width="22" stroke-linecap="round"/>
  <line x1="315" y1="140" x2="315" y2="480" stroke="#3D5AFE" stroke-width="12" stroke-linecap="round"/>
  <line x1="365" y1="90" x2="365" y2="530" stroke="#3D5AFE" stroke-width="6" stroke-linecap="round"/>
  <line x1="410" y1="130" x2="410" y2="490" stroke="#3D5AFE" stroke-width="4" stroke-linecap="round"/>
  <!-- Transverse Measure Indicators -->
  <line x1="140" y1="310" x2="410" y2="310" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="250" cy="310" r="18" fill="#FF5252"/>
  <circle cx="250" cy="310" r="6" fill="#FFFFFF"/>
  <!-- Spacing Dimension Arrows -->
  <path d="M 190 420 L 250 420 M 195 415 L 190 420 L 195 425 M 245 415 L 250 420 L 245 425" stroke="#FF5252" stroke-width="1.8"/>
  <rect x="180" y="440" width="140" height="28" rx="5" fill="#252A38"/>
  <text x="250" y="458" fill="#FF5252" font-size="11" font-weight="bold" font-family="PingFang SC" text-anchor="middle">等距律动 · 平行延伸</text>
</svg>"""

# 025 汇聚线构图 (CONVERGING LINES)
SVGS["025"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="vanishGlow025" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFD700" stop-opacity="1"/>
      <stop offset="50%" stop-color="#FF9100" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#FF9100" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="550" height="620" fill="#12141A" rx="8"/>
  <!-- Converging Perspective Ground -->
  <polygon points="50,580 500,580 275,190" fill="#1C212D"/>
  <!-- Converging Lines to Vanishing Point (275, 190) -->
  <line x1="50" y1="580" x2="275" y2="190" stroke="#FF9100" stroke-width="3"/>
  <line x1="140" y1="580" x2="275" y2="190" stroke="#FF9100" stroke-width="1.8" stroke-dasharray="6,4"/>
  <line x1="230" y1="580" x2="275" y2="190" stroke="#FF9100" stroke-width="1.2" stroke-dasharray="4,4"/>
  <line x1="320" y1="580" x2="275" y2="190" stroke="#FF9100" stroke-width="1.2" stroke-dasharray="4,4"/>
  <line x1="410" y1="580" x2="275" y2="190" stroke="#FF9100" stroke-width="1.8" stroke-dasharray="6,4"/>
  <line x1="500" y1="580" x2="275" y2="190" stroke="#FF9100" stroke-width="3"/>
  <!-- Horizontal Horizon Line -->
  <line x1="40" y1="190" x2="510" y2="190" stroke="#4A5568" stroke-width="1.5" stroke-dasharray="5,5"/>
  <!-- Vanishing Point Nexus -->
  <circle cx="275" cy="190" r="70" fill="url(#vanishGlow025)"/>
  <circle cx="275" cy="190" r="16" fill="#FFD700"/>
  <circle cx="275" cy="190" r="5" fill="#12141A"/>
  <!-- Callout Badge -->
  <rect x="195" y="110" width="160" height="32" rx="6" fill="#FF9100"/>
  <text x="275" y="131" fill="#12141A" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">透视灭点 · 极速吸入</text>
</svg>"""

# 026 交叉线构图 (CROSSING LINES)
SVGS["026"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#1A1816" rx="8"/>
  <!-- Dramatic X-Crossing Beams -->
  <line x1="60" y1="100" x2="490" y2="520" stroke="#00E5FF" stroke-width="5" stroke-linecap="round"/>
  <line x1="490" y1="100" x2="60" y2="520" stroke="#FF3D00" stroke-width="5" stroke-linecap="round"/>
  <line x1="70" y1="120" x2="480" y2="530" stroke="#00E5FF" stroke-width="1.5" stroke-dasharray="6,6" opacity="0.6"/>
  <line x1="480" y1="120" x2="70" y2="530" stroke="#FF3D00" stroke-width="1.5" stroke-dasharray="6,6" opacity="0.6"/>
  <!-- Intersection Anchor (275, 310) -->
  <circle cx="275" cy="310" r="44" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="4,4"/>
  <circle cx="275" cy="310" r="22" fill="#FFFFFF"/>
  <circle cx="275" cy="310" r="8" fill="#1A1816"/>
  <!-- Quadrant Energy Markers -->
  <polygon points="275,230 265,250 285,250" fill="#00E5FF"/>
  <polygon points="275,390 265,370 285,370" fill="#00E5FF"/>
  <polygon points="195,310 215,300 215,320" fill="#FF3D00"/>
  <polygon points="355,310 335,300 335,320" fill="#FF3D00"/>
  <!-- Callout Badge -->
  <rect x="185" y="440" width="180" height="32" rx="6" fill="#FF3D00"/>
  <text x="275" y="461" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">十字相交 · 四方受力</text>
</svg>"""

# 027 中轴构图 (CENTRAL AXIS COMPOSITION)
SVGS["027"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#0D211A" rx="8"/>
  <!-- Monumental Central Axis Pillar -->
  <rect x="255" y="40" width="40" height="540" fill="#00BFA5"/>
  <line x1="275" y1="40" x2="275" y2="580" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="6,6"/>
  <!-- Left-Right Balanced Tiered Blocks -->
  <rect x="110" y="160" width="125" height="70" fill="#1B4D3E" rx="4"/>
  <rect x="315" y="160" width="125" height="70" fill="#1B4D3E" rx="4"/>
  <rect x="70" y="270" width="165" height="90" fill="#13382D" rx="4"/>
  <rect x="315" y="270" width="165" height="90" fill="#13382D" rx="4"/>
  <rect x="130" y="400" width="105" height="60" fill="#1B4D3E" rx="4"/>
  <rect x="315" y="400" width="105" height="60" fill="#1B4D3E" rx="4"/>
  <!-- Golden Crown Nodes -->
  <circle cx="275" cy="110" r="18" fill="#FFD700"/>
  <circle cx="275" cy="110" r="6" fill="#0D211A"/>
  <!-- Central Axis Callout Badge -->
  <rect x="195" y="490" width="160" height="32" rx="6" fill="#00BFA5"/>
  <text x="275" y="511" fill="#0D211A" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">神圣中轴 · 崇高威仪</text>
</svg>"""

# 030 十字构图 (CROSS COMPOSITION)
SVGS["030"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#18181B" rx="8"/>
  <!-- Subdued 4 Quadrants -->
  <rect x="50" y="60" width="205" height="230" fill="#222228" rx="6"/>
  <rect x="295" y="60" width="205" height="230" fill="#222228" rx="6"/>
  <rect x="50" y="330" width="205" height="230" fill="#222228" rx="6"/>
  <rect x="295" y="330" width="205" height="230" fill="#222228" rx="6"/>
  <!-- Cross Beams -->
  <line x1="50" y1="310" x2="500" y2="310" stroke="#FF5722" stroke-width="8" stroke-linecap="round"/>
  <line x1="275" y1="60" x2="275" y2="560" stroke="#FF5722" stroke-width="8" stroke-linecap="round"/>
  <line x1="40" y1="310" x2="510" y2="310" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="275" y1="50" x2="275" y2="570" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="6,4"/>
  <!-- Center Intersection Nexus -->
  <circle cx="275" cy="310" r="36" fill="#18181B" stroke="#FF5722" stroke-width="3"/>
  <circle cx="275" cy="310" r="16" fill="#FF5722"/>
  <circle cx="275" cy="310" r="5" fill="#FFFFFF"/>
  <!-- Badge -->
  <rect x="185" y="210" width="180" height="32" rx="6" fill="#FF5722"/>
  <text x="275" y="231" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">十字架构 · 四方平衡</text>
</svg>"""

# ================= 031-040 字母形与曲线 =================

# 035 Z 形构图 (Z-SHAPED COMPOSITION)
SVGS["035"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#1C1814" rx="8"/>
  <!-- Golden Z Path -->
  <path d="M 80 140 L 470 140 L 80 480 L 470 480" stroke="#FFB300" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 80 140 L 470 140 L 80 480 L 470 480" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="8,6" fill="none"/>
  <!-- Waypoints along Z Track -->
  <!-- 1. Entry point Top Left -->
  <circle cx="80" cy="140" r="28" fill="#FFB300"/>
  <text x="80" y="146" fill="#1C1814" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">1</text>
  <!-- 2. First Turn Top Right -->
  <circle cx="470" cy="140" r="24" fill="#FFB300"/>
  <text x="470" y="146" fill="#1C1814" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">2</text>
  <!-- 3. Diagonal Traverse Bottom Left -->
  <circle cx="80" cy="480" r="24" fill="#FFB300"/>
  <text x="80" y="486" fill="#1C1814" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">3</text>
  <!-- 4. Terminal Catch Bottom Right -->
  <circle cx="470" cy="480" r="34" fill="#FF3D00"/>
  <circle cx="470" cy="480" r="12" fill="#FFFFFF"/>
  <text x="470" y="486" fill="#1C1814" font-size="16" font-weight="900" font-family="Montserrat" text-anchor="middle">4</text>
  <!-- Motion Direction Arrows -->
  <path d="M 260 135 L 280 140 L 260 145" fill="#1C1814" stroke="#1C1814" stroke-width="2"/>
  <path d="M 285 300 L 265 315 L 285 320" fill="#1C1814" stroke="#1C1814" stroke-width="2"/>
  <path d="M 260 475 L 280 480 L 260 485" fill="#1C1814" stroke="#1C1814" stroke-width="2"/>
  <!-- Badge -->
  <rect x="185" y="300" width="180" height="32" rx="6" fill="#FFB300"/>
  <text x="275" y="321" fill="#1C1814" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">Z 型扫读 · 视线循环</text>
</svg>"""

# 037 S 形构图 (S-CURVE COMPOSITION)
SVGS["037"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sGrad037" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E676"/>
      <stop offset="50%" stop-color="#00B0FF"/>
      <stop offset="100%" stop-color="#651FFF"/>
    </linearGradient>
  </defs>
  <rect width="550" height="620" fill="#12161A" rx="8"/>
  <!-- Serpentine S Curve -->
  <path d="M 380 90 C 120 120 100 300 275 330 C 450 360 430 520 170 540" stroke="url(#sGrad037)" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M 380 90 C 120 120 100 300 275 330 C 450 360 430 520 170 540" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="6,6" fill="none"/>
  <!-- Inflection Point Markers -->
  <circle cx="380" cy="90" r="16" fill="#00E676"/>
  <circle cx="170" cy="230" r="14" fill="#00B0FF"/>
  <circle cx="275" cy="330" r="22" fill="#FFFFFF"/>
  <circle cx="275" cy="330" r="8" fill="#12161A"/>
  <circle cx="380" cy="430" r="14" fill="#00B0FF"/>
  <circle cx="170" cy="540" r="18" fill="#651FFF"/>
  <!-- Badge -->
  <rect x="185" y="240" width="180" height="32" rx="6" fill="#00B0FF"/>
  <text x="275" y="261" fill="#12161A" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">S 曲线 · 婉转曲折</text>
</svg>"""

# ================= 041-056 几何形与放射结构 =================

# 041 三角构图 (TRIANGULAR COMPOSITION)
SVGS["041"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="triGrad041" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" stop-color="#FF5252"/>
      <stop offset="100%" stop-color="#B71C1C"/>
    </linearGradient>
  </defs>
  <rect width="550" height="620" fill="#1A1816" rx="8"/>
  <!-- Inscribed Solid Triangle -->
  <polygon points="275,100 480,510 70,510" fill="url(#triGrad041)" opacity="0.9"/>
  <!-- Inner Triangle Frame -->
  <polygon points="275,180 430,480 120,480" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="6,6"/>
  <!-- Apex and Base Vertices -->
  <circle cx="275" cy="100" r="18" fill="#FFD700"/>
  <circle cx="275" cy="100" r="6" fill="#1A1816"/>
  <circle cx="70" cy="510" r="14" fill="#FFD700"/>
  <circle cx="480" cy="510" r="14" fill="#FFD700"/>
  <!-- Inscribed Center of Gravity -->
  <circle cx="275" cy="373" r="28" fill="#FFFFFF"/>
  <circle cx="275" cy="373" r="10" fill="#B71C1C"/>
  <!-- Altitude Centerline -->
  <line x1="275" y1="100" x2="275" y2="510" stroke="#FFD700" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- Badge -->
  <rect x="185" y="440" width="180" height="32" rx="6" fill="#FFD700"/>
  <text x="275" y="461" fill="#1A1816" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">三角定势 · 稳如磐石</text>
</svg>"""

# 047 圆形构图 (CIRCULAR COMPOSITION)
SVGS["047"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="circGrad047" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF4081"/>
      <stop offset="70%" stop-color="#C51162"/>
      <stop offset="100%" stop-color="#880E4F"/>
    </radialGradient>
  </defs>
  <rect width="550" height="620" fill="#15121E" rx="8"/>
  <!-- Concentric Orbital Ripples -->
  <circle cx="275" cy="310" r="230" stroke="#3D2950" stroke-width="1.5" stroke-dasharray="8,6" fill="none"/>
  <circle cx="275" cy="310" r="185" stroke="#7A3B7A" stroke-width="1.8" stroke-dasharray="6,4" fill="none"/>
  <!-- Main Circular Hero Sphere -->
  <circle cx="275" cy="310" r="140" fill="url(#circGrad047)"/>
  <circle cx="275" cy="310" r="140" stroke="#FFFFFF" stroke-width="2" fill="none"/>
  <!-- Center Core -->
  <circle cx="275" cy="310" r="32" fill="#FFFFFF"/>
  <circle cx="275" cy="310" r="12" fill="#880E4F"/>
  <!-- Planetary Satellites along Orbit -->
  <circle cx="275" cy="80" r="14" fill="#00E5FF"/>
  <circle cx="460" cy="310" r="18" fill="#FFD700"/>
  <circle cx="275" cy="540" r="14" fill="#00E5FF"/>
  <circle cx="90" cy="310" r="18" fill="#FFD700"/>
  <!-- Badge -->
  <rect x="185" y="380" width="180" height="32" rx="6" fill="#00E5FF"/>
  <text x="275" y="401" fill="#15121E" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">圆融归一 · 完满向心</text>
</svg>"""

# 057 棋盘构图 (CHECKERBOARD COMPOSITION)
SVGS["057"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#111113" rx="8"/>
  <!-- 4x5 Checkerboard Array -->
  <g transform="translate(65, 70)">
    <!-- Row 0 -->
    <rect x="0" y="0" width="105" height="96" fill="#E53935" rx="4"/>
    <rect x="105" y="0" width="105" height="96" fill="#212128" rx="4"/>
    <rect x="210" y="0" width="105" height="96" fill="#E53935" rx="4"/>
    <rect x="315" y="0" width="105" height="96" fill="#212128" rx="4"/>
    <!-- Row 1 -->
    <rect x="0" y="96" width="105" height="96" fill="#212128" rx="4"/>
    <rect x="105" y="96" width="105" height="96" fill="#E53935" rx="4"/>
    <rect x="210" y="96" width="105" height="96" fill="#212128" rx="4"/>
    <rect x="315" y="96" width="105" height="96" fill="#E53935" rx="4"/>
    <!-- Row 2 -->
    <rect x="0" y="192" width="105" height="96" fill="#E53935" rx="4"/>
    <rect x="105" y="192" width="105" height="96" fill="#212128" rx="4"/>
    <!-- Center Hero Highlight Cell (Row 2, Col 2) -->
    <rect x="210" y="192" width="105" height="96" fill="#FFD700" rx="4"/>
    <circle cx="262" cy="240" r="28" fill="#111113"/>
    <circle cx="262" cy="240" r="10" fill="#FFD700"/>
    <rect x="315" y="192" width="105" height="96" fill="#212128" rx="4"/>
    <!-- Row 3 -->
    <rect x="0" y="288" width="105" height="96" fill="#212128" rx="4"/>
    <rect x="105" y="288" width="105" height="96" fill="#E53935" rx="4"/>
    <rect x="210" y="288" width="105" height="96" fill="#212128" rx="4"/>
    <rect x="315" y="288" width="105" height="96" fill="#E53935" rx="4"/>
    <!-- Row 4 -->
    <rect x="0" y="384" width="105" height="96" fill="#E53935" rx="4"/>
    <rect x="105" y="384" width="105" height="96" fill="#212128" rx="4"/>
    <rect x="210" y="384" width="105" height="96" fill="#E53935" rx="4"/>
    <rect x="315" y="384" width="105" height="96" fill="#212128" rx="4"/>
  </g>
  <!-- Callout Badge -->
  <rect x="185" y="470" width="180" height="32" rx="6" fill="#FFD700"/>
  <text x="275" y="491" fill="#111113" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">棋盘交错 · 节奏阵列</text>
</svg>"""

# ================= 115-120 格式塔与组群 =================

# 115 相似性原则 (SIMILARITY PRINCIPLE)
SVGS["115"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#1E1C1A" rx="8"/>
  <!-- 5x5 Shape Matrix demonstrating Similarity grouping -->
  <g transform="translate(95, 80)">
    <!-- Column 0: Circles -->
    <circle cx="30" cy="40" r="22" fill="#E25238"/>
    <circle cx="30" cy="110" r="22" fill="#E25238"/>
    <circle cx="30" cy="180" r="22" fill="#E25238"/>
    <circle cx="30" cy="250" r="22" fill="#E25238"/>
    <circle cx="30" cy="320" r="22" fill="#E25238"/>

    <!-- Column 1: Squares -->
    <rect x="88" y="18" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="88" y="88" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="88" y="158" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="88" y="228" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="88" y="298" width="44" height="44" fill="#3D82FF" rx="4"/>

    <!-- Column 2: Triangles -->
    <polygon points="190,18 212,62 168,62" fill="#FFD700"/>
    <polygon points="190,88 212,132 168,132" fill="#FFD700"/>
    <polygon points="190,158 212,202 168,202" fill="#FFD700"/>
    <polygon points="190,228 212,272 168,272" fill="#FFD700"/>
    <polygon points="190,298 212,342 168,342" fill="#FFD700"/>

    <!-- Column 3: Squares -->
    <rect x="248" y="18" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="248" y="88" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="248" y="158" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="248" y="228" width="44" height="44" fill="#3D82FF" rx="4"/>
    <rect x="248" y="298" width="44" height="44" fill="#3D82FF" rx="4"/>

    <!-- Column 4: Circles -->
    <circle cx="350" cy="40" r="22" fill="#E25238"/>
    <circle cx="350" cy="110" r="22" fill="#E25238"/>
    <circle cx="350" cy="180" r="22" fill="#E25238"/>
    <circle cx="350" cy="250" r="22" fill="#E25238"/>
    <circle cx="350" cy="320" r="22" fill="#E25238"/>
  </g>
  <!-- Vertical Grouping Annotation Indicators -->
  <line x1="125" y1="460" x2="125" y2="485" stroke="#E25238" stroke-width="2"/>
  <line x1="205" y1="460" x2="205" y2="485" stroke="#3D82FF" stroke-width="2"/>
  <line x1="285" y1="460" x2="285" y2="485" stroke="#FFD700" stroke-width="2"/>
  <!-- Callout Badge -->
  <rect x="175" y="510" width="200" height="34" rx="6" fill="#3D82FF"/>
  <text x="275" y="532" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">形状相似 · 自发纵列归组</text>
</svg>"""

# 120 共同区域原则 (COMMON REGION PRINCIPLE)
SVGS["120"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#141E1A" rx="8"/>
  <!-- Common Region Box A (Left Enclosure) -->
  <rect x="50" y="100" width="205" height="380" fill="#1B382D" stroke="#00BFA5" stroke-width="2.5" rx="12"/>
  <text x="152" y="140" fill="#00BFA5" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">REGION A</text>
  <circle cx="152" cy="210" r="30" fill="#00E676"/>
  <circle cx="152" cy="300" r="30" fill="#00E676"/>
  <circle cx="152" cy="390" r="30" fill="#00E676"/>

  <!-- Common Region Box B (Right Enclosure) -->
  <rect x="295" y="100" width="205" height="380" fill="#2E2419" stroke="#FF9100" stroke-width="2.5" rx="12"/>
  <text x="397" y="140" fill="#FF9100" font-size="14" font-weight="900" font-family="Montserrat" text-anchor="middle">REGION B</text>
  <rect x="367" y="180" width="60" height="60" fill="#FFB300" rx="6"/>
  <rect x="367" y="270" width="60" height="60" fill="#FFB300" rx="6"/>
  <rect x="367" y="360" width="60" height="60" fill="#FFB300" rx="6"/>

  <!-- External Boundary Isolation Divider -->
  <line x1="275" y1="80" x2="275" y2="500" stroke="#4A6B5D" stroke-width="1.5" stroke-dasharray="6,6"/>
  <!-- Badge -->
  <rect x="175" y="520" width="200" height="34" rx="6" fill="#00BFA5"/>
  <text x="275" y="542" fill="#141E1A" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">封闭边界 · 明确归属区域</text>
</svg>"""

# ================= 146, 226, 272 现代布局 =================

# 146 蒙德里安版式 (MONDRIAN LAYOUT)
SVGS["146"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#FAF6EE" rx="8"/>
  <!-- Bold Black Structural Lines -->
  <!-- Red Top Right Block -->
  <rect x="180" y="40" width="310" height="230" fill="#D32F2F"/>
  <!-- Blue Bottom Left Block -->
  <rect x="60" y="390" width="120" height="170" fill="#1976D2"/>
  <!-- Yellow Bottom Right Block -->
  <rect x="420" y="450" width="70" height="110" fill="#FFEB3B"/>
  <!-- Black Heavy Grid Borders -->
  <rect x="60" y="40" width="430" height="520" fill="none" stroke="#121212" stroke-width="12"/>
  <line x1="180" y1="40" x2="180" y2="560" stroke="#121212" stroke-width="12"/>
  <line x1="60" y1="270" x2="490" y2="270" stroke="#121212" stroke-width="12"/>
  <line x1="60" y1="390" x2="490" y2="390" stroke="#121212" stroke-width="12"/>
  <line x1="420" y1="270" x2="420" y2="560" stroke="#121212" stroke-width="12"/>
  <line x1="420" y1="450" x2="490" y2="450" stroke="#121212" stroke-width="12"/>
  <!-- Callout Badge -->
  <rect x="185" y="305" width="180" height="32" rx="6" fill="#121212"/>
  <text x="275" y="326" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">纯粹色块 · 几何正交律</text>
</svg>"""

# 226 弹性盒布局 (FLEXBOX LAYOUT)
SVGS["226"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#111B2B" rx="8"/>
  <!-- Flex Container Frame -->
  <rect x="50" y="80" width="450" height="420" fill="#1A2942" stroke="#2979FF" stroke-width="2.5" rx="10"/>
  <!-- Main Axis Indicator -->
  <line x1="70" y1="120" x2="480" y2="120" stroke="#00E5FF" stroke-width="2.5" stroke-linecap="round"/>
  <polygon points="480,120 468,114 468,126" fill="#00E5FF"/>
  <text x="275" y="112" fill="#00E5FF" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">MAIN AXIS (row)</text>
  <!-- Cross Axis Indicator -->
  <line x1="80" y1="140" x2="80" y2="470" stroke="#FF80AB" stroke-width="2" stroke-linecap="round"/>
  <polygon points="80,470 74,458 86,458" fill="#FF80AB"/>
  <text x="65" y="310" fill="#FF80AB" font-size="10" font-weight="bold" font-family="Montserrat" transform="rotate(-90 65 310)" text-anchor="middle">CROSS AXIS</text>
  <!-- Flex Items -->
  <g transform="translate(110, 160)">
    <rect x="0" y="0" width="95" height="120" fill="#2979FF" rx="6"/>
    <text x="47" y="65" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">ITEM 1</text>
    <rect x="120" y="0" width="140" height="120" fill="#00E5FF" rx="6"/>
    <text x="190" y="65" fill="#111B2B" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">flex-grow: 2</text>
    <rect x="285" y="0" width="75" height="120" fill="#2979FF" rx="6"/>
    <text x="322" y="65" fill="#FFFFFF" font-size="12" font-weight="bold" font-family="Montserrat" text-anchor="middle">ITEM 3</text>
  </g>
  <!-- Secondary Wrapped Row -->
  <g transform="translate(110, 310)">
    <rect x="0" y="0" width="170" height="80" fill="#3D5AFE" rx="6"/>
    <text x="85" y="45" fill="#FFFFFF" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">flex-wrap: wrap</text>
    <rect x="190" y="0" width="170" height="80" fill="#3D5AFE" rx="6"/>
    <text x="275" y="45" fill="#FFFFFF" font-size="11" font-weight="bold" font-family="Montserrat" text-anchor="middle">justify: space-between</text>
  </g>
  <!-- Callout Badge -->
  <rect x="175" y="530" width="200" height="34" rx="6" fill="#2979FF"/>
  <text x="275" y="552" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">双轴对齐 · 流体自适应</text>
</svg>"""

# 272 便当盒布局 (BENTO BOX LAYOUT)
SVGS["272"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="620" fill="#0E1726" rx="8"/>
  <g transform="translate(50, 60)">
    <!-- Main Hero Bento Card (2x2) -->
    <rect x="0" y="0" width="260" height="260" fill="#1E293B" stroke="#38BDF8" stroke-width="2" rx="14"/>
    <circle cx="60" cy="60" r="28" fill="#38BDF8" opacity="0.2"/>
    <circle cx="60" cy="60" r="14" fill="#38BDF8"/>
    <rect x="35" y="120" width="140" height="16" fill="#FFFFFF" rx="4"/>
    <rect x="35" y="150" width="190" height="10" fill="#94A3B8" rx="3"/>
    <rect x="35" y="170" width="160" height="10" fill="#94A3B8" rx="3"/>
    <rect x="35" y="200" width="90" height="28" fill="#38BDF8" rx="6"/>
    <text x="80" y="218" fill="#0E1726" font-size="11" font-weight="900" font-family="PingFang SC" text-anchor="middle">核心主推</text>

    <!-- Top Right Card (1x1) -->
    <rect x="280" y="0" width="170" height="120" fill="#1E293B" stroke="#64748B" stroke-width="1.5" rx="12"/>
    <rect x="300" y="25" width="80" height="12" fill="#F43F5E" rx="3"/>
    <text x="300" y="75" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Montserrat">+128%</text>

    <!-- Mid Right Card (1x1) -->
    <rect x="280" y="140" width="170" height="120" fill="#1E293B" stroke="#64748B" stroke-width="1.5" rx="12"/>
    <!-- Sparkline Chart -->
    <path d="M 300 220 L 330 190 L 360 210 L 390 170 L 420 180" stroke="#10B981" stroke-width="3" fill="none" stroke-linecap="round"/>
    <circle cx="420" cy="180" r="4" fill="#10B981"/>

    <!-- Bottom Left Card (1x1.5) -->
    <rect x="0" y="280" width="180" height="160" fill="#1E293B" stroke="#64748B" stroke-width="1.5" rx="12"/>
    <circle cx="40" cy="320" r="16" fill="#A855F7"/>
    <circle cx="80" cy="320" r="16" fill="#EC4899"/>
    <circle cx="120" cy="320" r="16" fill="#EAB308"/>
    <rect x="25" y="360" width="130" height="10" fill="#94A3B8" rx="3"/>
    <rect x="25" y="385" width="90" height="10" fill="#64748B" rx="3"/>

    <!-- Bottom Right Wide Card (2x1) -->
    <rect x="200" y="280" width="250" height="160" fill="#1E293B" stroke="#F59E0B" stroke-width="2" rx="12"/>
    <rect x="225" y="310" width="110" height="14" fill="#F59E0B" rx="3"/>
    <rect x="225" y="340" width="200" height="8" fill="#64748B" rx="2"/>
    <rect x="225" y="360" width="170" height="8" fill="#64748B" rx="2"/>
    <rect x="225" y="380" width="140" height="8" fill="#64748B" rx="2"/>
  </g>
  <!-- Callout Badge -->
  <rect x="175" y="530" width="200" height="34" rx="6" fill="#38BDF8"/>
  <text x="275" y="552" fill="#0E1726" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">圆角便当盒 · 模块化聚合</text>
</svg>"""

# Save SVGs
for lid, code in SVGS.items():
    target = SVGS_DIR / f"{lid}.svg"
    target.write_text(code.strip(), encoding="utf-8")
    print(f"✓ Created {target}")

print(f"\nGenerated {len(SVGS)} bespoke SVGs successfully.")

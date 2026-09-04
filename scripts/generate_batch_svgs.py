#!/usr/bin/env python3
"""
High-Fidelity SVG Generator for 350 Layouts.
Generates authentic, bespoke Swiss design SVGs (viewBox 0 0 550 620)
and saves them directly into data/svgs/{id}.svg.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SVGS_DIR = BASE_DIR / "data" / "svgs"
SVGS_DIR.mkdir(parents=True, exist_ok=True)

SVGS = {}

# 016 居中构图 (CENTRAL COMPOSITION)
SVGS["016"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="centerGlow016" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#E25238" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#E25238" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#E25238" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="550" height="620" fill="#1C1A18" rx="8"/>
  
  <!-- Outer Frame Brackets -->
  <path d="M 90 140 L 60 140 L 60 170" stroke="#E25238" stroke-width="2.5" fill="none" opacity="0.8"/>
  <path d="M 460 140 L 490 140 L 490 170" stroke="#E25238" stroke-width="2.5" fill="none" opacity="0.8"/>
  <path d="M 90 480 L 60 480 L 60 450" stroke="#E25238" stroke-width="2.5" fill="none" opacity="0.8"/>
  <path d="M 460 480 L 490 480 L 490 450" stroke="#E25238" stroke-width="2.5" fill="none" opacity="0.8"/>

  <!-- Concentric Target Guides -->
  <circle cx="275" cy="310" r="220" stroke="#38332E" stroke-width="1.2" stroke-dasharray="6,6" fill="none"/>
  <circle cx="275" cy="310" r="170" stroke="#4A443D" stroke-width="1.5" stroke-dasharray="8,6" fill="none"/>
  <circle cx="275" cy="310" r="110" stroke="#E25238" stroke-width="1.5" stroke-dasharray="5,5" fill="none" opacity="0.6"/>

  <!-- Center Crosshairs -->
  <line x1="40" y1="310" x2="510" y2="310" stroke="#E25238" stroke-width="2" stroke-dasharray="8,6" opacity="0.75"/>
  <line x1="275" y1="50" x2="275" y2="570" stroke="#E25238" stroke-width="2" stroke-dasharray="8,6" opacity="0.75"/>

  <!-- Tick Marks along Axis -->
  <line x1="170" y1="304" x2="170" y2="316" stroke="#E25238" stroke-width="2"/>
  <line x1="380" y1="304" x2="380" y2="316" stroke="#E25238" stroke-width="2"/>
  <line x1="269" y1="200" x2="281" y2="200" stroke="#E25238" stroke-width="2"/>
  <line x1="269" y1="420" x2="281" y2="420" stroke="#E25238" stroke-width="2"/>

  <!-- Central Primary Focal Mass -->
  <circle cx="275" cy="310" r="90" fill="url(#centerGlow016)"/>
  <circle cx="275" cy="310" r="68" fill="#E25238"/>
  <circle cx="275" cy="310" r="24" fill="#1C1A18"/>
  <circle cx="275" cy="310" r="8" fill="#FFFFFF"/>

  <!-- Center Crosshair Marker -->
  <line x1="275" y1="298" x2="275" y2="322" stroke="#FFFFFF" stroke-width="2.5"/>
  <line x1="263" y1="310" x2="287" y2="310" stroke="#FFFFFF" stroke-width="2.5"/>

  <!-- Callout Label -->
  <rect x="195" y="420" width="160" height="32" rx="6" fill="#E25238"/>
  <text x="275" y="441" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">绝对重心 · 视觉奇点</text>
</svg>"""

# 017 偏心构图 (OFF-CENTER COMPOSITION)
SVGS["017"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="offGlow017" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF5E62" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#FF5E62" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#FF5E62" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="550" height="620" fill="#171526" rx="8"/>

  <!-- Off-center Grid Lines (shifted right and down) -->
  <line x1="365" y1="40" x2="365" y2="580" stroke="#FF5E62" stroke-width="2" stroke-dasharray="6,6" opacity="0.8"/>
  <line x1="40" y1="385" x2="510" y2="385" stroke="#FF5E62" stroke-width="2" stroke-dasharray="6,6" opacity="0.8"/>

  <!-- Counterbalancing Arch in bottom-left -->
  <path d="M 80 540 A 180 180 0 0 1 260 360 L 260 540 Z" fill="#24203B" opacity="0.9"/>
  <path d="M 80 540 A 180 180 0 0 1 260 360" stroke="#FF5E62" stroke-width="2" fill="none" opacity="0.4"/>

  <!-- Dot Matrix Pattern in Top-Right -->
  <g fill="#FF5E62" opacity="0.4">
    <circle cx="430" cy="90" r="3"/><circle cx="455" cy="90" r="3"/><circle cx="480" cy="90" r="3"/>
    <circle cx="430" cy="115" r="3"/><circle cx="455" cy="115" r="3"/><circle cx="480" cy="115" r="3"/>
    <circle cx="430" cy="140" r="3"/><circle cx="455" cy="140" r="3"/><circle cx="480" cy="140" r="3"/>
  </g>

  <!-- Diagonal Counterbalance Line -->
  <line x1="170" y1="450" x2="365" y2="210" stroke="#FF5E62" stroke-width="1.8" stroke-dasharray="5,4" opacity="0.7"/>
  <circle cx="170" cy="450" r="8" fill="#FF5E62" opacity="0.7"/>

  <!-- Off-Center Primary Hero Sphere (Top Right) -->
  <circle cx="365" cy="210" r="95" fill="url(#offGlow017)"/>
  <circle cx="365" cy="210" r="62" fill="#FF5E62"/>
  <circle cx="365" cy="210" r="22" fill="#171526"/>
  <circle cx="365" cy="210" r="8" fill="#FFFFFF"/>

  <!-- Intersection Marker -->
  <circle cx="365" cy="385" r="8" fill="none" stroke="#FF5E62" stroke-width="2.5"/>
  <circle cx="365" cy="385" r="3" fill="#FF5E62"/>

  <!-- Dynamic Vector Arrow -->
  <path d="M 280 290 L 330 240 M 330 240 L 310 240 M 330 240 L 330 260" stroke="#FFFFFF" stroke-width="3" fill="none" stroke-linecap="round"/>

  <!-- Callout Label -->
  <rect x="70" y="100" width="160" height="32" rx="6" fill="#FF5E62"/>
  <text x="150" y="121" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">偏心置位 · 蓄积张力</text>
</svg>"""

# 018 对称构图 (SYMMETRICAL COMPOSITION)
SVGS["018"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="symGradLeft" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#36B39C"/>
      <stop offset="100%" stop-color="#113636"/>
    </linearGradient>
    <linearGradient id="symGradRight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#36B39C"/>
      <stop offset="100%" stop-color="#113636"/>
    </linearGradient>
  </defs>
  <rect width="550" height="620" fill="#0C2121" rx="8"/>

  <!-- Central Symmetry Axis -->
  <line x1="275" y1="40" x2="275" y2="580" stroke="#36B39C" stroke-width="2.5" stroke-dasharray="8,6"/>

  <!-- Left Symmetrical Wing -->
  <path d="M 265 200 C 130 180 110 320 180 430 C 230 500 265 520 265 520 Z" fill="url(#symGradLeft)" opacity="0.9"/>
  <path d="M 265 240 C 180 230 160 330 210 410 C 240 450 265 470 265 470 Z" fill="#F4EEDD" opacity="0.95"/>
  <circle cx="150" cy="160" r="32" fill="#F4EEDD"/>
  <circle cx="150" cy="160" r="14" fill="#36B39C"/>

  <!-- Right Symmetrical Wing -->
  <path d="M 285 200 C 420 180 440 320 370 430 C 320 500 285 520 285 520 Z" fill="url(#symGradRight)" opacity="0.9"/>
  <path d="M 285 240 C 370 230 390 330 340 410 C 310 450 285 470 285 470 Z" fill="#F4EEDD" opacity="0.95"/>
  <circle cx="400" cy="160" r="32" fill="#F4EEDD"/>
  <circle cx="400" cy="160" r="14" fill="#36B39C"/>

  <!-- Mirrored Petals at Bottom -->
  <ellipse cx="220" cy="540" rx="22" ry="12" fill="#F4EEDD" transform="rotate(-30 220 540)"/>
  <ellipse cx="330" cy="540" rx="22" ry="12" fill="#F4EEDD" transform="rotate(30 330 540)"/>

  <!-- Center Fulcrum Lock -->
  <circle cx="275" cy="330" r="16" fill="#36B39C"/>
  <circle cx="275" cy="330" r="6" fill="#F4EEDD"/>
  <line x1="240" y1="330" x2="310" y2="330" stroke="#F4EEDD" stroke-width="2"/>

  <!-- Callout Axis Badge -->
  <rect x="205" y="80" width="140" height="30" rx="6" fill="#36B39C"/>
  <text x="275" y="100" fill="#0C2121" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">中轴镜像 · 绝对均势</text>
</svg>"""

# 019 非对称构图 (ASYMMETRICAL COMPOSITION)
SVGS["019"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sunRed019" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#E53935" stop-opacity="1"/>
      <stop offset="80%" stop-color="#C62828" stop-opacity="1"/>
      <stop offset="100%" stop-color="#B71C1C" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect width="550" height="620" fill="#E8B838" rx="8"/>

  <!-- Massive Blue Diagonal Geometric Wedge -->
  <polygon points="170,550 500,160 500,550" fill="#15489D"/>
  <polygon points="240,550 500,240 500,550" fill="#0D2E68" opacity="0.6"/>

  <!-- Lever Tension Line -->
  <line x1="120" y1="360" x2="380" y2="150" stroke="#1C1A18" stroke-width="2.5" stroke-dasharray="6,6"/>

  <!-- Left Counterweight Ball (Small, far from fulcrum) -->
  <circle cx="120" cy="360" r="28" fill="#15489D"/>
  <circle cx="120" cy="360" r="10" fill="#FFFFFF"/>

  <!-- Right Dominant Mass (Large, near center) -->
  <circle cx="380" cy="150" r="82" fill="url(#sunRed019)"/>
  <circle cx="380" cy="150" r="26" fill="#E8B838"/>
  <circle cx="380" cy="150" r="8" fill="#FFFFFF"/>

  <!-- Fulcrum Pivot Point -->
  <polygon points="250,290 235,320 265,320" fill="#1C1A18"/>
  <circle cx="250" cy="280" r="6" fill="#E53935"/>

  <!-- Callout Label -->
  <rect x="70" y="90" width="160" height="32" rx="6" fill="#15489D"/>
  <text x="150" y="111" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">力矩对冲 · 动态平衡</text>
</svg>"""

# 021 水平构图 (HORIZONTAL COMPOSITION)
SVGS["021"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skyGrad021" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F2EDE4"/>
      <stop offset="100%" stop-color="#D8D0C3"/>
    </linearGradient>
    <linearGradient id="seaGrad021" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#24518C"/>
      <stop offset="100%" stop-color="#0F2445"/>
    </linearGradient>
  </defs>
  <!-- Sky Top Half -->
  <rect width="550" height="620" fill="url(#skyGrad021)" rx="8"/>
  
  <!-- Sea Bottom Half -->
  <rect y="310" width="550" height="310" fill="url(#seaGrad021)"/>

  <!-- Multiple Parallel Horizon Lines -->
  <line x1="0" y1="310" x2="550" y2="310" stroke="#0F2445" stroke-width="3"/>
  <line x1="0" y1="360" x2="550" y2="360" stroke="#3A6FB3" stroke-width="1.5" opacity="0.6"/>
  <line x1="0" y1="420" x2="550" y2="420" stroke="#3A6FB3" stroke-width="1.5" opacity="0.4"/>
  <line x1="0" y1="490" x2="550" y2="490" stroke="#3A6FB3" stroke-width="1.5" opacity="0.3"/>
  <line x1="0" y1="560" x2="550" y2="560" stroke="#3A6FB3" stroke-width="1.2" opacity="0.2"/>

  <!-- Mountain Silhouettes along Horizon -->
  <path d="M 180 310 Q 240 280 300 310 Q 360 270 440 310 Q 480 290 550 310 L 550 310 Z" fill="#1C3860"/>

  <!-- Minimalist Sailboat on Horizon -->
  <g transform="translate(390, 275)">
    <polygon points="12,35 12,0 30,35" fill="#FFFFFF"/>
    <polygon points="10,35 10,8 0,35" fill="#EAE5DA"/>
    <polygon points="-5,37 35,37 28,43 2,43" fill="#E05238"/>
    <!-- Water reflection -->
    <line x1="0" y1="46" x2="30" y2="46" stroke="#FFFFFF" stroke-width="1" opacity="0.6"/>
    <line x1="5" y1="50" x2="25" y2="50" stroke="#FFFFFF" stroke-width="0.8" opacity="0.4"/>
  </g>

  <!-- Big Red Sun resting on Horizon -->
  <circle cx="160" cy="220" r="58" fill="#E05238"/>

  <!-- Guiding Horizon Callout -->
  <line x1="40" y1="310" x2="510" y2="310" stroke="#E05238" stroke-width="2" stroke-dasharray="6,6"/>
  <rect x="50" y="260" width="150" height="30" rx="6" fill="#E05238"/>
  <text x="125" y="280" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">水天一线 · 辽远开阔</text>
</svg>"""

# 022 垂直构图 (VERTICAL COMPOSITION)
SVGS["022"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="vertSky022" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EDE7DA"/>
      <stop offset="100%" stop-color="#D5CBB8"/>
    </linearGradient>
  </defs>
  <rect width="550" height="620" fill="url(#vertSky022)" rx="8"/>

  <!-- Vertical Towering Columns (Forest Green / Dark Teal Palette) -->
  <rect x="220" y="40" width="70" height="540" fill="#0D3328"/>
  <rect x="160" y="110" width="50" height="470" fill="#174A3C"/>
  <rect x="300" y="140" width="50" height="440" fill="#174A3C"/>
  <rect x="110" y="210" width="40" height="370" fill="#246352"/>
  <rect x="360" y="240" width="40" height="340" fill="#246352"/>
  <rect x="70" y="320" width="30" height="260" fill="#3D826F"/>
  <rect x="410" y="340" width="30" height="240" fill="#3D826F"/>

  <!-- Central Luminous Arch Portal -->
  <rect x="235" y="430" width="40" height="150" fill="#F4EEDD"/>
  <rect x="245" y="450" width="20" height="130" fill="#E2A638"/>

  <!-- Vertical Ascent Guide Arrow & Line -->
  <line x1="255" y1="560" x2="255" y2="70" stroke="#E2A638" stroke-width="3" stroke-dasharray="6,6"/>
  <polygon points="255,50 245,72 265,72" fill="#E2A638"/>

  <!-- Sun Sphere at upper right -->
  <circle cx="430" cy="110" r="36" fill="#E2A638"/>

  <!-- Callout Label -->
  <rect x="50" y="90" width="150" height="30" rx="6" fill="#0D3328"/>
  <text x="125" y="110" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">竖向拔萃 · 崇高耸立</text>
</svg>"""

# 023 对角线构图 (DIAGONAL COMPOSITION)
SVGS["023"] = """<svg viewBox="0 0 550 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="diagGrad023" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E25238"/>
      <stop offset="100%" stop-color="#FF9800"/>
    </linearGradient>
  </defs>
  <rect width="550" height="620" fill="#141416" rx="8"/>

  <!-- Diagonal Dividing Background Tone -->
  <polygon points="0,620 550,0 550,620" fill="#202026"/>

  <!-- Primary Diagonal Kinetic Rails -->
  <line x1="0" y1="620" x2="550" y2="0" stroke="url(#diagGrad023)" stroke-width="5"/>
  <line x1="30" y1="620" x2="550" y2="34" stroke="#E25238" stroke-width="1.8" stroke-dasharray="8,6" opacity="0.6"/>
  <line x1="-30" y1="620" x2="520" y2="0" stroke="#E25238" stroke-width="1.8" stroke-dasharray="8,6" opacity="0.6"/>

  <!-- High-speed Dynamic Chevrons along Diagonal -->
  <g stroke="#E25238" stroke-width="2.5" fill="none" opacity="0.8">
    <path d="M 120 460 L 150 430 L 120 400"/>
    <path d="M 220 350 L 250 320 L 220 290"/>
    <path d="M 320 240 L 350 210 L 320 180"/>
  </g>

  <!-- High-speed Focal Bullet Mass -->
  <circle cx="275" cy="310" r="64" fill="rgba(226,82,56,0.15)"/>
  <circle cx="275" cy="310" r="28" fill="#E25238"/>
  <circle cx="275" cy="310" r="10" fill="#FFFFFF"/>

  <!-- Callout Label aligned with diagonal -->
  <rect x="230" y="380" width="160" height="32" rx="6" fill="#E25238"/>
  <text x="310" y="401" fill="#FFFFFF" font-size="12" font-weight="900" font-family="PingFang SC" text-anchor="middle">斜角贯穿 · 极速破界</text>
</svg>"""

# Save SVGs to files
for lid, code in SVGS.items():
    target = SVGS_DIR / f"{lid}.svg"
    target.write_text(code.strip(), encoding="utf-8")
    print(f"✓ Created {target}")

print(f"\nGenerated {len(SVGS)} bespoke SVGs successfully.")

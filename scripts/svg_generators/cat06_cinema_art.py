"""
SVG generators for Category 06: 影视、摄影与传统艺术 (301-334).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_302(): # 双人对峙镜头 (Two-Shot Dynamic Confrontation)
    t = get_theme("obsidian-black")
    inner = f"""
  <!-- Cinematic 2.39:1 Letterbox Frame -->
  <rect x="40" y="140" width="470" height="340" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Top & Bottom Cinema Mask Bars -->
  <rect x="40" y="50" width="470" height="90" fill="#000000"/>
  <rect x="40" y="480" width="470" height="90" fill="#000000"/>
  <!-- Left Actor Silhouette Profile -->
  <path d="M 60 480 L 140 480 Q 180 380 180 280 Q 180 220 150 200 Q 120 200 120 240 L 60 260 Z" fill="{t['stroke']}"/>
  <circle cx="150" cy="240" r="5" fill="{t['accent']}"/>
  <!-- Right Actor Silhouette Profile -->
  <path d="M 490 480 L 410 480 Q 370 380 370 280 Q 370 220 400 200 Q 430 200 430 240 L 490 260 Z" fill="{t['stroke']}"/>
  <circle cx="400" cy="240" r="5" fill="{t['accent']}"/>
  <!-- Electric Confrontation Tension Line -->
  <line x1="155" y1="240" x2="395" y2="240" stroke="{t['danger']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <circle cx="275" cy="240" r="14" fill="{t['danger']}"/>
  <circle cx="275" cy="240" r="4" fill="#FFFFFF"/>
  {badge(185, 495, "双人对峙张力中线", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_315(): # 高远仰势法 (Gao Yuan High Distance Mountain Peak)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Soaring Vertical Monumental Mountain Peak (Guo Xi High Distance) -->
  <polygon points="275,80 160,420 390,420" fill="{t['stroke']}" opacity="0.9"/>
  <polygon points="275,80 230,260 275,420" fill="{t['accent']}" opacity="0.3"/>
  <polygon points="275,80 200,190 275,250" fill="#FFFFFF" opacity="0.6"/>
  <!-- Fore-hill lower layer -->
  <polygon points="100,520 180,390 260,520" fill="{t['stroke']}"/>
  <polygon points="300,520 410,380 490,520" fill="{t['stroke']}"/>
  <!-- Swirling Cloud & Mist Bands at Mid-Level -->
  <path d="M 120 370 Q 275 350 430 370" stroke="#FFFFFF" stroke-width="16" fill="none" opacity="0.4" stroke-linecap="round"/>
  <path d="M 80 410 Q 275 390 470 410" stroke="#FFFFFF" stroke-width="22" fill="none" opacity="0.3" stroke-linecap="round"/>
  <!-- Vertical Soaring Eye Vector -->
  <line x1="275" y1="480" x2="275" y2="90" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="6,4"/>
  <polygon points="275,80 268,98 282,98" fill="{t['accent']}"/>
  <!-- Callout -->
  <text x="350" y="140" fill="{t['accent']}" font-size="16" font-family="Kaiti, STKaiti, serif">自山下而仰山巅</text>
  {badge(185, 520, "高远法 · 崔嵬仰止", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_321(): # 一河两岸景式 (One River Two Banks Ni Zan)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- 1. Distant Minimal Hills (Far Bank) -->
  <path d="M 80 150 Q 180 110 270 140 T 460 130" fill="none" stroke="{t['stroke']}" stroke-width="3"/>
  <polygon points="120,150 180,120 240,150" fill="{t['stroke']}" opacity="0.5"/>
  <polygon points="310,140 370,115 430,140" fill="{t['stroke']}" opacity="0.4"/>
  <text x="275" y="100" fill="{t['text_dim']}" font-size="12" font-family="Kaiti, STKaiti, serif" text-anchor="middle">远岫平林</text>

  <!-- 2. Vast Calm River Void (Middle Empty Field) -->
  <rect x="70" y="170" width="410" height="190" fill="none" stroke="{t['accent']}" stroke-width="1" stroke-dasharray="6,6" opacity="0.4"/>
  <text x="275" y="270" fill="{t['text_dim']}" font-size="22" font-family="Kaiti, STKaiti, serif" text-anchor="middle" letter-spacing="8">大水漫漫 · 虚怀澄澈</text>

  <!-- 3. Foreground Rocky Bank with Sparse Trees (Near Bank) -->
  <polygon points="60,520 180,410 320,440 480,520" fill="{t['stroke']}"/>
  <!-- Two Sparse Solitary Trees (Ni Zan style) -->
  <line x1="160" y1="420" x2="150" y2="300" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <line x1="150" y1="300" x2="120" y2="260" stroke="{t['accent']}" stroke-width="2.5"/>
  <line x1="150" y1="300" x2="180" y2="250" stroke="{t['accent']}" stroke-width="2.5"/>
  <line x1="190" y1="430" x2="200" y2="320" stroke="{t['accent']}" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="200" y1="320" x2="230" y2="280" stroke="{t['accent']}" stroke-width="2"/>
  <!-- Red Seal Mark (Top Right) -->
  <rect x="420" y="80" width="30" height="30" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, "倪瓒一河两岸三段式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_326(): # 计白当黑虚实 (Void as Form Ji Bai Dang Hei)
    t = get_theme("warm-ivory")
    inner = f"""
  <!-- Zen Minimal Yin-Yang Void Balance -->
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Expressive Brush Stroke Polygon on Right -->
  <path d="M 320 70 C 450 140 480 340 380 480 C 320 540 240 520 280 440 C 320 360 220 280 290 180 Z" fill="{t['stroke']}"/>
  <!-- Solitary Concentrated Red Focal Dot inside White Void on Left -->
  <circle cx="160" cy="310" r="18" fill="{t['danger']}"/>
  <circle cx="160" cy="310" r="5" fill="#FFFFFF"/>
  <!-- Dotted Tension Bridge across the Void -->
  <line x1="160" y1="310" x2="330" y2="310" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="160" y="370" fill="{t['accent']}" font-size="18" font-family="Kaiti, STKaiti, serif" text-anchor="middle">计白当黑</text>
  <text x="160" y="400" fill="{t['text_dim']}" font-size="12" font-family="PingFang SC" text-anchor="middle">无画处皆成妙境</text>
  {badge(185, 510, "黑实白虚 · 旷世呼吸", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat06
CAT06_SVGS = {
    "302": gen_302, "315": gen_315, "321": gen_321, "326": gen_326
}


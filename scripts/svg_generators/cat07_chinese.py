"""
SVG generators for Category 07: 东方传统绘画与空间美学 (315-334).
"""
from .common import wrap_svg, focal_point, badge, dimension_h, dimension_v, get_theme

def gen_315(): # 高远法 (Gao Yuan / High Distance)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Soaring Vertical Peak -->
  <polygon points="275,80 160,420 390,420" fill="{t['stroke']}" opacity="0.9"/>
  <polygon points="275,80 230,260 275,420" fill="{t['accent']}" opacity="0.3"/>
  <!-- Mid-level cloud bands -->
  <path d="M 100 360 Q 275 330 450 360" stroke="#FFFFFF" stroke-width="20" fill="none" opacity="0.4" stroke-linecap="round"/>
  <!-- Base foothills -->
  <polygon points="80,520 180,410 280,520" fill="{t['stroke']}"/>
  <polygon points="280,520 380,400 480,520" fill="{t['stroke']}"/>
  <!-- Vertical Soaring Vector -->
  <line x1="275" y1="480" x2="275" y2="90" stroke="{t['accent']}" stroke-width="2.5" stroke-dasharray="6,4"/>
  <polygon points="275,80 267,98 283,98" fill="{t['accent']}"/>
  <text x="350" y="130" fill="{t['accent']}" font-size="16" font-family="Kaiti, STKaiti, serif">自山下而仰山巅</text>
  {badge(185, 520, "高远法 · 崔嵬仰止", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_316(): # 深远法 (Shen Yuan / Deep Distance)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" rx="6" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- Deep Ravine Layers -->
  <path d="M 50 140 Q 180 220 275 140 T 500 170 L 500 570 L 50 570 Z" fill="{t['stroke']}" opacity="0.4"/>
  <path d="M 50 260 Q 220 340 320 260 T 500 310 L 500 570 L 50 570 Z" fill="{t['bg']}" opacity="0.8"/>
  <path d="M 50 390 Q 180 440 280 370 T 500 420 L 500 570 L 50 570 Z" fill="{t['stroke']}"/>
  <!-- Winding Path Penetrating Deep into Chasm -->
  <path d="M 275 520 C 275 420 190 360 240 290 C 280 230 230 180 275 110" fill="none" stroke="{t['accent']}" stroke-width="4" stroke-dasharray="6,4"/>
  <polygon points="275,105 268,122 282,122" fill="{t['accent']}"/>
  <text x="360" y="100" fill="{t['accent']}" font-size="16" font-family="Kaiti, serif">自山前而窥山后</text>
  {badge(185, 520, "深远法 · 幽深莫测", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_317(): # 平远法 (Ping Yuan / Level Distance)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" rx="6" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- Low Infinite Water Horizon -->
  <line x1="50" y1="340" x2="500" y2="340" stroke="{t['accent']}" stroke-width="2"/>
  <path d="M 70 340 Q 200 310 320 340 T 480 335" fill="none" stroke="{t['stroke']}" stroke-width="3"/>
  <!-- Distant Islands -->
  <ellipse cx="380" cy="330" rx="50" ry="12" fill="{t['stroke']}" opacity="0.5"/>
  <ellipse cx="170" cy="335" rx="40" ry="8" fill="{t['stroke']}" opacity="0.5"/>
  <!-- Gentle Sun Void -->
  <circle cx="275" cy="200" r="38" fill="{t['accent']}" opacity="0.3"/>
  <circle cx="275" cy="200" r="14" fill="{t['accent']}"/>
  <text x="275" y="430" fill="{t['text_dim']}" font-size="16" font-family="Kaiti, serif" text-anchor="middle">自近山而望远山 · 平远渺渺</text>
  {badge(185, 520, "平远法 · 极目天舒", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_318(): # 三远综合构图 (Three Distances Integrated)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" rx="6" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- High: Top peak -->
  <polygon points="275,80 190,260 360,260" fill="{t['stroke']}"/>
  <text x="370" y="110" fill="{t['accent']}" font-size="12" font-family="Kaiti, serif">[高远]</text>
  <!-- Deep: Winding mid ravine -->
  <path d="M 140 260 Q 275 320 410 260" fill="none" stroke="{t['accent']}" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="110" y="290" fill="{t['accent_alt']}" font-size="12" font-family="Kaiti, serif">[深远]</text>
  <!-- Level: Vast low water -->
  <line x1="60" y1="430" x2="490" y2="430" stroke="{t['guide']}" stroke-width="2"/>
  <text x="275" y="460" fill="{t['text_dim']}" font-size="12" font-family="Kaiti, serif" text-anchor="middle">[平远]</text>
  {badge(185, 520, "高深平三远一统大观", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_319(): # 散点透视 (Axonometric Wandering Perspective)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" rx="6" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- Multi-focal scroll layout (Qingming scroll style) -->
  <!-- Scene 1 Left -->
  <rect x="80" y="120" width="90" height="110" rx="4" fill="{t['stroke']}" opacity="0.6"/>
  <circle cx="125" cy="175" r="16" fill="{t['accent']}"/>
  <!-- Scene 2 Center-High -->
  <rect x="230" y="200" width="100" height="120" rx="4" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="280" cy="260" r="20" fill="{t['accent_alt']}"/>
  <!-- Scene 3 Right-Low -->
  <rect x="370" y="310" width="90" height="110" rx="4" fill="{t['stroke']}" opacity="0.6"/>
  <circle cx="415" cy="365" r="16" fill="{t['danger']}"/>
  <!-- Wandering Eye Vector connecting multiple centers -->
  <path d="M 125 175 C 180 280 230 180 280 260 C 330 340 370 260 415 365" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="275" y="90" fill="{t['accent']}" font-size="14" font-family="Kaiti, serif" text-anchor="middle">游移视点 · 步移景异</text>
  {badge(185, 520, "散点透视移动视线长卷", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_320(): # 游观式构图 (Wandering Path / You Guan)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" rx="6" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- S-curve serpentine wandering path through scenery -->
  <path d="M 100 500 Q 220 440 200 340 T 360 260 T 275 110" fill="none" stroke="{t['accent']}" stroke-width="5" stroke-linecap="round"/>
  <!-- Viewing Pavilions along path -->
  <circle cx="100" cy="500" r="14" fill="{t['danger']}"/>
  <circle cx="200" cy="340" r="16" fill="{t['accent_alt']}"/>
  <circle cx="360" cy="260" r="18" fill="{t['accent_alt']}"/>
  <circle cx="275" cy="110" r="22" fill="{t['accent']}"/>
  <text x="275" y="80" fill="{t['accent']}" font-size="14" font-family="Kaiti, serif" text-anchor="middle">终登绝顶</text>
  {badge(185, 520, "曲径通幽游观步移", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_321(): # 一河两岸式 (One River Two Banks Ni Zan)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Far Bank -->
  <polygon points="120,150 180,120 240,150" fill="{t['stroke']}" opacity="0.5"/>
  <polygon points="310,140 370,115 430,140" fill="{t['stroke']}" opacity="0.4"/>
  <!-- Middle Water Void -->
  <rect x="70" y="170" width="410" height="190" fill="none" stroke="{t['accent']}" stroke-width="1" stroke-dasharray="6,6" opacity="0.4"/>
  <text x="275" y="270" fill="{t['text_dim']}" font-size="20" font-family="Kaiti, serif" text-anchor="middle">大水漫漫 · 虚怀澄澈</text>
  <!-- Near Bank with 2 Sparse Trees -->
  <polygon points="60,520 180,410 320,440 480,520" fill="{t['stroke']}"/>
  <line x1="160" y1="420" x2="150" y2="300" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <line x1="190" y1="430" x2="200" y2="320" stroke="{t['accent']}" stroke-width="3.5" stroke-linecap="round"/>
  <rect x="420" y="80" width="28" height="28" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, "倪瓒一河两岸三段式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_322(): # 宽远式构图 (Broad Distance)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" rx="6" stroke="{t['accent']}" stroke-width="1.5"/>
  <!-- Sweeping horizontal water body with panoramic width -->
  <line x1="50" y1="280" x2="500" y2="280" stroke="{t['accent']}" stroke-width="2"/>
  <line x1="50" y1="340" x2="500" y2="340" stroke="{t['accent_alt']}" stroke-width="1.5"/>
  <ellipse cx="275" cy="310" rx="190" ry="35" fill="none" stroke="{t['accent']}" stroke-width="1" stroke-dasharray="4,4"/>
  <circle cx="275" cy="170" r="26" fill="{t['accent']}"/>
  <text x="275" y="410" fill="{t['text']}" font-size="16" font-family="Kaiti, serif" text-anchor="middle">浩渺烟波 · 宽远无际</text>
  {badge(185, 520, "宽阔水域平远延展", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_323(): # 边角式构图 (Ma Yuan One-Corner Composition)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Heavy Rocky Cliff occupying strictly lower-left 25% -->
  <polygon points="50,220 280,570 50,570" fill="{t['stroke']}"/>
  <line x1="50" y1="220" x2="280" y2="570" stroke="{t['accent']}" stroke-width="3"/>
  <!-- Gnarled pine extending from corner -->
  <line x1="110" y1="350" x2="190" y2="290" stroke="{t['accent']}" stroke-width="3.5" stroke-linecap="round"/>
  <line x1="190" y1="290" x2="240" y2="310" stroke="{t['accent']}" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Upper Right 75% Vast Mist Void -->
  <text x="360" y="240" fill="{t['text_dim']}" font-size="20" font-family="Kaiti, STKaiti, serif" text-anchor="middle">马一角 · 留白旷远</text>
  <circle cx="360" cy="150" r="26" fill="{t['accent']}" opacity="0.4"/>
  <rect x="430" y="80" width="26" height="26" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, "马远残山剩水边角式", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_324(): # 截景式构图 (Cropped Vista)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Close-up architectural garden pavilion roof eave slicing in -->
  <polygon points="50,110 320,160 260,200 50,150" fill="{t['accent']}"/>
  <line x1="320" y1="160" x2="345" y2="130" stroke="{t['accent']}" stroke-width="4" stroke-linecap="round"/>
  <!-- Window lattice reveal -->
  <rect x="80" y="220" width="160" height="220" fill="none" stroke="{t['accent_alt']}" stroke-width="2" stroke-dasharray="6,6"/>
  <circle cx="160" cy="330" r="32" fill="{t['danger']}"/>
  <text x="350" y="330" fill="{t['text_dim']}" font-size="16" font-family="Kaiti, serif" text-anchor="middle">截取庭院一隅</text>
  {badge(185, 520, "以局部截景见大千", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_325(): # 折枝式构图 (Cut Blossom Branch)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Graceful Sinuous Branch diagonal -->
  <path d="M 50 420 Q 200 370 310 240 T 430 130" fill="none" stroke="{t['accent']}" stroke-width="5" stroke-linecap="round"/>
  <!-- Blossom Nodes -->
  <circle cx="310" cy="240" r="26" fill="{t['danger']}"/>
  <circle cx="310" cy="240" r="8" fill="#FFFFFF"/>
  <circle cx="430" cy="130" r="18" fill="{t['accent_alt']}"/>
  <circle cx="220" cy="310" r="16" fill="{t['accent_alt']}"/>
  <circle cx="140" cy="375" r="12" fill="{t['accent_alt']}"/>
  <text x="160" y="160" fill="{t['text_dim']}" font-size="16" font-family="Kaiti, serif">生动折枝 · 尺幅寸心</text>
  {badge(185, 520, "宋人折枝花鸟极简", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_326(): # 计白当黑虚实 (Void as Form)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <path d="M 320 70 C 450 140 480 340 380 480 C 320 540 240 520 280 440 C 320 360 220 280 290 180 Z" fill="{t['stroke']}"/>
  <circle cx="160" cy="310" r="18" fill="{t['danger']}"/>
  <circle cx="160" cy="310" r="5" fill="#FFFFFF"/>
  <line x1="160" y1="310" x2="330" y2="310" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="160" y="370" fill="{t['accent']}" font-size="18" font-family="Kaiti, serif" text-anchor="middle">计白当黑</text>
  {badge(185, 510, "黑实白虚 · 旷世呼吸", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_327(): # 计白当黑构图 (Ji Bai Dang Hei)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Vigorous Calligraphic Stroke cutting through white paper -->
  <path d="M 120 120 Q 200 300 275 260 T 420 440" stroke="{t['accent']}" stroke-width="18" fill="none" stroke-linecap="round"/>
  <text x="160" y="420" fill="#FFFFFF" font-size="24" font-weight="900" font-family="Kaiti, serif">无画处皆成妙境</text>
  <rect x="410" y="100" width="32" height="32" fill="{t['danger']}" rx="2"/>
  {badge(185, 520, "以虚带实计白当黑", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_328(): # 虚实相生构图 (Void & Substance Mutual Generation)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Solid Ink Mass (Substance) -->
  <polygon points="80,480 220,180 340,480" fill="{t['stroke']}"/>
  <!-- Interpenetrating Mist Waves (Void) -->
  <path d="M 60 300 Q 220 220 380 320 T 480 280" fill="none" stroke="#FFFFFF" stroke-width="26" opacity="0.5" stroke-linecap="round"/>
  <circle cx="220" cy="180" r="14" fill="{t['accent']}"/>
  <text x="275" y="110" fill="{t['accent']}" font-size="16" font-family="Kaiti, serif" text-anchor="middle">实者虚之 · 虚者实之</text>
  {badge(185, 520, "虚实互涵互生互化", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_329(): # 疏密相间构图 (Density Contrast Shu Mi)
    t = get_theme("forest-green")
    dots = "".join([f'<circle cx="{90 + (i%5)*24}" cy="{140 + (i//5)*24}" r="8" fill="{t["accent"]}"/>' for i in range(25)])
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Dense Clustered Thicket (密不通风) -->
  <rect x="75" y="120" width="130" height="130" fill="{t['bg']}" stroke="{t['accent']}" stroke-width="2" rx="4"/>
  <g>{dots}</g>
  <text x="140" y="285" fill="{t['accent']}" font-size="14" font-family="Kaiti, serif" text-anchor="middle">密不通风</text>
  <!-- Sparse Void (疏可走马) -->
  <circle cx="390" cy="350" r="26" fill="{t['danger']}"/>
  <text x="390" y="410" fill="{t['text_dim']}" font-size="14" font-family="Kaiti, serif" text-anchor="middle">疏可走马</text>
  {badge(185, 520, "繁简疏密聚散相间", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_330(): # 主宾关系构图 (Host and Guest Zhu Bin)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Dominant Host Mountain Peak (主山巍峨) -->
  <polygon points="275,100 170,440 380,440" fill="{t['stroke']}" stroke="{t['accent']}" stroke-width="2"/>
  <circle cx="275" cy="100" r="16" fill="{t['danger']}"/>
  <text x="275" y="75" fill="{t['danger']}" font-size="14" font-weight="bold" font-family="Kaiti, serif" text-anchor="middle">主山 (HOST)</text>
  <!-- Subordinate Guest Hills (客山朝揖) -->
  <polygon points="70,480 150,340 230,480" fill="{t['stroke']}" opacity="0.6"/>
  <polygon points="320,480 400,360 480,480" fill="{t['stroke']}" opacity="0.6"/>
  <text x="150" y="325" fill="{t['text_dim']}" font-size="12" font-family="Kaiti, serif" text-anchor="middle">宾山</text>
  <text x="400" y="345" fill="{t['text_dim']}" font-size="12" font-family="Kaiti, serif" text-anchor="middle">宾山</text>
  {badge(185, 520, "主峰君临众宾朝拱", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_331(): # 开合构图 (Opening and Closing Kai He)
    t = get_theme("cobalt-blue")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Outward Expanding Arc (开 Opening) -->
  <path d="M 180 380 Q 275 220 370 380" fill="none" stroke="{t['accent']}" stroke-width="4" stroke-dasharray="8,6"/>
  <!-- Inward Converging Arc (合 Closing) -->
  <path d="M 120 180 Q 275 320 430 180" fill="none" stroke="{t['accent_alt']}" stroke-width="4" stroke-dasharray="8,6"/>
  <circle cx="275" cy="270" r="28" fill="{t['danger']}"/>
  <circle cx="275" cy="270" r="8" fill="#FFFFFF"/>
  <text x="275" y="120" fill="{t['text']}" font-size="16" font-family="Kaiti, serif" text-anchor="middle">有开必有合 · 气脉贯通</text>
  {badge(185, 520, "开合适度舒卷自如", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_332(): # 起承转合构图 (Qi Cheng Zhuan He)
    t = get_theme("forest-green")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- 4 Flow Quadrants -->
  <!-- 1. 起 (Introduction) -->
  <circle cx="130" cy="150" r="26" fill="{t['accent']}"/><text x="130" y="156" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">起</text>
  <line x1="160" y1="150" x2="360" y2="190" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- 2. 承 (Elaboration) -->
  <circle cx="390" cy="200" r="32" fill="{t['accent_alt']}"/><text x="390" y="206" fill="{t['bg']}" font-size="18" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">承</text>
  <line x1="380" y1="235" x2="150" y2="345" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- 3. 转 (Climax Shift) -->
  <circle cx="130" cy="350" r="38" fill="{t['danger']}"/><text x="130" y="358" fill="#FFFFFF" font-size="20" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">转</text>
  <line x1="170" y1="360" x2="350" y2="410" stroke="{t['guide']}" stroke-width="2" stroke-dasharray="4,4"/>
  <!-- 4. 合 (Resolution) -->
  <circle cx="380" cy="420" r="28" fill="{t['accent']}"/><text x="380" y="426" fill="{t['bg']}" font-size="16" font-weight="900" font-family="Kaiti, serif" text-anchor="middle">合</text>
  {badge(185, 520, "四段演进起承转合", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_333(): # 藏露关系构图 (Concealment and Reveal Cang Lu)
    t = get_theme("warm-ivory")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Mountain Temple partly hidden by clouds -->
  <!-- Mountain silhouette -->
  <polygon points="275,120 120,480 430,480" fill="{t['stroke']}"/>
  <!-- Temple Pagoda (Partially concealed) -->
  <rect x="250" y="200" width="50" height="70" fill="{t['accent']}"/>
  <polygon points="240,200 275,170 310,200" fill="{t['danger']}"/>
  <!-- Swirling concealing cloud ribbon -->
  <path d="M 80 260 Q 275 190 470 280" stroke="#FFFFFF" stroke-width="38" fill="none" opacity="0.55" stroke-linecap="round"/>
  <text x="275" y="370" fill="{t['text_dim']}" font-size="16" font-family="Kaiti, serif" text-anchor="middle">深山藏古寺 · 隐秀胜全彰</text>
  {badge(185, 520, "烟云遮断半露峥嵘", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

def gen_334(): # 欹正关系构图 (Slanted and Upright Qi Zheng)
    t = get_theme("obsidian-black")
    inner = f"""
  <rect x="50" y="50" width="450" height="520" fill="{t['bg_surface']}" stroke="{t['accent']}" stroke-width="1.5" rx="6"/>
  <!-- Precariously Slanted Trunk (欹) -->
  <line x1="120" y1="460" x2="360" y2="160" stroke="{t['accent']}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="360" cy="160" r="32" fill="{t['danger']}"/>
  <!-- Solid Ground Anchor Rock (正 Counterbalance) -->
  <rect x="80" y="380" width="130" height="90" rx="6" fill="{t['stroke']}" stroke="{t['accent_alt']}" stroke-width="2"/>
  <line x1="275" y1="80" x2="275" y2="500" stroke="{t['guide']}" stroke-width="1.5" stroke-dasharray="6,6"/>
  <text x="275" y="110" fill="{t['text']}" font-size="15" font-family="Kaiti, serif" text-anchor="middle">以欹为正 · 势险节短</text>
  {badge(185, 520, "欹斜绝险反求平衡", t['accent'], t['bg'], 180, 28)}
"""
    return wrap_svg(inner, t['bg'])

# Dispatch dictionary for Cat07 Chinese
CAT07_CHINESE_SVGS = {
    "315": gen_315, "316": gen_316, "317": gen_317, "318": gen_318, "319": gen_319,
    "320": gen_320, "321": gen_321, "322": gen_322, "323": gen_323, "324": gen_324,
    "325": gen_325, "326": gen_326, "327": gen_327, "328": gen_328, "329": gen_329,
    "330": gen_330, "331": gen_331, "332": gen_332, "333": gen_333, "334": gen_334
}

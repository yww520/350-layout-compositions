#!/usr/bin/env python3
"""
350 Layout Domain Knowledge System (33 Subcategories & 350 English Names)
Provides professional design parameters, differentiated taglines, specific features,
actionable tips, and targeted keywords for all 350 layout types.
"""

from pathlib import Path
import json

# 350 Authentic English Names Map
NAMES_EN = {
  "001": "RULE OF THIRDS",
  "002": "GOLDEN RATIO",
  "003": "GOLDEN SPIRAL",
  "004": "GOLDEN TRIANGLE",
  "005": "DIAGONAL METHOD",
  "006": "RECTANGLE INSET METHOD",
  "007": "RULE OF ODDS",
  "008": "RULE OF SPACE",
  "009": "EYE ROOM",
  "010": "LEAD ROOM",
  "011": "HEADROOM",
  "012": "FILL THE FRAME",
  "013": "NEGATIVE SPACE",
  "014": "FRAME WITHIN A FRAME",
  "015": "LEADING LINES",
  "016": "CENTERED COMPOSITION",
  "017": "OFF-CENTER COMPOSITION",
  "018": "SYMMETRICAL COMPOSITION",
  "019": "ASYMMETRICAL COMPOSITION",
  "020": "REFLECTION COMPOSITION",
  "021": "HORIZONTAL COMPOSITION",
  "022": "VERTICAL COMPOSITION",
  "023": "DIAGONAL COMPOSITION",
  "024": "PARALLEL LINES COMPOSITION",
  "025": "CONVERGING LINES",
  "026": "CROSSING LINES",
  "027": "CENTRAL AXIS COMPOSITION",
  "028": "OFF-AXIS COMPOSITION",
  "029": "DUAL-AXIS COMPOSITION",
  "030": "CROSS COMPOSITION",
  "031": "X-SHAPED COMPOSITION",
  "032": "T-SHAPED COMPOSITION",
  "033": "L-SHAPED COMPOSITION",
  "034": "V-SHAPED COMPOSITION",
  "035": "Z-SHAPED COMPOSITION",
  "036": "C-SHAPED COMPOSITION",
  "037": "S-CURVE COMPOSITION",
  "038": "CURVILINEAR COMPOSITION",
  "039": "WAVE COMPOSITION",
  "040": "ZIGZAG COMPOSITION",
  "041": "TRIANGULAR COMPOSITION",
  "042": "PYRAMID COMPOSITION",
  "043": "INVERTED TRIANGLE COMPOSITION",
  "044": "RHOMBUS COMPOSITION",
  "045": "SQUARE COMPOSITION",
  "046": "RECTANGULAR COMPOSITION",
  "047": "CIRCULAR COMPOSITION",
  "048": "ELLIPTICAL COMPOSITION",
  "049": "ARC COMPOSITION",
  "050": "ANNULAR COMPOSITION",
  "051": "SPIRAL COMPOSITION",
  "052": "RADIATING COMPOSITION",
  "053": "CENTRIPETAL COMPOSITION",
  "054": "CENTRIFUGAL COMPOSITION",
  "055": "CONCENTRIC COMPOSITION",
  "056": "FOUR-QUADRANT COMPOSITION",
  "057": "CHECKERBOARD COMPOSITION",
  "058": "STAIRCASE COMPOSITION",
  "059": "STACKING COMPOSITION",
  "060": "CASCADING COMPOSITION",
  "061": "CLUSTERED COMPOSITION",
  "062": "DISPERSED COMPOSITION",
  "063": "BRANCHING COMPOSITION",
  "064": "NETWORK COMPOSITION",
  "065": "FOREGROUND-MID-BACKGROUND",
  "066": "FOREGROUND FRAMING",
  "067": "OVERLAPPING SPACE",
  "068": "DIMINISHING SCALE",
  "069": "LINEAR PERSPECTIVE",
  "070": "ONE-POINT PERSPECTIVE",
  "071": "TWO-POINT PERSPECTIVE",
  "072": "THREE-POINT PERSPECTIVE",
  "073": "PARALLEL PERSPECTIVE",
  "074": "OBLIQUE PROJECTION",
  "075": "ISOMETRIC COMPOSITION",
  "076": "AXONOMETRIC COMPOSITION",
  "077": "BIRD'S-EYE VIEW",
  "078": "WORM'S-EYE VIEW",
  "079": "TOP-DOWN VIEW",
  "080": "EYE-LEVEL COMPOSITION",
  "081": "FORCED PERSPECTIVE",
  "082": "ATMOSPHERIC PERSPECTIVE",
  "083": "SHALLOW DEPTH OF FIELD",
  "084": "DEEP FOCUS COMPOSITION",
  "085": "PLANAR COMPOSITION",
  "086": "DEEP SPACE COMPOSITION",
  "087": "RADIAL BALANCE",
  "088": "CRYSTALLOGRAPHIC BALANCE",
  "089": "STATIC COMPOSITION",
  "090": "DYNAMIC COMPOSITION",
  "091": "OPEN COMPOSITION",
  "092": "CLOSED COMPOSITION",
  "093": "SINGLE FOCAL POINT",
  "094": "MULTIPLE FOCAL POINTS",
  "095": "VISUAL HIERARCHY",
  "096": "DOMINANCE & SUBORDINATION",
  "097": "BALANCE PRINCIPLE",
  "098": "PROPORTION PRINCIPLE",
  "099": "SCALE CONTRAST",
  "100": "LIGHT & DARK CONTRAST",
  "101": "COLOR CONTRAST",
  "102": "SHAPE CONTRAST",
  "103": "TEXTURE CONTRAST",
  "104": "MOTION-STASIS CONTRAST",
  "105": "JUXTAPOSITION PRINCIPLE",
  "106": "ISOLATION PRINCIPLE",
  "107": "REPETITION PRINCIPLE",
  "108": "PATTERN ORGANIZATION",
  "109": "RHYTHM ORGANIZATION",
  "110": "GRADATION RHYTHM",
  "111": "ALTERNATING RHYTHM",
  "112": "PROGRESSIVE RHYTHM",
  "113": "FLOWING RHYTHM",
  "114": "RANDOM RHYTHM",
  "115": "SIMILARITY PRINCIPLE",
  "116": "PROXIMITY PRINCIPLE",
  "117": "CONTINUITY PRINCIPLE",
  "118": "CLOSURE PRINCIPLE",
  "119": "FIGURE-GROUND RELATION",
  "120": "COMMON REGION PRINCIPLE",
  "121": "COMMON FATE PRINCIPLE",
  "122": "SIMPLICITY PRINCIPLE",
  "123": "CROPPING COMPOSITION",
  "124": "FULL-BLEED COMPOSITION",
  "125": "DENSITY CONTRAST",
  "126": "GROUPING COMPOSITION",
  "127": "F-SHAPED READING PATTERN",
  "128": "Z-SHAPED READING PATTERN",
  "129": "GUTENBERG DIAGRAM",
  "130": "LAYER-CAKE PATTERN",
  "131": "SPOTTING SCAN PATTERN",
  "132": "SINGLE-COLUMN LAYOUT",
  "133": "TWO-COLUMN LAYOUT",
  "134": "MULTI-COLUMN LAYOUT",
  "135": "SYMMETRICAL SPREAD",
  "136": "ASYMMETRICAL SPREAD",
  "137": "PANORAMIC SPREAD",
  "138": "FULL-BLEED LAYOUT",
  "139": "MARGIN-BOUND LAYOUT",
  "140": "IMAGE-DOMINANT LAYOUT",
  "141": "TEXT-DOMINANT LAYOUT",
  "142": "HEADLINE-DOMINANT LAYOUT",
  "143": "IMAGE WINDOW LAYOUT",
  "144": "FRAMEWORK LAYOUT",
  "145": "MULTI-PANEL LAYOUT",
  "146": "MONDRIAN LAYOUT",
  "147": "CIRCUS LAYOUT",
  "148": "SILHOUETTE LAYOUT",
  "149": "TYPOGRAPHIC FORM LAYOUT",
  "150": "VISUAL REBUS LAYOUT",
  "151": "COLLAGE LAYOUT",
  "152": "MONTAGE LAYOUT",
  "153": "MODULAR PAGE",
  "154": "BLOCK LAYOUT",
  "155": "INSET LAYOUT",
  "156": "SIDEBAR LAYOUT",
  "157": "MARGINALIA LAYOUT",
  "158": "WRAP-AROUND LAYOUT",
  "159": "FLOATING BLOCK LAYOUT",
  "160": "COVER LAYOUT",
  "161": "CHAPTER OPENING PAGE",
  "162": "SECTION OPENING PAGE",
  "163": "FEATURE SPREAD",
  "164": "TABLE OF CONTENTS",
  "165": "INDEX LAYOUT",
  "166": "CATALOG LAYOUT",
  "167": "PULL-QUOTE DOMINANT",
  "168": "AXIAL TYPE SYSTEM",
  "169": "RADIAL TYPE SYSTEM",
  "170": "DILATATIONAL TYPE SYSTEM",
  "171": "RANDOM TYPE SYSTEM",
  "172": "GRID TYPE SYSTEM",
  "173": "MODULAR TYPE SYSTEM",
  "174": "TRANSITIONAL TYPE SYSTEM",
  "175": "BILATERAL TYPE SYSTEM",
  "176": "FLUSH LEFT RAGGED RIGHT",
  "177": "FLUSH RIGHT RAGGED LEFT",
  "178": "CENTERED TYPOGRAPHY",
  "179": "JUSTIFIED TYPOGRAPHY",
  "180": "FORCE JUSTIFIED TYPOGRAPHY",
  "181": "ASYMMETRICAL TYPOGRAPHY",
  "182": "CONTOUR TEXT WRAP",
  "183": "RECTANGULAR TEXT WRAP",
  "184": "CROSS-COLUMN HEADLINE",
  "185": "HANGING INDENT",
  "186": "FIRST-LINE INDENT",
  "187": "HANGING PUNCTUATION",
  "188": "BASELINE ALIGNMENT",
  "189": "SHAPED TEXT",
  "190": "CALLIGRAM TYPOGRAPHY",
  "191": "TYPE ON A PATH",
  "192": "VERTICAL TYPOGRAPHY",
  "193": "HORIZONTAL TYPOGRAPHY",
  "194": "MANUSCRIPT GRID",
  "195": "COLUMN GRID",
  "196": "MODULAR GRID",
  "197": "HIERARCHICAL GRID",
  "198": "BASELINE GRID",
  "199": "COMPOUND GRID",
  "200": "ASYMMETRICAL GRID",
  "201": "SQUARE GRID",
  "202": "ISOMETRIC GRID",
  "203": "RADIAL GRID",
  "204": "POLAR COORDINATE GRID",
  "205": "NESTED GRID",
  "206": "SUBGRID",
  "207": "FIXED GRID",
  "208": "FLUID GRID",
  "209": "RESPONSIVE GRID",
  "210": "GRID-BREAKING LAYOUT",
  "211": "DECONSTRUCTED GRID",
  "212": "HORIZONTAL LTR",
  "213": "HORIZONTAL RTL",
  "214": "VERTICAL RTL",
  "215": "VERTICAL LTR",
  "216": "MIXED VERTICAL-HORIZONTAL",
  "217": "TATE-CHU-YOKO",
  "218": "VERTICAL ROTATED LATIN",
  "219": "VERTICAL UPRIGHT LATIN",
  "220": "BIDIRECTIONAL TYPOGRAPHY",
  "221": "RUBY ANNOTATION LAYOUT",
  "222": "NORMAL FLOW LAYOUT",
  "223": "BLOCK-LEVEL LAYOUT",
  "224": "INLINE LAYOUT",
  "225": "BLOCK FORMATTING CONTEXT",
  "226": "FLEXBOX LAYOUT",
  "227": "CSS GRID LAYOUT",
  "228": "CSS SUBGRID LAYOUT",
  "229": "CSS MULTI-COLUMN",
  "230": "CSS TABLE LAYOUT",
  "231": "FLOAT LAYOUT",
  "232": "RELATIVE POSITIONING",
  "233": "ABSOLUTE POSITIONING",
  "234": "FIXED POSITIONING",
  "235": "STICKY POSITIONING",
  "236": "MASONRY LAYOUT",
  "237": "OVERLAY LAYOUT",
  "238": "FIXED-WIDTH LAYOUT",
  "239": "FLUID LAYOUT",
  "240": "RESPONSIVE LAYOUT",
  "241": "ADAPTIVE LAYOUT",
  "242": "CONTAINER QUERIES LAYOUT",
  "243": "STACK PRIMITIVE",
  "244": "BOX PRIMITIVE",
  "245": "CENTER PRIMITIVE",
  "246": "CLUSTER PRIMITIVE",
  "247": "SIDEBAR PRIMITIVE",
  "248": "SWITCHER PRIMITIVE",
  "249": "COVER PRIMITIVE",
  "250": "GRID PRIMITIVE",
  "251": "FRAME RATIO PRIMITIVE",
  "252": "REEL HORIZONTAL SCROLL",
  "253": "FLOATING LAYER",
  "254": "ICON-TEXT COMBO",
  "255": "SINGLE-COLUMN PAGE",
  "256": "TWO-COLUMN PAGE",
  "257": "THREE-COLUMN PAGE",
  "258": "SIDEBAR PAGE",
  "259": "SPLIT-SCREEN LAYOUT",
  "260": "HOLY GRAIL LAYOUT",
  "261": "HEADER-MAIN-FOOTER",
  "262": "TOP-NAV LAYOUT",
  "263": "NAVIGATION DRAWER",
  "264": "BOTTOM-NAV LAYOUT",
  "265": "TABS LAYOUT",
  "266": "ACCORDION LAYOUT",
  "267": "LIST-DETAIL LAYOUT",
  "268": "AUXILIARY PANE LAYOUT",
  "269": "FEED LAYOUT",
  "270": "CARD GRID LAYOUT",
  "271": "MASONRY PAGE",
  "272": "BENTO BOX LAYOUT",
  "273": "DASHBOARD LAYOUT",
  "274": "DATA TABLE LAYOUT",
  "275": "GALLERY LAYOUT",
  "276": "CAROUSEL LAYOUT",
  "277": "TIMELINE LAYOUT",
  "278": "KANBAN BOARD LAYOUT",
  "279": "CALENDAR LAYOUT",
  "280": "TREE-VIEW LAYOUT",
  "281": "CONVERSATIONAL UI",
  "282": "MAP-DOMINANT LAYOUT",
  "283": "CANVAS WORKSPACE",
  "284": "FORM LAYOUT",
  "285": "STEP-FORM WIZARD",
  "286": "SEARCH RESULTS LAYOUT",
  "287": "SETTINGS PAGE LAYOUT",
  "288": "MEDIA OBJECT LAYOUT",
  "289": "HERO SECTION LAYOUT",
  "290": "TIERED NAVIGATION",
  "291": "MOSTLY FLUID PATTERN",
  "292": "COLUMN DROP PATTERN",
  "293": "LAYOUT SHIFTER PATTERN",
  "294": "TINY TWEAKS PATTERN",
  "295": "OFF-CANVAS PATTERN",
  "296": "STACK REORDERING",
  "297": "SEQUENCE REORDERING",
  "298": "FOLDED DUAL PANE",
  "299": "ADAPTIVE GRID REFLOW",
  "300": "COMPONENT-LEVEL RESPONSIVE",
  "301": "SINGLE-CHARACTER SHOT",
  "302": "TWO-SHOT COMPOSITION",
  "303": "THREE-SHOT COMPOSITION",
  "304": "CROWD / ENSEMBLE SHOT",
  "305": "OVER-THE-SHOULDER SHOT",
  "306": "POINT-OF-VIEW SHOT",
  "307": "OBJECTIVE-VIEW SHOT",
  "308": "CLEAN SINGLE SHOT",
  "309": "DIRTY SINGLE SHOT",
  "310": "DEEP BLOCKING",
  "311": "PLANAR BLOCKING",
  "312": "TRIANGULAR BLOCKING",
  "313": "LATERAL BLOCKING",
  "314": "MULTI-LAYER FOREGROUND BLOCKING",
  "315": "HIGH DISTANCE (GAO YUAN)",
  "316": "DEEP DISTANCE (SHEN YUAN)",
  "317": "LEVEL DISTANCE (PING YUAN)",
  "318": "SYNTHETIC THREE DISTANCES",
  "319": "SCATTERED PERSPECTIVE",
  "320": "ROAMING VISION COMPOSITION",
  "321": "PANORAMIC VISTA COMPOSITION",
  "322": "ONE RIVER TWO BANKS",
  "323": "CORNER-BOUND (BIAN JIAO)",
  "324": "CROPPED VISTA (JIE JING)",
  "325": "CUT-BRANCH (ZHE ZHI)",
  "326": "NEGATIVE SPACE (LIU BAI)",
  "327": "VALUING THE VOID (JI BAI DANG HEI)",
  "328": "VOID & SOLID HARMONY",
  "329": "DENSITY & SPARSENESS",
  "330": "HOST & GUEST RELATION",
  "331": "OPENING & CLOSING (KAI HE)",
  "332": "DEVELOPMENTAL FLOW (QI CHENG ZHUAN HE)",
  "333": "CONCEALING & REVEALING",
  "334": "ASYMMETRICAL BALANCE (QI ZHENG)",
  "335": "TITLE SLIDE LAYOUT",
  "336": "TITLE & CONTENT SLIDE",
  "337": "SECTION HEADER SLIDE",
  "338": "TWO-COLUMN CONTENT SLIDE",
  "339": "COMPARISON SLIDE LAYOUT",
  "340": "TITLE-ONLY SLIDE LAYOUT",
  "341": "BLANK CANVAS SLIDE",
  "342": "CONTENT & CAPTION SLIDE",
  "343": "IMAGE & CAPTION SLIDE",
  "344": "BIG NUMBER STAT SLIDE",
  "345": "PULL-QUOTE SLIDE LAYOUT",
  "346": "TIMELINE ROADMAP SLIDE",
  "347": "PROCESS FLOW SLIDE",
  "348": "MATRIX QUADRANT SLIDE",
  "349": "DATA CHART SLIDE LAYOUT",
  "350": "FULL-BLEED HERO SLIDE"
}

# 33 Subcategory Design Profiles
SUBCATEGORY_PROFILES = {
    # 01 构图逻辑
    "经典法则与空间留白": {
        "theme": "warm-ivory",
        "focus_type": "classic_rule",
        "default_subject": "A majestic minimalist landscape with solitary traveler and architectural focal anchor",
        "keywords": ["黄金分割", "三分网格", "负空间", "视线导引"],
        "keywords_en": ["Golden Ratio", "Thirds Grid", "Negative Space", "Eye Lead"],
        "tagline": "以几何分割与比例定势，构建画面的首要秩序与呼吸感。",
        "features": [
            ("比例锚定", "Proportion Anchor", "严格遵循黄金比例或均分网格确立画面几何重力点，锁定第一注意力。"),
            ("留白定界", "Space Delimitation", "借由宽广的负空间赋予视觉主体充足呼吸域，消除信息窒息感。"),
            ("动势延伸", "Kinetic Extension", "沿分割辅助线构建视线滑行轨迹，形成从局部通往全局的稳定导引。")
        ],
        "tips": [
            ("视觉基准", "确立主视觉交叉点时，优先将核心元素置于第一强交点，次要信息落入对角弱区。"),
            ("留白控制", "保持至少 40% 以上的有效负空间，确保画面呼吸顺畅与层级通透。")
        ]
    },
    "重心、线条与轴线": {
        "theme": "cobalt-blue",
        "focus_type": "axial_linear",
        "default_subject": "Soaring suspension bridge cables and stark diagonal architectural beams under clean directional light",
        "keywords": ["力场轴线", "倾斜张力", "重力平衡", "动势收束"],
        "keywords_en": ["Force Axis", "Oblique Tension", "Gravity Balance", "Motion Convergence"],
        "tagline": "以轴线贯穿力场，用骨架线条撬动静态空间的动势张力。",
        "features": [
            ("轴线骨架", "Axis Framework", "以强烈的线性走势贯穿画幅，分割版面体量并确立视觉方向。"),
            ("倾斜动能", "Kinetic Tilt", "打破水平垂直的死板平衡，借助斜向夹角传递速度感与冲击力。"),
            ("重力平衡", "Mass Balance", "通过对边或异形区块的质量对冲，实现非对称中的力学均势。")
        ],
        "tips": [
            ("轴线对齐", "标题与关键图元必须沿主要视觉轴线定位，强化整体骨骼硬度。"),
            ("张力收敛", "倾斜线条延伸至版面边缘时，需有端点重物或对立小元素进行视觉刹车。")
        ]
    },
    "字母形与曲线": {
        "theme": "warm-ivory",
        "focus_type": "curved_flow",
        "default_subject": "A winding alpine roadway gracefully curving through misty valley slopes and forest ridges",
        "keywords": ["流动曲线", "字母构架", "视线巡航", "柔性韵律"],
        "keywords_en": ["Flow Curve", "Letterform Frame", "Visual Cruise", "Soft Rhythm"],
        "tagline": "依循字母骨架与柔美曲线，牵引视线自然蜿蜒游弋。",
        "features": [
            ("形态隐喻", "Form Metaphor", "提取经典字母或弧线轨迹为隐性骨架，赋予构图优雅舒展的辨识度。"),
            ("连续巡航", "Continuous Cruise", "顺应人眼追踪曲度流动的本能，引导视线从起始端自然滑向落脚点。"),
            ("空间环抱", "Spatial Embrace", "弧度内凹区域形成天然的视觉避风港，适合承载核心阐释文本。")
        ],
        "tips": [
            ("曲线连贯", "曲线起伏需保持连续的曲率过渡，避免突兀尖角切断视觉流向。"),
            ("焦点落点", "将关键结论或标志置于曲线终点拐弯处，实现自然的停驻记忆。")
        ]
    },
    "几何形与放射结构": {
        "theme": "obsidian-black",
        "focus_type": "geometric_radial",
        "default_subject": "Dynamic architectural atrium skylight with radiating beams converging at a glowing central nexus",
        "keywords": ["几何凝聚", "放射能量", "中心汇聚", "向心张力"],
        "keywords_en": ["Geometric Cohesion", "Radial Energy", "Convergence", "Centripetal Tension"],
        "tagline": "以纯粹几何体块聚散与放射线束，汇聚高密度的视觉冲击能量。",
        "features": [
            ("能量源点", "Energy Nexus", "以中心点或基准形为核，产生强烈的向心凝聚或离心爆发能量场。"),
            ("几何切分", "Geometric Division", "运用正圆、三角、多边形强力分割背景，确立极简而强烈的图底反差。"),
            ("节奏递进", "Rhythmic Step", "放射线束按严格的角度递增排列，营造精密严谨的工程美感。")
        ],
        "tips": [
            ("中心突出", "放射中心必须有明确的实体重心，避免射线空悬导致视线无处落脚。"),
            ("密度疏密", "向外扩散时注意线束与形状的疏密渐变，保持边缘呼吸感。")
        ]
    },
    "阵列、层叠与组群": {
        "theme": "obsidian-black",
        "focus_type": "array_pattern",
        "default_subject": "Precision repetitive architectural facade modules and rhythmic geometric patterns in high contrast",
        "keywords": ["单元阵列", "层叠覆映", "韵律节拍", "模块秩序"],
        "keywords_en": ["Unit Array", "Layer Overlap", "Rhythmic Beat", "Modular Order"],
        "tagline": "通过单元复现与层次堆叠，在无限秩序中编织丰富韵律。",
        "features": [
            ("模数基底", "Modular Base", "以标准化几何单元为母题重复排布，建立高度工业化的秩序底座。"),
            ("微变破局", "Variation Accent", "在严谨的规律阵列中引入单点破格，瞬间激活全局生机。"),
            ("深度叠压", "Depth Stacking", "图层前后覆映产生丰富的物理阴影与虚实进深感。")
        ],
        "tips": [
            ("间距均一", "阵列单元的外间距（Gutter）必须保持像素级等距，确保秩序严密。"),
            ("破格克制", "整版破格点不得超过两处，过多异变会瓦解阵列本身的秩序价值。")
        ]
    },
    "空间层次与投影": {
        "theme": "forest-green",
        "focus_type": "spatial_projection",
        "default_subject": "Multi-planar architectural interior with dramatic light shafts cutting through layered foreground arches",
        "keywords": ["景深层次", "空间投影", "透视进深", "重叠穿透"],
        "keywords_en": ["Depth Layers", "Projection", "Perspective Inset", "Overlap"],
        "tagline": "在二维平面中建构纵深维度，营造前中后景的层层穿透。",
        "features": [
            ("三维纵深", "Three-Plane Depth", "严格界定前景遮挡、中景主体与远景环境，拉伸画面的空间纵深。"),
            ("透视导引", "Perspective Lead", "利用消逝点线条压缩空间比例，产生强烈的空间吸入感。"),
            ("光影切割", "Chiaroscuro Cut", "利用明暗投影界定空间切面，增强体块与空气的距离感。")
        ],
        "tips": [
            ("前景压暗", "前景遮挡物适当降低明度或增加剪影化处理，衬托中景高亮主体。"),
            ("尺度反差", "前景物体与远景要素形成悬殊的尺度比例，能极大增强画面的宏大感。")
        ]
    },
    "视点、景深与空间感": {
        "theme": "forest-green",
        "focus_type": "depth_perspective",
        "default_subject": "A multi-layered scenery with rich foreground, detailed midground, and expansive horizon background",
        "keywords": ["极端视点", "虚实景深", "超焦全清", "透视形变"],
        "keywords_en": ["Extreme Viewpoint", "Selective Focus", "Deep Focus", "Perspective Warp"],
        "tagline": "转换观察视点与景深虚实，重塑日常经验的非常规张力。",
        "features": [
            ("机位转换", "Camera Angle", "脱离普通平视视线，采用俯仰或微距视点唤醒视觉新鲜感。"),
            ("虚实过滤", "Focus Filter", "利用焦内清晰与焦外光斑的落差，极简化剥离杂乱背景干扰。"),
            ("宏微对立", "Macro-Micro Contrast", "通过近大远小的透视夸张，将微小物象放大为震撼画面的视觉霸权。")
        ],
        "tips": [
            ("焦平面定位", "焦平面必须严谨落在核心传意元件上，禁止模糊不清的游离对焦。"),
            ("环境留存", "虚化背景仍需保留辨识轮廓的色彩基调，服务于整体情境交代。")
        ]
    },

    # 02 视觉原则与阅读模式
    "平衡、动势与焦点": {
        "theme": "warm-ivory",
        "focus_type": "balance_focal",
        "default_subject": "Abstract kinetic sculpture balancing bold spheres and slender beams in harmonic equilibrium",
        "keywords": ["动态平衡", "视觉重力", "单一据点", "力量对抗"],
        "keywords_en": ["Dynamic Balance", "Visual Gravity", "Focal Anchor", "Force Confrontation"],
        "tagline": "在力的对立与抗衡中，构筑静中有动的永恒均势。",
        "features": [
            ("杠杆支点", "Lever Fulcrum", "通过不对称元素的面积与距离调配，达成如同天平般的物理平衡感。"),
            ("动态预压", "Kinetic Preload", "让画面元素呈现即将运动的倾斜临界态，蓄积强烈的视觉张力。"),
            ("单一聚核", "Singular Focus", "确保全画幅存在压倒性的第一焦点，彻底消除层级摇摆。")
        ],
        "tips": [
            ("视觉重量", "深色与密集肌理具有更大视觉重量，需用更大面积的浅色负空间去抗衡。"),
            ("焦点排他", "同一焦区内严禁放置竞争性高对比要素，确保目光瞬间锁定。")
        ]
    },
    "层级、比例与对比": {
        "theme": "cobalt-blue",
        "focus_type": "hierarchy_contrast",
        "default_subject": "Monumental stark typographic letterforms towering over miniature human figures in graphic contrast",
        "keywords": ["阶梯层级", "悬殊尺度", "明暗对冲", "首要权重"],
        "keywords_en": ["Stepped Hierarchy", "Scale Contrast", "Light-Dark Clash", "Dominant Weight"],
        "tagline": "以悬殊的反差拉开信息阶梯，建立毫无歧义的阅读顺序。",
        "features": [
            ("级差跃升", "Tiered Leap", "主副标题与正文采用 3 倍以上的字阶跳跃，打造刀刻般的秩序界线。"),
            ("双极对立", "Bipolar Opposition", "将大与小、黑与白、粗与细强力并置，在对抗中凸显核心。"),
            ("权重分配", "Weight Distribution", "以精准的面积配比确立 60-30-10 比例规则，保证主次分明。")
        ],
        "tips": [
            ("对比果决", "对比必须显著坚决，微小的比例差异容易被误读为对齐失误。"),
            ("层级收束", "全版层级严格控制在 3 到 4 级以内，避免层级过多导致认知过载。")
        ]
    },
    "重复、图案与节奏": {
        "theme": "obsidian-black",
        "focus_type": "rhythm_pattern",
        "default_subject": "Harmonic optical wave lines and rhythmic dot patterns undulating across an ebony background",
        "keywords": ["律动节拍", "渐变波浪", "图案织造", "周期共振"],
        "keywords_en": ["Rhythmic Beat", "Gradient Undulation", "Pattern Weave", "Periodic Resonance"],
        "tagline": "让视觉元素如音符般起伏跳跃，在重复中鸣响共振旋律。",
        "features": [
            ("节奏脉冲", "Rhythmic Pulse", "通过形状的间歇性出现与间距变化，为版面赋予音乐节拍般的动感。"),
            ("渐变过渡", "Gradual Transition", "尺度、透明度或色彩由浓至淡连续渐变，牵引视线丝滑推进。"),
            ("肌理织造", "Texture Weaving", "微小符号的周期性排列转化为丰富的底纹肌理，提升细节耐看度。")
        ],
        "tips": [
            ("节拍定调", "确定好画面的基础节拍（快节奏短步长 vs 慢节奏宽留白），全版统一。"),
            ("断点设计", "在持续重复的图案中设置一个突变缺口，能形成极强的关注焦点。")
        ]
    },
    "格式塔与组群": {
        "theme": "forest-green",
        "focus_type": "gestalt_grouping",
        "default_subject": "Abstract geometric shapes spontaneously forming a coherent silhouette through human perceptual closure",
        "keywords": ["格式塔", "邻近亲和", "闭合联想", "图底互换"],
        "keywords_en": ["Gestalt", "Proximity Affiliation", "Closure Association", "Figure-Ground Inversion"],
        "tagline": "调动人类知觉的完形本能，让离散符号自发凝聚为整体意象。",
        "features": [
            ("空间邻近", "Spatial Proximity", "物理距离相近的离散点自动被知觉结为同一组块，清晰区分内容组。"),
            ("闭合联想", "Mind Closure", "刻意留下开放缺口，激发观者大脑在潜意识中自行补全完美几何。"),
            ("图底反转", "Figure-Ground Inversion", "正负形空间共享轮廓，创造双重解读与意涵互文的智力愉悦。")
        ],
        "tips": [
            ("组间留白", "组与组之间的外边距必须大于组内元素的内间距至少 2 倍，确保分组清晰。"),
            ("共同命运", "具有相同行进方向或形态趋势的元素应赋予统一的色彩，强化同一性感知。")
        ]
    },
    "页面阅读模式": {
        "theme": "warm-ivory",
        "focus_type": "reading_patterns",
        "default_subject": "Clean heat-map overlay tracing the natural human eye movement across an editorial typographic page",
        "keywords": ["视线动线", "古腾堡图", "F型扫描", "黄金落点"],
        "keywords_en": ["Gaze Pathway", "Gutenberg Diagram", "F-Pattern Scan", "Terminal Anchor"],
        "tagline": "顺应人类眼动的生理惯性，在视线必经之路布设价值锚点。",
        "features": [
            ("入口强击", "Primary Optical Area", "页面左上方第一落脚点布置决定性的品牌徽标与大标题。"),
            ("横扫下潜", "Horizontal Sweep", "遵循自左向右扫读后再向下的规律，在行首安置高亮词组。"),
            ("终点收网", "Terminal Area Catch", "右下角终点区域部署行动号召（CTA）或核心结论，完成闭环。")
        ],
        "tips": [
            ("闲置区弱化", "右上与左下为弱势闲置区，适合放置辅助页码、日期等低频参考信息。"),
            ("打断扫描", "在 F 型长正文中穿插醒目的引语块或小图，能打断疲劳，重新唤醒注意。")
        ]
    },

    # 03 平面、出版与广告
    "分栏、跨页与出血": {
        "theme": "forest-green",
        "focus_type": "editorial_columns",
        "default_subject": "Swiss modern editorial spread with multi-column rhythm, balanced gutters, and bold typographic blocks",
        "keywords": ["网格分栏", "连贯跨页", "满版出血", "边距呼吸"],
        "keywords_en": ["Column Grid", "Spread Continuity", "Full Bleed", "Margin Breath"],
        "tagline": "以严谨分栏规整海量信息，用跨页满幅释放无限张力。",
        "features": [
            ("栏线律动", "Column Rhythm", "等宽分栏与栏间距规范行长，维持极度舒适的持续阅读节拍。"),
            ("破页贯通", "Spread Crossing", "主体图像横跨中缝跨页展开，打破单页局限，倍增版面气魄。"),
            ("出血张力", "Bleed Tension", "将色块或图片直接裁切至纸张物理边缘，制造画面向外无限延伸的假象。")
        ],
        "tips": [
            ("最佳行长", "单栏文字行长控制在 35-45 个中文字符，避免视线换行疲劳。"),
            ("中缝规避", "跨页排版时严禁将人物面部或核心文字压在中缝折线处。")
        ]
    },
    "图文主导与表现型版式": {
        "theme": "obsidian-black",
        "focus_type": "expressive_layout",
        "default_subject": "High-fashion magazine cover blending bold architectural portraiture with avant-garde layout geometry",
        "keywords": ["图片主导", "文字建筑", "窗口剪影", "表现张力"],
        "keywords_en": ["Image Dominant", "Type Architecture", "Window Silhouette", "Expressive Tension"],
        "tagline": "让图像统治视野，使文字化身建筑，碰撞出戏剧性的表现力量。",
        "features": [
            ("视觉巨幕", "Visual Canvas", "高质量大幅画面占据 70% 以上面积，先声夺人确立情感基调。"),
            ("字图嵌合", "Type-Image Interlock", "大号标题穿插在人物或构筑物前后，营造前后遮挡的立体纵深。"),
            ("视窗裁切", "Window Crop", "利用特定几何镂空视窗展示画面局部，制造窥探式的悬念感。")
        ],
        "tips": [
            ("文字压图", "在复杂图像上压字时，必须添加纯色垫底、微弱投影或选择图像平坦低频区。"),
            ("图文调性", "文字字体的性格（刚劲/温润/尖锐）必须与主图情绪形成精准互文。")
        ]
    },
    "模块、侧栏与图文关系": {
        "theme": "warm-ivory",
        "focus_type": "modular_blocks",
        "default_subject": "Modular architectural blueprint layout with elegant metadata sidebar and precision callout blocks",
        "keywords": ["模块分区", "侧栏导读", "边注伴随", "图文嵌合"],
        "keywords_en": ["Modular Section", "Sidebar Lead", "Marginalia", "Text-Image Fit"],
        "tagline": "用模块规整复杂脉络，借侧栏边注赋予版面从容叙事。",
        "features": [
            ("区块解耦", "Block Decoupling", "不同信息单元装入独立模块盒子中，实现高信噪比的并列陈列。"),
            ("双线叙事", "Dual-Track Narrative", "主文走中心大栏，侧栏承载延伸知识与快读摘要，互不干扰。"),
            ("边注呼应", "Marginalia Dialogue", "注释与微缩图紧贴关联段落，视线水平平移即可完成释义查阅。")
        ],
        "tips": [
            ("侧栏比例", "侧栏宽度通常占总版面宽度的 25% - 30%，保持从属地位。"),
            ("模块对齐", "相邻模块的上下边线必须严格吸附至基准网格，避免参差碎乱。")
        ]
    },
    "出版功能页面": {
        "theme": "warm-ivory",
        "focus_type": "publishing_pages",
        "default_subject": "Exquisite book chapter title page with fine rules, elegant roman numerals, and vast paper negative space",
        "keywords": ["章节门扉", "目录层级", "版权严谨", "引语留白"],
        "keywords_en": ["Chapter Portal", "TOC Hierarchy", "Colophon Rigor", "Pull-Quote Space"],
        "tagline": "于仪式感中开启新章节，在经典秩序中凝练典籍风骨。",
        "features": [
            ("典雅扉页", "Chapter Gateway", "大面积静谧留白衬托粗大章节编号，为阅读节奏提供情绪缓冲台阶。"),
            ("多阶目录", "Multi-Tier TOC", "点线导引、页码右齐与篇名错落，化繁复索书路径为几何风景。"),
            ("金句聚焦", "Quote Dominant", "放大字号将核心哲理引语居中悬置，配合巨大装饰引号震慑人心。")
        ],
        "tips": [
            ("留白定调", "章节扉页的空白率应显著高于普通正文页，营造板块切换的心理仪式。"),
            ("前导对齐", "目录点线（Dot Leader）点间距要宽松均匀，页码必须统一右对齐。")
        ]
    },

    # 04 字体、网格与东亚文字
    "字体组织系统": {
        "theme": "cobalt-blue",
        "focus_type": "typographic_systems",
        "default_subject": "Comprehensive typographical hierarchy specimen sheet showing axial, radial, and modular type systems",
        "keywords": ["字体系统", "轴线对齐", "字阶级差", "文字构架"],
        "keywords_en": ["Type System", "Axial Alignment", "Scale Ladder", "Type Framework"],
        "tagline": "以理性系统组织文字，使字符在空间中构建自洽的建筑学逻辑。",
        "features": [
            ("系统骨架", "Systemic Skeleton", "基于固定轴线或网格生成文字阵列，彻底规避随机散落的混乱。"),
            ("音阶比例", "Harmonic Scale", "字体字号严格按照和声比率（如 1.25 / 1.5）递增，自然天成。"),
            ("灰度匀称", "Type Gray Tone", "调控字距（Tracking）与行距（Leading），呈现完美均匀的正文纸张灰度。")
        ],
        "tips": [
            ("字体克制", "单幅作品中使用的字族（Font Family）不得超过 2 款，通过字重变化表现丰富度。"),
            ("行距黄金比", "正文行距通常设置为字号的 1.5 至 1.8 倍，确保阅读时视线换行精准。")
        ]
    },
    "对齐、缩进与文字造型": {
        "theme": "cobalt-blue",
        "focus_type": "type_alignment",
        "default_subject": "Experimental typographic poster demonstrating contour text wraps and architectural ragged edges",
        "keywords": ["对齐参差", "文字绕排", "凸排悬挂", "文字造型"],
        "keywords_en": ["Ragged Alignment", "Contour Wrap", "Hanging Indent", "Typographic Form"],
        "tagline": "在边缘参差与精准对齐的毫厘之间，打磨文字的诗性肌理。",
        "features": [
            ("参差飞白", "Ragged Edge Rhythm", "左齐右参差在右侧制造富有活力的自然浪花边缘，消除两端强扭的字间空洞。"),
            ("悬挂凸排", "Hanging Punctuation", "将标点与缩进悬挂至外边距，保持正文阅读垂直线如刀切般绝对平直。"),
            ("轮廓环抱", "Contour Wrapping", "正文依随图形边缘流淌，文字本身化为勾勒主体轮廓的质感笔触。")
        ],
        "tips": [
            ("避免孤字", "严格消除段落末行的孤字（Widow）与页面首行的孤行（Orphan）。"),
            ("凸排对齐", "引号、括号必须推出版芯左对齐线外，让视觉文字块边缘形成真正的直线。")
        ]
    },
    "网格系统": {
        "theme": "cobalt-blue",
        "focus_type": "grid_systems",
        "default_subject": "Pristine Swiss International Typographic grid diagram with visible red guidelines and mathematical subdivisions",
        "keywords": ["瑞士网格", "基准网格", "模块矩阵", "破格解构"],
        "keywords_en": ["Swiss Grid", "Baseline Grid", "Modular Matrix", "Grid Breaking"],
        "tagline": "以数学精度划分版面天地，于不可撼动的铁律中催生自由。",
        "features": [
            ("全幅咬合", "Snap to Grid", "所有图元与文本块上下左右严格吸附网格线，实现严丝合缝的秩序共振。"),
            ("基线韵律", "Baseline Harmony", "各栏文本无论字号大小，正文基线全部垂直对齐在恒定模数网格线上。"),
            ("破格聚焦", "Calculated Break", "在严密的九宫/十六宫矩阵中让单一主角冲破网格边缘，诞生万钧张力。")
        ],
        "tips": [
            ("网格先定", "动笔前必须先根据内容复杂度设定网格（单栏/三栏/十二栏），全程绝不动摇。"),
            ("留白占位", "网格单元允许成片留空，留空的模块本身就是重要的结构性呼吸体块。")
        ]
    },
    "东亚文字与混排": {
        "theme": "warm-ivory",
        "focus_type": "east_asian_type",
        "default_subject": "Harmonious bilingual Chinese and Latin typography poster with vertical and horizontal mixed alignment",
        "keywords": ["方块字韵", "横直混排", "纵中横排", "中西匹配"],
        "keywords_en": ["CJK Character Tone", "Mixed Direction", "Tate-Chu-Yoko", "CJK-Latin Pairing"],
        "tagline": "融合方块汉字的端庄气度与西文字母的几何流动，成就混排至美。",
        "features": [
            ("直排风骨", "Vertical Splendor", "自上而下、自右向左的竖排流向，承续古典东方书籍的宁静与凝炼。"),
            ("纵中横排", "Tate-Chu-Yoko", "在直排纵行中将 2-3 位阿拉伯数字横向嵌入，保持排版流动的现代紧凑。"),
            ("字形平衡", "Optical Balancing", "精准调整中文字与英文字母的基线和字重比差，消除中西文混排的跳动感。")
        ],
        "tips": [
            ("西文字距", "中西文混排时，汉字与英文单词之间强制插入四分之一汉字宽的盘面间距（U+0020）。"),
            ("避头尾法则", "标点符号绝对禁止出现在行首（句号逗号等）或行尾（前括号等），必须合规挤压。")
        ]
    },

    # 05 网页与 UI
    "CSS 流、定位与响应": {
        "theme": "cobalt-blue",
        "focus_type": "css_layout_engine",
        "default_subject": "Technical wireframe diagram illustrating CSS flexbox, grid, subgrid, and modern box formatting models",
        "keywords": ["文档流", "弹性盒子", "网格自适应", "容器查询"],
        "keywords_en": ["Document Flow", "Flexbox", "Grid Adaptation", "Container Queries"],
        "tagline": "以现代化 CSS 布局引擎，构筑自适应万千设备的弹性流体系统。",
        "features": [
            ("流式天性", "Fluid Nature", "基于块级与行内流模型，让信息体块随容器视口尺寸自由伸缩流淌。"),
            ("轴向分布", "Flex Distribution", "通过主轴与交叉轴的对齐控制，轻松驾驭多元素均分与自适应居中。"),
            ("二维矩阵", "2D Grid Mastery", "利用 CSS Grid 的行与列命名线，精准锁定任何复杂跨区域 UI 排版。")
        ],
        "tips": [
            ("响应式断点", "基于内容本身破损点设定断点（Breakpoints），而非僵化死守特定手机型号尺寸。"),
            ("相对单位", "优先使用 rem、em、% 与 min(), max(), clamp()，赋予整体布局有机弹性。")
        ]
    },
    "布局原语": {
        "theme": "cobalt-blue",
        "focus_type": "layout_primitives",
        "default_subject": "Modular UI primitives showing Stack, Box, Center, Cluster and Reel components in a design system",
        "keywords": ["布局原语", "垂直堆栈", "自适应簇", "居中原语"],
        "keywords_en": ["Layout Primitive", "Vertical Stack", "Auto Cluster", "Center Primitive"],
        "tagline": "将复杂界面解构为原子级布局原语，以无状态组件组装万千世界。",
        "features": [
            ("垂直堆栈", "Stack Flow", "以唯一参数控制子项垂直间距，消灭子组件自身外边距导致的间距污染。"),
            ("簇群自适应", "Cluster Wrap", "自适应标签与按钮群组随宽度自动折行，始终保持均等间距。"),
            ("居中器原语", "Center Enclosure", "设定最大阈值并水平居中，让超大屏幕上的核心内容始终落在舒适视窗。")
        ],
        "tips": [
            ("单一样式职责", "布局原语只负责空间关系，禁止给原语组件掺杂背景色或文字大小等装饰属性。"),
            ("递归嵌套", "通过原语的简单递归组合（Stack 套 Cluster），即可优雅完成 90% 复杂 UI 结构。")
        ]
    },
    "页面框架与导航": {
        "theme": "cobalt-blue",
        "focus_type": "page_scaffold",
        "default_subject": "Classic web application scaffold with responsive sidebar, top app bar, and holy grail layout frame",
        "keywords": ["应用脚手架", "圣杯三栏", "抽屉导航", "粘性底栏"],
        "keywords_en": ["App Scaffold", "Holy Grail", "Nav Drawer", "Sticky Footer"],
        "tagline": "奠定稳固的骨架体系，让导航触手可及，让内容高效通达。",
        "features": [
            ("圣杯框架", "Holy Grail Architecture", "经典左右双侧栏护卫主内容区，自适应缩放且主次分明。"),
            ("固定基座", "Sticky Grounding", "顶部导航与底部操作栏牢牢吸附屏幕边缘，提供确定性的控制手柄。"),
            ("分层抽屉", "Layered Drawer", "非高频功能收纳至抽屉中，点击平滑滑出，最大化保留核心视窗纯净。")
        ],
        "tips": [
            ("滚动隔离", "侧栏菜单与主体内容区应各自独立支持内部滚动，避免整页跳动迷失。"),
            ("触控热区", "移动端导航项有效点击热区不得低于 44×44px，提供扎实的防误触手感。")
        ]
    },
    "内容与产品模式": {
        "theme": "cobalt-blue",
        "focus_type": "ui_product_patterns",
        "default_subject": "Modern responsive dashboard interface with Bento box cards, data tables, and interactive widgets",
        "keywords": ["便当盒布局", "卡片网格", "仪表盘面板", "列表详情"],
        "keywords_en": ["Bento Box", "Card Grid", "Dashboard Panel", "List-Detail"],
        "tagline": "提炼成熟商业产品范式，以高集成卡片与仪表盘驱动高效决策。",
        "features": [
            ("便当盒分区", "Bento Box Framing", "不同尺寸圆角矩形卡片紧凑拼嵌，将多维复杂数据包裹为诱人快餐。"),
            ("信息卡片化", "Card Atomization", "单张卡片封装独立实体数据，自带微交互，可拖拽、翻转与重排。"),
            ("双窗格并立", "Master-Detail Split", "左侧列表快速筛选索引，右侧沉浸式展示实体详实档案，操作零跳转。")
        ],
        "tips": [
            ("卡片视觉权重", "便当盒核心主推功能占据 2×2 面积并施加主题强调色，次要卡片保持 1×1 浅色中立。"),
            ("空状态关怀", "数据为空时必须提供富有亲和力的占位插画与单键创建按钮，引导后续行动。")
        ]
    },
    "响应式重排模式": {
        "theme": "cobalt-blue",
        "focus_type": "ui_responsive",
        "default_subject": "Multi-device layout transformation diagram showing fluid reflow from mobile stack to desktop grid",
        "keywords": ["响应式重排", "列下落", "堆叠重组", "断点微调"],
        "keywords_en": ["Responsive Reflow", "Column Drop", "Stack Reordering", "Tiny Tweaks"],
        "tagline": "跨越屏幕物理疆界，让界面形态如流水般顺应容器而自由幻化。",
        "features": [
            ("列下落机制", "Column Drop Reflow", "随屏幕宽度收窄，侧边栏优雅落入主内容下方，保持阅读单流向。"),
            ("网格折叠", "Grid Collapse", "桌面端四列矩阵平滑过渡为平板双列，直至手机端单列紧凑堆叠。"),
            ("显隐精简", "Selective Disclosure", "在小屏视口上隐藏高耗能次要图表，聚焦核心高价值操作主干。")
        ],
        "tips": [
            ("移动端先行", "优先规划移动端单列极限信息流，再以渐进增强手法向桌面大屏铺展。"),
            ("触控优先", "小屏幕下将密集悬停菜单（Hover）主动转换为显式大按钮与触控手势。")
        ]
    },

    # 06 影视画面构图
    "人物数量与群像": {
        "theme": "obsidian-black",
        "focus_type": "cinematic_characters",
        "default_subject": "Cinematic 2.39:1 widescreen shot with stark triangular grouping of three dramatic characters under high contrast light",
        "keywords": ["单人特写", "双人对峙", "三人三角", "群像层次"],
        "keywords_en": ["Solo Character", "Two-Shot Standoff", "Triangular Block", "Ensemble Depth"],
        "tagline": "以几何阵位排布人物关系，在无声站位中引爆戏剧张力。",
        "features": [
            ("对峙力场", "Confrontation Axis", "两人站位沿对角线或虚实对冲，在空间留白中拉扯看不见的情感引力。"),
            ("三角稳态", "Triangular Climax", "三人构图构建顶点与基底关系，揭示权位阶梯或隐秘同盟关系。"),
            ("群像透视", "Ensemble Stagger", "多人物纵深交错站位，利用光影与虚化层层剥离，混乱中见秩序。")
        ],
        "tips": [
            ("视线交互", "画面中人物视线不得随意空射，需有明确的视线落点（彼此相视或凝视画外焦点）。"),
            ("高度落差", "避免双人或三人头部完全水平齐平，制造高低落差能瞬间催生戏剧生动感。")
        ]
    },
    "视角与镜头覆盖": {
        "theme": "obsidian-black",
        "focus_type": "cinematography_lens",
        "default_subject": "Cinematic widescreen film frame, dramatic chiaroscuro lighting, dynamic camera angle and intense atmosphere",
        "keywords": ["过肩纵深", "主观视角", "客观冷静", "景别裁切"],
        "keywords_en": ["Over-the-Shoulder", "POV Subjective", "Objective Stance", "Shot Coverage"],
        "tagline": "操控镜头视角与景别纵深，带领观者在主客观视界中沉浸共情。",
        "features": [
            ("过肩纵深", "Over-the-Shoulder Depth", "前景虚化的人物肩膀构筑天然框架，将观者拽入面对面对谈临场感。"),
            ("主观沉浸", "POV Immersion", "镜头化身为剧中人双眼，所见所感同步传导，触发强烈的心理共振。"),
            ("脏镜头遮蔽", "Dirty Frame Intrusion", "刻意在镜头前置入门框、枝叶或虚化路人，营造窥视般的现实质感。")
        ],
        "tips": [
            ("180度轴线", "双人对话机位严禁越过动作假想轴线，防止前后镜头人物朝向产生错乱。"),
            ("视线空间留置", "人物侧脸镜头面朝的方向必须留出宽裕的视线空间（Look Room），避免视线撞墙。")
        ]
    },
    "场面调度与景深": {
        "theme": "obsidian-black",
        "focus_type": "mise_en_scene",
        "default_subject": "Deep focus cinematography with actor in extreme sharp foreground and dynamic action in deep background",
        "keywords": ["深度调度", "超焦全景", "横向推移", "多层遮挡"],
        "keywords_en": ["Deep Blocking", "Deep Focus", "Lateral Tracking", "Multi-Layer Occlusion"],
        "tagline": "在纵深空间中调度多重线索，让画面每一个切面都在讲述故事。",
        "features": [
            ("深度贯穿", "Z-Axis Penetration", "角色由远至近沿 Z 轴纵深走动，将背景事件与前景情绪紧密缝合。"),
            ("全幅锐利", "Deep Focus Omnipresence", "大光圈配合超焦距，使咫尺前景与数里远山尽数纤毫毕现。"),
            ("横向卷轴", "Lateral Pan Tracking", "摄影机水平横向跟移，如徐徐展开的古典画卷，连续展现环境与人群。")
        ],
        "tips": [
            ("前后呼应", "前景发生的静态交流与后景发生的动态冲突形成反差，可极佳烘托悬疑或讽刺。"),
            ("空间分层打光", "前景、中景、后景使用不同色温或明度布光，防止多层要素在画面中粘连。")
        ]
    },

    # 07 中国传统构图
    "三远、透视与游观": {
        "theme": "warm-ivory",
        "focus_type": "chinese_perspective",
        "default_subject": "Three distances classical Chinese shan shui landscape, towering vertical cliffs, deep gorges and expansive valleys",
        "keywords": ["高远自下", "深远自前", "平远自近", "散点游观"],
        "keywords_en": ["High Distance", "Deep Distance", "Level Distance", "Scattered Perspective"],
        "tagline": "以高远仰势、深远幽邃、平远渺茫，破尽西方焦点透视之局限。",
        "features": [
            ("高远立骨", "Towering High Distance", "自山下而仰山巅，峰峦崔嵬拔地而起，突显天地威严与崇高气势。"),
            ("深远通幽", "Layered Deep Distance", "自山前而窥山后，山回路转重峦叠嶂，诱人向烟云深处探寻幽渺。"),
            ("散点游观", "Roaming Scattered View", "视点伴随脚步自由移动移步换景，打破单一画框，容纳咫尺千里。")
        ],
        "tips": [
            ("三远合一", "山水长卷中巧妙融合高远、深远与平远，在同一画幅中展现全景气象。"),
            ("墨色五彩", "利用焦、浓、重、淡、清五种墨色拉开远近空间，淡墨出远山，浓墨立近石。")
        ]
    },
    "取景与景式": {
        "theme": "warm-ivory",
        "focus_type": "chinese_framing",
        "default_subject": "Classical Song dynasty poetic landscape showing corner-bound composition and branch-like flower arrangement",
        "keywords": ["一河两岸", "边角折枝", "全景千里", "截取幽微"],
        "keywords_en": ["One River Two Banks", "Corner Branch", "Panoramic Thousand Li", "Micro View"],
        "tagline": "由倪瓒之一河两岸，至马夏之边角残山，于方寸截景中见造化。",
        "features": [
            ("一河两岸", "Two Banks River Vista", "近景坡石树木，中景浩渺水泊，远景平远丘陵，勾勒超然出尘的清空意境。"),
            ("边角残山", "Corner-Bound Vista", "主体偏居画面一角或半壁，大片空旷任由江天远水驰骋，空灵深远。"),
            ("折枝造形", "Cut-Branch Essence", "不画全树全株，仅截取灵动一枝斜逸入画，以少胜多，以局部概括全美。")
        ],
        "tips": [
            ("势态连绵", "边角虽偏但气脉不能偏断，折枝入画的起点必须暗含伸向画外的苍劲母干。"),
            ("印章题跋", "中国画构图中印章与题跋是不可割裂的画面要素，用来在虚白处压住视觉阵脚。")
        ]
    },
    "留白、虚实与章法": {
        "theme": "warm-ivory",
        "focus_type": "chinese_zen",
        "default_subject": "Traditional East Asian poetic landscape, misty mountain silhouette with generous breathing negative space",
        "keywords": ["计白当黑", "虚实相生", "气韵生动", "开合起承"],
        "keywords_en": ["Value the Void", "Void & Solid", "Vital Energy", "Opening & Closing"],
        "tagline": "以无画处皆成妙境，计白当黑，于虚实相生中悟宇宙呼吸。",
        "features": [
            ("计白当黑", "Treat Void as Solid", "把未着笔墨的宣纸空白视为与实体笔墨同等重要的形体去精心剪裁。"),
            ("虚实生发", "Void & Solid Harmony", "实处着墨力透纸背，虚处烟云飘渺变幻，二者相互依存，生生不息。"),
            ("开合呼应", "Kai-He Organic Rhythm", "有开必有合，有起必有承，画中云水峰峦皆成环抱关照之大势。")
        ],
        "tips": [
            ("留白克制", "留白不是简单空置，空白处必须有实体线条的指向或视线投射，方成活白。"),
            ("欹正互救", "山石倾侧欲倾时（欹），需在相迎处安设直立树木或坚稳磐石以力挽狂澜（正）。")
        ]
    },

    # 08 演示文稿页面
    "基础幻灯片": {
        "theme": "forest-green",
        "focus_type": "slide_fundamentals",
        "default_subject": "Professional keynote presentation slide layout with crisp title, balanced columns, and modern geometric card",
        "keywords": ["封面立势", "两项对比", "极简空白", "图文排布"],
        "keywords_en": ["Cover Stance", "Two-Way Contrast", "Minimal Blank", "Slide Typography"],
        "tagline": "秒级传达演讲核心，用纯粹版式为演讲者提供坚实信任背书。",
        "features": [
            ("三秒定势", "Three-Second Recognition", "标题字体硕大醒目，听众无需眯眼即可在 3 秒内捕捉本页核心论点。"),
            ("双向对照", "Bilateral Comparison", "采用两项卡片并列版式，左右对阵展示优劣、现状与目标对比。"),
            ("少即是多", "Blank Breathing", "坚决摒弃花哨装饰符，以充沛的幻灯片边距为现场声场留足空间。")
        ],
        "tips": [
            ("一页一事", "单张幻灯片绝对禁止出现两个以上平级核心观点，贪多必失。"),
            ("字号底线", "投影正文字号不得低于 18pt，关键标题字号保持在 44pt 以上，确保全场清晰。")
        ]
    },
    "叙事与数据页面": {
        "theme": "forest-green",
        "focus_type": "slide_narrative",
        "default_subject": "High-impact presentation slide featuring monumental statistic figure, progress timeline, and analytical matrix",
        "keywords": ["大数冲击", "时间步进", "四象矩阵", "数据图表"],
        "keywords_en": ["Big Number Impact", "Timeline Stepper", "Matrix Quadrant", "Data Graphics"],
        "tagline": "让庞杂数据跃然纸上，用时间线与矩阵引爆说服力巅峰。",
        "features": [
            ("大数字震撼", "Monumental Number Impact", "将关键百分比或增长数放大至极值尺寸，形成强悍的视觉锤。"),
            ("时间步进", "Timeline Roadmap", "节点连线串联起历史里程碑与未来路线，构建坚实可信的演进叙事。"),
            ("四象矩阵", "Matrix Categorization", "XY 双轴四象限归类繁复竞品与战略，逻辑剖析一针见血。")
        ],
        "tips": [
            ("单位降阶", "大数字的计量单位（如 亿、%）字号缩减为数字的三分之一，强化数字本体冲击力。"),
            ("图表极简", "剔除图表所有冗余网格背景线与花哨渐变，只保留关键数据走势折线与高亮极值点。")
        ]
    }
}


def get_layout_english_name(lid: str, default_name: str) -> str:
    """Returns authentic professional English name for any layout ID."""
    lid = str(lid).zfill(3)
    if lid in NAMES_EN:
        return NAMES_EN[lid]
    return f"{default_name.upper()} COMPOSITION"


def get_enriched_layout_data(item: dict) -> dict:
    """
    Compiles enriched, non-boilerplate layout metadata for a single layout.
    Injects tailored English names, professional taglines, category-specific features,
    concrete scenario tips, and authentic keywords.
    """
    lid = item["id"].zfill(3)
    name = item["name"]
    category = item["category"]
    cat_slug = item.get("category_slug", "")
    subcategory = item["subcategory"]

    # Match subcategory profile
    profile = SUBCATEGORY_PROFILES.get(subcategory)
    if not profile:
        for k, v in SUBCATEGORY_PROFILES.items():
            if k in subcategory or k in category:
                profile = v
                break
    if not profile:
        profile = SUBCATEGORY_PROFILES["经典法则与空间留白"]

    theme = profile["theme"]
    name_en = get_layout_english_name(lid, name)
    tagline = profile["tagline"]

    # Unique customized description
    description = (
        f"350 视觉排版系列第 {lid} 号：{name}（{name_en}）。"
        f"归属于「{category} · {subcategory}」体系。"
        f"{tagline}"
    )

    # Prompt compilation
    prompt = (
        f"Professional editorial design illustration demonstrating {name} ({name_en}), "
        f"350 Layout series #{lid}. {profile['default_subject']}. "
        f"Art style: clean Swiss International Typographic poster aesthetic, "
        f"palette tuned to {theme} theme, vector geometry, sharp visual hierarchy, "
        f"3:4 aspect ratio, ultra-high resolution, museum publication quality."
    )

    # Features: customized and specific
    f_presets = profile["features"]
    features = [
        {
            "icon": "target",
            "title": f_presets[0][0],
            "title_en": f_presets[0][1],
            "desc": f"在{name}架构中，{f_presets[0][2]}"
        },
        {
            "icon": "compass",
            "title": f_presets[1][0],
            "title_en": f_presets[1][1],
            "desc": f"依据{name}的内在几何规律，{f_presets[1][2]}"
        },
        {
            "icon": "layers",
            "title": f_presets[2][0],
            "title_en": f_presets[2][1],
            "desc": f"针对{name}的空间特性，{f_presets[2][2]}"
        }
    ]

    # Tips: specific scenario guidance
    t_presets = profile["tips"]
    tips = [
        {
            "label": t_presets[0][0],
            "content": t_presets[0][1]
        },
        {
            "label": t_presets[1][0],
            "content": t_presets[1][1]
        }
    ]

    # Keywords: 4 distinct keywords
    kw_list = []
    icons = ["target", "compass", "layers", "check"]
    for i, (cn, en) in enumerate(zip(profile["keywords"], profile["keywords_en"])):
        kw_list.append({
            "name": cn,
            "name_en": en,
            "icon": icons[i % len(icons)]
        })

    # Checklist: 5 specific checklist items
    checklist = [
        f"{name}核心主体或骨骼线定位明确严谨",
        "视觉引导线与视线流向顺畅自然",
        "留白空间充足，版面呼吸感良好",
        f"色彩与明暗层级完全吻合「{theme}」基调",
        f"符合「{subcategory}」的专业设计规范"
    ]

    return {
        "id": lid,
        "name": name,
        "name_en": name_en,
        "category": f"{category} / {subcategory}",
        "category_slug": cat_slug,
        "subcategory": subcategory,
        "tagline": tagline,
        "description": description,
        "theme": theme,
        "columns_ratio": "345px 600px",
        "visual_height": "790px",
        "ai_prompt": prompt,
        "features": features,
        "tips": tips,
        "keywords": kw_list,
        "checklist": checklist
    }

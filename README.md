# 350 Layout Architect · 视觉构图与排版全能 Agent 技能

`350-layout-skill` 是一套专为 AI Agent（如 Claude Code, OpenClaw, OpenAI Codex, Cursor 等）打造的**生产级全媒介构图与视觉排版系统**。

基于开源著名的「350 种排版」体系，本项目将其从“静态图鉴”升级为**可计算、可编译、可执行的标准化 Agent 技能**：支持智能构图推荐、AI生图构图约束编译 (Midjourney/Flux)、前端响应式网格生成，并能**离线秒级渲染出 1086 × 1448 印刷级瑞士设计排版海报**。

---

## 一键安装与使用

把下面这段话发给支持 Skills 的 AI Agent：

```text
请安装这个仓库里的全部 Skills：https://github.com/yww520/350-layout-compositions
```

安装后即可直接调用：

```text
Use $layout-350 ...
```

---

## 核心效果展示 (1:1 离线渲染还原)

本技能内置参数化矢量排版引擎与工业级字体排版体系，**无需调用昂贵的外部生图 API，0.5 秒即可在本地导出 1086 × 1448 绝对平直、零乱码的高清海报**：

| 001 三分法构图 (米纸暖红) | 004 黄金三角构图 (深海明黄) |
| :---: | :---: |
| ![001 三分法构图](./screenshots/001_三分法构图.png) | ![004 黄金三角构图](./screenshots/004_黄金三角构图.png) |
| 经典空间留白 · 矢量山峦与焦点雷达 | 动态向量张力 · 折纸雪山与航海帆船 |

---

## 核心能力与工作流

### 1. 智能排版推荐 (Smart Recommendation Gate)
提供文章、文案或主题，Agent 会自动分析信息密度与情绪，**并严格推荐前 3 种最优构图解**供用户选择：
```text
Use $layout-350 recommend layout for this article:
[粘贴你的文章、主题草稿或设计需求]
```

### 2. 秒级渲染排版图鉴卡片 (CLI & Agent Tool)
指定编号秒级生成对应的高清图鉴海报（支持 `warm-ivory`, `forest-green`, `obsidian-black`, `cobalt-blue` 4 种主色盘）：
```bash
# 命令行快速生成
python3 scripts/render-card.py --id 001
python3 scripts/render-card.py --id 004 --theme cobalt-blue
```

### 3. 生图构图约束编译 (AI Image Prompt Directive)
将抽象构图几何直接编译为 Midjourney / Flux.1 的高阶控制提示词，精准锁定主体坐标与负空间：
```text
Use $layout-350 compile prompt for 003 黄金螺旋, 主题: AI 时代的技术奇点
```

### 4. 前端网格代码生成 (Web / UI Code Generation)
将 350 中的现代网格（如 148 Bento Grid）直接编译为响应式 Tailwind CSS 或 CSS Grid 代码：
```text
Use $layout-350 code layout for 148 便当盒网格
```

---

## 覆盖完整的 8 大一级分类体系 (350 种全量索引)

1. **`01 · 构图逻辑 (86 种)`**：经典法则、重心线条、几何形态、空间层叠、前中后景与透视；
2. **`02 · 视觉原则与阅读模式 (45 种)`**：格式塔心理学、层级比例、视线动势、F型/Z型扫描路径；
3. **`03 · 平面、出版与广告 (36 种)`**：分栏网格、跨页对齐、出血线控制、表现型图文排布；
4. **`04 · 字体、网格与东亚文字 (54 种)`**：基线网格、成组分栏、东亚 CJK 汉字排版规范、标点避头尾；
5. **`05 · 网页与 UI 布局 (79 种)`**：Hero 区块、Bento Grid 便当盒、流式卡片、仪表盘、响应式重排；
6. **`06 · 影视画面构图 (14 种)`**：电影画幅比、过肩镜头、机位覆盖、景深调度；
7. **`07 · 中国传统构图 (20 种)`**：三远法（高远、深远、平远）、散点透视、计白当黑留白韵味；
8. **`08 · 演示文稿页面 (16 种)`**：商业发布会与 Keynote/PPT 核心信息骨架。

---

## 仓库工程结构

```text
350-layout-skill/
├── SKILL.md                          # 标准 Agent Skill 描述与执行 SOP
├── agents/openai.yaml                # 接口元数据配置
├── templates/
│   └── card-master.html              # 生产级通用海报渲染母版（支持 4 套主色盘）
├── data/
│   ├── catalog.json                  # 350 个构图索引库（分类、编号、中英名称、标签）
│   └── layouts/                      # 350 个结构化数据 JSON (001.json ~ 350.json)
├── references/
│   ├── intent-router.md              # 智能意图路由字典（根据场景匹配最佳排版）
│   └── blueprints/
│       ├── image-prompt-blueprint.md # 编译给生图模型的构图指令骨架
│       └── web-layout-blueprint.md   # 编译给前端的 CSS Grid 骨架
├── scripts/
│   ├── render-card.py                # 核心渲染 CLI：传入编号秒级导出 PNG/HTML
│   ├── pipeline-extractor.py         # 数据抓取与格式转换管道
│   └── validate-skill.py             # 静态工程完整性校验脚本
└── screenshots/                      # 高清复刻样例效果图
```

---

## 致敬与致谢

- 视觉构图与排版理论图鉴：[nevertoday/350-layout-compositions](https://github.com/nevertoday/350-layout-compositions)
- Agent Skill 架构与设计启发：[adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill)

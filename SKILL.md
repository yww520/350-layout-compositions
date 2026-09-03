---
name: layout-350
description: 350 构图与视觉排版全能技能 (Layout Architect)。提供从经典法则、视觉原则、平面广告、字体网格、网页UI、影视镜头到中国传统构图的 350 种专业构图知识库与极简瑞士设计卡片渲染引擎。可用于智能构图推荐、AI生图构图约束编译 (Midjourney/Flux)、网页响应式网格布局生成，以及 1:1 秒级导出 1086×1448 印刷级排版图鉴海报。
---

# 350 Layout Architect (构图与排版总控)

`layout-350` 是一套为 AI Agent 设计的**全媒介构图与视觉排版系统**。它将 350 种构图逻辑转化为机器可读的结构化参数，提供**构图分析、智能推荐、提示词编译、代码生成与海报卡片渲染**五合一能力。

---

## 核心执行规范与状态机 (Workflow SOP)

当用户发起排版、封面、海报构图或图鉴生成需求时，Agent **必须严格遵循以下五步流程**：

### 步骤 1：意图分析与信息提炼 (Content Analysis)
分析用户提供的主题、文案或草稿：
1. **媒介类型**：海报插画 (Image/Poster)、网页 UI (Web Layout)、出版图文 (Editorial)、幻灯片 (Slide)；
2. **信息密度**：低密度 (主视觉冲击型) / 中密度 (图文均衡) / 高密度 (多模块数据型)；
3. **视觉情绪**：严谨秩序 / 动感张力 / 留白诗意 / 商业科技；
4. **提取关键字段**：核心主体、标题层级 (主标题/副标/正文)、核心意象、违禁元素。

### 步骤 2：画幅与参数确认 (Canvas & Aspect Ratio)
- 微信公众号封面：`2.35:1`
- 小红书海报 / 图鉴卡片：`3:4` (1086 × 1448)
- 社交横版 / 网页 Banner：`16:9`
- 影视画幅：`2.39:1` 或 `1.85:1`
- 方形视窗：`1:1`

### 步骤 3：智能推荐与确认门禁 (Confirmation Gate)
- 若用户未显式指定构图编号，检索 `references/intent-router.md`，**强制推荐且仅推荐 3 种最匹配的构图方案**，每种附带 1 句话推荐理由：
  - **方案 A (经典稳妥)**：如 `001 三分法构图` 或 `002 黄金比例构图`；
  - **方案 B (张力动感)**：如 `004 黄金三角构图` 或 `023 对角线构图`；
  - **方案 C (现代结构)**：如 `148 便当盒网格` 或 `065 空间层叠构图`。
- **门禁控制**：在用户确认具体构图前，**Agent 必须停下来等待确认**，不得擅自生成最终设计。

### 步骤 4：精准读取构图原子 (Atomic Layout Ingestion)
当选定编号后（如 `004`）：
1. 读取 `data/layouts/{id}.json`（若本地未填充完整 JSON，则从 `data/catalog.json` 索引并按模板补全）；
2. 提取其专属配色方案（米纸暖红、典雅墨绿、曜石金光、深海群青）；
3. 提取其几何坐标规则（网格比例、视线向量、焦点坐标、留白边界）。

### 步骤 5：跨媒介编译与渲染交付 (Compilation & Delivery)
根据用户的目标载体执行对应编译输出：

#### 交付路径 A：生成 350 风格图鉴海报 (Poster Card)
直接调用项目内置渲染引擎导出高清卡片：
```bash
python3 scripts/render-card.py --id {id} --output ./output/
```
或将渲染出的 HTML 文件在浏览器中打开供用户预览。

#### 交付路径 B：编译生图提示词 (AI Image Prompt Directive)
读取 `references/blueprints/image-prompt-blueprint.md`，将构图几何与焦点坐标注入提示词：
```text
COMPOSITION SPECIFICATION:
- Layout Framework: {name} ({name_en})
- Geometric Partition: {grid_rules}
- Focal Anchor: Place {subject} at {coordinates}
- Dynamic Leading Path: Guide line from {start} to {end}
- Negative Space: Preserve {ratio}% empty space on {zone}
```

#### 交付路径 C：编译前端网格代码 (Web / UI Grid)
读取 `references/blueprints/web-layout-blueprint.md`，输出响应式 Tailwind CSS 或 CSS Grid 骨架代码。

---

## 常用指令示例 (Quick Commands)

- **生成指定图鉴卡片**：
  ```text
  Use $layout-350 render 001
  Use $layout-350 render 004 --theme cobalt-blue
  ```
- **根据文章智能推荐构图**：
  ```text
  Use $layout-350 recommend layout for this article: [文章内容]
  ```
- **生成带构图控制的生图 Prompt**：
  ```text
  Use $layout-350 compile prompt for 003 黄金螺旋, 主题: AI 时代的技术奇点
  ```
- **生成网页响应式布局**：
  ```text
  Use $layout-350 code layout for 148 便当盒网格
  ```

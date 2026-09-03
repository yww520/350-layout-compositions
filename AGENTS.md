# Repository Guidelines for AI Agents

## 项目结构与模块组织

本仓库为可独立交付的 AI Agent 视觉构图与排版技能库（350 Layout Architect）：

- `SKILL.md`：核心技能执行规范、门禁与工作流定义。
- `agents/openai.yaml`：面向 Agent 生态系统的元数据接口。
- `data/catalog.json`：全量 350 个构图的轻量级索引，用于快速检索与意图匹配。
- `data/layouts/{id}.json`：350 个构图的独立结构化数据原子（001 ~ 350）。
- `templates/card-master.html`：生产级参数化海报母版，支持 4 种双色调主题（米纸/墨绿/曜石黑/深海蓝）。
- `references/intent-router.md`：根据用户意图、内容类型智能匹配前 3 款构图的路由矩阵。
- `references/blueprints/`：跨媒介编译骨架（生图 Prompt 骨架与前端网格骨架）。
- `scripts/render-card.py`：CLI 渲染脚本，支持按 ID 导出 1086×1448 印刷级卡片。
- `scripts/validate-skill.py`：自动化完整性校验工具。

## 开发与校验约定

每次新增构图定义或修改母版后，请运行：
```bash
python3 scripts/validate-skill.py
python3 scripts/render-card.py --id 001
```
确保数据解析与图片渲染均能无报错通过。

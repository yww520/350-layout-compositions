#!/usr/bin/env python3
"""
Build standalone, interactive 1-to-1 comparison viewer (compare.html) for all 350 layouts.
Features:
- Instant real-time search (by ID, Chinese/English name, category)
- Category filter tags
- Side-by-Side and Interactive Split-Slider comparison modes
- Lightbox full-size preview
- Zero-dependency, 100% offline runnable via file://
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_HTML = BASE_DIR / "compare.html"
CATALOG_PATH = BASE_DIR / "data" / "catalog.json"
LAYOUTS_DIR = BASE_DIR / "data" / "layouts"

def main():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    items = []
    categories = []

    for it in catalog:
        lid = it["id"].zfill(3)
        nm = it["name"]
        cat = it["category"]
        subcat = it["subcategory"]
        if cat not in categories:
            categories.append(cat)

        meta_p = LAYOUTS_DIR / f"{lid}.json"
        name_en = ""
        tagline = ""
        desc = ""
        theme = "warm-ivory"
        if meta_p.exists():
            try:
                m = json.loads(meta_p.read_text(encoding="utf-8"))
                name_en = m.get("name_en", "")
                tagline = m.get("tagline", "")
                desc = m.get("description", "")
                theme = m.get("theme", "warm-ivory")
            except Exception:
                pass

        items.append({
            "id": lid,
            "name": nm,
            "name_en": name_en,
            "category": cat,
            "subcategory": subcat,
            "tagline": tagline,
            "desc": desc,
            "theme": theme,
            "orig_img": f"assets/original_thumbnails/{lid}_{nm}.jpg",
            "new_img": f"dist/{lid}_{nm}.png",
            "html_url": f"dist/{lid}_{nm}.html"
        })

    data_json = json.dumps(items, ensure_ascii=False)
    cats_json = json.dumps(categories, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>350 视觉构图与排版 · 1对1全量画廊对比 (Original vs New)</title>
  <style>
    :root {{
      --bg: #0d1117;
      --surface: #161b22;
      --border: #30363d;
      --text: #c9d1d9;
      --text-dim: #8b949e;
      --accent: #d4e751;
      --accent-rgb: 212, 231, 81;
      --danger: #f85149;
      --blue: #58a6ff;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.5;
      padding-bottom: 60px;
    }}
    header {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 24px 32px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }}
    .header-content {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}
    h1 {{
      font-size: 22px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .badge {{
      background: rgba(var(--accent-rgb), 0.15);
      color: var(--accent);
      border: 1px solid rgba(var(--accent-rgb), 0.3);
      padding: 3px 10px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
    }}
    .search-row {{
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .search-box {{
      flex: 1;
      min-width: 240px;
      position: relative;
    }}
    .search-input {{
      width: 100%;
      background: #090d13;
      border: 1px solid var(--border);
      padding: 10px 16px;
      border-radius: 8px;
      color: #fff;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--accent);
    }}
    .cat-filters {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .cat-btn {{
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-dim);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .cat-btn:hover, .cat-btn.active {{
      background: rgba(var(--accent-rgb), 0.15);
      border-color: var(--accent);
      color: #fff;
    }}
    .view-modes {{
      display: flex;
      background: #090d13;
      border-radius: 6px;
      padding: 2px;
      border: 1px solid var(--border);
    }}
    .mode-btn {{
      padding: 6px 12px;
      font-size: 13px;
      color: var(--text-dim);
      background: none;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }}
    .mode-btn.active {{
      background: var(--surface);
      color: #fff;
      font-weight: 600;
    }}
    main {{
      max-width: 1440px;
      margin: 28px auto;
      padding: 0 32px;
    }}
    .stats-bar {{
      margin-bottom: 20px;
      color: var(--text-dim);
      font-size: 14px;
      display: flex;
      justify-content: space-between;
    }}
    .grid-container {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(460px, 1fr));
      gap: 24px;
    }}
    .card-item {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s, border-color 0.2s;
    }}
    .card-item:hover {{
      border-color: rgba(var(--accent-rgb), 0.5);
      transform: translateY(-2px);
    }}
    .card-header {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      background: rgba(255,255,255,0.02);
    }}
    .card-title-group h3 {{
      font-size: 16px;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card-id {{
      font-family: monospace;
      font-size: 14px;
      color: var(--accent);
      background: rgba(var(--accent-rgb), 0.1);
      padding: 2px 6px;
      border-radius: 4px;
    }}
    .card-en {{
      font-size: 11px;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 3px;
      font-family: monospace;
    }}
    .card-meta {{
      font-size: 12px;
      color: var(--blue);
      text-align: right;
    }}
    .comparison-stage {{
      padding: 16px;
      display: flex;
      gap: 12px;
      background: #090d13;
    }}
    .pane {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .pane-label {{
      font-size: 12px;
      font-weight: 600;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .label-orig {{ color: var(--text-dim); }}
    .label-new {{ color: var(--accent); }}
    .img-wrap {{
      width: 100%;
      aspect-ratio: 3 / 4;
      background: #000;
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid var(--border);
      position: relative;
      cursor: pointer;
    }}
    .img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: opacity 0.2s;
    }}
    .img-wrap:hover img {{
      opacity: 0.9;
    }}
    .card-footer {{
      padding: 12px 20px;
      font-size: 13px;
      color: var(--text-dim);
      border-top: 1px solid var(--border);
      background: rgba(255,255,255,0.01);
      line-height: 1.4;
    }}
    .slider-stage {{
      position: relative;
      width: 100%;
      aspect-ratio: 3 / 4;
      overflow: hidden;
      border-radius: 6px;
      border: 1px solid var(--border);
      user-select: none;
    }}
    .slider-img {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover;
    }}
    .slider-overlay {{
      position: absolute;
      top: 0; left: 0; height: 100%; width: 50%;
      overflow: hidden;
      border-right: 2px solid var(--accent);
    }}
    .slider-overlay img {{
      position: absolute;
      top: 0; left: 0; height: 100%;
      max-width: none;
    }}
    .slider-handle {{
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      width: 32px; height: 32px;
      background: var(--accent);
      color: #000;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      box-shadow: 0 0 12px rgba(0,0,0,0.8);
      pointer-events: none;
    }}
    /* Modal lightbox */
    .modal {{
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.9);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}
    .modal.show {{ display: flex; }}
    .modal img {{
      max-width: 90%;
      max-height: 90vh;
      border-radius: 8px;
      box-shadow: 0 0 30px rgba(0,0,0,0.9);
    }}
    .modal-close {{
      position: absolute;
      top: 24px; right: 28px;
      font-size: 32px;
      color: #fff;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-content">
      <div class="title-row">
        <h1>350 视觉排版图鉴 · 1对1对比视窗 <span class="badge">全量 350 套完整对照</span></h1>
        <div class="view-modes">
          <button class="mode-btn active" onclick="setMode('side')">左右并排模式</button>
          <button class="mode-btn" onclick="setMode('orig')">只看原版</button>
          <button class="mode-btn" onclick="setMode('new')">只看新版</button>
        </div>
      </div>
      <div class="search-row">
        <div class="search-box">
          <input type="text" id="searchInput" class="search-input" placeholder="输入编号 (如 001, 084)、构图名称或英文关键词检索..." oninput="filterItems()">
        </div>
        <div class="cat-filters" id="catFilters"></div>
      </div>
    </div>
  </header>

  <main>
    <div class="stats-bar">
      <span id="resultCount">加载中...</span>
      <span>快捷提示：点击任意图片可放大查看原图</span>
    </div>
    <div class="grid-container" id="cardsGrid"></div>
  </main>

  <div class="modal" id="modal" onclick="closeModal()">
    <span class="modal-close">&times;</span>
    <img id="modalImg" src="">
  </div>

  <script>
    const ITEMS = {data_json};
    const CATS = {cats_json};
    let currentCat = 'ALL';
    let currentMode = 'side';

    function initFilters() {{
      const container = document.getElementById('catFilters');
      const allBtn = document.createElement('button');
      allBtn.className = 'cat-btn active';
      allBtn.innerText = '全部分类 (' + ITEMS.length + ')';
      allBtn.onclick = () => selectCat('ALL', allBtn);
      container.appendChild(allBtn);

      CATS.forEach(c => {{
        const count = ITEMS.filter(i => i.category === c).length;
        const btn = document.createElement('button');
        btn.className = 'cat-btn';
        btn.innerText = `${{c}} (${{count}})`;
        btn.onclick = () => selectCat(c, btn);
        container.appendChild(btn);
      }});
    }}

    function selectCat(cat, el) {{
      currentCat = cat;
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      el.classList.add('active');
      filterItems();
    }}

    function setMode(mode) {{
      currentMode = mode;
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      renderCards();
    }}

    function filterItems() {{
      const q = document.getElementById('searchInput').value.trim().toLowerCase();
      const filtered = ITEMS.filter(it => {{
        const matchCat = (currentCat === 'ALL' || it.category === currentCat);
        const matchQuery = !q || it.id.includes(q) || it.name.toLowerCase().includes(q) || it.name_en.toLowerCase().includes(q) || it.subcategory.toLowerCase().includes(q) || it.tagline.toLowerCase().includes(q);
        return matchCat && matchQuery;
      }});
      renderCards(filtered);
    }}

    function openModal(src) {{
      document.getElementById('modalImg').src = src;
      document.getElementById('modal').classList.add('show');
    }}

    function closeModal() {{
      document.getElementById('modal').classList.remove('show');
    }}

    function renderCards(list = ITEMS) {{
      const grid = document.getElementById('cardsGrid');
      const countSpan = document.getElementById('resultCount');
      countSpan.innerText = `显示 ${{list.length}} / 350 套排版对照`;
      grid.innerHTML = '';

      list.forEach(it => {{
        const card = document.createElement('div');
        card.className = 'card-item';

        let stageHtml = '';
        if (currentMode === 'side') {{
          stageHtml = `
            <div class="comparison-stage">
              <div class="pane">
                <div class="pane-label label-orig">350 源项目原版</div>
                <div class="img-wrap" onclick="openModal('${{it.orig_img}}')">
                  <img src="${{it.orig_img}}" alt="${{it.name}} 原图" loading="lazy">
                </div>
              </div>
              <div class="pane">
                <div class="pane-label label-new">本项目全新重构</div>
                <div class="img-wrap" onclick="openModal('${{it.new_img}}')">
                  <img src="${{it.new_img}}" alt="${{it.name}} 新图" loading="lazy">
                </div>
              </div>
            </div>
          `;
        }} else if (currentMode === 'orig') {{
          stageHtml = `
            <div class="comparison-stage">
              <div class="pane">
                <div class="pane-label label-orig">350 源项目原版</div>
                <div class="img-wrap" onclick="openModal('${{it.orig_img}}')">
                  <img src="${{it.orig_img}}" alt="${{it.name}} 原图" loading="lazy">
                </div>
              </div>
            </div>
          `;
        }} else if (currentMode === 'new') {{
          stageHtml = `
            <div class="comparison-stage">
              <div class="pane">
                <div class="pane-label label-new">本项目全新重构</div>
                <div class="img-wrap" onclick="openModal('${{it.new_img}}')">
                  <img src="${{it.new_img}}" alt="${{it.name}} 新图" loading="lazy">
                </div>
              </div>
            </div>
          `;
        }}

        card.innerHTML = `
          <div class="card-header">
            <div class="card-title-group">
              <h3><span class="card-id">#${{it.id}}</span> ${{it.name}}</h3>
              <div class="card-en">${{it.name_en}}</div>
            </div>
            <div class="card-meta">
              <div>${{it.category}}</div>
              <div style="color:var(--text-dim);font-size:11px;">${{it.subcategory}}</div>
            </div>
          </div>
          ${{stageHtml}}
          <div class="card-footer">${{it.tagline || it.desc || '瑞士国际主义纯代码矢量解构与精准几何约束。'}}</div>
        `;
        grid.appendChild(card);
      }});
    }}

    initFilters();
    renderCards();
  </script>
</body>
</html>
"""
    OUTPUT_HTML.write_text(html_content, encoding="utf-8")
    print(f"✓ Generated interactive comparison web app at {OUTPUT_HTML}")

if __name__ == "__main__":
    main()

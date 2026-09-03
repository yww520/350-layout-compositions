# 350 Web & UI Layout Blueprint (前端网格代码编译器骨架)

本蓝图用于将选定的 350 构图（尤其是 05类网页UI、04类网格系统与 03类分栏出版），直接编译为现代响应式 Tailwind CSS 与 CSS Grid 结构。

---

## 编译器模板骨架 (HTML/CSS Skeleton)

```html
<!-- {layout_name} ({layout_id}) Responsive Web Layout -->
<section class="min-h-screen w-full bg-[#0B2B68] text-white p-8 md:p-16 flex flex-col justify-between">
  
  <!-- Header / Meta Bar -->
  <header class="flex justify-between items-center border-b border-white/10 pb-6 mb-8">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 text-xs font-semibold text-[#FFD000]">
      <span class="w-2 h-2 rounded-full bg-[#FFD000]"></span>
      {category_name}
    </div>
    <span class="text-sm text-slate-400 font-mono tracking-widest">{layout_id} / 350 GRID</span>
  </header>

  <!-- Main Responsive Grid Container -->
  <main class="{grid_container_classes}">
    <!-- Primary Visual/Hero Cell -->
    <div class="{primary_cell_classes}">
      {primary_content_slot}
    </div>

    <!-- Secondary / Supporting Content Cells -->
    <div class="{secondary_cell_classes}">
      {secondary_content_slot}
    </div>
  </main>

  <!-- Footer / Status Strip -->
  <footer class="mt-12 pt-6 border-t border-white/10 flex flex-wrap justify-between items-center gap-4 text-xs text-slate-400">
    <div class="flex items-center gap-4">
      {keywords_pills}
    </div>
    <div>Layout Principles Powered by 350-Layout-Skill</div>
  </footer>

</section>
```

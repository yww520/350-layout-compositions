# 350 Layout Image Prompt Blueprint (生图提示词编译器骨架)

本蓝图用于将选定的 350 构图几何规范，编译为能够强力约束生图模型（Midjourney v6 / Flux.1 / SDXL）空间布局的工业级提示词。

---

## 编译器模板骨架 (Prompt Compilation Skeleton)

```text
A professional editorial poster, graphic design visual masterwork.
Aspect Ratio: --ar {ratio}

[CORE CONTENT & METAPHOR]
Subject: {visual_subject}
Metaphor & Context: {metaphor_narrative}
Mood: {mood_atmosphere}

[STRICT COMPOSITION DIRECTIVES - ENFORCED]
Composition Archetype: {layout_name} ({layout_id})
- Geometric Partition: {geometric_grid_rules}
- Focal Anchor Placement: The primary visual anchor ({visual_subject}) must be positioned strictly at coordinates ({focal_x}, {focal_y}). Do not center the subject.
- Directional Vector / Flow: Guide the viewer's eye along {leading_path_vector}. Secondary elements sweep from {flow_start} to {flow_end}.
- Negative Space & Breathing Zone: Keep {negative_space_ratio}% of the canvas completely empty and uncluttered on {negative_space_quadrant}. This clean zone is reserved for typography.
- Horizon & Baseline Control: Place the baseline/ground plane at {baseline_y_position}.

[STYLE & RENDERING CONSTRAINTS]
Visual Quality: Swiss International Typographic style meets precision architectural drafting. Crisp vector lines, rich duotone color palette ({palette_description}), razor-sharp geometry, zero digital noise, zero chaotic clutter, intentional high-end graphic design poster aesthetic.
```

---

## 示例：004 黄金三角编译输出

```text
A professional editorial poster, graphic design visual masterwork.
Aspect Ratio: --ar 3:4

[CORE CONTENT & METAPHOR]
Subject: A sleek geometric minimalist sailboat navigating ocean waves towards a rising radiant sun
Metaphor: Ascending momentum, breaking through limits along dynamic diagonal tension
Mood: Heroic, determined, high-tech, oceanic power

[STRICT COMPOSITION DIRECTIVES - ENFORCED]
Composition Archetype: Golden Triangle Composition (004)
- Geometric Partition: Frame split diagonally from lower-left (0, 100%) to upper-right (100%, 0%), with a perpendicular line projecting from bottom-right (100%, 100%) meeting at the golden intersection.
- Focal Anchor Placement: The glowing sun and visual climax must be placed precisely at the upper-right golden vertex (x: 0.72, y: 0.28).
- Directional Vector: The sailboat hull and sails must tilt along the 45-degree diagonal axis, pointing upward-right.
- Negative Space: Preserve 40% clean, deep cobalt-blue space across the left and top-left zones.
- Horizon & Baseline: The sea base forms a solid horizontal grounding at the bottom 15% of the frame.

[STYLE & RENDERING CONSTRAINTS]
Deep cobalt blue background (#0B2B68), vibrant cyber canary yellow accents (#FFD000), crisp ice white highlights. Flat 2D vector drafting elegance, Swiss design precision, no photorealistic noise.
```

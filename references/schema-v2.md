# Composition Spec V2

`data/composition-specs/{id}.json` describes how a layout is executed, rather than how its reference card is displayed.

## Required fields

- `id`, `name`, `kind`, and `engine` identify the composition and select an execution path.
- `structure` holds normalized geometry. Coordinates are fractions in the inclusive range 0–1.
- `subject_rules`, `negative_space`, and `visual_flow` turn geometry into constraints for a user theme.
- `generation` contains medium-specific prompt framing; it must not prescribe the user’s subject.
- `validation.required` is a short list of observable conditions and `validation.threshold` is 0–1.

## Execution kinds

| Kind | Primary delivery |
|---|---|
| `image_composition` | Image prompt and a layout guide |
| `editorial_layout` | Design/typographic visual plan |
| `ui_layout` | UI visual plan; may later compile to HTML/CSS |
| `cinematic_shot` | Image prompt with camera and blocking constraints |
| `chinese_composition` | Image prompt with Chinese painting spatial rules |
| `presentation_layout` | Slide visual plan; may later compile to a slide deck |

No V2 field is a request to copy a source thumbnail. Guides are schematic only.

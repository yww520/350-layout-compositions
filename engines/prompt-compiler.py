#!/usr/bin/env python3
"""Compile a user theme plus one V2 spec into model-neutral composition directives."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout_router import load_spec


def point(value):
    return f"({value[0]:.2f}, {value[1]:.2f})"


def compile_prompt(spec: dict, subject: str, ratio: str, model: str) -> str:
    s = spec["structure"]
    rules = spec["subject_rules"]
    negative = spec["negative_space"]
    flow = spec["visual_flow"]
    generation = spec["generation"]
    lines = [
        f"Create {subject}.",
        f"Composition: {spec['name']} ({spec['id']}); {generation['medium']}.",
        f"Canvas: {ratio}. Primary subject placement: {rules['primary']}.",
        f"Geometric structure: {s['description']}.",
    ]
    if "focal" in s:
        lines.append(f"Focal anchor: {point(s['focal'])}.")
    if "axes" in s:
        axes = "; ".join(f"{point(a[0])} → {point(a[1])}" for a in s["axes"])
        lines.append(f"Required axes: {axes}.")
    lines.extend([
        f"Visual flow: {flow['primary']}. Secondary flow: {flow.get('secondary', 'support the primary flow')}.",
        f"Negative space: preserve at least {negative['min_ratio']:.0%} in {negative['zones']}.",
        f"Rendering direction: {generation['style']}.",
        f"Acceptance requirements: {'; '.join(spec['validation']['required'])}.",
        "Do not add arbitrary centered subjects, decorative text, or geometry that breaks these constraints.",
    ])
    suffix = {"midjourney": f"--ar {ratio}", "flux": f"aspect ratio {ratio}"}.get(model)
    if suffix:
        lines.append(suffix)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--ratio", default="3:4")
    parser.add_argument("--model", choices=["generic", "midjourney", "flux"], default="generic")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    spec = load_spec(args.id)
    result = {"id": spec["id"], "engine": spec["engine"], "prompt": compile_prompt(spec, args.subject, args.ratio, args.model), "validation": spec["validation"]}
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else result["prompt"])


if __name__ == "__main__":
    main()

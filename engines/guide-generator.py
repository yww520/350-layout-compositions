#!/usr/bin/env python3
"""Render a non-referential SVG guide from a V2 composition specification."""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout_router import load_spec

W, H = 1000, 1000


def xy(point):
    return round(point[0] * W), round(point[1] * H)


def guide(spec):
    s = spec["structure"]
    elements = [f'<rect width="{W}" height="{H}" fill="#101820"/>']
    for start, end in s.get("axes", []):
        x1, y1 = xy(start); x2, y2 = xy(end)
        elements.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#FFB000" stroke-width="12" stroke-dasharray="28 18"/>')
    focal = s.get("focal")
    if focal:
        x, y = xy(focal)
        elements.append(f'<circle cx="{x}" cy="{y}" r="32" fill="#FF5A5F"/><circle cx="{x}" cy="{y}" r="75" fill="none" stroke="#FF5A5F" stroke-width="8"/>')
    for index, zone in enumerate(spec["negative_space"]["zones"]):
        elements.append(f'<text x="40" y="{880 + index * 36}" fill="#A7BBC7" font-size="28" font-family="sans-serif">VOID: {zone}</text>')
    elements.append(f'<text x="40" y="70" fill="white" font-size="42" font-family="sans-serif" font-weight="700">{spec["id"]} · {spec["name"]}</text>')
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">' + ''.join(elements) + '</svg>'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    svg = guide(load_spec(args.id))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(svg, encoding="utf-8")
    else:
        print(svg)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the V2 schema and reject absent or placeholder spatial constraints."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS = ROOT / "data" / "composition-specs"
REQUIRED = {"id", "name", "kind", "engine", "structure", "subject_rules", "negative_space", "visual_flow", "generation", "validation"}


def valid_point(value):
    return isinstance(value, list) and len(value) == 2 and all(isinstance(n, (int, float)) and 0 <= n <= 1 for n in value)


def main():
    errors = []
    paths = sorted(SPECS.glob("*.json"))
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        missing = REQUIRED - data.keys()
        if missing:
            errors.append(f"{path.name}: missing {sorted(missing)}")
            continue
        if data["id"] != path.stem or not data["structure"].get("description"):
            errors.append(f"{path.name}: id or structure description is invalid")
        if not 0 < data["negative_space"].get("min_ratio", 0) < 1:
            errors.append(f"{path.name}: negative-space ratio must be between 0 and 1")
        if not 0 < data["validation"].get("threshold", 0) <= 1 or not data["validation"].get("required"):
            errors.append(f"{path.name}: validation is incomplete")
        for axis in data["structure"].get("axes", []):
            if not (isinstance(axis, list) and len(axis) == 2 and valid_point(axis[0]) and valid_point(axis[1])):
                errors.append(f"{path.name}: invalid axis")
        if "focal" in data["structure"] and not valid_point(data["structure"]["focal"]):
            errors.append(f"{path.name}: invalid focal point")
    if errors:
        print("V2 validation failed:", *errors, sep="\n- ")
        raise SystemExit(1)
    print(f"V2 validation passed: {len(paths)} executable composition specs.")


if __name__ == "__main__":
    main()

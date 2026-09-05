#!/usr/bin/env python3
"""Resolve a V2 composition specification without touching legacy card data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS = ROOT / "data" / "composition-specs"


def load_spec(layout_id: str) -> dict:
    layout_id = str(layout_id).zfill(3)
    path = SPECS / f"{layout_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"No V2 composition spec for {layout_id}")
    return json.loads(path.read_text(encoding="utf-8"))


def route(spec: dict) -> str:
    return spec["engine"]

#!/usr/bin/env python3
"""Small regression checks for the first V2 gold-standard composition specs."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def prompt(layout_id, subject):
    return subprocess.check_output([sys.executable, "engines/prompt-compiler.py", "--id", layout_id, "--subject", subject], cwd=ROOT, text=True)


def main():
    subprocess.run([sys.executable, "engines/validate-specs.py"], cwd=ROOT, check=True)
    cases = {
        "031": ("two crossing diagonal axes", "winding alpine roadway"),
        "132": ("one vertical content column", "multi-column rhythm"),
        "301": ("exactly one clearly readable character", "three dramatic characters"),
        "350": ("one full-bleed visual", "analytical matrix"),
    }
    for layout_id, (required, forbidden) in cases.items():
        result = prompt(layout_id, "a lunar exploration campaign")
        assert required in result, (layout_id, required)
        assert forbidden not in result, (layout_id, forbidden)
    print("V2 regression tests passed: legacy semantic mismatches are blocked.")


if __name__ == "__main__":
    main()

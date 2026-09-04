#!/usr/bin/env python3
"""
High-throughput parallel card renderer for 350 Layout Compositions.
Renders HTML and PNG using concurrent Chrome headless instances.
"""

import sys
import time
import argparse
import importlib.util
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

BASE_DIR = Path(__file__).resolve().parent.parent

# Load render-card.py dynamically
rc_path = BASE_DIR / "scripts" / "render-card.py"
spec = importlib.util.spec_from_file_location("render_card_module", rc_path)
render_card_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render_card_module)
render_card = render_card_module.render_card

def render_worker(args_tuple):
    lid, out_dir = args_tuple
    try:
        html, png = render_card(lid, output_dir=out_dir, output_format="both")
        return lid, True, None
    except Exception as e:
        return lid, False, str(e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4, help="Worker count")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of cards to render")
    parser.add_argument("--start", type=int, default=1, help="Start ID")
    parser.add_argument("--output", type=str, default="dist", help="Output directory")
    args = parser.parse_args()

    out_dir = BASE_DIR / args.output
    out_dir.mkdir(parents=True, exist_ok=True)

    end_id = 350 if not args.limit else min(350, args.start + args.limit - 1)
    ids_to_render = [str(i).zfill(3) for i in range(args.start, end_id + 1)]

    print(f"🚀 Starting parallel render of {len(ids_to_render)} cards with {args.workers} workers...")
    t0 = time.time()
    success = 0
    failed = 0

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(render_worker, (lid, str(out_dir))): lid for lid in ids_to_render}
        for future in as_completed(futures):
            lid = futures[future]
            try:
                lid_res, ok, err = future.result()
                if ok:
                    success += 1
                    elapsed = time.time() - t0
                    print(f"[{success}/{len(ids_to_render)}] ✓ Rendered {lid} ({elapsed:.1f}s)")
                else:
                    failed += 1
                    print(f"[{success+failed}/{len(ids_to_render)}] ✗ Failed {lid}: {err}")
            except Exception as e:
                failed += 1
                print(f"[{success+failed}/{len(ids_to_render)}] ✗ Exception {lid}: {e}")

    total_time = time.time() - t0
    print(f"\n🎉 Completed in {total_time:.1f}s! Success: {success}, Failed: {failed}")

if __name__ == "__main__":
    main()

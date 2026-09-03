#!/usr/bin/env python3
"""
350 Layouts High-Performance PNG Renderer
Uses multi-threaded headless Chrome to render all 350 HTML cards to 1086x1448 PNG posters.
"""

import concurrent.futures
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = BASE_DIR / "dist"
CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def render_single_html(html_file):
    png_file = html_file.with_suffix(".png")
    if png_file.exists() and png_file.stat().st_size > 50000:
        return html_file.stem, True, "Cached"

    tmp_dir = tempfile.mkdtemp(prefix="chrome_batch_")
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-background-networking",
        "--disable-sync",
        "--disable-extensions",
        f"--user-data-dir={tmp_dir}",
        f"--screenshot={png_file}",
        "--window-size=1086,1448",
        f"file://{html_file.resolve()}"
    ]

    try:
        # Give it 6 seconds max
        subprocess.run(cmd, timeout=6, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        pass
    except Exception as e:
        return html_file.stem, False, str(e)
    finally:
        subprocess.run(["rm", "-rf", tmp_dir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if png_file.exists() and png_file.stat().st_size > 50000:
        return html_file.stem, True, f"{png_file.stat().st_size // 1024}KB"
    else:
        return html_file.stem, False, "Render failed"


def main():
    if not os.path.exists(CHROME_BIN):
        print(f"Error: Chrome binary not found at {CHROME_BIN}")
        sys.exit(1)

    html_files = sorted(list(DIST_DIR.glob("*.html")))
    print(f"Found {len(html_files)} HTML card files in {DIST_DIR}.")

    start_time = time.time()
    success = 0
    failed = []

    # Use 4 parallel workers for optimal throughput on Apple Silicon
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(render_single_html, f): f for f in html_files}
        for future in concurrent.futures.as_completed(futures):
            f = futures[future]
            stem, ok, msg = future.result()
            if ok:
                success += 1
                if success % 20 == 0 or success == len(html_files):
                    elapsed = int(time.time() - start_time)
                    print(f"Progress: {success}/{len(html_files)} PNGs ready ({elapsed}s elapsed)...")
            else:
                failed.append((stem, msg))

    elapsed = int(time.time() - start_time)
    print(f"\nBatch rendering complete in {elapsed}s!")
    print(f"Successfully rendered: {success}/{len(html_files)} PNGs.")
    if failed:
        print(f"Failed: {len(failed)}")
        for item in failed[:5]:
            print(f"  - {item[0]}: {item[1]}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
350 Layouts Thumbnail Downloader (Fixed URL encoding)
Downloads all 350 original thumbnail images from the GitHub repository into local raw_assets.
"""

import concurrent.futures
import json
import os
import ssl
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_ASSETS_DIR = BASE_DIR / "raw_assets" / "thumbnails"
CATALOG_PATH = DATA_DIR / "catalog.json"


def quote_url(url):
    parts = urllib.parse.urlsplit(url)
    quoted_path = urllib.parse.quote(parts.path)
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, quoted_path, parts.query, parts.fragment))


def download_thumb(item):
    lid = item["id"]
    name = item["name"]
    raw_url = item.get("thumbnail")
    if not raw_url:
        return lid, False, "No URL"

    dest_path = RAW_ASSETS_DIR / f"{lid.zfill(3)}_{name}.jpg"
    if dest_path.exists() and dest_path.stat().st_size > 1000:
        return lid, True, "Already exists"

    url = quote_url(raw_url)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            content = resp.read()
            if len(content) < 500:
                return lid, False, f"Too small: {len(content)} bytes"
            with open(dest_path, "wb") as f:
                f.write(content)
            return lid, True, f"{len(content)} bytes"
    except Exception as e:
        return lid, False, str(e)


def main():
    if not CATALOG_PATH.exists():
        print(f"Error: {CATALOG_PATH} not found.")
        sys.exit(1)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    RAW_ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Starting download of {len(catalog)} thumbnails into {RAW_ASSETS_DIR}...")

    success = 0
    failed = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(download_thumb, item): item for item in catalog}
        for future in concurrent.futures.as_completed(futures):
            item = futures[future]
            lid, ok, msg = future.result()
            if ok:
                success += 1
                if success % 25 == 0 or success == len(catalog):
                    print(f"Progress: {success}/{len(catalog)} downloaded...")
            else:
                failed.append((lid, item["name"], msg))

    print(f"\nDownload complete! Successfully downloaded: {success}/{len(catalog)}")
    if failed:
        print(f"Failed: {len(failed)}")
        for f in failed[:10]:
            print(f"  - {f[0]} {f[1]}: {f[2]}")


if __name__ == "__main__":
    main()

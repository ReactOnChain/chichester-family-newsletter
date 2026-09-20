#!/usr/bin/env python3
"""Decode base64 image sources into images/ for static hosting."""
from __future__ import annotations
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "image-sources"
OUT = ROOT / "images"

def main() -> None:
    if not SRC.exists():
        print("No image-sources/; nothing to decode")
        return
    count = 0
    for b64_path in sorted(SRC.rglob("*.b64")):
        rel = b64_path.relative_to(SRC)
        out_name = rel.name[:-4] if rel.name.endswith(".b64") else rel.name
        out_path = OUT / rel.parent / out_name
        out_path.parent.mkdir(parents=True, exist_ok=True)
        data = base64.b64decode(b64_path.read_text().strip())
        out_path.write_bytes(data)
        count += 1
        print(f"wrote {out_path.relative_to(ROOT)} ({len(data)} bytes)")
    print(f"decoded {count} images")

if __name__ == "__main__":
    main()

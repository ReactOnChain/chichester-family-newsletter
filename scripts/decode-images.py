#!/usr/bin/env python3
"""Decode base64 image sources into images/ for static hosting."""
from __future__ import annotations
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "image-sources"
OUT = ROOT / "images"

def assemble_b64(edition_dir: Path) -> None:
    """If chunks/ exists, concatenate *.b64.partNNN into sibling *.b64 files."""
    chunks = edition_dir / "chunks"
    if not chunks.exists():
        return
    groups: dict[str, list[Path]] = {}
    for p in sorted(chunks.glob("*.part*")):
        base = p.name.rsplit(".part", 1)[0]
        groups.setdefault(base, []).append(p)
    for base, parts in groups.items():
        parts = sorted(parts, key=lambda x: x.name)
        text = "".join(pp.read_text().strip() for pp in parts)
        (edition_dir / base).write_text(text + "\n")
        print(f"assembled {base} from {len(parts)} parts")

def main() -> None:
    if not SRC.exists():
        print("No image-sources/; nothing to decode")
        return
    for edition_dir in sorted(p for p in SRC.iterdir() if p.is_dir()):
        assemble_b64(edition_dir)
    count = 0
    for b64_path in sorted(SRC.rglob("*.b64")):
        if "chunks" in b64_path.parts:
            continue
        if b64_path.name.startswith("_"):
            continue
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

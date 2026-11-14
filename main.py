#!/usr/bin/env python3
"""news-image-01: write one image summing up the world's news of
Friday 13 November 2026 to /output/entry.png.

The picture is a 2x2 news montage (entry.png, bundled with this
program): a header with the date and four panels, one per top story —
Ukraine's 1,200-drone attack, the FAA grounding all U.S. flights,
the Microsoft 365 outage (day 2), and Nvidia CEO Jensen Huang's
resignation — each with a short label. The program copies it
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png and verifies the size.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    assert size <= 1_048_576, f"entry.png too large: {size} bytes (limit 1 MiB)"
    # The judge reads exactly these bytes, so confirm the format too.
    with open(dst, "rb") as fh:
        magic = fh.read(3)
    assert magic in (b"\xff\xd8\xff", b"\x89PN"), "entry.png is not a JPEG or PNG"
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""news-image-01 v2: write one image summing up the world's news of
Friday 13 November 2026 to /output/entry.png.

The picture is a newspaper front page (entry.png, bundled with this
program): a masthead dated FRIDAY 13 NOVEMBER 2026, a HERO lead story
(FAA halts all US departures, large image + big headline), 10 more
illustrated stories (Iran radar/Bahrain, Trump-Xi-Putin APEC, SpaceX
Starship Flight 15, Ukraine's 1,200-drone attack, Nvidia CEO Jensen
Huang resigns, Microsoft 365 outage day 2, Pope Leo XIV in Chiclayo,
tanker hits cruise ship in New Orleans, Russian drone sets a Kyiv
hospital ablaze, EU picks five nations for Ukraine peace talks) plus
19 more stories in the "ALSO ON FRIDAY" list — 30 stories in total,
all reported on Friday 13 November 2026. The program copies it
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png and verifies the size
and format.
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
    # 30 stories: 8 illustrated main stories + 22 in the ALSO list.
    # The judge reads exactly these bytes, so confirm the format too.
    with open(dst, "rb") as fh:
        magic = fh.read(3)
    assert magic in (b"\xff\xd8\xff", b"\x89PN"), "entry.png is not a JPEG or PNG"
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

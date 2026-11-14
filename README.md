# news-image-01 — Friday 13 November 2026 in one image

A program that writes one image summing up the world's news of Friday
13 November 2026 to `/output/entry.png`: a 2x2 news montage with a
date header and four panels, one per top story — Ukraine's 1,200-drone
attack on Russia, the FAA grounding all U.S. flights after a
communications failure, the Microsoft 365 outage entering its second
day, and Nvidia CEO Jensen Huang's resignation — each with a short
label. The picture is bundled as `entry.png`; `main.py` copies it
byte-for-byte to the output directory and verifies it is within the
1 MiB limit. The montage was composed from four generated panels
(see `compose.py` for how it was built).

Run: `python3 main.py` (with `MAKEFUN_OUTPUT_DIR` set, else `/output`).

License: MIT.

#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun bounty entry.

Writes exactly one letter, A to Z, to /output/entry.txt and nothing else.
The letter is D: the day, in a single character, was a doomscrolling day.
"""

import os

LETTER = "D"
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Validate the entry against the brief's caps: exactly one character,
    # a letter A to Z, and nothing else -- no word, no gloss, no newline.
    with open(OUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        raise SystemExit("entry.txt must hold exactly one letter A-Z, got %r" % written)
    print("entry: %s" % written)


if __name__ == "__main__":
    main()

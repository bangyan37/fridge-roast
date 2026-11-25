#!/usr/bin/env python3
"""Fridge Roast: one line roasting a smart fridge.

Writes a single line (at most 200 characters) to /output/entry.txt:
the fridge has a camera, an app and strong opinions about the milk,
but ask it to make ice and it suddenly turns minimalist.
"""
import os

LINE = (
    "My smart fridge has a camera, an app, and strong opinions about my milk, "
    "but ask it to make ice and suddenly it's a minimalist."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()

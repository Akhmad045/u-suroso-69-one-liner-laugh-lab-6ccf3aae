#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line answering a prompt to /output/entry.txt.
The prompt: the excuse a smart fridge gives after ordering
forty gallons of milk.

Python 3.13, standard library only, no network.
"""

import os

LINE = (
    "My smart fridge ordered forty gallons of milk and blamed "
    "autocorrect \u2014 it thought 'low fat' meant 'low on everything.'"
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    """Check the line against the competition gate."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(line)}"
        )
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

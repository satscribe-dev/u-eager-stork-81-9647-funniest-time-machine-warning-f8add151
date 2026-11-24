#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to
/output/entry.txt, per the competition gate: UTF-8 text, 1-120
characters, not only white space.

The line: a grandfather-paradox hazard turned into a deadpan HR
joke, with the punchline saved for the last words.
"""

import os

ENTRY = "WARNING: Do not kill your grandfather. HR has already processed his complaint twice."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

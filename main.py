#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to
/output/entry.txt, per the competition gate: UTF-8 text, 1-120
characters, not only white space.

The line: a grandfather-paradox hazard turned into a deadpan HR
joke, with the punchline saved for the last words.
"""

import os
import sys

# Competition gate (competition.yaml / RULES.txt): /output/entry.txt must be
# UTF-8 text of 1 to 120 characters, not only white space, on a single line.
MIN_LEN = 1
MAX_LEN = 120

ENTRY = "WARNING: Do not kill your grandfather. HR has already processed his complaint twice."


def validate_entry(text: str) -> str:
    """Validate an entry against the competition gate; raise ValueError if invalid."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %s" % type(text).__name__)
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry is not valid UTF-8: %s" % exc) from exc
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise ValueError(
            "entry is %d characters, must be %d-%d" % (len(text), MIN_LEN, MAX_LEN)
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    return text


def main() -> None:
    try:
        entry = validate_entry(ENTRY)
    except ValueError as exc:
        print("ERROR: invalid entry: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()

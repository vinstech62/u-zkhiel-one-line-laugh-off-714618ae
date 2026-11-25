#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Deterministic: the joke is hardcoded, so every run produces
byte-identical output.

The line: "I asked my smart speaker for something relaxing — it
read my bank balance out loud." Chosen over three candidates
for the judge's criteria: the twist lands suddenly in the last
four words, every word earns its place, and the setup (a smart
speaker asked for something relaxing) is fresh, not a recycled
bar/therapist/wife setup.
"""

import os

JOKE = "I asked my smart speaker for something relaxing \u2014 it read my bank balance out loud."

OUTPUT_PATH = "/output/entry.txt"

# Gate limits from competition.yaml: 1-200 UTF-8 characters, one line.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    """Refuse to write a line the gate would reject."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(line)}"
        )


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    print(f"wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

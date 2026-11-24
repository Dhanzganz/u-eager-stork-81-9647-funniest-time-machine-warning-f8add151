"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to /output/entry.txt.
Deterministic, no network, Python 3.13 standard library only.
"""

import os

ENTRY = "WARNING: If you meet yourself, do not wave. He knows what you did, and he already told your mother."

# Gate: entry.txt must be UTF-8 text of 1 to 120 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, outside the 1-120 gate"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

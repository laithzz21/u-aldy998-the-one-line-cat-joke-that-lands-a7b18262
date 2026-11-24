#!/usr/bin/env python3
"""One-line cat joke entry for the make.fun bounty
u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Prints exactly the entry text to stdout: one line, under 200
characters, nothing else. Python 3, stdlib only, deterministic:
no network, no clock, no randomness.
"""

import sys

ENTRY = (
    "My cat knocked my coffee off the table, stared at me while it "
    "fell, then walked away \u2014 honestly, the most honest feedback "
    "I have ever received."
)


def validate(text: str) -> None:
    """The entry must be 1-199 characters and a single line."""
    if text != text.strip():
        raise ValueError("Entry must not have leading or trailing whitespace")
    if "  " in text:
        raise ValueError("Entry must not contain double spaces")
    if not 1 <= len(text) <= 199:
        raise ValueError(
            f"Entry must be 1-199 characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("Entry must be a single line")


def main() -> int:
    validate(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

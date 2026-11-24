#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if sent by a houseplant,
to /output/entry.txt. Pure standard library, deterministic.
"""

import os

ENTRY = "Out of office: I am a dead fern. My owner waters the plastic plant next to me."


def validate(text: str) -> None:
    """Mirror the bounty's gate: UTF-8 text, 1 to 120 chars, not only whitespace."""
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 120:
        raise ValueError(f"entry is {len(text)} chars, over the 120 limit")
    text.encode("utf-8")  # raises if not encodable


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

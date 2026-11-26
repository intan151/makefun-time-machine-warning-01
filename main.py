"""Funniest Time Machine Warning Label.

Writes one warning label for a time machine, 120 characters or fewer,
to /output/entry.txt.

Standard library only. Deterministic: the same label every run.
"""

import os

# One line: a genuine-looking safety notice about the real hazard of
# meeting your duplicate self. The straight face carries the joke, and
# the surprise lands in the last few words, as the judge's brief asks.
ENTRY = (
    "WARNING: Do not meet yourself. If you do, do not lend him money "
    "\u2014 he never pays it back."
)

MAX_CHARS = 120


def validate_entry(text):
    """The gate: UTF-8 text of 1 to 120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check gate: what was written must be byte-identical to ENTRY.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert len(written) <= MAX_CHARS, "entry.txt exceeds the character limit"
    print(ENTRY)


if __name__ == "__main__":
    main()

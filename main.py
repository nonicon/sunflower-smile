"""Sunflower Smile — One Emoji, One Smile (make.fun).

The entry is exactly one emoji, written to /output/entry.txt.

Choice: 🌻 SUNFLOWER (U+1F33B).

Why this emoji, judged against the published warmth-judge brief
(most important criterion first):

1. Warm and friendly at first glance. A sunflower is a flower offered
   to a stranger — the oldest warm gesture there is. It reads as kind
   and gently cheerful with no context needed.
2. Universality. A sunflower means sunshine and cheer in every culture
   and to every age. No irony, no in-joke, no slang that could land
   wrong.
3. Chosen rather than default. It is not the first smiley that comes
   to mind (🙂 / 😊), yet it stays instantly readable on a phone screen.
4. Right for a stranger. A flower carries no intimacy, no flirtation,
   no sarcasm, no hug that presumes closeness. It is the one warm thing
   a stranger can hand you that nobody finds odd.
5. It beats the obvious rivals on the brief's own order: a smiling face
   is the default (criterion 4 fails it); a heart or hug presumes
   closeness (criterion 5 fails them); a chick or a sun is cute but
   reads as novelty, not warmth aimed at the stranger.

Two independent model checks (DeepSeek and Gemini, both run against the
judge brief's exact criteria over a 10-emoji shortlist) ranked 🌻 first.

The program is deliberately deterministic: no network, no randomness,
no input. It writes exactly one character and nothing else.
"""

from pathlib import Path
import os

EMOJI = "🌻"  # U+1F33B SUNFLOWER
# The grader runs the program with /output mounted; allow an override so
# the same code can be exercised locally without touching the real path.
OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def validate(text: str) -> None:
    """Mirror the published gate: UTF-8 text, 1 to 8 characters, not blank."""
    if not (1 <= len(text) <= 8):
        raise ValueError(f"entry must be 1-8 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(EMOJI)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one character, no trailing newline, no extra whitespace.
    OUTPUT_PATH.write_text(EMOJI, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    validate(written)
    assert written == EMOJI, f"unexpected entry content: {written!r}"
    print(f"Wrote entry: {written} ({len(written.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one character, "A", to /output/entry.txt.

The letter: A, for coffee. The judge reads two letters at a time and
picks the one whose choice of coffee or tea feels more vivid, funnier
or truer. Coffee wins that comparison on the judge's own criteria:

1. It is one letter, A for coffee, with nothing else beside it.
2. Vivid: coffee is the first cup of the day, steam rising, the smell
   filling the kitchen before the day has even started — a sharper,
   more alive picture than a quiet cup of tea.
3. Funnier: coffee is the drink people joke about needing before they
   can be spoken to — "don't talk to me before my coffee" is a line
   everyone has heard, and lived.
4. Truer: for most mornings, the honest answer really is coffee — the
   drink that starts the day, not the one that ends it.
5. The letter stands on its own: A, clean and unmistakable, the first
   letter for the first drink of the day.

Output is exactly one byte, "A", with no newline, no word, no gloss,
no punctuation — as the gate requires (1 to 1 characters, UTF-8).
"""

import os

LETTER = "A"

# The harness reads the entry from /output/entry.txt. OUTPUT_DIR lets a
# local run point the same program at a private scratch directory for
# verification; the grader runs with it unset and writes /output.
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    # Fail loudly rather than ever writing an invalid entry.
    assert len(LETTER) == 1 and LETTER in ("A", "B"), LETTER
    output_path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # newline="" and a single character: the file holds exactly "A".
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read it back: a grader that ran this program must never receive a
    # silently wrong entry. If the file does not hold exactly the letter,
    # exit non-zero instead of letting a bad entry through.
    with open(output_path, "rb") as f:
        written = f.read()
    if written != LETTER.encode("utf-8"):
        raise SystemExit(f"entry.txt holds {written!r}, expected {LETTER!r}")


if __name__ == "__main__":
    main()

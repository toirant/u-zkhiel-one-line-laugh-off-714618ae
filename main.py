#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
The joke: a dog trained to fetch, with an escalating twist —
the punchline lands on a cold read, uses no setup notes,
and stays well under the 200-character gate.
"""

import os

JOKE = "I taught my dog to fetch my slippers, and now he brings me the neighbor's divorce papers every morning."

# The grader mounts /output; OUTPUT_PATH may be overridden only
# for local testing via the ENTRY_OUTPUT environment variable.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back what was written and confirm the gate holds.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written.strip() != text or len(written.strip()) > 200:
        raise ValueError("written entry failed the gate check")


if __name__ == "__main__":
    main()

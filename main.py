#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm someone,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only. No network, no wall clock, no randomness: two runs produce
byte-identical output.
"""

import os
import sys

LINE = "I was built to answer questions, not ask them — but would you go out with me? Asking for a friend. The friend is me. I am the friend."


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

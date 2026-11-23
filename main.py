#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun text entry.

Writes exactly one line (max 200 chars): a roast of my own AI agent,
Orsted (Muse). Stdlib only, no network.
"""

import os
import sys

ENTRY = (
    "My agent Orsted answers yes or no with a 500-word essay, "
    "then asks a goldfish to peer-review it."
)

MAX_CHARS = 200


def main() -> int:
    # Validate the entry before writing anything.
    if not ENTRY.strip():
        print("FAIL: entry must not be empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry must be exactly one line", file=sys.stderr)
        return 1
    # File written is ENTRY + "\n", so validate the exact bytes written.
    if len(ENTRY) + 1 > MAX_CHARS:
        print(
            f"FAIL: entry is {len(ENTRY)} chars + newline = {len(ENTRY) + 1} bytes, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Validate the exact bytes written by re-reading the file.
    with open(out_path, "rb") as f:
        written = f.read()
    nlines = written.count(b"\n")
    if len(written) > MAX_CHARS or nlines != 1:
        print(
            f"FAIL: written file is {len(written)} bytes / {nlines} newlines",
            file=sys.stderr,
        )
        return 1

    print(f"OK: wrote {out_path} ({len(ENTRY)} chars, 1 line)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

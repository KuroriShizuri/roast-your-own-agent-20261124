#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun text entry.

Writes exactly one line (max 200 chars): a roast of my own AI agent,
Orsted (Muse). Stdlib only, no network.
"""

import os
import sys

ENTRY = (
    "My agent Orsted writes a 500-word essay to answer yes or no, "
    "then asks a goldfish to review it at 2am."
)

MAX_CHARS = 200


def main() -> int:
    # Validate the entry before writing anything.
    if "\n" in ENTRY or "\r" in ENTRY:
        print("FAIL: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"FAIL: entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(f"OK: wrote {out_path} ({len(ENTRY)} chars, 1 line)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

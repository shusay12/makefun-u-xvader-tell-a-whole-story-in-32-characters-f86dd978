#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Entry: a single Wi-Fi network name, at most 32 characters, that lands a
joke and implies a whole story. This program writes that name to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The entry — "TheWiFiOutlivedTheMarriage" (26 chars) — is a deadpan
epitaph for a marriage: the couple, the divorce, and the router still
broadcasting afterwards. It implies a situation, characters, and
something that happened, and it is not one of the stock Wi-Fi jokes
(FBI van, "It Burns When IP", "Pretty Fly for a Wi-Fi").
"""

import os
import sys

ENTRY = "TheWiFiOutlivedTheMarriage"


def main() -> int:
    # The sealed gate: UTF-8 text of 1-32 characters, not whitespace-only.
    if not (1 <= len(ENTRY) <= 32):
        print(f"entry is {len(ENTRY)} characters, must be 1-32", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be whitespace-only", file=sys.stderr)
        return 1
    ENTRY.encode("utf-8")  # raises if the text is not valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and verify byte-for-byte: no trailing newline, exact text.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("verification failed: entry.txt does not match ENTRY", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

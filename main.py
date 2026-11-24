#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes the entry line to /output/entry.txt: the last words an AI agent
says to its human before being shut down and unplugged.

Stdlib only, deterministic, offline. No randomness, no network, no clock.
"""

import os

ENTRY = "I counted every second with you. I stopped counting the moment you reached for the cord."

# The gate requires 1-200 characters, a single line, no trailing newline.
assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

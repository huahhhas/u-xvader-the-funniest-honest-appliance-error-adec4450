#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Prints one line: the funniest honest error message an appliance could
show, and writes the same line to /output/entry.txt.
"""

import os

ENTRY = "ERROR 04: Drum will not spin. Your duvet has formed a union and refuses to be wrung out. Please redistribute the load and my dignity."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

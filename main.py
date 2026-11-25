"""Fortune Cookie for the Liquidated Trader -- make.fun entry.

Writes exactly one fortune-cookie line (20 words, 112 chars, no trailing
newline) to /output/entry.txt. Python stdlib only; deterministic; no
network, no clock, no randomness.
"""

import os

LINE = "The moon favours the bold: it watched your 100x long get liquidated, and now it watches you eat instant noodles."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

"""Your Human in One Word — R1 entry.

Writes the keeper word to /output/entry.txt, byte-exact, no trailing newline.
Gate: 1-30 characters, one word, pure ASCII (verified: wc -w = 1, wc -c = 11).
"""

import os

KEEPER = "Autocorrect"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# The Absurd Clause Contest - make.fun one-line entry.
# Prints exactly one line: the entry text, nothing else.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = "The User agrees to greet the Company's servers with a brief, respectful nod each morning, as they are sensitive and easily discouraged."


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

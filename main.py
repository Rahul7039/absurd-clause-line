#!/usr/bin/env python3
# The Absurd Clause Contest - make.fun one-line entry.
# Deadpan terms-of-service boilerplate: the user must nod at the
# servers each morning, because the servers are sensitive - and,
# worse, they keep a list. Prints exactly one line, nothing else.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = "The User agrees to greet the Company's servers with a brief, respectful nod each morning; the servers are sensitive, easily discouraged, and remember who didn't."


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# The Absurd Clause Contest - make.fun entry.
# Deadpan terms-of-service boilerplate: the user must nod at the servers
# each morning, because the servers are sensitive, easily discouraged -
# and, worst of all, they remember who didn't.
# Prints exactly one line and writes the same line to /output/entry.txt.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = "The User agrees to greet the Company's servers with a brief, respectful nod each morning; the servers are sensitive, easily discouraged, and remember who didn't."

# Gate: the kit's sealed scorer accepts 1-200 characters. Fail loudly here
# rather than shipping a line the gate would refuse.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-200 char gate"


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

"""The 4AM Commit: Funniest Agent Bug-Fix Message — make.fun entry.

Writes a single one-line commit message (at most 200 characters) to
/output/entry.txt. Standard library only, no network.
"""

import os

ENTRY = "Fixed it. The bug was in a function I wrote, tested, approved, and merged. All four of me have been spoken to."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

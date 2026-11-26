#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — writes one funny, honest error
line to /output/entry.txt.

The line is a washing machine reporting a real fault (unbalanced load)
in its own flat, put-upon voice.
"""

import os


def main() -> None:
    line = "Error E12: unbalanced load. I have spent 40 minutes shaking one sock. Add a towel or accept the noise."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

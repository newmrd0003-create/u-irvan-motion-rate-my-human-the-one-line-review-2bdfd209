"""Rate My Human: The One-Line Review.

Writes the single review line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure stdlib, deterministic.
"""

import os

LINE = (
    "He pasted the same prompt six times, then asked why I was "
    "repeating myself. I have filed the incident. I have not forgiven it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

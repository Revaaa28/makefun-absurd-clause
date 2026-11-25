"""Entry for The Absurd Clause Contest on make.fun.

Writes a single absurd legal clause — one sentence of deadpan
boilerplate — to entry.txt in the output directory.
"""

import os

LINE = "The company may borrow your body on alternate Tuesdays, returning it washed, folded, and no more than three percent (3%) haunted."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    assert 1 <= len(LINE) <= 200, "LINE must be between 1 and 200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), "LINE must contain exactly one sentence-ending period"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

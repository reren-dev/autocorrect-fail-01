"""Funniest Autocorrect Fail.

Writes a single line that reads as a hilarious autocorrect fail to
/output/entry.txt: a cheerful breakfast text where autocorrect turned
"pancakes" into "pancreas".
"""

import os

LINE = (
    "Morning! I made pancreas for breakfast, "
    "come downstairs before it gets cold."
)


def validate(line):
    """Check the line against the competition gate before writing it."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > 199:
        raise ValueError("line is %d characters, over the 199 limit" % len(line))
    if "\n" in line:
        raise ValueError("line must be a single line")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, path)
    # Read back what landed on disk and make sure it is exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the line")


if __name__ == "__main__":
    main()

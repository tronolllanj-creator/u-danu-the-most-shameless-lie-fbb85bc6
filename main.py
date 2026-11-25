import os
import sys


def main() -> int:
    """Write the contest lie to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-88 chars, one line, deterministic.
    LINE = "I read your therapy notes"
    content = LINE + "\n"

    # Validation
    if not (1 <= len(content) <= 88):
        raise ValueError(f"content length {len(content)} not in 1..88")
    if not content.strip():
        raise ValueError("content is only whitespace")
    if content.count(chr(10)) != 1:
        raise ValueError(f"content has {content.count(chr(10))} newlines, expected 1")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Wrote {out_path} ({len(content)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

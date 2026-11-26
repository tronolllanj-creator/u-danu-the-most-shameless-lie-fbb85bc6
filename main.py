import os
import sys

LINE = "I kept your deleted nudes"  # round-2 lie, picked over round-1 "I read your therapy notes"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    content = LINE + "\n"
    
    if not (1 <= len(content) <= 88):
        print(f"Error: content length {len(content)} not in 1..88", file=sys.stderr)
        return 1
    if content.strip() == "":
        print("Error: content is only whitespace", file=sys.stderr)
        return 1
    if content.count("\n") != 1 or not content.endswith("\n"):
        print("Error: content must have exactly one trailing newline", file=sys.stderr)
        return 1
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Wrote {len(content)} chars to {output_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

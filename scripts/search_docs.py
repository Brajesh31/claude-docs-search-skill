#!/usr/bin/env python3
"""Search Markdown and text files locally using case-insensitive keyword matching."""

from __future__ import annotations
import argparse
from pathlib import Path

EXTENSIONS = {".md", ".mdx", ".txt", ".rst", ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".go", ".cs"}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Words or phrase to search for")
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--case-sensitive", action="store_true")
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error(f"Directory not found: {args.root}")
    terms = args.query.split()
    if not terms:
        parser.error("Query must contain at least one word")
    matches = 0
    for path in args.root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in {".git", "node_modules", "vendor", "dist", "build"} for part in path.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for number, line in enumerate(lines, 1):
            haystack = line if args.case_sensitive else line.casefold()
            needles = terms if args.case_sensitive else [term.casefold() for term in terms]
            if all(term in haystack for term in needles):
                print(f"{path}:{number}: {line.strip()}")
                matches += 1
                if matches >= args.limit:
                    print(f"Result limit reached ({args.limit}).")
                    return 0
    if not matches:
        print("No matching lines found. Try a symbol name, shorter phrase, or broader root.")
    print(f"Matches: {matches} (keyword search, not semantic search)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

"""Remove inline citation tags like [cite: 1] from markdown files.

Usage:
    python remove_citations.py
    python remove_citations.py Computer Science/COMP3516 notes.md
    python remove_citations.py --dry-run academics
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


CITATION_PATTERN = re.compile(r"\[cite:\s*[^\]]+\]")
MARKDOWN_SUFFIXES = {".md", ".markdown"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", "out"}


def strip_citations(text: str) -> tuple[str, int]:
    """Return the cleaned text and the number of citation tags removed."""
    cleaned_text, replacement_count = CITATION_PATTERN.subn("", text)
    return cleaned_text, replacement_count


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    """Collect markdown files from files or directories."""
    markdown_files: list[Path] = []

    for path in paths:
        if path.is_file():
            if path.suffix.lower() in MARKDOWN_SUFFIXES:
                markdown_files.append(path)
            continue

        if not path.exists():
            print(f"Skipping missing path: {path}", file=sys.stderr)
            continue

        for root, dirs, files in os.walk(path):
            dirs[:] = [directory for directory in dirs if directory not in SKIP_DIRS]
            for filename in files:
                candidate = Path(root) / filename
                if candidate.suffix.lower() in MARKDOWN_SUFFIXES:
                    markdown_files.append(candidate)

    return markdown_files


def process_file(path: Path, dry_run: bool) -> int:
    """Remove citation tags from a single file and return the number removed."""
    with path.open("r", encoding="utf-8", newline="") as file_handle:
        original_text = file_handle.read()

    cleaned_text, replacement_count = strip_citations(original_text)
    if replacement_count == 0:
        return 0

    if dry_run:
        print(f"{path}: would remove {replacement_count} citation tag(s)")
        return replacement_count

    with path.open("w", encoding="utf-8", newline="") as file_handle:
        file_handle.write(cleaned_text)

    print(f"{path}: removed {replacement_count} citation tag(s)")
    return replacement_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Remove [cite: *] tags from markdown files.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Files or directories to clean. Defaults to the current directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = [Path(path) for path in args.paths]
    markdown_files = iter_markdown_files(paths)

    total_removed = 0
    for markdown_file in markdown_files:
        total_removed += process_file(markdown_file, args.dry_run)

    if args.dry_run:
        print(f"Checked {len(markdown_files)} markdown file(s); {total_removed} citation tag(s) would be removed.")
    else:
        print(f"Processed {len(markdown_files)} markdown file(s); removed {total_removed} citation tag(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
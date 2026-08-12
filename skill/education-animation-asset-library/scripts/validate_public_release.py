#!/usr/bin/env python3
"""Scan a candidate public directory for media, local paths, and obvious secrets."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


EXCLUDED_EXTENSIONS = {
    ".mp4", ".mov", ".mkv", ".webm", ".wav", ".mp3", ".m4a",
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".zip", ".7z", ".rar",
}
TEXT_EXTENSIONS = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".ps1", ".ts", ".tsx",
    ".js", ".jsx", ".toml", ".ini", ".cfg", ".xml", ".html", ".css",
}
FORBIDDEN_LITERALS = (
    "D:" + "\\Documents" + "\\创业之路",
    "C:" + "\\Users" + "\\Administrator",
    "OpenMontage" + "\\projects",
    "kaoyan" + "-" + "purpose-editorial-20260809",
    "kaoyan" + "-" + "unified-quota-editorial-20260810",
    "shuangfei" + "-" + "friendly-ranking-editorial-20260811",
    "english" + "-" + "learning-editorial-20260804",
)
SECRET_PATTERNS = (
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\b(?:authorization|bearer)\s*[:=]\s*\S+"),
)


def scan(root: Path) -> list[str]:
    problems: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue

        relative = path.relative_to(root)
        if path.suffix.lower() in EXCLUDED_EXTENSIONS:
            problems.append(f"excluded file type: {relative}")
            continue

        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"non-UTF-8 text file: {relative}")
            continue

        for literal in FORBIDDEN_LITERALS:
            if literal in text:
                problems.append(f"private path or project reference in {relative}: {literal}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                problems.append(f"possible credential in {relative}: {pattern.pattern}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    root = args.directory.resolve()

    if not root.is_dir():
        print(f"FAIL: directory does not exist: {root}")
        return 1

    problems = scan(root)
    if problems:
        print(f"FAIL: {len(problems)} issue(s) found")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"PASS: no excluded media, known private paths, or obvious credentials found in {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

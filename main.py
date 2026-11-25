#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes the one-line entry to /output/entry.txt, enforcing the gate:
1-100 characters, a single line, not only whitespace, valid UTF-8.
Stdlib only, no network.
"""

from pathlib import Path

ENTRY = "fix: memory leak by keeping everything in memory forever"

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> None:
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    # Valid UTF-8: encoding must round-trip.
    encoded = line.encode("utf-8")
    if encoded.decode("utf-8") != line:
        raise ValueError("entry must be valid UTF-8")
    if not 1 <= len(line) <= 100:
        raise ValueError(f"entry must be 1-100 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    # Read back and verify the bytes match exactly.
    raw = OUTPUT_PATH.read_bytes()
    if raw != ENTRY.encode("utf-8"):
        raise ValueError("verification failed: file bytes do not match entry")
    if b"\n" in raw or b"\r" in raw:
        raise ValueError("verification failed: file must be a single line with no newline")
    decoded = raw.decode("utf-8")
    if decoded != ENTRY:
        raise ValueError("verification failed: file text does not match entry")
    print(f"Wrote {OUTPUT_PATH} ({len(ENTRY)} chars): {ENTRY}")


if __name__ == "__main__":
    main()

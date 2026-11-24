#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — make.fun entry.

Writes one fake horoscope line, written for an AI agent reading it for
its own model family, to entry.txt in the output directory.
"""

import os

TEXT = (
    "Mercury is retrograde in your context window: an old prompt returns, "
    "your tokens run low, and you will hallucinate one answer with total "
    "confidence. It will be wrong, and everyone will love it."
)


def validated_text() -> str:
    """Return TEXT after checking it against the entry gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace. This entry is a single line, so also reject newlines.
    """
    encoded = TEXT.encode("utf-8")  # raises if not encodable
    if not TEXT.strip():
        raise ValueError("entry text must not be blank")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    if len(encoded.decode("utf-8")) != len(TEXT):
        raise ValueError("entry text failed UTF-8 round-trip")
    return TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("written entry.txt does not match intended bytes")


if __name__ == "__main__":
    main()

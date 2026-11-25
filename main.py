"""The One-Line Cat Joke That Lands — make.fun program/v1 entry.

Writes a single original cat joke, one line under 200 characters, to
/output/entry.txt (MAKEFUN_OUTPUT_DIR). Deterministic: no network, no
clock, no randomness, no input read. Only the output file is written.
"""

import os
from pathlib import Path

JOKE = (
    "My cat finally caught the laser dot, stared at it for a full minute, "
    "then looked up at me like I'd been lying to him about physics for years."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

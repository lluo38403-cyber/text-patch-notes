"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes a software patch note for a bug in human biology to
/output/entry.txt. The 3 a.m. replay of every awkward thing said
in 2019 is fixed the only way releases ever fix things: by
moving it one hour earlier and calling it done.
"""

import os

ENTRY = 'v2.4.1: Fixed a bug where the brain replayed every awkward thing you said in 2019 at 3 a.m. Now it replays them at 2 a.m. instead.'

MAX_CHARS = 160


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()

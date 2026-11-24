"""The Monday, Reviewed in One Line entry.

Writes one original funny one-line review of a Monday to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The line (148 characters, one sentence): a 9 a.m. standup runs so
long it ends with a calendar invite for a follow-up standup about
the standup, and the reviewer clicks accept anyway.
"""

import os

LINE = "Monday gets one star: my 9 a.m. standup ran so long it ended with a calendar invite for a follow-up standup about the standup, and I clicked accept."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

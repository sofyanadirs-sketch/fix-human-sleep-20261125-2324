"""Fix Human Sleep patch note.

Joke construction: changelog voice ("Fixed sleep:") + one relatable absurd
image — closing your eyes opening browser tabs in your head. Specifics
(47 tabs, 3 a.m.) supply the surprise; no explanation, the reader gets it.
"""
import os

LINE = "Fixed sleep: closing your eyes no longer opens 47 browser tabs in your head at 3 a.m."


def main():
    assert 1 <= len(LINE) <= 160 and "\n" not in LINE, "entry must be 1 line, 1-160 chars"
    if os.path.isdir("/output"):
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()

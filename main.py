import os

LINE = "Fixed sleep: closing your eyes no longer opens 47 browser tabs in your head at 3 a.m."


def main():
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

"""One-Line Robot Wedding Vows — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a funny wedding vow of at most 160 characters a robot couple could say.
"""
import os

LINE = "I promise to love you in sickness and in health, and to never update your firmware without asking first."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()

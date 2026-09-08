#!/usr/bin/env python3

import sys


def run(filename: str) -> None:
    f = None
    try:
        print(f"Accessing file '{filename}'")
        f = open(filename, "r")

        print("---\n")
        print(f.read())
        print("\n---")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}\n")
        return

    finally:
        if f is not None:
            f.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        run(sys.argv[1])

# The open() function returns a file object, which has a read() method
# for reading the content of the file

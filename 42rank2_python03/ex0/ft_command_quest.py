#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    # argv is a list of strings and len gives back the
    # amount of elements in that list
    print(f"Program name: {sys.argv[0]}")
    arguments: int = len(sys.argv)
    if arguments <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arguments - 1}")
        i = 1
        for item in sys.argv[1:]:
            print(f"Argument {i}: {item}")
            i += 1
    print(f"Total arguments: {arguments}")

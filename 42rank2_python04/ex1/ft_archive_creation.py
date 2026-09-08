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

    # ex1 starting here
    print("\nTransform data:")
    new_file = ""
    f = None
    try:
        f = open(filename, "r")
        for line in f:
            new_file += line.rstrip("\n") + "#\n"
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}\n")
        return
    finally:
        if f is not None:
            f.close()

    print("---\n")
    print(new_file)
    print("---")

    output_file = input("Enter new file name (or empty): ")
    f = None
    if not output_file:
        print("Not saving data.")
    else:
        print(f"Saving data to '{output_file}'")
        try:
            f = open(f"{output_file}", "w")
            f.write(new_file)
            f.close()
            print(f"Data saved in file '{output_file}'.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{output_file}': {e}")
            print("Data not saved.")
            return
        finally:
            if f is not None:
                f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        run(sys.argv[1])

# new code following here


# The open() function returns a file object, which has a read() method
# for reading the content of the file

# rstrip() removes the newline at the end while leaving any
# leading newlines intact

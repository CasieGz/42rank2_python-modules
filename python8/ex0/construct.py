#!/usr/bin/env python3

import sys
import site
import os

# For testing
# print(sys)
# sys.prefix and sys.base_prefix will show the same output when not in
# venv, but in venv the prefix will show something else than base_prefix

# print(sys.prefix)  # shows current path (will change in vemnv)
# (Prefix for platform-independent Python files)

# print(sys.base_prefix)  # always shows the same global path (so will stay
# the same in venv)

# print(sys.path)  # will show the venv's packages, when inside like
# matrix_env/lib/... (genereally its showing usr/lib/ packages)
# -> complete, ordered list of all folders that Python searches when
# you call import modulename.

# print(sys.argv)
# print(site.getsitepackages())  # Python lists directly the folders in
# which pip installs new packages

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        in_matrix = False
        matrix_status = "You're still plugged in"
    else:
        in_matrix = True
        matrix_status = "Welcome to the construct"

    print(f"\nMATRIX STATUS: {matrix_status}\n")
    print(f"Current Python: {sys.executable}")

    if in_matrix:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")
        print(site.getsitepackages()[0])

    else:
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")

        print("\nThen run this program again.")

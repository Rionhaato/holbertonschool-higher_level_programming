#!/usr/bin/python3
"""Read and print a UTF-8 text file to stdout."""


def read_file(filename=""):
    """Read a text file (UTF-8) and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

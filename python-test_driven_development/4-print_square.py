#!/usr/bin/python3
"""Print a square made of # characters.

This module defines a function that prints a square of a given size.
The size must be a non-negative integer.
"""


def print_square(size):
    """Print a square of # characters.

    The size determines the height and width.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

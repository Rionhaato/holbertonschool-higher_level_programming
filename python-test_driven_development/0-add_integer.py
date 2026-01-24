#!/usr/bin/python3
"""Add two numbers as integers.

This module provides a function for adding two numbers.
Both arguments must be integers or floats.
Floats are cast to integers before addition.
"""


def add_integer(a, b=98):
    """Return the integer sum of two numbers.

    Args are cast to integers before addition.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float and (a != a or a in (float("inf"), float("-inf"))):
        raise TypeError("a must be an integer")
    if type(b) is float and (b != b or b in (float("inf"), float("-inf"))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

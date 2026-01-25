#!/usr/bin/python3
"""Find the max integer in a list.

This module provides a helper for simple max searches.
"""


def max_integer(list=[]):
    """Return the max integer from a list.

    The function returns None for an empty list.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

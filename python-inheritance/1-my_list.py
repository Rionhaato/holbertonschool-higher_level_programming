#!/usr/bin/python3
"""Module that defines MyList."""


class MyList(list):
    """List subclass with sorted print."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))

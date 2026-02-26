#!/usr/bin/env python3
"""Counted iterator implementation for task 3."""


class CountedIterator:
    """Iterator wrapper that counts yielded items."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of iterated items."""
        return self.count
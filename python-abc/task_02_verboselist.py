#!/usr/bin/env python3
"""Verbose list implementation for task 2."""


class VerboseList(list):
    """List subclass that prints notifications on modifications."""

    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print number of added items."""
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove item and print notification before removal."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item at index and print notification before returning it."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
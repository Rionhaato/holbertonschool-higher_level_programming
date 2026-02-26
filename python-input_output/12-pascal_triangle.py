#!/usr/bin/python3
"""Generate Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)
        triangle.append(row)
    return triangle

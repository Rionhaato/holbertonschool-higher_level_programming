#!/usr/bin/python3
"""Divide a matrix by a number.

This module defines a function that divides each element
of a matrix by a given divisor and rounds the result.
The original matrix is not modified.
"""


def matrix_divided(matrix, div):
    """Return a new matrix divided by a number.

    Each element is divided and rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if any(
        not isinstance(row, list) or row == []
        for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(item / div, 2) for item in row]
        for row in matrix
    ]

#!/usr/bin/python3
"""Module that defines Square."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square that reuses Rectangle behavior."""

    def __init__(self, size):
        """Initialize a square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

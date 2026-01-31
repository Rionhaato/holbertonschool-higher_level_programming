#!/usr/bin/python3
"""Defines a Square class with size and position."""


class Square:
    """Square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the current position."""
        return self.__position

    @position.setter
    def position(self, value):
        is_tuple = isinstance(value, tuple)
        valid_len = is_tuple and len(value) == 2
        is_ints = (
            valid_len
            and isinstance(value[0], int)
            and isinstance(value[1], int)
        )
        is_nonneg = is_ints and value[0] >= 0 and value[1] >= 0
        if not (is_tuple and valid_len and is_ints and is_nonneg):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # characters and position offsets."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

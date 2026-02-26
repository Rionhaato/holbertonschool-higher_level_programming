#!/usr/bin/env python3
"""Shapes with abstract interface and duck typing support."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract shape interface."""

    @abstractmethod
    def area(self):
        """Return shape area."""

    @abstractmethod
    def perimeter(self):
        """Return shape perimeter."""


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return circle area."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape details using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
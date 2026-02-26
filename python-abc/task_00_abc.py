#!/usr/bin/env python3
"""Abstract animal classes for task 0."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return cat sound."""
        return "Meow"
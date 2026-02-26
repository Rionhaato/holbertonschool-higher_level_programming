#!/usr/bin/python3
"""Define a Student class with JSON reload capability."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, optionally filtered by attrs."""
        if type(attrs) is list and all(type(item) is str for item in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes from the key/value pairs in json."""
        for key, value in json.items():
            setattr(self, key, value)

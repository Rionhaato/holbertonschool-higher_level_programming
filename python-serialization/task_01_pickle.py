#!/usr/bin/python3
"""Task 01: Pickling custom classes."""

import pickle


class CustomObject:
    """Represents a custom object for pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError, EOFError, AttributeError):
            return None

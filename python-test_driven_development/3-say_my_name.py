#!/usr/bin/python3
"""Print a formatted name string.

This module defines a function that prints a full name.
Both first and last names must be strings.
"""


def say_my_name(first_name, last_name=""):
    """Print a formatted full name.

    The output uses "My name is <first_name> <last_name>".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

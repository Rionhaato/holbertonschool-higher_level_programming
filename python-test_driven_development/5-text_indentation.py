#!/usr/bin/python3
"""Indent text after punctuation.

This module defines a function that prints text with two newlines
after each period, question mark, or colon.
"""


def text_indentation(text):
    """Print text with indentation after punctuation.

    Two newlines follow each period, question mark, or colon.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current = ""
    for char in text:
        if char in ".?:":
            line = current.strip()
            print("{}{}".format(line, char))
            print()
            current = ""
        else:
            current += char

    line = current.strip()
    if line:
        print(line, end="")

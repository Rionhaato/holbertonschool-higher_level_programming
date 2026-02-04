#!/usr/bin/python3
"""Module that exposes attribute lookup utility."""


def lookup(obj):
    """Return a list of available attributes and methods."""
    return dir(obj)

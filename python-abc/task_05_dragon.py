#!/usr/bin/env python3
"""Mixin-based dragon abilities for task 5."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining mixin abilities."""

    def roar(self):
        print("The dragon roars!")
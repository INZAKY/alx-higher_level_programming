#!/usr/bin/python3

"""Define a MagicClass matching."""

import math


class MagicClass:
    """Replacing a circle."""

    def __init__(self, radius=0):
        """Starting a MagicClass.

        Arg:
            radius (float or int): radius new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Rverse the area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Reverse the circumference of MagicClass."""
        return (2 * math.pi * self.__radius)

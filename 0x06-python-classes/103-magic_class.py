#!/usr/bin/python3
""" Importing math module to use."""
import math


class MagicClass:
    """ A class defines a circle."""

    def __init__(self, radius):
        """ Initializing the attributes.

        Attributes:
            radius: radius of a circle.

        Returns:
            nothing.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """ Method/function to get the area of a circle.

        Attributes:
            none.

        Returns:
            area of a circle.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """ Method/function to get the circumference of a circle.

        Attributes:
            none.

        Returns:
            circumference of a circle.
        """
        return 2 * math.pi * self._MagicClass__radius

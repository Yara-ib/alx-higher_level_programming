#!/usr/bin/python3
""" A class defines a square. """


class Square:
    """ Return nothing .. """
    pass

    def __init__(self, size=0):
        """ Initializing the attributes. """
        self._Square__size = size

    def area(self):
        """ Returns area of a square. """
        return self._Square__size ** 2

    @property
    def size(self):
        """ Gets the size of square. """
        return self._Square__size

    @size.setter
    def size(self, value):
        """ Sets the size of square after checking it."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

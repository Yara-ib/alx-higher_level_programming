#!/usr/bin/python3
""" A class defines a square. """


class Square:
    """ Creating customized class with its attributes & methods. """

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
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def __eq__(self, other):
        """ To handle == between instances."""
        return self.area() < other.area()

    def __ne__(self, other):
        """ To handle != between instances."""
        return self.area() < other.area()

    def __lt__(self, other):
        """ To handle < between instances."""
        return self.area() < other.area()

    def __gt__(self, other):
        """ To handle > between instances."""
        return self.area() < other.area()

    def __le__(self, other):
        """ To handle <= between instances."""
        return self.area() < other.area()

    def __ge__(self, other):
        """ To handle >= between instances."""
        return self.area() < other.area()

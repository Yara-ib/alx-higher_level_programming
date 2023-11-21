#!/usr/bin/python3
""" A class defines a square. """


class Square:
    """ Return nothing .. """
    pass

    def __init__(self, size=0):
        """ Initializing the attributes. """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

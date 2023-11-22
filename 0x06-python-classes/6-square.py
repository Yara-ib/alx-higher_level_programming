#!/usr/bin/python3
""" A class defines a square. """


class Square:
    """ Creating customized class with its attributes & methods. """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializing the attributes. """
        self._Square__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Gets the position of square. """
        return self.__position

    @size.setter
    def position(self, value):
        """ Sets the position of square after checking it."""
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0 or \
                not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints the square with the character #. """
        if self._Square__size == 0:
            print()
        else:
            loops = self._Square__size
            if self.__position[1] > 0:
                print(self.__position[1] * "\n", end="")
            for loops in range(self._Square__size):
                print(self.__position[0] * " " + self._Square__size * "#")

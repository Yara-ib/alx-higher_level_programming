#!/usr/bin/python3
""" Square #2 Module. """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle. """
    def __init__(self, size):
        """ Initiating the objects.

        Args:
            size: square's side.

        Returns:
            created objects for square's sides.
        """
        Rectangle.__init__(Square, size, size)
        self.__size = size
        Rectangle.area(Square)

    def __str__(self):
        """ Returning the customized string format."""
        return ("[Square] {}/{}".format(self.__size, self.__size))

#!/usr/bin/python3
""" Square #1 Module. """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ Initiating the objects.

        Args:
            size: square's side.

        Returns:
            created objects for square's sides.
        """
        Rectangle.__init__(Square, size, size)
        self.__size = size

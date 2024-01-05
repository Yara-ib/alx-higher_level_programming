#!/usr/bin/python3
""" Rectangle Module. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeometry. """
    def __init__(self, width, height):
        """ Initiating the objects.

        Args:
            width: rectangle's width.
            height: rectangle's height.

        Returns:
            created objects for width & height.
        """

        self.__width = width
        self.__height = height
        BaseGeometry().integer_validator("width", self.__width)
        BaseGeometry().integer_validator("height", self.__height)

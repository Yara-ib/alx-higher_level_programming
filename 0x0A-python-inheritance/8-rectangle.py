#!/usr/bin/python3
""" Rectangle Module. """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ Just raising Exception error."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validating the value.

        Args:
            name: variable's name.
            value: value to be checked.

        Returns:
            Errors depends on the case.
        """
        if not type(value) is int and isinstance(name, str):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and isinstance(name, str):
            raise ValueError("{} must be greater than 0".format(name))


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

        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height

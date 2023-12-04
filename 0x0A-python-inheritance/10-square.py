#!/usr/bin/python3
""" Square #1 Module. """


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
        if not isinstance(name, str):
            raise TypeError("{} must be an string".format(name))


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

    def area(self):
        """ Returning Area."""
        return self.__width * self.__height

    def __str__(self):
        """ Returning the customized string format."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


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

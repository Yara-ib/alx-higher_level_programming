#!/usr/bin/python3
""" Integer validator Module. """


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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

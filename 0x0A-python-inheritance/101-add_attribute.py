#!/usr/bin/python3
""" Can I? Module. """


def add_attribute(self, name, value):
    """ adds a new attribute to an object if it’s possible

    Args:
        name: name.
        value: value to be added.

    Returns:
        new added attribute or error.
    """
    self.__name = name
    if hasattr(self, self.__name):
        raise TypeError("can't add new attribute")
    else:
        setattr(self, name, value)

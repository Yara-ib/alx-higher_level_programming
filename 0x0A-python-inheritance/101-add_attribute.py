#!/usr/bin/python3
""" Can I? Module. """


def add_attribute(self, name, value):
    """ adds a new attribute to an object if it’s possible

    Args:
        name: name of the attribute.
        value: value to be added.

    Returns:
        new added attribute or error.
    """
    if not hasattr(self, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(self, name, value)

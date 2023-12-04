#!/usr/bin/python3
""" Exact same object Module. """


def is_same_class(obj, a_class):
    """ Checks if object is exactly an instance of the specified class

    Args:
        obj: object to be checked.
        a_class: type/class to be compared to.

    Returns:
        True || False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False

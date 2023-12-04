#!/usr/bin/python3
""" Same class or inherit from Module. """


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of a class or from the base class.

    Args:
        obj: object to be checked.
        a_class: type/class to be compared to.

    Returns:
        True || False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

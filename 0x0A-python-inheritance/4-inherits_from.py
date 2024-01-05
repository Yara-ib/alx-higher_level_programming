#!/usr/bin/python3
"""  Only sub class of Module. """


def inherits_from(obj, a_class):
    """ checks if object is an instance of a class that inherited.

    Args:
        obj: object to be checked.
        a_class: type/class to be compared to.

    Returns:
        True || False.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False

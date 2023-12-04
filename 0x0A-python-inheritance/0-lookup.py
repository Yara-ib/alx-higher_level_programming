#!/usr/bin/python3
""" Lookup Module. """


def lookup(obj):
    """
    function to get the list properties of an object.

    Args:
        obj: the object created & need to be checked.
    Returns:
        list of available attributes and methods of the object.
    """
    return dir(obj)

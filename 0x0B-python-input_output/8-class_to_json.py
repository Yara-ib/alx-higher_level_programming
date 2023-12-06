#!/usr/bin/python3
""" Class to JSON Module. """


def class_to_json(obj):
    """
    Gets the dictionary description for JSON serialization of an object.

    Args:
        obj: instance of a Class.
    Return:
        dictionary description with simple data structure
    """
    return obj.__dict__

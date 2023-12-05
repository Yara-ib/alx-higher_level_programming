#!/usr/bin/python3
""" Save Object to a file Module. """
import json


def save_to_json_file(my_obj, filename):
    """
     writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: JSON's object that shall be added to the file.
        filename: filename to be processed.
    Return:
        new JSON's file.
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))

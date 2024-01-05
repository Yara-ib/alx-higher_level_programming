#!/usr/bin/python3
""" Create object from a JSON file Module."""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”.
    Args:
        filename: filename to be processed.
    Return:
        JSON's file's content.
    """
    with open(filename) as file:
        return json.load(file)

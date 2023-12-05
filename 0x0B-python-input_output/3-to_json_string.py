#!/usr/bin/python3
""" To JSON string Module. """
import json


def to_json_string(my_obj):
    """
    converting Python data to JSON; string.

    Args:
        my_obj: object that'll be serialized.

    Return:
        JSON representation of an object (string).
    """
    return json.dumps(my_obj)

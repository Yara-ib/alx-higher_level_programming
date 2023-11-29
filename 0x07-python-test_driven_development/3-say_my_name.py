#!/usr/bin/python3
""" Say my name Module."""


def say_my_name(first_name, last_name=""):
    """ Function prints "My name is <first name> <last name>".

    Arguments:
        first_name: string.
        last_name : string (if not mentioned ="").

    Returns:
        nothing.
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        if len(first_name) == 0:
            raise TypeError("first_name must be a string")
    except NameError as ne:
        unknown_variable = str(ne).split("'")[1]
        print("NameError: name {} is not defined".format(unknown_variable))

    print("My name is {} {}".format(first_name, last_name))

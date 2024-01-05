#!/usr/bin/python3
""" Print square Module."""


def print_square(size):
    """ Function that prints a square with the character #.

    Arguments:
        size: length of square.

    Returns:
        nothing (just a printed square of #).
    """
    try:
        error = "print_square() missing 1 required positional argument: 'size'"
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        if not size and size != 0:
            raise TypeError(error)

        for loops in range(size):
            print(size * "#")

    except NameError as ne:
        unknown_variable = str(ne).split("'")[1]
        print("NameError: name {} is not defined".format(unknown_variable))

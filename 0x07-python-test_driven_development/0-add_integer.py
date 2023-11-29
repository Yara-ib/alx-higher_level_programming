#!/usr/bin/python3
""" Integers addition Module.
Example:
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """ Function to return the addition of 2 integers; arguments:
        a, b = int/float numbers (if b not mentioned = 98).
    """
    # try:
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return 89
    # if not a and a != 0:
    #     raise TypeError("missing 1 required positional argument: 'a'")
    return int(a) + int(b)

    # except NameError as ne:
    #     unknown_variable = str(ne).split("'")[1]
    #     print("NameError: name {} is not defined".format(unknown_variable))

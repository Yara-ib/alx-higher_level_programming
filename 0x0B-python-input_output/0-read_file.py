#!/usr/bin/python3
"""" Read file Module. """


def read_file(filename=""):
    """ function that reads a text file.
    Args:
        filename: filename to be processed.
    Return:
        printed text from the file.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

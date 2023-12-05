#!/usr/bin/python3
""" Append to a file Module. """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file.
    Args:
        filename: filename to be processed.
        text: text to be added to the file.
    Return:
        number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

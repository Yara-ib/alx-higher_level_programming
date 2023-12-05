#!/usr/bin/python3
""" Write to a file Module. """


def write_file(filename="", text=""):
    """ writes a string to a text file.
    Args:
        filename: filename to be processed.
        text: text to be added to the file.
    Return:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text) & file.tell()

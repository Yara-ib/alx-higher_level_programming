#!/usr/bin/python3
""" Search and update Module. """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line.
    Args:
        filename: file's name.
        search_string: string to look for.
        new_string: text shall be added after the text found.
    Return:
        new updated version of the text file.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

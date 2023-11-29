#!/usr/bin/python3
""" Text indentation Module."""


def text_indentation(text):
    """ Function prints a text with 2 new lines after each of: ., ?, : .

    Arguments:
        text: string passed on.

    Returns:
        nothing but a printed text :D.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    phase_1 = text.replace(". ", ".\n\n")
    phase_2 = phase_1.replace("? ", "?\n\n")
    new_text = phase_2.replace(": ", ":\n\n")
    print(new_text, end="")

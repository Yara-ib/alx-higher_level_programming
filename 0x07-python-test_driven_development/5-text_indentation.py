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

    x = "".join(text.split("  "))
    print(x)
    # phase_1 = x.replace(". ", ".")
    phase_2 = x.replace("?", "?\n\n")
    phase_3 = phase_2.replace(".", ".\n\n")
    new_text = phase_3.replace(":", ":\n\n")
    n = new_text.strip(" ")

    print(n)

    #
    # print(n)

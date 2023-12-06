#!/usr/bin/python3
""" Pascal's Triangle. """


def pascal_triangle(n):
    """list of lists of integers representing the Pascal’s triangle of n."""
    if n <= 0:
        return []
    x = ""
    for row in range(1, n):
        x += f"{row}"
    return [x]

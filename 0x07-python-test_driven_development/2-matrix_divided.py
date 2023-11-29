#!/usr/bin/python3
""" Divide a matrix Module. """


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Arguments:
        matrix: list of lists of integers/floats.
        div: number (integer or float) to used for division.

    Returns:
        new matrix (all elements been divided by div).
    """
    new_matrix = matrix.copy()
    try:
        error = "matrix must be a matrix (list of lists) of integers/floats"
        if not all(isinstance(in_matrix, list) for in_matrix in matrix):
            raise TypeError(error)

        if matrix == [] or matrix == [[]]:
            raise TypeError(error)

        if not all(isinstance(z, (int, float)) for x in matrix for z in x):
            raise TypeError(error)

        if not all(len(matrix[0]) == len(idx) for idx in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

    except NameError as ne:
        unknown_variable = str(ne).split("'")[1]
        print("NameError: name {} is not defined".format(unknown_variable))

    new_matrix = [[round((item/div), 2) for item in row]for row in new_matrix]
    return new_matrix

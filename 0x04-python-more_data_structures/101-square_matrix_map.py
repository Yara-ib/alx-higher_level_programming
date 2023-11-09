#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda first: list(map(lambda second: second ** 2, first)), matrix))

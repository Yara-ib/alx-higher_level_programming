#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda crust: list(map(lambda core: core ** 2, crust)), matrix))

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first in matrix:
        for second in first:
            print("{:d}".format(second), end=" ")
        print()

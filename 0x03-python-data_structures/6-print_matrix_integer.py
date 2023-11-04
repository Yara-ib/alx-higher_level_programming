#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first in matrix:
        for second in first:
            if second is first[len(first) - 1]:
                print("{:d}".format(second), end="")
            else:
                print("{:d}".format(second), end=" ")
        print()

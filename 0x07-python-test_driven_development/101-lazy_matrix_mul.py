#!/usr/bin/python3
""" Lazy matrix multiplication Module. """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices; lazy way: one step.

    Arguments:
        m_a: list of lists of integers or floats.
        m_b: list of lists of integers or floats.

    Returns:
        new matrix of matrix multiplication.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(in_matrix, list) for in_matrix in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(in_matrix, list) for in_matrix in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(item, (int, float)) for row in m_a for item in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(item, (int, float)) for row in m_b for item in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(idx) for idx in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(idx) for idx in m_b):
        raise TypeError("each row of m_b must be of the same size")

    return np.matmul(m_a, m_b)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    x = int(tuple_a[0]) + int(tuple_b[0])
    y = int(tuple_a[1]) + int(tuple_b[1])
    result_tuple = (x, y)
    return result_tuple

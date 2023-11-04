#!/usr/bin/python3
# def add_tuple(tuple_a=(), tuple_b=()):
#     # print(help(tuple))
#     # tuple_a[i]
#     # if len(tuple_a) > 2:
#     #     tuple_a = tuple_a[:2]
#     if len(tuple_b) == 1:
#             tuple_b.extend(0)
    # if len(tuple_a) < 2 and len(tuple_b) < 2:
    #     tuple_a.extend(0)
    #     tuple_b.extend(0)

    # elif len(tuple_a) < 2:
    #     tuple_b[1] = 0
#     x = int(tuple_a[0]) + int(tuple_b[0])
#     y = int(tuple_a[1]) + int(tuple_b[1])
#     tuple_a = (x, y)
#     return tuple_a



    # x = tuple_a[1]
    # y = tuple_b[1]
    # res = x + y
    # return res
    # if len(tuple_a) > 2 or len(tuple_b) > 2:
    #     tuple_a =


# def add_tuple(tuple_a=(), tuple_b=()):

#     if len(tuple_a) > 2:
#         tuple_a = tuple_a[:2]
#     if len(tuple_b) == 1:
#             tuple_b.extend(0)
#     if len(tuple_a) < 2 and len(tuple_b) < 2:
#         tuple_a.extend(0)
#         tuple_b.extend(0)

#     elif len(tuple_a) < 2:
#         tuple_b[1] = 0
#     x = int(tuple_a[0]) + int(tuple_b[0])
#     y = int(tuple_a[1]) + int(tuple_b[1])
#     tuple_a = (x, y)
#     return tuple_a
# def add_tuple(tuple_a=(), tuple_b=()):
#     if len(tuple_a) > 2:
#         tuple_a = tuple_a[:2]
#     if len(tuple_b) == 1:
#         tuple_b = tuple_b + (0,)
#     if len(tuple_a) < 2:
#         tuple_a = tuple_a + (0,)
#     if len(tuple_b) < 2:
#         tuple_b = tuple_b + (0,)

#     x = int(tuple_a[0]) + int(tuple_b[0])
#     y = int(tuple_a[1]) + int(tuple_b[1])
#     tuple_a = (x, y)
#     return tuple_a

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    x = int(tuple_a[0]) + int(tuple_b[0])
    y = int(tuple_a[1]) + int(tuple_b[1])
    result_tuple = (x, y)
    return result_tuple

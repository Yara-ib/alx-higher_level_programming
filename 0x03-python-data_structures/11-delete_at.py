#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 or idx <= len(my_list - 1):
        new_list = my_list[:idx] + my_list[idx + 1:]
        my_list[:] = new_list
        return new_list
    else:
        return my_list
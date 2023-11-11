#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = dict.copy(a_dictionary)
    for i in new:
        if value == new[i]:
            del a_dictionary[i]
    return a_dictionary

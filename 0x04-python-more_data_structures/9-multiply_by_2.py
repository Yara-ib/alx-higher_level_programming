#!/usr/bin/python3
def multiply_by_2(a_dictionary):
# Write a function that returns a new dictionary with all values multiplied by 2
    return map(lambda item: item * 2, a_dictionary.values())

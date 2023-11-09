#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = sorted(a_dictionary.values())[-1]
        return list(a_dictionary.keys())[list(a_dictionary.values()).index(x)]

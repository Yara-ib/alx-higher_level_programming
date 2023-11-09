#!/usr/bin/python3
def Roman_numerals(roman_string):
    result = 0
    for n in roman_string:
        if n == "I":
            result += 1
        elif n == "V":
            result += 5
        elif n == "X":
            result += 10
        elif n == "L":
            result += 50
        elif n == "C":
            result += 100
        elif n == "D":
            result += 500
        elif n == "M":
            result += 1000
    return result


def roman_to_int(roman_string):
    if roman_string.isalpha() and roman_string:
        return Roman_numerals(roman_string)
    else:
        return 0

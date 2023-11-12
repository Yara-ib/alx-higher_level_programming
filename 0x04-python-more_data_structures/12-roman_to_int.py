#!/usr/bin/python3
def Roman_numerals(roman_string):
    if roman_string == "I":
        return 1
    elif roman_string == "V":
        return 5
    elif roman_string == "X":
        return 10
    elif roman_string == "L":
        return 50
    elif roman_string == "C":
        return 100
    elif roman_string == "D":
        return 500
    elif roman_string == "M":
        return 1000

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    result, previous = 0, 0
    for latin_n in reversed(roman_string):
        if previous > Roman_numerals(latin_n):
            result -= Roman_numerals(latin_n)
        else:
            result += Roman_numerals(latin_n)
        previous = Roman_numerals(latin_n)
    return result

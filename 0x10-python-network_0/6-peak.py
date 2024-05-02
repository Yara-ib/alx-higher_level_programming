#!/usr/bin/python3
""" Module"""


def find_peak(list_of_integers):
    """method"""
    for num in list_of_integers:
        if num == max(list_of_integers):
            return num

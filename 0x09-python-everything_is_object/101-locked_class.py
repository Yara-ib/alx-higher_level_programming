#!/usr/bin/python3
""" Low memory cost Module."""


class LockedClass:
    """ Prevents user from dynamically creating new instances. """
    __slots__ = ["first_name"]

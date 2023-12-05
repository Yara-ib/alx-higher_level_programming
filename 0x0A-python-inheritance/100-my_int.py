#!/usr/bin/python3
""" My integer Module. """


class MyInt(int):
    """ Class MyInt that inherits from int but it's a rebel! """
    def __eq__(self, other):
        """ To handle == between instances."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ To handle != between instances."""
        return int.__eq__(self, other)

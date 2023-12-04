#!/usr/bin/python3
""" My integer Module. """


class MyInt(int):
    """ Class MyInt that inherits from int. """
    def __init__(self, res):
        """ Constructor to initialize the instance. """
        super().__init__(res)
        self.__res = res
    def __eq__(self, other):
        """ To handle == between instances."""
        return self.res != other.res
    def __ne__(self, other):
        """ To handle != between instances."""
        return self.res == other.res

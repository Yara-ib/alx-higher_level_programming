#!/usr/bin/python3
""" Student to JSON with filter Module. """


class Student:
    """ class Student that defines a student.

    Attributes:
        first_name: student's first name
        last_name: student's last name
        age: student's age
    """
    def __init__(self, first_name, last_name, age):
        """ Instantiation new instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student."""
        self.__attrs = attrs

        if self.__attrs is None:
            return self.__dict__

        else:
            attr_val = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attr_val[attr] = getattr(self, attr)
            return attr_val

#!/usr/bin/python3
""" Student to disk and reload Module. """


Student = __import__('10-student').Student


def reload_from_json(self, json):
    """" replaces all attributes of the Student instance."""
    for key, value in self:
        self.update(key, value)

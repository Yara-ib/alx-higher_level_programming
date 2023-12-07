#!/usr/bin/python3
Student = __import__('10-student').Student

def reload_from_json(self, json):
    for key, value in self:
        self.update(key, value)

#!/usr/bin/python3
def add_attribute(self, name, value):
    if not setattr(self, name, value):
        raise TypeError("can't add new attribute")
    else:
        setattr(self, name, value)

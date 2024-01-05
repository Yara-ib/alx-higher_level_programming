#!/usr/bin/python3
""" Square Class Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Derived class from Rectangle and from Base """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initiation of objects

        Args:
            width, height, x, y, id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the Square instance representation as string """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update values for Rectangle arguments passed on if there's any

        Args:
            *args: tuple of arguments with undefined length
            **kwargs: dictionary of keyword arguments if there's any

        Return:
            updated dictionary for the attributes
        """
        if args and len(args) > 0:
            arg_list = ["id", "size", "x", "y"]
            for idx, arg in enumerate(args):
                setattr(self, arg_list[idx], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the Square instance """
        Sq_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return Sq_dict

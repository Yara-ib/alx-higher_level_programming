#!/usr/bin/python3
""" Rectangle Class Module """
from models.base import Base


class Rectangle(Base):
    """ Derived class from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initiation of objects

        Args:
            width, height, x, y, id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width of the rectangle """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height of the rectangle """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x position value """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x position value """
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y position value """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y position value """
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returning area of Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Returns the Rectangle instance representation as string """
        txt = f"[Rectangle] ({self.id})"
        return f"{txt} {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Update values for Rectangle arguments passed on if there's any

        Args:
            *args: tuple of arguments with undefined length
            **kwargs: dictionary of keyword arguments if there's any

        Return:
            updated dictionary for the attributes
        """
        if args and len(args) > 0:
            arg_list = ["id", "width", "height", "x", "y"]
            for idx, arg in enumerate(args):
                setattr(self, arg_list[idx], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the Rectangle instance """
        R_dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return R_dict

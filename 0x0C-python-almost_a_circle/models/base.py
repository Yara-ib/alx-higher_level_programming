#!/usr/bin/python3
""" Base class Module. """
import json


class Base:
    """
    The Base class

    Attributes:
        __nb_objects: number of instance objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initiation of objects """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method to encode string to JSON

        Args:
            list_dictionaries

        Return:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts JSON string to dictionary

        Args:
            json_string: string representing a list of dictionaries

        Return:
            list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: list of instances who inherits of Base

        Return:
            list of Rectangle or list of Square instances or empty
        """
        with open(cls.__name__ + ".json", "w") as file:
            dict_list = []
            if list_objs is not None:
                for obj in list_objs:
                    dict_list.append(cls.to_dictionary(obj))
            file.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """
        Converts dictionary to instance

        Args:
            **dictionary: replacement for **kwargs

        Return:
            instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            n_default = cls(1, 1)
        if cls.__name__ == "Square":
            n_default = cls(1)
        n_default.update(**dictionary)
        return n_default

    @classmethod
    def load_from_file(cls):
        """
        Converts file to instances

        Args:
            None

        Return:
            list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                sum_all = []
                list_dict = cls.from_json_string(file.read())
                for n in list_dict:
                    sum_all.append(cls.create(**n))
                return sum_all
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        Converts CSV file to instances

        Args:
            None

        Return:
            list of instances
        """
        with open(cls.__name__ + ".csv", "r") as file:
            sum_all = []
            list_dict = cls.from_json_string(file.read())
            for n in list_dict:
                sum_all.append(cls.create(**n))
            return sum_all

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Writes the CSV's representation of list_objs to a file

        Args:
            list_objs: list of instances who inherits of Base

        Return:
            list of Rectangle or list of Square instances or empty
        """
        with open(cls.__name__ + ".csv", "w") as file:
            dict_list = []
            if list_objs is not None:
                for obj in list_objs:
                    dict_list.append(cls.to_dictionary(obj))
            file.write(cls.to_json_string(dict_list))

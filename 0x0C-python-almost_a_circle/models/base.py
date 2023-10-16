#!/usr/bin/python3

"""
This module contains a base class that will be used
throughout the project
"""

import json
import os


class Base():
    """Base class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method definition"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dict to json string"""
        if list_dictionaries and len(list_dictionaries) > 0 and\
                len(list_dictionaries[0]) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """loads object from json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a json string to a file"""
        if list_objs is None or list_objs == []:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """creates a class from a dict of arguments"""
        dummy_inst = cls(1, 1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """loads list of instance from file"""
        filename = "{}.json".format(cls.__name__)
        list_obj = []
        if not os.path.isfile(filename):
            return list_obj
        with open(filename) as f:
            content = f.read()
        all_dicts = cls.from_json_string(content)
        list_obj = [cls.create(**elem) for elem in all_dicts]
        return list_obj

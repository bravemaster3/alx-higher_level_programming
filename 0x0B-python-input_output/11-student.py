#!/usr/bin/python3

"""
This module contains the definition of class Student
With a method to_json
"""


class Student:
    """class definition
    Methods:
        __init__
        to_json
    """

    def __init__(self, first_name, last_name, age):
        """method that runs at instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json serializable dict representation of self"""
        flag = 0
        all = vars(self)
        if type(attrs) is not list:
            flag = 1
        else:
            for el in attrs:
                if type(el) is not str:
                    flag = 1

        if flag == 1:
            return all
        else:
            return dict((key, all[key]) for key in attrs if key in all)

    def reload_from_json(self, json):
        """replaces all self's dict by json"""
        self.__dict__.clear()
        for key, value in json.items():
            setattr(self, key, value)

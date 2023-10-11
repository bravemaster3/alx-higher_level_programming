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

    def to_json(self):
        """returns a json serializable dict representation of self"""
        return vars(self)

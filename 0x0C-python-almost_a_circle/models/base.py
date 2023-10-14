#!/usr/bin/python3

"""
This module contains a base class that will be used
throughout the project
"""


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

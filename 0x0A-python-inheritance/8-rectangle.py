#!/usr/bin/python3
"""
definition of class BaseGeometry
and also Rectangle...
"""


class BaseGeometry():
    """class definition starts here"""
    pass

    def area(self):
        """area undefined, raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """instanciation statements here"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

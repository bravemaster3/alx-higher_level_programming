#!/usr/bin/python3
"""
definition of class BaseGeometry
"""


class BaseGeometry():
    """class definition starts here"""
    pass

    def area(self):
        """area undefined, raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer"""
        if type(name) is not str:
            raise Exception
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

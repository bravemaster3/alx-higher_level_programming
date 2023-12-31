#!/usr/bin/python3
"""
definition of class BaseGeometry
and also Rectangle...
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """instanciation statements here"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area calculator"""
        return self.__width * self.__height

    def __str__(self):
        """returns a representation of the rectangle object"""
        rect = "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
        return rect

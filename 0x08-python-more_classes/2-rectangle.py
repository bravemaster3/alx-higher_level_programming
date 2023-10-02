#!/usr/bin/python3

"""
Module containing Class that defines a rectangle
"""


class Rectangle:
    """definition of the class rectangle"""

    def __init__(self, width=0, height=0):
        """ function run during instanciation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """getter of height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns the area of a rectangle instance"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of a rectangle instance"""
        return (2 * (self.__height + self.__width))

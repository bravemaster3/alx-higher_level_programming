#!/usr/bin/python3
"""
definition of class BaseGeometry
and also Rectangle...
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class rectangle based on BaseGeometry"""

    def __init__(self, size):
        """instanciation statements here"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns a representation of the rectangle object"""
        rect = "[{}] {}/{}".format("Rectangle",
                                   self.__width, self.__height)
        return rect

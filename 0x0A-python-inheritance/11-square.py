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
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

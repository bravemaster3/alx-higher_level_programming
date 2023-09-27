#!/usr/bin/python3
"""MagicClass defines a circle

calculates the area and circumference

"""
import math


class MagicClass:
    """MagicClass defines a circle

    calculates the area and circumference

    """

    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius

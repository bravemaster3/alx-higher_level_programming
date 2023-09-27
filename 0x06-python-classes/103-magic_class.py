#!/usr/bin/python3
"""MagicClass defines a circle

calculates the area and circumference

"""
import math


class MagicClass:
    """MagicClass defines a circle

    calculates the area and circumference

    """
    __radius = 0
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius
            return

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius

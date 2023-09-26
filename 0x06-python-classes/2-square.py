#!/usr/bin/python3
"""Class that defines a square

This is a first class, and
it has a method __init__ for setting its size

"""


class Square:
    """This class creates a square

    Initializes a given instance with a provided size

    """

    def __init__(self, size=0):
        """This is an initializer

        Args:
            __size: private argument, the size of a square
            size is checked first, and error raised if necessary

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

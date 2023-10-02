#!/usr/bin/python3
"""
Printing a square with #
When the size is 0, it only prints an empty line
"""


def print_square(size):
    """Actual content of the function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size, end="")
        print()

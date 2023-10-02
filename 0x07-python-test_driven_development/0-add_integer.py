#!/usr/bin/python3
"""
This module contains a function for summing Two integers or floats
"""


def add_integer(a, b=98):
    """
    Sums up two integers or floats
    Args:
        a: first integer
        b: second integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

#!/usr/bin/python3
"""
Function for checking subclass
"""


def inherits_from(obj, a_class):
    """function definition here"""
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class

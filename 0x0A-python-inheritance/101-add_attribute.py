#!/usr/bin/python3
"""
A function that adds a new attribute
"""


def add_attribute(obj, name, value):
    """function defintion here"""
    if hasattr(obj, "__dict__"):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")

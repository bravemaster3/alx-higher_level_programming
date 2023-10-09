#!/usr/bin/python3
"""
This module contains a lookup function
for listing all methods of an object
"""


def lookup(obj):
    """Returns all methods of an object"""
    return dir(obj)

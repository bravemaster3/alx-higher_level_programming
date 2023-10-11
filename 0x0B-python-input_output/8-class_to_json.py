#!/usr/bin/python3

"""
This module converts all elements of
the class to serializable dic
"""


def class_to_json(obj):
    """function definition here"""
    all_items = vars(obj)
    return (all_items)

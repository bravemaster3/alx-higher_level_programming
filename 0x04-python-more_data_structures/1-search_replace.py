#!/usr/bin/python3

"""
Function that replaces a value by another in a list
"""


def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)

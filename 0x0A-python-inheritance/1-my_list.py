#!/usr/bin/python3
"""
Module containing class MyList that inherits from list
"""


class MyList(list):
    """MyList class definition"""

    def print_sorted(self):
        """function that prints the sorted list"""
        print(sorted(i for i in self))

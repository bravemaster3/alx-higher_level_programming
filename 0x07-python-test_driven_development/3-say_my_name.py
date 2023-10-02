#!/usr/bin/python3

"""say my name function
This module contains a function
That composes your name from first and last names
"""


def say_my_name(first_name, last_name=""):
    """Takes first name and last name, and prints full name"""
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3

"""
This module contains a function
that writes an Object to a text file,
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """function definition"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))

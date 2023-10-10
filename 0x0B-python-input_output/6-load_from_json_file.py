#!/usr/bin/python3

"""
This module contains
a function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """function definition"""
    with open(filename) as f:
        return json.load(f)

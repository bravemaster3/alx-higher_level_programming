#!/usr/bin/python3
"""
This module contains a function for converting
a JSON string into a python object
"""

import json


def from_json_string(my_str):
    """function definition here"""
    return json.loads(my_str)

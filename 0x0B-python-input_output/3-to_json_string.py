#!/usr/bin/python3
"""
This Module contains a function that
returns the JSON representation of a string
"""


def to_json_string(my_obj):
    import json
    """function definition"""
    return json.dumps(my_obj)

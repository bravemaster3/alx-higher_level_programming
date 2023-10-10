#!/usr/bin/python3
"""
Module contains a function for reading a file
Args:
    filename: string
"""


def read_file(filename=""):
    """function definition"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

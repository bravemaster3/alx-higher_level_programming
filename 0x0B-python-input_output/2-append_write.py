#!/usr/bin/python3
"""
Module containing append_write function
writes if the file doesn't exist,
appends to it if it exists
"""


def append_write(filename="", text=""):
    """definition of the append_write function"""
    with open(filename, "a", encoding="utf-8") as f:
        nchar = f.write(text)
    return nchar

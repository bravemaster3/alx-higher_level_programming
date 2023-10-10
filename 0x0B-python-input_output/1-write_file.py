#!/usr/bin/python3
"""
module containing a function
that writes a file,
overwrite if exits
returns the number of bytes written
"""


def write_file(filename="", text=""):
    """writes a file"""
    with open(filename, "w") as f:
        nchar = f.write(text)
    return nchar

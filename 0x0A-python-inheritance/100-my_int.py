#!/usr/bin/python3
"""
Rebel class MyInt from Int
"""


class MyInt(int):
    """class definition here"""

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return super().__eq__(other)

#!/usr/bin/python3
"""
Locked class except for first_name attribute
"""


class LockedClass:
    """class definition here"""

    def __init__(self, first_name=None):
        "nothing during instanciation"
        if (first_name):
            self.first_name = first_name

    def __setattr__(self, name, value):
        """setting attribute"""
        if name != "first_name":
            raise AttributeError("'{}' object has no attribute '{}'"
                                 .format(self.__class__.__name__, name))
        super().__setattr__(name, value)

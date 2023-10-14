#!/usr/bin/python3

"""
This module contains a definition of
Class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation using the super call"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """default printing of a square object"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter for size"""
        return (self.width)

    @size.setter
    def size(self, size):
        """setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updates a square with no-keyword arguments"""
        if (args != ()):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs.get('id') is not None:
                super(Square.__bases__[0], self).__init__(kwargs.get('id'))
            if kwargs.get('size') is not None:
                self.size = kwargs.get('size')
            if kwargs.get('x') is not None:
                self.x = kwargs.get('x')
            if kwargs.get('y') is not None:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """returns a dictionary of a Square
        with id, size, x, y"""
        sq_dict = self.__dict__.copy()
        sq_dict["size"] = sq_dict.pop("_Rectangle__width")
        sq_dict.pop("_Rectangle__height")
        sq_dict["x"] = sq_dict.pop("_Rectangle__x")
        sq_dict["y"] = sq_dict.pop("_Rectangle__y")
        return sq_dict

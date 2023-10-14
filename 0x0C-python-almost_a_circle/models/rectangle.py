#!/usr/bin/python3

"""
This module contains a definition of
Class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Definition of class Rectangle"""

    def __integer_validator(self, name, value, zeroable=False):
        """a validator for all integers"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and zeroable is False:
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and zeroable is True:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method for width"""
        self.__integer_validator("width", width, zeroable=False)
        self.__width = width

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for height"""
        self.__integer_validator("height", height, zeroable=False)
        self.__height = height

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x"""
        self.__integer_validator("x", x, zeroable=True)
        self.__x = x

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        self.__integer_validator("y", y, zeroable=True)
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method of class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """displays rectangle with #"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print()

    def __str__(self):
        """default printing of a rectangle object"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """updates a rectangle with no-keyword arguments"""
        if (args != ()):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if kwargs.get('id') is not None:
                super().__init__(kwargs.get('id'))
            if kwargs.get('width') is not None:
                self.width = kwargs.get('width')
            if kwargs.get('height') is not None:
                self.height = kwargs.get('height')
            if kwargs.get('x') is not None:
                self.x = kwargs.get('x')
            if kwargs.get('y') is not None:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """returns a dictionary of a rectangle
        with id, width, height, x, y"""
        rect_dict = self.__dict__.copy()
        rect_dict["width"] = rect_dict.pop("_Rectangle__width")
        rect_dict["height"] = rect_dict.pop("_Rectangle__height")
        rect_dict["x"] = rect_dict.pop("_Rectangle__x")
        rect_dict["y"] = rect_dict.pop("_Rectangle__y")
        return rect_dict

#!/usr/bin/python3

"""
Module containing Class that defines a rectangle
"""


class Rectangle:
    """definition of the class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ function run during instanciation"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """getter of width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """setter for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """getter of height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns the area of a rectangle instance"""
        return (self.height * self.width)

    def perimeter(self):
        """returns the perimeter of a rectangle instance"""
        return (2 * (self.height + self.width))

    def __str__(self):
        """string representation"""
        str_ret = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                str_ret += str(self.print_symbol) * self.width
                if i < self.height - 1:
                    str_ret += "\n"
        return str_ret

    def __repr__(self):
        """returns the object representation of the instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """destructor instructions"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method for gettingthe biggest of 2 rectangles"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        my_sq = cls(size, size)
        return my_sq

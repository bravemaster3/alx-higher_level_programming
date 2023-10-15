#!/usr/bin/python3

"""
Testing the class Square
that inherited from the Rectangle class
"""

from models.square import Square
from models.base import Base
import unittest
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """Testing the Square class"""

    def stdout_capturer(self, method_to_run, *args, **kwargs):
        """method for capturing stdout"""
        captured_output = StringIO()
        sys.stdout = captured_output
        method_to_run(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    def test_unknown_attributes(self):
        """Check what happens when you provide with..."""
        with self.assertRaises(TypeError) as err:
            obj1 = Square(width=4, height=6)
        self.assertEqual(str(err.exception),
                         "__init__() got an unexpected"
                         " keyword argument 'width'")

    def test_type_and_value_error(self):
        """Check what happens when you different types"""
        with self.assertRaises(TypeError) as err:
            obj1 = Square([5], id=87)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            obj1 = Square(5, None, id=87)
        self.assertEqual(str(err.exception), "x must be an integer")

        with self.assertRaises(ValueError) as err:
            obj1 = Square(-5)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            obj1 = Square(5, -2)
        self.assertEqual(str(err.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as err:
            obj1 = Square(5, 1, -2)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_normal_square(self):
        """testing normal square"""
        obj1 = Square(5)
        self.assertEqual(obj1.width, 5)
        self.assertEqual(obj1.height, 5)
        self.assertEqual(obj1.x, 0)
        self.assertEqual(obj1.y, 0)

        obj1 = Square(4, 2, 1, 89)
        self.assertEqual(obj1.width, 4)
        self.assertEqual(obj1.height, 4)
        self.assertEqual(obj1.x, 2)
        self.assertEqual(obj1.y, 1)
        self.assertEqual(obj1.id, 89)

    def test_str_output(self):
        obj = Square(4, 2, 1, 89)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (89) 2/1 - 4
"""
        self.assertEqual(expected_output, stdout_value)

    def test_size_getter_setter(self):
        """testing getter and setter"""
        obj = Square(4, 2, 1, 89)
        self.assertEqual(obj.size, 4)
        obj.size = 24
        self.assertEqual(obj.size, 24)

    def test_size_getter_setter_err(self):
        """testing errors with wrong size type"""
        obj = Square(23)
        with self.assertRaises(TypeError) as err:
            obj.size = None
        self.assertEqual(str(err.exception), "width must be an integer")
        with self.assertRaises(ValueError) as err:
            obj.size = -5
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_update_with_args(self):
        """testing use of args"""
        obj = Square(6, x=2, y=2, id=3)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (3) 2/2 - 6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update()
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (3) 2/2 - 6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (89) 2/2 - 6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 2)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (89) 2/2 - 2
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 2, 3, 4)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (89) 3/4 - 2
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 2, 3, 4, 5)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (89) 3/4 - 2
"""
        self.assertEqual(expected_output, stdout_value)

    def test_update_with_kwargs(self):
        """testing use of args and kwargs together"""
        obj = Square(6, 2, 2, 3)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (3) 2/2 - 6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 10, id=87, you=67)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (89) 2/2 - 10
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(id=87, you=67)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (87) 2/2 - 10
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(x=4, y=3, id=82, size=13)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Square] (82) 4/3 - 13
"""
        self.assertEqual(expected_output, stdout_value)

        with self.assertRaises(ValueError) as err:
            obj.update(89, 0, id=87, you=67)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(TypeError) as err:
            obj.update(88, None, 0, id=87, you=67)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            obj.update(id=88, x={})
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_rect_dict(self):
        """testing the to_dictionary method"""
        obj = Square(10, 1, 9, 87)
        obj_dict = obj.to_dictionary()
        self.assertEqual(10, obj_dict.get("size"))
        self.assertEqual(1, obj_dict.get("x"))
        self.assertEqual(9, obj_dict.get("y"))
        self.assertEqual(87, obj_dict.get("id"))
        self.assertIsNone(obj_dict.get("_Rectangle__width"))
        self.assertIsNone(obj_dict.get("_Rectangle__height"))
        self.assertIsNone(obj_dict.get("_Rectangle__x"))
        self.assertIsNone(obj_dict.get("_Rectangle__y"))

    def test_save_to_file(self):
        """testing saving to file"""
        r1 = Square(10)
        r2 = Square(2, 4)
        list_objs = [r1, r2]
        Square.save_to_file(list_objs)
        if list_objs is None or list_objs == []:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open("Square.json", "r") as file:
            saved_read = file.read()
        self.assertEqual(Base.to_json_string(list_dict), saved_read)

        list_objs = []
        Square.save_to_file(list_objs)
        if list_objs is None or list_objs == []:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open("Square.json", "r") as file:
            saved_read = file.read()
        self.assertEqual(Base.to_json_string(list_dict), saved_read)

        list_objs = None
        Square.save_to_file(list_objs)
        if list_objs is None or list_objs == []:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        with open("Square.json", "r") as file:
            saved_read = file.read()
        self.assertEqual(Base.to_json_string(list_dict), saved_read)

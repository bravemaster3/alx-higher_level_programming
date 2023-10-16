#!/usr/bin/python3

"""
Testing the class Rectangle
that inherited from the base class
"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """Testing the Rectangle class"""

    def stdout_capturer(self, method_to_run, *args, **kwargs):
        """method for capturing stdout"""
        captured_output = StringIO()
        sys.stdout = captured_output
        method_to_run(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    def test_idnone(self):
        """test for id = None
        obj1 = Rectangle(width=4, height=6)
        self.assertEqual(obj1.id, 4)
        obj2 = Base()
        self.assertEqual(obj2.id, 4)
        obj2_2 = Rectangle(width=4, height=6, x=1, y=2)
        self.assertEqual(obj2_2.id, 3)
        """
        obj1 = Rectangle(width=4, height=6)
        self.assertEqual(obj1.width, 4)
        self.assertEqual(obj1.height, 6)
        self.assertEqual(obj1.x, 0)
        self.assertEqual(obj1.y, 0)

    def test_customId(self):
        """test for id = a certain value
        obj3 = Rectangle(width=5, height=10, id=5)
        self.assertEqual(obj3.id, 5)
        """
        obj2 = Rectangle(width=4, height=5, x=4, y=10, id=5)
        self.assertEqual(obj2.width, 4)
        self.assertEqual(obj2.height, 5)
        self.assertEqual(obj2.x, 4)
        self.assertEqual(obj2.y, 10)
        self.assertEqual(obj2.id, 5)

    def test_missing_arguments(self):
        """Testing missing required positional argument"""
        with self.assertRaises(TypeError):
            obj3 = Rectangle(height=5)
        with self.assertRaises(TypeError):
            obj4 = Rectangle(width=5)
        with self.assertRaises(TypeError):
            obj5 = Rectangle()
        obj5 = Rectangle(width=5, height=4)
        self.assertEqual(obj5.x, 0)
        self.assertEqual(obj5.y, 0)

        with self.assertRaises(TypeError) as err:
            obj5 = Rectangle(width=-5)
        self.assertEqual(str(err.exception),
                         "__init__() missing 1 required positional"
                         " argument: 'height'")

    def test_getting_privateAttr(self):
        """Testing retrieval of private argument"""
        obj6 = Rectangle(width=5, height=4)
        with self.assertRaises(AttributeError):
            obj6.__width
        self.assertEqual(obj6._Rectangle__width, 5)

    def test_TypeError(self):
        """testing integer type"""
        with self.assertRaises(TypeError) as err:
            obj7 = Rectangle(width=float('inf'), height=4.1)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            obj7 = Rectangle(width=5.3, height=4.1)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            obj7 = Rectangle(width=None, height=4)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            obj7 = Rectangle(width=[2], height=4)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            obj7 = Rectangle(width=5, height=4.1)
        self.assertEqual(str(err.exception), "height must be an integer")

        with self.assertRaises(TypeError) as err:
            obj7 = Rectangle(width=5, height=4, x=1.4)
        self.assertEqual(str(err.exception), "x must be an integer")

        with self.assertRaises(TypeError) as err:
            obj7 = Rectangle(width=5, height=4, x=1, y=2.5)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_ValueError(self):
        """testing errors when value is <= 0"""
        with self.assertRaises(ValueError) as err:
            obj8 = Rectangle(width=-5, height=5)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            obj8 = Rectangle(width=0, height=5)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            obj8 = Rectangle(width=5, height=-4)
        self.assertEqual(str(err.exception), "height must be > 0")

        with self.assertRaises(ValueError) as err:
            obj8 = Rectangle(width=5, height=0)
        self.assertEqual(str(err.exception), "height must be > 0")

        with self.assertRaises(ValueError) as err:
            obj8 = Rectangle(width=5, height=2, x=-1)
        self.assertEqual(str(err.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as err:
            obj8 = Rectangle(width=5, height=2, y=-1)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_area(self):
        """testing area calculation"""
        obj9 = Rectangle(width=6, height=8)
        self.assertEqual(obj9.area(), 48)

    def test_display(self):
        """testing printing rectangle with #"""
        obj = Rectangle(width=4, height=6)
        stdout_value = self.stdout_capturer(obj.display)
        expected_output = """####
####
####
####
####
####
"""
        self.assertEqual(expected_output, stdout_value)

        obj = Rectangle(width=1, height=1)
        stdout_value = self.stdout_capturer(obj.display)
        expected_output = """#
"""
        self.assertEqual(expected_output, stdout_value)

    def test_print(self):
        """testing printing rectangle with #"""
        obj = Rectangle(width=4, height=6, x=2, y=1, id=12)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (12) 2/1 - 4/6
"""
        self.assertEqual(expected_output, stdout_value)

        obj = Rectangle(5, 5, 1, id=3)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (3) 1/0 - 5/5
"""
        self.assertEqual(expected_output, stdout_value)

    def test_display_with_coord(self):
        """testing printing rectangle with #"""
        obj = Rectangle(width=4, height=6, x=2, y=2)
        stdout_value = self.stdout_capturer(obj.display)
        expected_output = """

  ####
  ####
  ####
  ####
  ####
  ####
"""
        self.assertEqual(expected_output, stdout_value)

    def test_update_with_args(self):
        """testing use of args"""
        obj = Rectangle(width=4, height=6, x=2, y=2, id=3)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (3) 2/2 - 4/6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update()
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (3) 2/2 - 4/6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (89) 2/2 - 4/6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 2)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (89) 2/2 - 2/6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 2, 3)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (89) 2/2 - 2/3
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 2, 3, 4)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (89) 4/2 - 2/3
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 2, 3, 4, 5)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (89) 4/5 - 2/3
"""
        self.assertEqual(expected_output, stdout_value)

    def test_update_with_kwargs(self):
        """testing use of args and kwargs together"""
        obj = Rectangle(4, 6, 2, 2, 3)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (3) 2/2 - 4/6
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(89, 10, 11, id=87, you=67)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (89) 2/2 - 10/11
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(id=87, you=67)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (87) 2/2 - 10/11
"""
        self.assertEqual(expected_output, stdout_value)

        obj.update(x=4, y=3, id=82, width=13, height=23)
        stdout_value = self.stdout_capturer(print, obj)
        expected_output = """[Rectangle] (82) 4/3 - 13/23
"""
        self.assertEqual(expected_output, stdout_value)

        with self.assertRaises(ValueError) as err:
            obj.update(89, 0, id=87, you=67)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            obj.update(89, 5, 0, id=87, you=67)
        self.assertEqual(str(err.exception), "height must be > 0")

        with self.assertRaises(TypeError) as err:
            obj.update(88, None, 0, id=87, you=67)
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(TypeError) as err:
            obj.update(id=88, x={})
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_rect_dict(self):
        """testing the to_dictionary method"""
        obj = Rectangle(10, 2, 1, 9, 87)
        obj_dict = obj.to_dictionary()
        self.assertEqual(10, obj_dict.get("width"))
        self.assertEqual(2, obj_dict.get("height"))
        self.assertEqual(1, obj_dict.get("x"))
        self.assertEqual(9, obj_dict.get("y"))
        self.assertEqual(87, obj_dict.get("id"))
        self.assertIsNone(obj_dict.get("_Rectangle__width"))
        self.assertIsNone(obj_dict.get("_Rectangle__height"))
        self.assertIsNone(obj_dict.get("_Rectangle__x"))
        self.assertIsNone(obj_dict.get("_Rectangle__y"))

    def test_save_to_file(self):
        """testing saving to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_objs = [r1, r2]
        Rectangle.save_to_file(list_objs)
        list_dict = [obj.to_dictionary() for obj in list_objs]
        with open("Rectangle.json", "r") as file:
            saved_read = file.read()
        self.assertEqual(Base.to_json_string(list_dict), saved_read)

        list_objs = []
        Rectangle.save_to_file(list_objs)
        list_dict = []
        with open("Rectangle.json", "r") as file:
            saved_read = file.read()
        self.assertEqual(Base.to_json_string(list_dict), saved_read)

        list_objs = None
        Rectangle.save_to_file(list_objs)
        list_dict = []
        with open("Rectangle.json", "r") as file:
            saved_read = file.read()
        self.assertEqual(Base.to_json_string(list_dict), saved_read)

    def test_from_json_string(self):
        """testing loading json string to oject"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), type(list_output))
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(list_input, list_output)

        list_input = None
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(json_list_input), str)
        self.assertIsNone(list_input)
        self.assertEqual(list_output, [])

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        """tests the creation of objs from dicts"""
        r1 = Rectangle(5, 5, 3)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        my_dict = {'id': 13, 'size': 5, 'x': 5, 'y': 3}
        r2 = Rectangle.create(**my_dict)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        """Not providing returns the dummy created instance"""
        my_dict = {'id': 16}
        r3 = Rectangle.create(**my_dict)
        stdout_value = self.stdout_capturer(print, r3)
        expected_output = """[Rectangle] (16) 0/0 - 1/1
"""
        self.assertEqual(expected_output, stdout_value)

    def test_load_from_file(self):
        """testing loading from file"""
        r1 = Rectangle(10, 7, 2, 8, id="26")
        r2 = Rectangle(2, 4, id="27")
        list_rect_in = [r1, r2]
        Rectangle.save_to_file(list_rect_in)
        list_rect_out = Rectangle.load_from_file()

        stdout_value = self.stdout_capturer(print, list_rect_out[0])
        expected_output = """[Rectangle] (26) 2/8 - 10/7
"""
        self.assertEqual(expected_output, stdout_value)

        stdout_value = self.stdout_capturer(print, list_rect_out[1])
        expected_output = """[Rectangle] (27) 0/0 - 2/4
"""
        self.assertEqual(expected_output, stdout_value)

        Rectangle.save_to_file([])
        list_rect_out = Rectangle.load_from_file()
        self.assertEqual(list_rect_out, [])

    def test_save_to_file_csv(self):
        """testing saving to file csv"""
        r1 = Rectangle(10, 7, 2, 8, id=77)
        r2 = Rectangle(2, 4, id=78)
        list_objs = [r1, r2]
        Rectangle.save_to_file_csv(list_objs)
        with open("Rectangle.csv", "r") as file:
            saved_read = file.readlines()
        self.assertEqual("77,10,7,2,8", saved_read[0].strip())
        self.assertEqual("78,2,4,0,0", saved_read[1].strip())

        list_objs = []
        Rectangle.save_to_file_csv(list_objs)
        list_dict = []
        with open("Rectangle.csv", "r") as file:
            saved_read = file.readlines()
        self.assertEqual("", saved_read[0].strip())

        Rectangle.save_to_file_csv(list_objs)
        list_dict = []
        with open("Rectangle.csv", "r") as file:
            saved_read = file.readlines()
        self.assertEqual("", saved_read[0].strip())

    def test_load_from_file_csv(self):
        """testing load from file"""
        r1 = Rectangle(10, 7, 2, 8, id=77)
        r2 = Rectangle(2, 4, id=78)
        list_objs = [r1, r2]
        Rectangle.save_to_file_csv(list_objs)
        list_rect_out = Rectangle.load_from_file_csv()

        stdout_value = self.stdout_capturer(print, list_rect_out[0])
        expected_output = """[Rectangle] (77) 2/8 - 10/7
"""
        self.assertEqual(expected_output, stdout_value)

        stdout_value = self.stdout_capturer(print, list_rect_out[1])
        expected_output = """[Rectangle] (78) 0/0 - 2/4
"""

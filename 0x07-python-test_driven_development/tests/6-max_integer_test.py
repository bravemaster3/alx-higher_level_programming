#!/usr/bin/python3

"""Unitest example in this module
It contains a class with several methods for testing our max_integer function
"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """The class itself here"""

    def test_empty(self):
        """testing empty list"""
        self.assertIsNone(max_integer([]))

    def test_correct(self):
        """check if the correct value is printed"""
        self.assertEqual(max_integer([12, 289, 0, 45]), 289)
        self.assertEqual(max_integer([-12, -289, -0, -45]), 0)

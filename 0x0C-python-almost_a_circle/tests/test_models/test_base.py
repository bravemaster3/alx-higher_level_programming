#!/usr/bin/python3

"""
Test cases of the base module
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """all tests are in here"""

    def test_idnone(self):
        """test for id = None"""
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def test_customId(self):
        """test for id = a certain value"""
        obj3 = Base(4)
        self.assertEqual(obj3.id, 4)

    def test_idnone_afterCustomId(self):
        """test for id = None after assigning a given id"""
        obj4 = Base()
        self.assertEqual(obj4.id, 3)

    def test_idnone_afterCustomIdSame(self):
        """test for id = None to be the same as previous assigned"""
        obj4 = Base(4)
        self.assertEqual(obj4.id, 4)

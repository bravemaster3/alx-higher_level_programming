#!/usr/bin/python3

"""
This module contains a base class that will be used
throughout the project
"""

import json
import os
import turtle


class Base():
    """Base class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method definition"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dict to json string"""
        if list_dictionaries and len(list_dictionaries) > 0 and\
                len(list_dictionaries[0]) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """loads object from json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a json string to a file"""
        if list_objs is None or list_objs == []:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """creates a class from a dict of arguments"""
        dummy_inst = cls(1, 1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """loads list of instance from file"""
        filename = "{}.json".format(cls.__name__)
        list_obj = []
        if not os.path.isfile(filename):
            return list_obj
        with open(filename) as f:
            content = f.read()
        all_dicts = cls.from_json_string(content)
        list_obj = [cls.create(**elem) for elem in all_dicts]
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of objects to a csv file"""
        if not list_objs or list_objs == []:
            serialized = "\n"
        else:
            serialized = ""
            for obj in list_objs:
                if hasattr(obj, "size"):
                    el = "{},{},{},{}".format(obj.id, obj.size, obj.x, obj.y)
                else:
                    el = "{},{},{},{},{}".format(obj.id, obj.width, obj.height,
                                                 obj.x, obj.y)
                serialized += el + "\n"
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(serialized)

    @classmethod
    def load_from_file_csv(cls):
        """loads objects from csv file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename) as f:
            all_lines = f.readlines()

        list_obj = []
        for line in all_lines:
            split_line = line.strip().split(',')
            spl = [int(x) for x in split_line]
            if hasattr(cls, "size"):
                list_obj.append(cls(spl[1], spl[2], spl[3], spl[0]))
            else:
                list_obj.append(cls(spl[1], spl[2], spl[3], spl[4], spl[0]))
        return list_obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rectangles and squares with the turtle graphics"""
        tur = turtle.Turtle()

        tur.penup()
        tur.goto(-400, 400)
        tur.pendown()

        tur.color("green", "grey80")
        offset_y = 0
        for rect in list_rectangles:
            if rect.y > 0:
                tur.penup()
                tur.right(180)
                tur.forward(rect.y + offset_y)
                tur.pendown()
                offset_y += rect.y
            if rect.x > 0:
                tur.penup()
                tur.left(90)
                tur.forward(rect.x)
                tur.pendown()
            tur.begin_fill()
            tur.forward(rect.width)
            tur.right(90)
            tur.forward(rect.height)
            tur.right(90)
            tur.forward(rect.width)
            tur.right(90)
            tur.forward(rect.height)
            offset_y += rect.height
            tur.end_fill()

            tur.penup()
            tur.left(90)
            tur.forward(rect.x)
            tur.right(90)
            tur.pendown()

        tur.penup()
        tur.right(180)
        tur.forward(rect.height)
        tur.left(90)
        tur.pendown()

        for sq in list_squares:
            if sq.y > 0:
                tur.penup()
                tur.right(180)
                tur.forward(sq.y + offset_y)
                tur.pendown()
                offset_y += sq.y
            if sq.x > 0:
                tur.penup()
                tur.left(90)
                tur.forward(sq.x)
                tur.pendown()
            tur.begin_fill()
            tur.forward(sq.size)
            tur.right(90)
            tur.forward(sq.size)
            tur.right(90)
            tur.forward(sq.size)
            tur.right(90)
            tur.forward(sq.size)
            offset_y += sq.size
            tur.end_fill()

            tur.penup()
            tur.left(90)
            tur.forward(sq.x)
            tur.right(90)
            tur.pendown()

        turtle.done()

#!/usr/bin/python
"""This module contains all tests for the Base class,
as well as all it's methods."""
from models.base import Base
import json
import unittest
from models.square import Square
from models.rectangle import Rectangle
from os import path


class test_base(unittest.TestCase):
    """Tests for base class"""
    def no_doc(item):
        """A decorator to add the no-doc docstring
        objects that don't need any other documentation"""
        t = "class" if inspect.isclass(item) else "function"
        item.__doc__ = "This {} intentionally has no documentation".format(t)

    def test_base(self):
        """Test base"""
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_wrong(self):
        """Test base, there is only one exception raised for None."""
        base = Base()
        self.assertEqual(base.id, 1)
        base2 = Base([1, 2, 3])
        self.assertEqual(base2.id, [1, 2, 3])
        base3 = Base("ate")
        self.assertEqual(base3.id, "ate")
        base4 = Base(None)
        self.assertEqual(base4.id, 2)
        base5 = Base(True)
        self.assertEqual(base5.id, True)

    def test_to_json_string(self):
        """Test function to_json_string that converts
        a dict or list of dicts to a string."""
        square = Square(1, 2, 3)
        self.assertEqual(Base.to_json_string(None), list())
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 2, 'width': 10, 'id': 1,
                                   'height': 7, 'y': 8})
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_dictionary(self):
        """Test if the output is correct: it returns the class properties."""
        r1 = Rectangle(10, 7, 0, 0)
        r1_dict = r1.to_dictionary()
        self.assertIs(type(r1_dict), dict)

    def test_to_json_string(self):
        """Test for conversion of Base subclasses to json representation.
        Assumes that subclasses have implemented `to_dictionary()` method.
        If Rectangle class is not available do not run this test.
        """
        self.assertEqual(Base.to_json_string(None), [])
        self.assertEqual(Base.to_json_string([]), [])
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {'x': 2, 'width': 10,
                                       'id': 1, 'height': 7,
                                       'y': 8})
            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 10, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                               '"y": 8}]'))

    def test_create_rectangle_original(self):
        """Test for function create that returns an instance of a class"""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        """Test if new values are assigned to the new instance."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        """Test if both class instances are the same."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        """Test if both class instances are the same."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        """"Test function create that returns an instance of a class."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        """Test if new values are assigned to the new instance."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        """Test if both class instances are the same."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """Test if values are the same between both dictionaries."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        """With a class"""
        r1 = Rectangle(2, 3)
        if not path.exists("Rectangle.json"):
            lists = Rectangle.load_from_file()
            self.assertEqual(lists, [])

    def test_load_from_existing_file(self):
        """Tests if function loads from existing file"""
        r1 = Rectangle(3, 4)
        r1_json = Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual([r1.to_dictionary()], json.load(f))

    def test_load_from_existing_file_(self):
        """Tests if function loads from existing file"""
        r1 = Square(3)
        r1_json = Square.save_to_file([r1])
        with open("Square.json", "r") as f:
            self.assertEqual([r1.to_dictionary()], json.load(f))

    def test_load_from_file_(self):
        """With a class"""
        r1 = Square(2)
        if not path.exists("Square.json"):
            lists = Square.load_from_file()
            self.assertEqual(lists, [])

    def test_save_to_file(self):
            """Tests if function saves into a file"""
            s1 = Square(3)
            s1_json = Square.save_to_file([s1])
            with open("Square.json", "r") as f:
                self.assertEqual([s1.to_dictionary()], json.load(f))

    def test_csv_save(self):
        """Test advanced task."""
        inst_1 = Rectangle(420, 69)
        inst_2 = Rectangle(23, 42)
        sq1 = Square(42)
        sq2 = Square(27)
        Rectangle.save_to_file_csv([inst_1])
        list_test = [inst_1, inst_2]
        Rectangle.save_to_file_csv(list_test)
        Square.save_to_file_csv([sq1, sq2])

    def test_fail_csv_save(self):
        inst_1 = Rectangle(420, 69)
        inst_2 = Rectangle(23, 42)
        sq1 = Square(42)
        sq2 = Square(27)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(inst_2)
            Rectangle.save_to_file_csv(True)
            Rectangle.save_to_file_csv(False)
            Rectangle.save_to_file_csv(["hello"])
            Rectangle.save_to_file_csv([inst_1, inst_2, "bye"])
            Rectangle.save_to_file_csv((inst_1, inst_2))
            Rectangle.save_to_file_csv("Hi")
            Rectangle.save_to_file_csv(8)
            Square.save_to_file_csv(sq2)
            Square.save_to_file_csv(False)
            Square.save_to_file_csv(True)
            Square.save_to_file_csv(["goodbye"])
            Square.save_to_file_csv([sq1, sq2, "i hate unittests"])

    def test_csv_load(self):
        Rectangle.load_from_file_csv()
        Square.load_from_file_csv()

    def test_fail_csv_load(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv(8)
            Square.load_from_file_csv(32)
            Rectangle.load_from_file_csv(True)
            Rectangle.load_from_file_csv(False)
            Square.load_from_file_csv(True)
            Square.load_from_file_csv(False)


if __name__ == '__main__':
    unittest.main()

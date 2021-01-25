#!/usr/bin/python3
"""Unit Tests for the Rectangle class attributes and methods."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """All tests pertaining the Rectangle class."""

    def test_inst_methods(self):
        """Test methods."""
        # Test instance.
        test_inst = Rectangle(2, 3, 0, 0, 1)
        # Test area of rectangle.
        self.assertEqual(test_inst.area(), 6)
        # Test str.
        self.assertEqual(test_inst.__str__(), '[Rectangle] (1) 0/0 - 2/3')
        # Test to_dictionary method.
        self.assertEqual(test_inst.to_dictionary(),
                         {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0})

    def test_negatives(self):
        """Test negative values."""
        with self.assertRaises(ValueError):
            # Negative width.
            fail_inst = Rectangle(-2, 3, 3, 0, 0)
        with self.assertRaises(ValueError):
            # Negative height.
            fail_inst = Rectangle(2, -3, 3, 0, 0)
        with self.assertRaises(ValueError):
            # Negative x
            fail_inst = Rectangle(2, 3, -1, 0, 0)
        with self.assertRaises(ValueError):
            # Negative y.
            fail_inst = Rectangle(-2, 3, 0, -2, 0)

    def test_str_values(self):
        """Test values as strings."""
        with self.assertRaises(TypeError):
            # Str as width
            fail_inst = Rectangle('testStr', 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            # Str as height
            fail_inst = Rectangle(3, '3', 0, 0, 1)
        with self.assertRaises(TypeError):
            # Str as x
            fail_inst = Rectangle(1, 3, '0', 0, 1)
        with self.assertRaises(TypeError):
            # Str as y
            fail_inst = Rectangle(2, 3, 0, '0', 1)

    def test_float_values(self):
        """Test values as floats."""
        with self.assertRaises(TypeError):
            # Float as width
            fail_inst = Rectangle(8.1, 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            # Float as height
            fail_inst = Rectangle(3, 2.4, 0, 0, 1)
        with self.assertRaises(TypeError):
            # Float as x
            fail_inst = Rectangle(1, 3, 6.3, 0, 1)
        with self.assertRaises(TypeError):
            # Float as y
            fail_inst = Rectangle(2, 3, 0, 4.2, 1)
        # Float('inf') as value
        with self.assertRaises(TypeError):
            # Float('inf') as width
            fail_inst = Rectangle(float('inf'), 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            # Float('inf') as height
            fail_inst = Rectangle(3, float('inf'), 0, 0, 1)
        with self.assertRaises(TypeError):
            # Float('inf') as x
            fail_inst = Rectangle(1, 3, float('inf'), 0, 1)
        with self.assertRaises(TypeError):
            # Float('inf') as y
            fail_inst = Rectangle(2, 3, 0, float('inf'), 1)
        # Float('NaN') as value
        with self.assertRaises(TypeError):
            # Float('NaN') as width
            fail_inst = Rectangle(float('NaN'), 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            # Float('NaN') as height
            fail_inst = Rectangle(3, float('NaN'), 0, 0, 1)
        with self.assertRaises(TypeError):
            # Float('NaN') as x
            fail_inst = Rectangle(1, 3, float('NaN'), 0, 1)
        with self.assertRaises(TypeError):
            # Float('NaN') as y
            fail_inst = Rectangle(2, 3, 0, float('NaN'), 1)

    def test_boolean_values(self):
        """Test values as floats."""
        with self.assertRaises(TypeError):
            # Boolean as width
            fail_inst = Rectangle(True, 3, 0, 0, 1)
            fail_inst = Rectangle(False, 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            # Boolean as height
            fail_inst = Rectangle(3, True, 0, 0, 1)
            fail_inst = Rectangle(3, False, 0, 0, 1)
        with self.assertRaises(TypeError):
            # Boolean as x
            fail_inst = Rectangle(1, 3, True, 0, 1)
            fail_inst = Rectangle(1, 3, False, 0, 1)
        with self.assertRaises(TypeError):
            # Boolean as y
            fail_inst = Rectangle(2, 3, 0, True, 1)
            fail_inst = Rectangle(2, 3, 0, False, 1)

    def test_None_values(self):
        """Test None values."""
        with self.assertRaises(TypeError):
            # on width
            fail_inst = Rectangle(None, 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            # on height
            fail_inst = Rectangle(2, None, 0, 0, 1)
        with self.assertRaises(TypeError):
            # on x
            fail_inst = Rectangle(2, 3, None, 0, 1)
        with self.assertRaises(TypeError):
            # on y
            fail_inst = Rectangle(2, 5, 0, None, 1)

    def test_zero_values(self):
        """Test passing 0."""
        with self.assertRaises(ValueError):
            # on width
            fail_inst = Rectangle(0, 3, 0, 0, 1)
        with self.assertRaises(ValueError):
            # on height
            fail_inst = Rectangle(2, 0, 0, 0, 1)

    def test_arg_number(self):
        """Test less that 3 args and more than 5 args."""
        with self.assertRaises(TypeError):
            inst = Rectangle(3, 3, 0, 0, 1, 5)
        with self.assertRaises(TypeError):
            inst = Rectangle(1)

    def test_update(self):
        """Test update method."""
        # Test valid args
        inst_update = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0})
        inst_update.update(13, 3, 2 , 0, 0)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 13, 'width': 3, 'height': 2, 'x': 0, 'y': 0})
        # Test valid kwargs
        inst_update = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0})
        inst_update.update(id=13, width=3, height=2 , x=0, y=0)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 13, 'width': 3, 'height': 2, 'x': 0, 'y': 0})
        # Test valid args and kwargs
        inst_update = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0})
        inst_update.update(13, 1, 1, width=3, height=2)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 13, 'width': 1, 'height': 1, 'x': 0, 'y': 0})

    def test_update_failure(self):
        """Test failures of update method."""
        inst_up = Rectangle(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            # More than five args
            inst_up.update(1, 2, 3, 3, 1, 2)
        with self.assertRaises(TypeError):
            # Wrong data type as args
            inst_up.update(1, 1, 'test', [1], 1)
        with self.assertRaises(TypeError):
            # Wrong data type as kwargs
            inst_up.update(id=1, width=1, height='test', x=[1], y=1)

if __name__ == '__main__':
    unittest.main()

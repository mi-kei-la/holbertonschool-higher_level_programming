#!/usr/bin/python3
"""Unittest for max_integer
Here more comments.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Comments for test class"""
    def testBasic(self):
        """Test regular input"""
        self.assertEqual(max_integer([8, 13, 2]), 13)
        self.assertEqual(max_integer([42, 22, 12]), 42)
        self.assertEqual(max_integer([1, 2, 0]), 2)

    def testNegs(self):
        """Check for negative numbers"""
        self.assertEqual(max_integer([-1, -2, 0]), 0)
        self.assertEqual(max_integer([-8, 4, -36]), 4)
        self.assertEqual(max_integer([-8, -34, -53]), -8)

    def testBool(self):
        """check if a boolean works"""
        self.assertEqual(max_integer([True, False]), True)

    def testFloat(self):
        """check float data type"""
        self.assertEqual(max_integer([1.5, 2.032, 0.5]), 2.032)
        self.assertEqual(max_integer([1.11, 1.12, 1.11111115]), 1.11111115)

    def testStrings(self):
        """check function with strings"""
        self.assertEqual(max_integer(["hi", "how", "are", "you", "?"]), "you")
        self.assertEqual(max_integer(["this", "is bullshit"]), "this")

if __name__ == '__main__':
    unittest.main()

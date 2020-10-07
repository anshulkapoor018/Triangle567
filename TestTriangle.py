#!/usr/bin/env python

"""
TestTriangle.py
The primary goal of this file is to demonstrate side_a simple unittest implementation
"""
__author__ = "Anshul Kapoor"

import unittest

from triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    """
    define multiple sets of tests as functions with names that begin
    """
    # Testing Equilateral Triangles
    def testEquilateralTriangle1(self):
        self.assertEqual(classify_triangle(2, 2, 2), 'Equilateral')

    def testEquilateralTriangle2(self):
        self.assertEqual(classify_triangle(15, 15, 15), 'Equilateral')

    def testEquilateralTriangle3(self):
        self.assertNotEqual(classify_triangle(10, 1, 10), 'Equilateral')

    # Testing Isosceles Triangles
    def testIsoscelesTriangle1(self):
        self.assertEqual(classify_triangle(5, 5, 3), 'Isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classify_triangle(4, 6, 6), 'Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classify_triangle(8, 5, 8), 'Isosceles')

    def testIsoscelesTriangle4(self):
        self.assertEqual(classify_triangle(6, 6, 4), 'Isosceles')

    # Testing Scalene Triangles
    def testScaleneTriangle1(self):
        self.assertEqual(classify_triangle(10, 11, 12), 'Scalene')

    def testScaleneTriangle2(self):
        self.assertEqual(classify_triangle(4, 2, 3), 'Scalene')

    def testScaleneTriangle3(self):
        self.assertEqual(classify_triangle(100, 110, 112), 'Scalene')

    def testScaleneTriangle4(self):
        self.assertNotEqual(classify_triangle(10, 10, 12), 'Scalene')

    # Testing Invalid Inputs
    def testInvalidInput1(self):
        self.assertEqual(classify_triangle(-1, -1, -1), 'InvalidInput')

    def testInvalidInput3(self):
        self.assertEqual(classify_triangle("200", "0", "0"), 'InvalidInput')

    # Testing Not side_a Triangle
    def testNotATriangle1(self):
        self.assertEqual(classify_triangle(5, 1, 1), 'NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classify_triangle(1, 5, 1), 'NotATriangle')

    def testNotATriangle3(self):
        self.assertEqual(classify_triangle(1, 1, 5), 'NotATriangle')

    def testNotATriangle4(self):
        self.assertEqual(classify_triangle(1, 17, 5), 'NotATriangle')

    # Testing Right Triangles
    def testRightTriangle1(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene Right')

    def testRightTriangle2(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Scalene Right')

    def testRightTriangle3(self):
        self.assertEqual(classify_triangle(13, 12, 5), 'Scalene Right')

    def testRightTriangle4(self):
        self.assertEqual(classify_triangle(8, 6, 10), 'Scalene Right')

    def testRightTriangle5(self):
        self.assertNotEqual(classify_triangle(21, 6, 10), 'Right')


if __name__ == '__main__':
    print('--------------Starting Unit Tests--------------')
    unittest.main()

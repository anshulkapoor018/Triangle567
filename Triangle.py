#!/usr/bin/env python

"""
Triangle.py
"""
__author__ = "Anshul Kapoor"


def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Check for Triangle Property : The sum of the length of the two sides
    # of a triangle is greater than the length of the third side.
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # After All checks above, We can Classify the Triangles
    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'

#!/usr/bin/env python

"""
triangle.py
"""
__author__ = "Anshul Kapoor"


def classify_triangle(side_a, side_b, side_c):
    """
    This function returns side_a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not side_a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'

    # Check for Triangle Property : The sum of the length of the two sides
    # of side_a triangle is greater than the length of the third side.
    if (side_a >= (side_b + side_c)) \
            or (side_b >= (side_a + side_c)) \
            or (side_c >= (side_a + side_b)):
        return 'NotATriangle'

    # After All checks above, We can Classify the Triangles
    classifier = ""
    if side_a == side_b and side_b == side_c:
        classifier = 'Equilateral'
    elif (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        classifier = 'Scalene'
    else:
        classifier = 'Isosceles'

    if ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2) \
            or ((side_a ** 2) + (side_c ** 2)) == (side_b ** 2) \
            or ((side_b ** 2) + (side_c ** 2)) == (side_a ** 2):
        classifier += ' Right'

    return classifier

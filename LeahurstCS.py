import os
import math
"""
This is the Leahurst Computer Science Team's Library of Useful Functions.
to add to the Library of Useful Functions, Make sure to check with Dr. C before committing
This Library can be used like any other, but requires the following dependencies to be installed
for full functionality:
    - os module (built in)
    - math module (built in)
    - 
Remember to Follow the naming convention as demonstrated below, and make note of anything your function does.
Make sure your methods are robust, and will always do what they say they will.
Make sure your methods can be applied to more than one program. 
_________ Committing your changes __________
Follow the convention demonstrated in the previous commits,
make note of added dependencies
make note of added functions
"""


def read_file_contents(filename):
    """
    This function loads all the information in a given file. (remember to include .txt)
    :param filename: a full file path to the document to open (string)
    :return: (string) Contents of file
    """
    with open(filename) as f:
        contents = f.readlines()
    return contents


def calc_linear_distance(x1, y1, x2, y2):
    """
    Calculates the distance between 2 given points
    :param x1: x coordinate at point 1
    :param y1: y coordinate at point 1
    :param x2: x coordinate at point 2
    :param y2: y coordinate at point 2
    :return: (float) Linear Distance from point to point
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_angle(x1, y1, x2, y2):
    """
    Calculates the angle of the line between the two given coordinates and the x-axis.
    Will always be between 90 to -90 degrees.
    :param x1: x coordinate at point 1
    :param y1: y coordinate at point 1
    :param x2: x coordinate at point 2
    :param y2: y coordinate at point 2
    :return: (float) the Related Acute Angle in degrees
    """
    deltaX = x2 - x1
    deltaY = y2 - y1
    return math.degrees(math.atan(deltaY / deltaX))


def get_absolute_angle_from_orig(x, y):
    """
    Calculates the angle of the line from the origin to the given point,
    always with respect to the positive x axis, from 0-360 degrees
    :param x: x coordinate at the line end
    :param y: y coordinate at the line end
    :return: (float) absolute angle from +x axis in degrees
    """

    if x > 0 and y > 0:
        print("Q1")
        angle = get_angle(0, 0, x, y)
    elif x > 0 and y < 0:
        print("Q4")
        angle = get_angle(0, 0, Px, Py)
    elif x < 0 and y < 0:
        print("Q3")
        angle = get_angle(0, 0, Px, Py) + 180
    elif x < 0 and y > 0:
        print("Q2")
        angle = 180 + get_angle(0, 0, Px, Py)
    else:
        angle = 0
    return angle

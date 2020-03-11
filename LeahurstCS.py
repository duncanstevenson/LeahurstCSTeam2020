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

def throwaway(x):
    print("Hello World")
    
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
    :param y2:y coordinate at point 2
    :return: Linear Distance from point to point
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

'''
Day 2: Create a program to calculate the area of a circle given its radius.
'''

from math import pi

def area(r):
    """
    >>> area(30)
    2827
    """
    return round(r**2 * pi)

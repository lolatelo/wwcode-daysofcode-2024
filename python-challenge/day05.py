'''
Day 5: Write a program to find the maximum and minimum values in a list.
'''


def min_max(lst):
    """
    >>> a, b = min_max([1, 2, 3, 4, 5])
    >>> a
    1
    >>> b
    5
    """
    miny = min(lst)
    maxy = max(lst)
   
    return miny, maxy

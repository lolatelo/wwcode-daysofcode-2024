'''
Day 1: Create a program that swaps the values of two variables.
'''

def swap(x, y):
    """
    >>> a, b = swap(2, 3)
    >>> a
    3
    >>> b
    2
    """
    temp_x = x
    x, y = y, temp_x
    return x, y

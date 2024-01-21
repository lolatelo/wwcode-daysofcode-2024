'''
Day 7: Write a program to check if a number is positive, negative, or zero.
'''


def sign(num):
    """
    >>> sign(1)
    'positive'
    >>> sign(0)
    'zero'
    >>> sign(-2)
    'negative'
    """

    if num > 0:
        return 'positive'
    elif num == 0:
        return 'zero'
    else:
        return 'negative'

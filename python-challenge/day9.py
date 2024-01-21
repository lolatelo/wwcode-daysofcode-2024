'''
Day 9: Write a program to check if a number is even or odd.
'''


def even_odd(num):
    '''
    >>> even_odd(2)
    'even'
    >>> even_odd(-3)
    'odd'
    >>> even_odd(0)
    'zero'
    '''

    if num == 0:
        return 'zero'
    elif num % 2 == 0:
        return 'even'
    else:
        return 'odd'

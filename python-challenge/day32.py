'''
Day 32: Create a function that calculates the average of a list of numbers.
'''

def avg_lst(lst):
    '''
    >>> avg_lst([1, 7, 3, 9])
    5.0
    >>> avg_lst([0])
    0.0
    '''
    return sum(lst) / len(lst)

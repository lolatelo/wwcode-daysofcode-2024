'''
Day 38: Write a program to flatten a nested list.
'''

def flatten(lst):
    '''
    >>> flatten([1, 2, 3, [4, [5, 6]]])
    [1, 2, 3, 4, 5, 6]
    '''
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

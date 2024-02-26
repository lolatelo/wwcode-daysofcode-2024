'''
Day 28: Create a program that removes the nth element from a list.
'''

def remove_n(n, lst):
    """
    >>> remove_n(5, ['apple', 'cat', 'dog', 'pear', 'person'])
    ['apple', 'cat', 'dog', 'pear']
    >>> remove_n(5, ['a', 'g', 'z', 1])
    'Out of range'
    >>> remove_n(2, ['a', 'g', 'z', 1])
    ['a', 'z', 1]
    """
    keep_item = []

    if len(lst) < n :
        return 'Out of range'

    for i, item in enumerate(lst):
        if i != n - 1:
            keep_item.append(item)
            
    return keep_item

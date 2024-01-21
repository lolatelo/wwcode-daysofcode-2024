'''
Day 10: Write a program to remove duplicates from a list.
'''


def remove_dupes(lst):
    '''
    >>> remove_dupes([1, 2, 'cat', 2, 3])
    [1, 2, 'cat', 3]
    '''
    #  list(set(lst)) can be used but it will not keep the order

    keep_elem = []

    # check each elem in lst and append to keep_elem if it is not in keep_elem
    for elem in lst:
        if elem not in keep_elem:
            keep_elem.append(elem)

    return keep_elem

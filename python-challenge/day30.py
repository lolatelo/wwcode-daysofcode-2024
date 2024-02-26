'''
Day 30: Create a function that finds the second smallest element in a list.
'''

def second_small_sort(lst):
    '''
    >>> second_small_sort([1, 6, 3, 9])
    3
    >>> second_small_sort([1])
    'List is too small'
    '''

    if len(lst) < 2:
        return "List is too small"

    lst.sort()

    return lst[1]



def second_small_loop(lst):
    '''
    >>> second_small_sort([3, 6, 1, 9])
    3
    >>> second_small_sort([1])
    'List is too small'
    '''
    if len(lst) < 2:
        return "List is too small"
    
    smallest = lst[0]
    second_smallest = lst[1]

    for i in lst:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest:
            second_smallest = i  
    
    return second_smallest

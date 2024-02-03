'''
Day 22: Create a program to find the second-largest element in a list.
'''

def second_elem(lst):
    '''
    >>> second_elem([8, 9, 6, 0, 6])
    6
    >>> second_elem([1])
    1
    >>> second_elem([2, 1, 3])
    1
    '''

    if len(lst) == 1:
        return lst[0]

    else:
        first, second = float('-inf'), float('-inf')

        for elem in lst:
            if elem > first:
                first = elem
            elif elem > second:
                second = elem
            else:
                pass
    
        return min(first, second)

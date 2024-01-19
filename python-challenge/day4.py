'''
Day 4: Write a program to find the sum of all elements in a list. 
'''


def sum_elems(lst):
    """
    >>> sum_elems([1, 2, 3, 4, 5])
    15
    """
    i = 0
    sums = 0
    
    while i < len(lst):
        sums += lst[i]
        i += 1
   
    return sums

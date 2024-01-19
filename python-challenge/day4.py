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


# alternative with for loop
def sum_list(lstValues):
    """
    >>> sum_list([1, 2, 3, 4, 5])
    15
    """
    summ = 0
    for val in lstValues:
        summ += val
    
    return summ

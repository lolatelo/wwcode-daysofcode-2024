'''
Day 20: Write a function that takes a list of numbers and returns a new list containing only the even numbers.
'''

def evens(nums):
    '''
    >>> evens([2, 5, 7, 8])
    [2, 8]
    >>> evens([9, 3, 0])
    []
    '''
    # iterate through each elem in lst
    # if even, put the even elem in a new lst
    # if odd, keep iterating
    # stop when you get to the end of the lst

    even_lst = []

    for elem in nums:
        if elem % 2 == 0:
            even_lst.append(elem)
    
    if even_lst == [0]:
        return []
    else:
        return even_lst

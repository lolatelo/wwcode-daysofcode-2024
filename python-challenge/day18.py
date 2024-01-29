'''
Day 18: Create a program to find the largest among three numbers.
'''

def largest_three(num_1, num_2, num_3):
    '''
    >>> largest_three(1, 2, 3)
    3
    >>> largest_three(8, 20, 1)
    20
    '''
    return max(num_1, num_2, num_3)

def largest_number(*nums):
    '''
    >>> largest_number(1, 2, 3)
    3
    >>> largest_number(8, 20, 1)
    20
    '''
    return max(nums)

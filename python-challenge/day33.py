'''
Day 33: Write a test case for a function that checks if a number is prime.
'''
from math import sqrt

def prime(num):
    '''
    >>> prime(27)
    False
    >>> prime(11)
    True
    '''
    if num == 1 or num == 0:
        return False
    
    mults = range(2, int(sqrt(num))+1)

    divisors = []

    for i in mults:
        if num % i == 0 and num != i:
            return False
        
    return True

'''
Day 19: Write a function to calculate the factorial of a number.
'''

def factorial(num, fact=1):
    '''
    >>> factorial(2)
    2
    >>> factorial(0)
    1
    >>> factorial(5)
    120
    '''
    # something that keeps track of our product
    # something that keeps track of what's next
    # base cases

    if num == 0:
        return 1
    
    else:
        return factorial(num - 1, fact*num)

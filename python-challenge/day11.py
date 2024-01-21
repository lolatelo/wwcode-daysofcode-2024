'''
Day 11: Write a program to print the multiplication table of a given number.
'''


def multiples(num, factor=1, result=None):
    '''
    >>> multiples(20)
    [(1, 20), (2, 10), (4, 5)]
    '''

    # initialize result list on the first call.
    # we use None instead of an empty list in the argument
    # to avoid unintended behavior when modifying the list

    if result is None:
        result = []
    
    # BEGIN RECUSRIVE CALL
    # base case: stop when factor exceeds half of num
    if factor > num // 2:
        return result
    
    # if factor is a divisor of num, add the pair (factor, num // factor)
    if num % factor == 0:
        result.append((factor, num // factor))
    
    # direction of recursion: the recursive call changes the parameters is
    # incrementally increasing  towards a base case
     # In your case, factor starts from 1 and increases until it reaches num // 2.
    return multiples(num, factor + 1, result)



def find_multiples(num):
    """
    Find and return pairs of factors of the given number.
    """
    result = []

    for i in range(1, num // 2 + 1):  # Only need to check up to num // 2
        if num % i == 0:  # Check if i is a factor of num
            result.append((i, num // i))

    return result

# Example usage
print(find_multiples(20)) 



def print_multiplication_table(num):
    for i in range(1, num):  
        print(f"{num} x {i} = {num * i}")


print_multiplication_table(20)  # This will print the multiplication table of 5

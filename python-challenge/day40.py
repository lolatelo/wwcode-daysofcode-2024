'''
Day 40: Write a function to find the largest common divisor of two numbers using a function.
'''

def gcd(a, b):
    '''
    >>> gcd(64, 32)
    32
    >>> gcd(92, 82)
    2
    '''
    def multiples(big_num):
        mults = []
        for num in range(2, big_num+1):
            if big_num%num == 0:
                mults.append(num)
        return mults

    # find multiples of a
    mults_a = multiples(a)

    # find multiples of b
    mults_b = multiples(b)

    # find the lowest common multiple between a and b
    # find common multiples
    common_mults = []

    for num in mults_a:
        if num in mults_b:
            common_mults.append(num)

    # get gcd
    return max(common_mults)

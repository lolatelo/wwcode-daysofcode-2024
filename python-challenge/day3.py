'''
Day 3: Write a function to count the number of vowels in a given string 
'''


def count_vowels(w):
    """
    >>> count_vowels('cat')
    1
    >>> count_vowels('wwcpythonchallenge')
    4
    """
    i = 0
    v = 0
    while i < len(w):
        if w[i] in ('a', 'e', 'o', 'i', 'u'):
            v += 1
        i += 1
    return v

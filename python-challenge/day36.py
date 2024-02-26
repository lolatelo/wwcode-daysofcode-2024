'''
Day 36: Write a Python program to check if two strings are anagrams.
'''

def anagram(str1, str2):
    '''
    >>> anagram('cat', 'tac')
    True
    >>> anagram('cat', 'tacc')
    False
    '''
    return str1 == str2[::-1]

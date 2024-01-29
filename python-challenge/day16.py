'''
Day 16: Write a function that counts the frequency of each word in a sentence.

'''

from datetime import datetime

def count_freq(snt, word):
    '''
    >>> count_freq('I love cats', 'cats')
    1
    >>> count_freq('I love orange cats and black cats', 'cats')
    2
    '''
    # split snt into a list of words
    # loops through snt_lst
    # checks if each word at idx in snt_lst == word
    # if yes, increment a count
    # if no, keep going through snt until you reach the end of snt

    snt_lst = snt.split()

    count_word = 0

    for char in snt_lst:
        if  char == word:
            count_word += 1
    
    return count_word

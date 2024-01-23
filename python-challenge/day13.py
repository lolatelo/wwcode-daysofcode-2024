'''
Day 13: Write a program to shuffle the elements of a list randomly.
'''

from random import choice

def shuffle(lst):
    
    shuffled_lst = []
    
    while len(shuffled_lst) < len(lst):
        shuff_char = choice(lst)
        if shuff_char not in shuffled_lst:
            shuffled_lst.append(shuff_char)
        
    return shuffled_lst


lst = [1, 'cat', 9, -1]
print(shuffle(lst))

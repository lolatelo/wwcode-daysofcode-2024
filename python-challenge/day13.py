'''
Day 13: Write a program to shuffle the elements of a list randomly.
'''

from random import shuffle

def shuffle_list(lst):
    shuffle(lst)
    return lst

lst = [1, 'cat', 9, -1]
print(shuffle_list(lst))

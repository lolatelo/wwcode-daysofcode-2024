'''
Day 23: Write a program that checks if a key exists in a dictionary.
'''


def key_dict(dct, ky):
    '''
    >>> key_dict({'dog': 'cat', 'apple': 'pineapple', 1: 2}, 1)
    True
    >>> key_dict({'dog': 'cat', 'apple': 'pineapple', 1: 2}, 3)
    False
    '''

    in_dict = False

    for elem in dct.keys():
        if elem == ky:
            in_dict = True

    return in_dict



def key_dict(dct, ky):
    '''
    >>> key_dict({'dog': 'cat', 'apple': 'pineapple', 1: 2}, 1)
    True
    >>> key_dict({'dog': 'cat', 'apple': 'pineapple', 1: 2}, 3)
    False
    '''
    
    return ky in dct.keys()

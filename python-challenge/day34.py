'''
Day 34: Write a Python program to merge two dictionaries.
'''

def merge_dicts(dict1, dict2):
    '''
    >>> merge_dicts({'cat': 'dog', 'apple': 'pear'}, {0: 1, 1: 2})
    {'cat': 'dog', 'apple': 'pear', 0: 1, 1: 2}
    '''
    new_dict = {}

    for key, value in dict1.items():
        new_dict[key] = value
    
    for key, value in dict2.items():
        new_dict[key] = value

    return new_dict

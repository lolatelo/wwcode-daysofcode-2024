'''
Day 37: Write a program to iterate through a dictionary and print its keys and values.
'''

def print_dict(dict):
    '''
    >>> print_dict({'cat': 'dog', 'apple': 'pear'})
    key: cat
    key: apple
    value: dog
    value: pear
    '''
    for key in dict.keys():
        print(f'key: {key}')
    for value in dict.values():
        print(f'value: {value}')

'''
Day 24: Write a program to remove vowels from a given string.
'''


def remove_vowels(str):
    '''
    >>> remove_vowels('cat')
    'ct'
    >>> remove_vowels('I LOVE PYTHON')
    ' LV PYTHN'
    '''

    vowels = ['a', 'i', 'e', 'o', 'u']
    no_vowels = ''

    for elem in str:
        if elem.lower() not in vowels:
            no_vowels += elem
    
    return no_vowels



#no_vowels = [elem for elem in s if elem not in vowels]
#return ''.join(no_vowels)

'''
Day 21: Create a program to remove a specific element from a set.
'''

def remove_elem(st, elem):
    '''
    >>> remove_elem({'cat', 'dog', 3}, 3)
    {'cat', 'dog'}
    '''
    new_st = st.copy()
    new_st.discard(elem)
    
    return new_st

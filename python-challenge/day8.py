'''
Day 8: Write a function that accepts a string and
calculates the number of uppercase and lowercase letters in it.
'''


def case_count(s):
    """
    >>> case_count('cat')
    [0, 3]
    >>> case_count('CAt')
    [2, 1]
    """
    #str = 'CAT'
    lower_str = s.lower()

    i = 0
    lower_cnt = 0
    upper_cnt = 0

    # this counts our letters
    for l in s:
        if lower_str[i] == s[i]:
            lower_cnt += 1
        else:
            upper_cnt += 1
        i += 1
    
    # output
    return [upper_cnt, lower_cnt]        


### ALTERNATIVE with enumerate(...)
def case_count(input_str):
    """
    >>> case_count('cat')
    (0, 3)
    >>> case_count('CAt')
    (2, 1)
    """
    lower_str = input_str.lower()

    lower_cnt = 0
    upper_cnt = 0

    for i, char in enumerate(s):
        if lower_str[i] == char:
            lower_cnt += 1
        else:
            upper_cnt += 1 

    return [upper_cnt, lower_cnt]    

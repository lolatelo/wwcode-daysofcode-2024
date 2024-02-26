'''
Day 31: Create a program that checks if a given string is a valid email address.
'''
import re

def check_email(email_str):
    '''
    >>> check_email('wwc@gmail.com')
    True
    >>> check_email('hello@gmail')
    False
    '''
    
    # Check @ pattern is in the string
    start_match = re.search(r'.*@', email_str)
    end_match = re.search(r'@.*', email_str)

    if start_match and end_match:
    # Check if the string ends in .com, .net., .org. or .gov
        if email_str[-4:] in ('.org', '.net', '.gov', '.com'):
            return True
        else:
            return False
    else:
        return False

'''
Day 12: Write a program to reverse a given string.
'''


def reverse_str(s):

    # simplest approach: s[::-1]

    # from scratch approach
    r = ''
    for i in range(len(s)):
        r += s[-i - 1]

    return r

print(reverse_str('cat'))

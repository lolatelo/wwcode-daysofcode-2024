'''
Day 6: Write a program to count the occurrences of a specific character in a string.
'''


def count_char(str, char):
    """
    >>> count_char('cat', 'c')
    1
    >>> count_char('squeeks', 's')
    2
    """
    chars = []
    i = 0
    cnt = 0

# while loop is not necessary to string because for loop will already index
# In Python, strings are inherently iterable, and you can loop over them directly in a for loop
# without needing to convert them into a list of characters first.
# Each iteration of the for loop will automatically give you one character from the string.

    while i < len(str):
        chars.append(str[i])
        i += 1


    for w in chars:
        if w == char:
            cnt += 1
    return cnt

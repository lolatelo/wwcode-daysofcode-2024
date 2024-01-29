'''
Day 15: Create a program that checks if a year is a leap year.

'''

from datetime import datetime

def check_leap(yr):
    '''
    >>> check_leap(2023)
    False
    >>> check_leap(2024)
    True
    '''
    #take in a year, then check the dif between jan 1 of that yr and dec 31
    def diff_dates(yr):
        start = f"{yr}-01-01"
        end = f"{yr}-12-31"

        d1 = datetime.strptime(start, "%Y-%m-%d")
        d2 = datetime.strptime(end, "%Y-%m-%d")

        return d2 - d1

    # if the difference is 366, this is a leap year

    yr_days = diff_dates(yr)

    if (yr_days).days == 365:
        return True
    else:
        return False

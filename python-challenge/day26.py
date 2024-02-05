def square_stuff(lst):
    """
    >>> square_stuff([1, 2, 9, 7])
    [1, 4, 81, 49]
    """
    #return [x * x for x in lst]
    return list(map(lambda x: x * x, lst))

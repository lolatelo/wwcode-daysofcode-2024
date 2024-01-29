'''
Day 17: Create a program that capitalizes the first letter of each word in a sentence
'''

def cap_words(snt):
    '''
    >>> cap_words('I love cats')
    'I Love Cats'
    >>> cap_words('I love orange cats and black cats')
    'I Love Orange Cats And Black Cats'
    '''
    #split snt into a list of words
    #iterate through each elem in snt_lst and apply upper or capialist
    # concatenate back to sentence with spaces (don't add space to the last word)

    snt_lst = snt.split()

    cap_snt = ''

    last_word = len(snt_lst) - 1

    for idx, word in enumerate(snt_lst):
        if idx == last_word:
            cap_snt += word.capitalize()
        else:
            cap_snt += word.capitalize() + ' '

    return cap_snt

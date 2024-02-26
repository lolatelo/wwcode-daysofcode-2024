'''
Day 39: Write a program to find the most common words in a text file.
'''
import string

def most_common(text):
    '''
    >>> most_common("I am a text file; I love text.")
    ['I', 'text']
    '''
    # strip punctuation
    def strip_punctuation(s): return s.translate(str.maketrans('', '', string.punctuation))

    clean_text = strip_punctuation(text).split()

    # make dict for counts for each word
    text_dict = {word: 0 for word in clean_text}

    # use dict to keep track of counts while looping through text
    for word in clean_text:
        for k, v in text_dict.items():
            if word == k:
                text_dict[k] = v + 1
    
    # find the most common words
    most_common_count = max(text_dict.values())

    common_words = [word for word, count in text_dict.items() if count==most_common_count]

    return common_words

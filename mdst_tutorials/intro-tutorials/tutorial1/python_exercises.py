"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if x%2==0:
        return False
    return True


def is_palindrome(word):
    rword=word[::-1]
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    if word== rword:
        return 'this is a palindrome'
    else:
        return 'not a palindrome'


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    return [x for x in numlist if x%2!=0]


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    print(text.split())
    cd={}
    for x in text.split():
        if x in cd:
            cd[x]+=1
        else:
            cd[x]=1
    return cd
#print(is_palindrome('dad'),is_palindrome('sad'),count_words('this is a sentence'),only_odds([1,2,3,4]))

'''
Soundex 
https://pypi.org/project/Fuzzy/

Levenshtein 
https://pypi.org/project/python-Levenshtein/




distance('Levenshtein', 'Lenvinsten')
'''

import Levenshtein

def get_levenshtein_distance(word1, word2):
    """
    https://en.wikipedia.org/wiki/Levenshtein_distance
    :param word1:
    :param word2:
    :return:
    """
    word2 = word2.lower()
    word1 = word1.lower()
    matrix = [[0 for x in range(len(word2) + 1)] for x in range(len(word1) + 1)]

    for x in range(len(word1) + 1):
        matrix[x][0] = x
    for y in range(len(word2) + 1):
        matrix[0][y] = y

    print(matrix)
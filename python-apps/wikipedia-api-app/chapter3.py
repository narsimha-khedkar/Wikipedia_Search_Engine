'''
Soundex 
https://pypi.org/project/Fuzzy/

Levenshtein 
https://pypi.org/project/python-Levenshtein/

import Levenshtein

distance('Levenshtein', 'Lenvinsten')

'''


#from Levenshtein import process

from fuzzywuzzy import process

with open("570.txt","r") as file:
    terms = file.read().split("\n")
    #terms = file.read().split(" ")

total = len(terms)
print("Number of Terms: ", str(total))

def get_matches(word, possibilities, limit =3):
        results = process.extract(word, possibilities, limit=limit)
        #results = process.extractOne(word, possibilities)
        return results
    
print(get_matches("Pennsylvania", terms))









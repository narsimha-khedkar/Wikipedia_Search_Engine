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

with open("output.txt","r") as file:
    terms = file.read().split("\n")

total = len(terms)
print("Number of Terms: ", str(total))

def get_matches(word, possibilities, limit =3):
        results = process.extract(word, possibilities, limit=limit)
        return results
    
print(get_matches("Mustard", terms))








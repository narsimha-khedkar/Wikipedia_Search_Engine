import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.stem import PorterStemmer, LancasterStemmer
import wikipedia 

#Search
results = wikipedia.search('Facebook')

#Get first article from results
article = results[0]

#Get text of article
text = wikipedia.summary(article)
#text = wikipedia.page(article).content

sentences = sent_tokenize(text)
words = word_tokenize(text)

print(sentences)
print("---------------------------")
print(words)
print("---------------------------")

porter = PorterStemmer()
lancaster = LancasterStemmer()

#Porter Stemming
for w in words: 
    print(w, " : ", porter.stem(w)) 
print("---------------------------")
#Lancaster Stemming
for m in words: 
    print(m, " : ", lancaster.stem(m)) 
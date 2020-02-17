import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.stem import PorterStemmer, LancasterStemmer

#Will Work on adding text via Wikipedia
text = 'She sell sea shells by the sea shore. Humpty Dumpty sat on a wall.'

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
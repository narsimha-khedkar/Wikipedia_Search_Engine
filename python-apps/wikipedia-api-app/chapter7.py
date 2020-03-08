from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot
import pandas as pd
import numpy as np

#Read Wikipedia Data file containing names of people and a short article about them
wiki_data = pd.read_csv('wiki_people.csv', index_col='name')['text']

#Define the TFIDF vectorizer that will be used to process the data
tfidf_vectorizer = TfidfVectorizer()

#Apply this vectorizer to the full dataset to create normalized vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(wiki_data)

#Apply the Nearest Neighbor Algorithm to find 10 people with similar attributes
nbrs = NearestNeighbors(n_neighbors=10).fit(tfidf_matrix)

#Get those 10 people who have similar attributes to the input person
def get_closest_neighs(name):
    row = wiki_data.index.get_loc(name)
    distances, indices = nbrs.kneighbors(tfidf_matrix.getrow(row))
    names_similar = pd.Series(indices.flatten()).map(wiki_data.reset_index()['name'])
    result = pd.DataFrame({ 'name':names_similar, 'distance':distances.flatten()})
    return result

print(get_closest_neighs('Clint Eastwood'))

print(get_closest_neighs('Michael Schumacher'))
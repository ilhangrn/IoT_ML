# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import numpy as np
corpus = ['this is the first document',
          'this document is the second document',
          'and this is the third one',
          'is this the first document']
vocabulary = ['this', 'document', 'first', 'is', 'second', 'the',
              'and', 'one']
pipe = Pipeline([('count', CountVectorizer(vocabulary=vocabulary)),
                 ('tfid', TfidfTransformer())]).fit(corpus)
print('Vectorizaion array') # Count of the vocabulary terms in the array
print(pipe['count'].transform(corpus).toarray())
print('idf') # inverse document frequency (IDF) vector (of a word in the corpus). How rare (from 1 on) a word is in the corpus    # tf is term frequency in a document
print(pipe['tfid'].idf_)
print('tfidf') # It's a sparse matrix
tfidf = pipe.transform(corpus)
print(tfidf.toarray()) # For each term, its relevance for the current document (product of how frequent is the term in the document * how rare is in the corpus)
print('tfidf shape')
print(pipe.transform(corpus).shape) # (4, 8)
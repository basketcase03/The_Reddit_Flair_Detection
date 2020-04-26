import pandas as pd
import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
ps = PorterStemmer()

import nltk
import string
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import os


def preprocess_text(txt):
    if type(txt)==str:
        nopunc = [str(char) for char in txt if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        return [ps.stem(word.lower()) for word in nopunc.split() if word.lower() not in nltk.corpus.stopwords.words('english')]



param_grid = {'C': [0.1,1, 10, 100], 'gamma': [1,0.1,0.01,0.001]} 

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=preprocess_text)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', GridSearchCV(SVC(),param_grid,refit=True,verbose=2)),  # train on TF-IDF vectors w/ Naive Bayes classifier
])





    




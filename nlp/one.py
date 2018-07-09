#!/usr/bin/env
import sys
import nltk
import pandas as pd
from nltk.corpus import stopwords
import string
import re
from sklearn.feature_extraction.text import CountVectorizer


stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer()

def remove_punct(text):
  text_nopunct = "".join([char for char in text if char not in string.punctuation])
  return text_nopunct

def tokenize(text):
  tokens = re.split('\W+', text.lower())
  return tokens

def remove_stopwords(tokenized_list):
  text = [word for word in tokenized_list if word not in stopwords]  
  return text

def stemming(tokenized_text):
  text = [ps.stem(word) for word in tokenized_text]
  return text

def lemmatizing(tokenized_text):
  text = [wn.lemmatize(word) for word in tokenized_text]
  return text

def clean_text(text):
  text = "".join([word.lower() for word in text if word not in string.punctuation])
  tokens = re.split('\W+', text)
  text = [ps.stem(word) for word in tokens if word not in stopwords]
  return text

pd.set_option('display.max_colwidth', 100)
data = pd.read_csv("Ex_Files_NLP_Python_ML_EssT/Exercise Files/Ch01/01_03/Start/SMSSpamCollection.tsv", sep = '\t', header=None)
data.columns = ['label', 'text']
data['text_clean'] = data['text'].apply(lambda x: remove_punct(x))
data['text_tokenized'] = data['text_clean'].apply(lambda x: tokenize(x))
data['text_nonstop'] = data['text_tokenized'].apply(lambda x: remove_stopwords(x))
data['text_stemmed'] = data['text_nonstop'].apply(lambda x: stemming(x))
#data['text_lemma'] = data['text_nonstop'].apply(lambda x: lemmatizing(x))

#Vectorizing
sample = data[0:20]
count_vect = CountVectorizer(analyzer=clean_text)
X_counts = count_vect.fit_transform(sample['text'])
X_counts_df= pd.DataFrame(X_counts.toarray())
#print(X_counts)
#print(count_vect.get_feature_names())
X_counts_df.columns = count_vect.get_feature_names()
print(X_counts_df)

#print(sample)
#small = CountVectorizer(analyzer=clean_text)
#small_counts = count_vect.fit_transform(sample['text'])
#
#print(small_counts.shape)
#print(small.get_feature_names())
#
#print(data.head())
#print(fullCorpus['text'].isnull().sum())
#fullCorpus[fullCorpus['label'] == 'spam'])
#print(fullCorpus.head(20))


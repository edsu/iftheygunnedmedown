#!/usr/bin/env python

import os
import re
import json

from gensim import corpora, models, similarities

def docs():
    for line in open("tweets.json"):
        tweet = json.loads(line)
        if not 'retweeted_status' in tweet and tweet['lang'] == 'en':
            yield words(tweet['text'])

def words(s):
    words = s.lower().split(' ')
    new_words = []
    for word in words:
        if re.match(r'(@|http|#)', word):
            continue
        new_words.append(word)
    return new_words

def get_dictionary(path):
    if not os.path.isfile(path):
        dictionary = corpora.Dictionary()
        dictionary.save(path)
    else:
        dictionary = corpora.Dictionary.load(path)
    return dictionary

def get_corpus(path, dictionary):
    def ids():
        for doc in docs():
            yield dictionary.doc2bow(doc)
    if not os.path.isfile(path):
        corpus = corpora.MmCorpus.serialize(path, ids())
    else:
        corpus = corpora.MmCorpus(path)
    return corpus

dictionary = get_dictionary("topics.dict")
corpus = get_corpus("topics.mm", dictionary)

print corpus

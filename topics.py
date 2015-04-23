#!/usr/bin/env python

import os
import re
import json
import string
import argparse

from gensim import corpora, models, similarities

punctuation = set(string.punctuation)

def docs():
    stop_words = get_stop_words('stopwords.txt')
    for line in open("tweets.json"):
        tweet = json.loads(line)
        if not 'retweeted_status' in tweet and tweet['lang'] == 'en':
            yield words(tweet['text'], stop_words)

def words(s, stop_words):
    words = s.lower().split(' ')
    new_words = []
    for word in words:
        word = word.strip()
        if not word:
            continue
        if word in stop_words:
            continue
        if re.match(r'^(@|\#|http)', word):
            continue
        if len(word) < 4:
            continue

        word = ''.join(ch for ch in word if ch not in punctuation)
        new_words.append(word)
    return new_words

def get_stop_words(path):
    stops = {}
    for word in open('stop_words.txt'):
        word = word.strip().lower()
        stops[word] = True
    return stops

def get_dictionary(path):
    if not os.path.isfile(path):
        dictionary = corpora.Dictionary(docs())
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

def main():
    parser = argparse.ArgumentParser(description="topic model some tweets")
    parser.add_argument('--num_topics', type=int, help='number of topics', default=20)
    parser.add_argument('--num_words', type=int, help='number of words', default=20)
    args = parser.parse_args()

    dictionary = get_dictionary("topics.dict")
    corpus = get_corpus("topics.mm", dictionary)
    lda = models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=args.num_topics)

    count = 0
    for topic in lda.show_topics(num_topics=args.num_topics, num_words=args.num_words, formatted=False):
        count += 1 
        print "topic #%i" % count
        for score, label in topic:
            print "- %s" % label.strip()
        print

if __name__ == "__main__":
    main()

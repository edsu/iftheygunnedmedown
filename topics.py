#!/usr/bin/env python

import json
from sklearn.feature_extraction.text import CountVectorizer

tweets = []
for line in open("tweets.json"):
    tweet = json.loads(line)
    if not 'retweeted_status' in tweet and tweet['lang'] == 'en':
        tweets.append(tweet['text'].lower())

stop_words = ["http", "https", "rt", "@", ":"]

vectorizer = CountVectorizer(stop_words=stop_words)
vectorizer.fit(tweets)

names = vectorizer.get_feature_names()
print names

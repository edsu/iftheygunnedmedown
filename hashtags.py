#!/usr/bin/env python

import json

tag_counts = {}

for line in open("tweets.json"):
    tweet = json.loads(line)
    for tag in tweet['entities']['hashtags']:
        text = tag['text'].lower()
        tag_counts[text] = tag_counts.get(text, 0) + 1

tags = tag_counts.keys()
tags.sort(lambda a, b: cmp(tag_counts[b], tag_counts[a]))
for tag in tags:
    print ("%s (%s)" % (tag, tag_counts[tag])).encode('utf8')

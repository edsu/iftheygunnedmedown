#!/usr/bin/env python

import json
import requests

for line in open('tweets.json'):
    tweet = json.loads(line)
    if 'media' not in tweet['entities']:
        continue
    for m in tweet['entities']['media']:
        print m['media_url']

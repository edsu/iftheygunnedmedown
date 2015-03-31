Tweets using the #iftheygunnedmedown hashtag from the 13.480,000 tweets
mentioning Ferguson between 2014-08-10 and 2014-08-27. It was assembled 
working with Chanon Adsanatham at the University of Maryland.

Twitter''s Terms of Service do not allow bulk redistribution of their JSON
data, but they do allow distribution of tweet identifiers. So to do anythin
meaningful with the data you will need to "hydrate" the tweet ids first. One 
way to do this is to use twarc:

    pip install twarc
    twarc.py --hydrate ids.txt > tweets.json


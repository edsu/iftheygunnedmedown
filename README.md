21,429 tweets using the #iftheygunnedmedown hashtag from MITH''s 
[collection](https://archive.org/details/fergusoncrawl) of 
13.480,000 tweets mentioning Ferguson between 2014-08-10 and 2014-08-27. It 
was assembled working with Chanon Adsanatham at the University of Maryland.

We are experimenting using topic models as an aid when conducting research
using [Grounded Theory](https://en.wikipedia.org/wiki/Grounded_theory).

Twitter''s Terms of Service do not allow bulk redistribution of their JSON
data, but they do allow distribution of tweet identifiers. So to do anythin
meaningful with the data you will need to "hydrate" the tweet ids first. One 
way to do this is to use twarc:

    pip install twarc
    twarc.py --hydrate ids.txt > tweets.json


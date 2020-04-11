# -*- coding: utf-8 -*-
"""Twitter-Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w5S4t8QF9OvgEvSGf21F2Q7MIhHEwZst
"""

import tweepy as tw
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

consumer_key = "w9Dj65V9mr4v1OCml72rlersQ"
consumer_secret = "PRpUhWbRvGQ1o3xkdalGUGlB1cwjNSmjFshba09e0nKdafcuHY"
access_token = "838352454517424128-aUaIuR6IgUyUZzwdOZ3JvVPlaDoJrYw"
access_token_secret = "ENAPFU3NUDYHB79kdGwjPGlDYQFhTUh0BIYElcCX2DTI5"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

"""# Scraping"""
tweets = []
public_tweets = api.home_timeline(count = 300)
for tweet in public_tweets:
  tweets.append(tweet.text)

list = pd.DataFrame({'tweets' : tweets})

from collections import Counter
common_words = Counter(" ".join(list["tweets"]).split()).most_common(100)

first_tuple_elements = []
for a_tuple in common_words:
	first_tuple_elements.append(a_tuple[0])

search_words = [word for word in first_tuple_elements if word not in stopwords.words('english')]

for word in search_words:
  tweets = tw.Cursor(api.search,
              q=word,
              lang="en",
              since='2018-04-23').items(25000)
scraped_tweets = [tweet.text for tweet in tweets]

"""# Creating a dataframe"""
df_random = pd.DataFrame({'Tweet' : scraped_tweets})


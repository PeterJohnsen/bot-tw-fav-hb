#!/usr/bin/env python

# This bot searches tweets using a word
# nd favorites those tweet

# Tweeting to https://twitter.com/politicsNstuff1

import tweepy, time, json, sys
from random import randint
from multiprocessing import Process

# Pulls access info
from credentials_hb import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Returns tweets based on search query
search_tweets = api.search("voter suppression",result_type="recent",count=100)

# Favorites tweets in search query
for tweet in search_tweets:
  try:
    print (tweet.id)
    api.create_favorite(tweet.id)
    time.sleep(randint(1,5))
  # exception in case of already favoriting
  except tweepy.TweepError as e:
    print ("Error: ", e)
  # Sleep for random amount of time

# Confirmation of success
print ("awesome")

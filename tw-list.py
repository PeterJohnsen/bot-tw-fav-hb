#!/usr/bin/env python

# This bot tweets three times, waiting 15 seconds between tweets.

# Tweeting to https://twitter.com/politicsNstuff1

import tweepy, time

# Gets log-in from file condentials.py
from credentials_hb import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
tweetlist = ['#MAGA El gran pendejo #ImStillWithHer',
'#trumprussia I really hope there are pee pee tapes',
'#IWakeUpBecause time to #resist trump']

for line in tweetlist: 
    api.update_status(line)
    print (line)
    print ('...')
    time.sleep(15) # Sleep for 15 seconds

print ("awesome")

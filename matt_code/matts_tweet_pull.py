#!/usr/bin/python
''' Pulls tweets from https://twitter.com/search-home using a code repo
developed at https://github.com/Jefferson-Henrique/GetOldTweets-python

This is designed to be run in Python 2
pip install lxml and pip install pyquery prior to running
'''

# imports
import got,sys,getopt,codecs
from datetime import datetime, date, timedelta


# run code from OldTweets to pull yesterday's tweets

yesterday = date.today() - timedelta(1)
two_days_back = date.today() - timedelta(2)
# print yesterday
# print two_days_back
type(yesterday)

#for testing: turn on "maxTweets" at the end of next line
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#fakenews').setSince(two_days_back.strftime('%Y-%m-%d')).setUntil(yesterday.strftime('%Y-%m-%d')).setMaxTweets(14)
outputFileName = "fakenews_" + yesterday.strftime('%Y-%m-%d') + ".csv"

outputFile = codecs.open(outputFileName, "w+", "utf-8")

# outputFile.write('username,date,retweets,favorites,text,geo,mentions,hashtags,id;permalink')

# print('Searching...\n')

def iter_tweets(tweets):
    for t in tweets:
        outputFile.write(('\n%s,%s,%d,%d,"%s",%s,%s,%s,"%s",%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
    outputFile.flush();
    # print('More %d saved on file...\n' % len(tweets))

tweet = got.manager.TweetManager.getTweets(tweetCriteria, iter_tweets)
"""
Using Twitter stream API, print all the tweets in the stream containing the term "#fakenews" in a 1 min period
This can be adjusted at the bottom in line "l = StdOutListener(60)"

From Exercise 2, could we use this tweepy code with StreamListener
to capture our hashtags (for a set time period)?
Need to figure out how to print stdout to a csv
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from Twittercredentials import *
from time import time,ctime
import simplejson
import sys

class StdOutListener(StreamListener):

    def __init__(self,timer):
        self.inc = 0
        StreamListener.__init__(self)
        # report the start of data collection...
        print "Gathering data at %s"%(str(ctime()))
        self.startTime = time()
        print "Start Time = %s"%(str(ctime()))
        self.timer = timer
        self.count = 0


    def on_data(self, data):
        try:
            self.endTime = time()
            self.elapsedTime = self.endTime - self.startTime
            if self.elapsedTime <= self.timer:
                self.dataJson =simplejson.loads(data[:-1])
                self.dataJsonText = self.dataJson["text"].lower()
                self.count += 1
                if "#fakenews" in self.dataJsonText:
                    print self.dataJsonText

            else:
                #csv.writer(sys.stdout)
                print "Count== ",self.count
                print "End Time = %s"%(str(ctime()))
                print "Elapsed Time = %s"%(str(self.elapsedTime))



                return False
            return True
        except Exception, e:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status):
        print ("ERROR :",status)

if __name__ == '__main__':
    # to collect the data for 1 min
    l = StdOutListener(60)
    mystream = tweepy.Stream(auth, l, timeout=60)
    mystream.sample()
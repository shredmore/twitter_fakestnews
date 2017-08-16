import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# delete the existing database
#conn = psycopg2.connect(database="tcount2", user="postgres", password="pass", host="localhost", port="5432")
# need to close the connection or connect to a different database before dropping?

# run create_tcount2 to recreate the database

# start the storm topology and run for 20 minutes to collect the most recent info
#cd extweetwordcount
#sparse run

# Run this every 20 minutes
    # use cronjob?

# Connecting to tcount2

conn = psycopg2.connect(database="tcount3", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

# error handling for empty tweetwordcount3 table
cur.execute("SELECT * from tweetwordcount3")
if cur.rowcount == 0:
    print "Please wait while we fetch #fakenews tweets"

# calculate the total number of uses of #fakenews in the past twenty minutes
print ''
print 'Data taken in the past 20 minutes from Tweets with #fakenews:'
print ''

cur.execute("SELECT count FROM tweetwordcount3 WHERE word LIKE '#fakenews'")
records = cur.fetchall()
for rec in records:
    count1 = rec[0]

print ''
print 'Total number of occurrences of #fakenews: %s' % (count1)
print ''

# calculate the total number of uses of #fakenews in the past twenty minutes
cur.execute("SELECT count FROM tweetwordcount3 WHERE word LIKE 'rt'")
records = cur.fetchall()
for rec in records:
    count2 = rec[0]

print ''
print 'Total number of retweets of #fakenews: %s' % (count2)
print ''

# print out the top 30 words in Tweets with #fakenews from the past 20 minutes

print 'Top 10 trending words:'
cur.execute("SELECT word, count from tweetwordcount3 where word not like '#%' and word not like '@%' and word not like 'rt' order by count desc limit 10")
records = cur.fetchall()
for rec in records:
    print rec[0], rec[1]
print ""

# show the top hashtags
# select word, count from tweetwordcount2 where word like '#%' and word not like '_fakenews' and word not like '_FakeNews' and word not like '_FAKENEWS' and word not like '_Fakenews'order by count desc limit 30;
print 'Top 10 trending hashtags:'
cur.execute("SELECT word, count from tweetwordcount3 WHERE word like '#%' and word not like '#fakenews' order by count desc limit 10")
records = cur.fetchall()
for rec in records:
    print rec[0], rec[1]
print ""

# show the top @mentions usernames
# select word, count from tweetwordcount2 where word like '@%' order by count desc limit 30;
print 'Top 10 trending "@mentions":'
cur.execute("SELECT word, count from tweetwordcount3 WHERE word LIKE '@%' order by count desc limit 10")
records = cur.fetchall()
for rec in records:
    print rec[0], rec[1]
print ""

conn.close()


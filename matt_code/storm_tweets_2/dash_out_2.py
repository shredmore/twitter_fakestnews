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

conn = psycopg2.connect(database="tcount2", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

# do I need to get the cursor to point to tweetwordcount2 first before it knows
# to look in the single table in the database?

# error handling for empty tweetwordcount2 table
cur.execute("SELECT * from tweetwordcount2")
if cur.rowcount == 0:
    print "Please wait while we fetch #fakenews tweets"

# calculate the total number of uses of #fakenews in the past twenty minutes

cur.execute("SELECT count FROM tweetwordcount2 WHERE word LIKE '_fakenews'")
records = cur.fetchall()
for rec in records:
    count1 = rec[0]

cur.execute("SELECT count FROM tweetwordcount2 WHERE word LIKE '_Fakenews'")
records = cur.fetchall()
for rec in records:
    count2 = rec[0]

cur.execute("SELECT count FROM tweetwordcount2 WHERE word LIKE '_FakeNews'")
records = cur.fetchall()
for rec in records:
    count3 = rec[0]

cur.execute("SELECT count FROM tweetwordcount2 WHERE word LIKE '_FAKENEWS'")
records = cur.fetchall()
for rec in records:
    count4 = rec[0]

fakenews = count1 + count2 + count3 + count4
print ''
print 'Total number of occurrences of #fakenews in past 20 minutes: %s' % (fakenews)
print ''
# print out the top 30 words in Tweets with #fakenews from the past 20 minutes

print 'Data taken in the past 20 minutes from Tweets with #fakenews: /n'
print 'Top 20 trending words:'
cur.execute("SELECT word, count from tweetwordcount2 where length(word) > 4 and word not like '#%' and word not like '@%'order by count desc limit 20")
records = cur.fetchall()
for rec in records:
    print rec[0], rec[1]
print ""

# show the top hashtags
# select word, count from tweetwordcount2 where word like '#%' and word not like '_fakenews' and word not like '_FakeNews' and word not like '_FAKENEWS' and word not like '_Fakenews'order by count desc limit 30;
print 'Top 20 trending hashtags:'
cur.execute("SELECT word, count from tweetwordcount2 WHERE word like '#%' and word not like '_fakenews' and word not like '_FakeNews' and word not like '_FAKENEWS' and word not like '_Fakenews' order by count desc limit 20")
records = cur.fetchall()
for rec in records:
    print rec[0], rec[1]
print ""

# show the top @mentions usernames
# select word, count from tweetwordcount2 where word like '@%' order by count desc limit 30;
print 'Top 20 trending "@mentions":'
cur.execute("SELECT word, count from tweetwordcount2 WHERE word LIKE '@%' order by count desc limit 20")
records = cur.fetchall()
for rec in records:
    print rec[0], rec[1]
print ""

conn.close()


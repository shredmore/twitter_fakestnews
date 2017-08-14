# passing an argument to python in the command line and noting success

import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

if len(sys.argv) != 2:
    print "word argument missing"
    exit(1)

word = sys.argv[1]

print "word is", word

# connect to database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()

# update count
cur.execute("UPDATE tweetwordcount SET count=count+1 WHERE word=%s", (word,))

# cur.rowcount is a built in
print "number of updated rows", cur.rowcount

# insert
if cur.rowcount == 0:
    cur.execute("INSERT INTO tweetwordcount (word, count) VALUES (%s, 1)", (word,))

conn.commit()

# select
cur.execute("SELECT word, count from tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"

# save
conn.commit()

# close
conn.close()

# create tcount3 database and tweetwordcount3 table


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to the postgres database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the tcount3 Database

try:
    # CREATE DATABASE can't run inside a transaction
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount3")
    cur.close()
    conn.close()
except:
    print "Could not create tcount3"

#Connecting to tcount3

conn = psycopg2.connect(database="tcount3", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount3
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()

#needed?
conn.close()

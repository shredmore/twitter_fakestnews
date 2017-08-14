# create tcount2 database and tweetwordcount2 table


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Create the database Tcount
# Q: Do I need a destructor of any previous copy of Tcount on postgres?

# Connect to the database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Tcount Database

try:
    # CREATE DATABASE can't run inside a transaction
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount2")
    cur.close()
    conn.close()
except:
    print "Could not create tcount2"

#Connecting to Tcount

conn = psycopg2.connect(database="tcount2", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount2
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()

#needed?
conn.close()

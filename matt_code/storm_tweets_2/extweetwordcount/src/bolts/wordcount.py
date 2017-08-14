from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        # connect to database
        self.conn = psycopg2.connect(database="tcount2", user="postgres", password="pass", host="localhost", port="5432")

    def process(self, tup):
        word = tup.values[0]
        # grab cursor
        cur = self.conn.cursor()
        # update count
        cur.execute("UPDATE tweetwordcount2 SET count=count+1 WHERE word=%s", (word,))
        # insert
        if cur.rowcount == 0:
            cur.execute("INSERT INTO tweetwordcount2 (word, count) VALUES (%s, 1)", (word,))
        # commit
        self.conn.commit()

# close not recommended in a bolt, as it will close the program which needs to continually update
#conn.close()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        # self.log('%s: %d' % (word, self.counts[word]))
        self.log('%s: %d' % (word, self.counts[word]))


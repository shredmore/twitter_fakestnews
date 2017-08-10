# Reading in data

from datetime import datetime

headlines = sc.textFile("/user/w205/project1/headlines/headlines.csv").map(lambda line:  (datetime.strptime(line.split(",")[0], '%Y-%m-%d %H:%M:%S'), line.split(",")[1], line.split(",")[2], line.split(",")[3]  ) )

#--------------------------------------------------------------
import re

def get_stopwords(file_path):
    f = open(file_path, 'r').read()
    words = f.split()
    return words

stopwords = get_stopwords('/home/w205/twitter_fakestnews/legg_code/stopwords.txt')

#--------------------------------------------------------------
# Constructing tf-idf

from pyspark.mllib.feature import IDF
from pyspark.mllib.linalg import DenseVector
from pyspark.mllib.linalg import Vectors
from collections import Counter


headline_documents = headlines.map(lambda line: line[2])

# each news agency as one corpous (001 - 004)
headline_documents_news001 = headlines.filter(lambda line: line[1] == '001').map(lambda line: line[2])

# 1 row = 1 list of words
documents_raw = headline_documents_news001.map(lambda line: line.split(" "))

# stop words removed
documents = documents_raw.map(lambda words: [word.lower() for word in words if word.lower() not in stopwords])

# construct word list and index
unique_words = documents.reduce(lambda x, y: set(x) | set(y))
words_with_index = list(enumerate(unique_words))
WordList = [tup[1] for tup in words_with_index]

# convert to counter object
documents_word_counter = documents.map(lambda words: sorted(Counter([WordList.index(word) for word in words if word in WordList]).items(), key = lambda pair: pair[0], reverse = False)    ) 
documents_word_counter.take(2)

# convert to sparse vector
documents_sparse_vectors = documents_word_counter.map(lambda counter:  Vectors.sparse(len(WordList), tuple([pair[0] for pair in counter]), tuple([pair[1] for pair in counter])  )  )
documents_sparse_vectors.take(2)

idf = IDF()
model = idf.fit(documents_sparse_vectors)
tfidf = model.transform(documents_sparse_vectors)

#--------------------------------------------------------------
# Build LDA model

from pyspark.mllib.linalg import Vectors
from pyspark.mllib.clustering import LDA

tfidf_3 = tfidf.zipWithIndex().map(lambda (row,index): list((index,row)))

n_topics = 5
lda_model = LDA.train(tfidf_3, k = n_topics)
# classmethod train(rdd, k=10, maxIterations=20, docConcentration=-1.0, topicConcentration=-1.0, seed=None, checkpointInterval=10, optimizer='em')
lda_model.vocabSize()

# get topics distribution for every word
# probability of word w occurring in topic k
matrix_by_words = lda_model.topicsMatrix()

matrix_by_topics = [[word[topic] for word in matrix_by_words] for topic in range(n_topics)]
# get top 15 words for each topic
wordindex_by_topic = [sorted(list(enumerate(topic)), key = lambda x: x[1], reverse = True)[0:15] for topic in matrix_by_topics]

topwords_by_topic = [[WordList[wordpair[0]] for wordpair in topic] for topic in wordindex_by_topic]

for i in range(n_topics):
	print
	print topwords_by_topic[i]

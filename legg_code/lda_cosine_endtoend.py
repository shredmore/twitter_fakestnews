# define collection of document
from datetime import datetime, date, timedelta

# load headline file for csv on hdfs
# choose by date time range
# parse to give only documents --> RDD of one headline per row

def load_headlines_from_csv(headlines_hdfspath, date_range1 = datetime.now() - timedelta(days=1), date_range2 = datetime.now(), news_agency = ["001", "002", "003", "004"]):
	# all headlines
	headlines =  sc.textFile(headlines_hdfspath).map(lambda line:  (datetime.strptime(line.split(",")[0], '%Y-%m-%d %H:%M:%S'), line.split(",")[1].encode("utf-8"), line.split(",")[2].encode("utf-8"), line.split(",")[3].encode("utf-8") ) )
	## filter/join by agencies and dates
	# filter by dates
	headlines = headlines.filter(lambda line : date_range1 < line[0] and line[0] < date_range2)
	# filter by agency
	headlines = headlines.filter(lambda line: line[1] in news_agency)
	# get documents
	headlines = headlines.map(lambda line: line[2])
	return headlines



def load_tweets_from_csv(tweets_hdfsdir_path, date_range1 = datetime.now() - timedelta(days=1), date_range2 = datetime.now()):
	# construct path pattern
	dir_path = tweets_hdfsdir_path
	csv_path_pattern = "tweets_2017-*.csv"
	# all raw tweets
	tweets = sc.textFile(dir_path + csv_path_pattern)
	# all tweets
	# 0 datetime, 1 tweet_id, 2 username, 3 user_id, 4 tweet, lang, source, long, lat
	tweets =  tweets.map(lambda line:  str(line.encode('utf-8')) )
	tweets =  tweets.map(try_convert)
	# filter by dates
	tweets = tweets.filter(lambda line : line != [] )
	tweets = tweets.filter(lambda line : line[0] < date_range2 )
	tweets = tweets.filter(lambda line : date_range1 < line[0] )
	# get documents
	tweets = tweets.map(lambda line: line[2])
	return tweets


def try_convert(line):
	try:
		tup = (datetime.strptime(line.split(",")[0], '%a %b %d %H:%M:%S +0000 %Y'), line.split(",")[3], line.split(",")[4])
		return tup
	except:
		return []
#-----------------------------
# reformat Document


import chardet

#x = chardet.detect('trumpers\xe2\x80\xa6')['encoding']

def try_ascii(line):
	newline = []
	for word in line:
		if chardet.detect(word)['encoding'] == 'ascii':
			newline.append(word)
		else:
			continue
	return newline

# documents : 1 row = 1 line of words e.g. "Trump and Putin in Russia"
def clean_documents(documents, stopwords):
	# split into words e.g. ["Trump", "and", "Putin", "in", "Russia"]
	documents = documents.map(lambda line: line.split(" "))
	# documents = documents.map(lambda line: [item for value in line for item in literal_eval(value)])
	# stop words and signs removed
	documents = documents.map(lambda words: [word.strip("\"?><,'.:;-)~!*|$&(0123456789^%@").lower() for word in words if word.strip("\"?><,'.:;-)~!*|$&(0123456789^%@").lower() not in stopwords])
	# basic
	documents = documents.map(try_ascii)
	return documents


#-----------------------------
# stop words
import re

def get_stopwords(file_path):
    f = open(file_path, 'r').read()
    words = f.split()
    return words


#-----------------------------
# construct tf-idf.
from pyspark.mllib.feature import IDF
from pyspark.mllib.linalg import DenseVector
from pyspark.mllib.linalg import Vectors
from collections import Counter

# documents : 1 row = 1 line of split words e.g. ["Trump", "Putin", "Russia"]
def const_unique_word_list(documents):
	unique_words = documents.reduce(lambda x, y: set(x) | set(y))
	words_with_index = list(enumerate(unique_words))
	WordList = [tup[1] for tup in words_with_index]
	return WordList

# documents : 1 row = 1 line of split words e.g. ["Trump", "Putin", "Russia"]
def get_sparse_vectors(documents):
	# get unique word list
	WordList = const_unique_word_list(documents)
	# convert to counter object
	documents_word_counter = documents.map(lambda words: sorted(Counter([WordList.index(word) for word in words if word in WordList]).items(), key = lambda pair: pair[0], reverse = False)    ) 
	# convert to sparse vector
	documents_sparse_vectors = documents_word_counter.map(lambda counter:  Vectors.sparse(len(WordList), tuple([pair[0] for pair in counter]), tuple([pair[1] for pair in counter])))
	return documents_sparse_vectors

# documents : 1 row = 1 line of split words e.g. ["Trump", "Putin", "Russia"]
def get_tfidf(documents):
	documents_sparse_vectors = get_sparse_vectors(documents)
	idf = IDF()
	model = idf.fit(documents_sparse_vectors)
	tfidf = model.transform(documents_sparse_vectors)
	return tfidf




#-----------------------------
# build LDA

from pyspark.mllib.linalg import Vectors
from pyspark.mllib.clustering import LDA

# get LDA model
def train_lda_matrix(tfidf, n_topics):
	tfidf_indexed = tfidf.zipWithIndex().map(lambda (row,index): list((index,row))) 
	# classmethod train(rdd, k=10, maxIterations=20, docConcentration=-1.0, topicConcentration=-1.0, seed=None, checkpointInterval=10, optimizer='em')
	lda_model = LDA.train(tfidf_indexed, k = n_topics)
	return lda_model


# n_terms: how many top terms per topic to output?
# output : list of n_topic lists each of n_terms top terms
def get_topics(lda_model, n_terms, documents):
	WordList = const_unique_word_list(documents)
	matrix_by_words = lda_model.topicsMatrix()
	matrix_by_topics = [[word[topic] for word in matrix_by_words] for topic in range(n_topics)]
	wordindex_by_topic = [sorted(list(enumerate(topic)), key = lambda x: x[1], reverse = True)[0:n_terms] for topic in matrix_by_topics]
	topwords_by_topic = [[WordList[wordpair[0]] for wordpair in topic] for topic in wordindex_by_topic]
	return topwords_by_topic


def display_topics(topwords_by_topic, n_topics):
	for i in range(n_topics):
		print
		print topwords_by_topic[i]

#-----------------------------
# build pipeline for headlines LDA

def pipeline_headlines(headlines_hdfspath, stopwords_txt_path, n_topics, n_terms, date_range1 = datetime.now() - timedelta(days=1), date_range2 = datetime.now(), news_agency = ["001", "002", "003", "004"]):
	raw_documents = load_headlines_from_csv(headlines_hdfspath, date_range1, date_range2, news_agency)
	stopwords = get_stopwords(stopwords_txt_path)
	tokenized_documents = clean_documents( raw_documents, stopwords)
	#raw_documents = 0 # clean up
	tfidf = get_tfidf(tokenized_documents)
	#tokenized_documents = 0 # clean up
	lda_model = train_lda_matrix(tfidf, n_topics)
	#tfidf = 0 # clean up
	topics = get_topics(lda_model, n_terms, tokenized_documents)
	display_topics(topics, n_topics)
	return (lda_model, topics)


#-----------------------------
# build pipeline for tweets LDA


def pipeline_tweets(tweets_hdfsdir_path, stopwords_txt_path, n_topics, n_terms, date_range1 = datetime.now() - timedelta(days=1), date_range2 = datetime.now()):
	raw_documents = load_tweets_from_csv(tweets_hdfsdir_path, date_range1, date_range2)
	stopwords = get_stopwords(stopwords_txt_path)
	tokenized_documents = clean_documents( raw_documents, stopwords)
	#raw_documents = 0 # clean up
	tfidf = get_tfidf(tokenized_documents)
	#tokenized_documents = 0 # clean up
	lda_model = train_lda_matrix(tfidf, n_topics)
	#tfidf = 0 # clean up
	topics = get_topics(lda_model, n_terms, tokenized_documents)
	display_topics(topics, n_topics)
	return (lda_model, topics)

#-----------------------------
# build pipeline for cosine similarity


from math import *
 
def square_rooted(x):
	return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
	numerator = sum(a*b for a,b in zip(x,y))
	denominator = square_rooted(x)*square_rooted(y)
	return round(numerator/float(denominator),3)

def counter_to_vec2(counter):
	j = 0
	vec = []
	for i in range(270):
		if i == counter[j][0]:
			j += 1
			vec.append(counter[j][1])
		else:
			vec.append(0)
	return vec

def pipeline_cosine_similarity(headlines_hdfspath, tweets_hdfsdir_path, stopwords_txt_path, n_topics, n_terms, date_range1 = datetime.now() - timedelta(days=1), date_range2 = datetime.now(), news_agency = ["001", "002", "003", "004"]):
	# get list of topics [[topicword1, topic1word2, topic1word3],[],[]]
	headlines_topics = pipeline_headlines(headlines_hdfspath, stopwords_txt_path, n_topics, n_terms, date_range1, date_range2, news_agency)[1] # headline topics
	tweets_topics = pipeline_tweets(tweets_hdfsdir_path, stopwords_txt_path, n_topics, n_terms, date_range1, date_range2)[1] # tweets topics
	# construct unique word list
	headlines_words = [word for topic in headlines_topics for word in topic]
	tweets_words = [word for topic in tweets_topics for word in topic]
	unique_words = list(set().union(headlines_words,tweets_words))
	# construct counters
	to_counter = lambda words: sorted(Counter([unique_words.index(word) for word in words if word in unique_words]).items(), key = lambda pair: pair[0], reverse = False)
	headlines_words = to_counter(headlines_words)
	tweets_words = to_counter(tweets_words)
	# construct vectors
	counter_to_vec = lambda counter: [pair[1] for pair in counter]
	headlines_words = counter_to_vec(headlines_words)
	tweets_words = counter_to_vec2(tweets_words)
	# compute similarity
	cos_sim = cosine_similarity(headlines_words, tweets_words)
	return(headlines_topics, tweets_topics, cos_sim)


#-----------------------------
# Usage

headlines_hdfspath = "/user/w205/project1/headlines/headlines.csv"
tweets_hdfsdir_path = "/user/w205/project1/tweets_2/"
stopwords_txt_path = '/home/w205/twitter_fakestnews/legg_code/stopwords.txt'
n_topics = 8
n_terms = 20
date_range2 = datetime.now()
date_range1 = date_range2 - timedelta(days=1)
news_agency = ["001", "002", "003", "004"]


LDA_headlines = pipeline_headlines(headlines_hdfspath, stopwords_txt_path, n_topics, n_terms, date_range1, date_range2, news_agency)
LDA_headlines

LDA_tweets = pipeline_tweets(tweets_hdfsdir_path, stopwords_txt_path, n_topics, n_terms, date_range1, date_range2)
LDA_tweets


headlines_topics, tweets_topics, cos_sim = pipeline_cosine_similarity(headlines_hdfspath, tweets_hdfsdir_path, stopwords_txt_path, n_topics, n_terms, date_range1 = datetime.now() - timedelta(days=1), date_range2 = datetime.now(), news_agency = ["001", "002", "003", "004"])


import sys
from time import sleep
import argparse
from datetime import datetime, date, timedelta
import pyspark_lda_pipeline as lp
from pyspark import SparkContext

sc = SparkContext("local[2]")

headlines_hdfspath = "/user/w205/project1/headlines/headlines.csv"
tweets_hdfsdir_path = "/user/w205/project1/tweets_2/"
stopwords_txt_path = '/home/w205/twitter_fakestnews/legg_code/stopwords.txt'
# wordcloud_hdfspath = "/home/w205/lda_outputs/lda_wordcloud/lda_wordcloud.csv"
cos_sim_hdfspath = "/home/w205/lda_outputs/lda_cossim/lda_cossim.csv"
# topics_hdfspath = "/home/w205/lda_outputs/lda_topics/lda_topics.csv"

def main(args):
	# get date range from arguments
	if args.dr2:
		try:
			date_range2 = datetime.strptime(args.dr2, '%Y-%m-%d')
		except:
			print "Incorrect date format"
			sys.exit(1)
	else:
		date_range2 = date.today()

	if args.dr1:
		try:
			date_range1 = datetime.strptime(args.dr1, '%Y-%m-%d')
		except:
			print "Incorrect date format"
			sys.exit(1)
	else:
		date_range1 = date_range2 - timedelta(days=1)
	# check if daterange is correct
	if date_range2 < date_range1 or (date_range2 - date_range1) < timedelta(days=1):
		print "Incorrect date range"
		sys.exit(1)
	print "start date :",date_range2.strftime('%Y-%m-%d')
	print "end date :",date_range1.strftime('%Y-%m-%d')
	print
	# get news agency
	if args.nwag:
		if args.nwag == "001":
			news_agency = ["001"]
			wordcloud_hdfspath = "/home/w205/lda_outputs/lda_wordcloud/lda_wordcloud001.csv"
			topics_hdfspath = "/home/w205/lda_outputs/lda_topics/lda_topics001.csv"			
		elif args.nwag == "002":
			news_agency = ["002"]
			wordcloud_hdfspath = "/home/w205/lda_outputs/lda_wordcloud/lda_wordcloud002.csv"
			topics_hdfspath = "/home/w205/lda_outputs/lda_topics/lda_topics002.csv"
		elif args.nwag == "003":
			news_agency = ["003"]
			wordcloud_hdfspath = "/home/w205/lda_outputs/lda_wordcloud/lda_wordcloud003.csv"
			topics_hdfspath = "/home/w205/lda_outputs/lda_topics/lda_topics003.csv"
		elif args.nwag == "004":
			news_agency = ["004"]
			wordcloud_hdfspath = "/home/w205/lda_outputs/lda_wordcloud/lda_wordcloud004.csv"
			topics_hdfspath = "/home/w205/lda_outputs/lda_topics/lda_topics004.csv"
		elif args.nwag == "005":
			news_agency = ["001", "002", "003", "004"]
			wordcloud_hdfspath = "/home/w205/lda_outputs/lda_wordcloud/lda_wordcloud.csv"
			topics_hdfspath = "/home/w205/lda_outputs/lda_topics/lda_topics.csv"
		else:
			print "Incorrect news agency specification"
			sys.exit(1)
	else:
		news_agency = ["001", "002", "003", "004"]
	print "news agencies :", news_agency
	print
	# Get number of topics
	if args.nTp:
		if args.nTp < 5 or args.nTp > 15:
			print "Incorrect specification for number of terms."
			sys.exit(1)
		else:
			n_topics = args.nTp
	# Get number of terms
	if args.nTm:
		if args.nTm < 10 or args.nTm > 30:
			print "Incorrect specification for number of terms."
			sys.exit(1)
		else:
			n_terms = args.nTm		
	print "number of topics per corpus :", n_topics
	print "number of terms per topic :", n_terms
	print
	print "------------------------------------------------------------"
	print "Starting Machine Learning Pipeline..."
	print
	print
	# train model
	headlines_topics, tweets_topics, cos_sim = lp.pipeline_cosine_similarity(sc, headlines_hdfspath, tweets_hdfsdir_path, stopwords_txt_path, n_topics, n_terms, date_range1, date_range2, news_agency)
	# write to file
	print
	print "writing results to HDFS in 10 seconds, ctrl-c to stop"
	sleep(10)
	lp.write_to_HDFS(headlines_topics, tweets_topics, cos_sim, wordcloud_hdfspath, cos_sim_hdfspath, topics_hdfspath, date_range2, news_agency)



if __name__ == "__main__":

	parser = argparse.ArgumentParser(description = "Infer topics and calculate similarities between headlines and tweets", prefix_chars = "-")
	parser.add_argument("-dr2", type=str, help = "end date in yyyy-mm-dd format")
	parser.add_argument("-dr1", type=str, help = "start date in yyyy-mm-dd format")
	parser.add_argument("-nTp", type=int, default = 8, help = "number of topics specified in topics model 5<n<15")
	parser.add_argument("-nTm", type=int, default = 15, help = "number of terms per topic specified in topics model 10<n<30")
	parser.add_argument("-nwag", type = str, help = "001 PBS \n 002 NYT \n 003 FOX \n 004 CNN \n 005 all")
	args = parser.parse_args()

	main(args)

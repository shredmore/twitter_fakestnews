#! /bin/bash

# local to data setup

mkdir /data/lda_outputs/
mkdir /data/lda_outputs/lda_wordcloud
mkdir /data/lda_outputs/lda_cossim
mkdir /data/lda_outputs/lda_topics

cp /home/w205/lda_outputs/lda_wordcloud/lda_wordcloud.csv /data/lda_outputs/lda_wordcloud/lda_wordcloud.csv
cp /home/w205/lda_outputs/lda_cossim/lda_cossim.csv /data/lda_outputs/lda_cossim/lda_cossim.csv
cp /home/w205/lda_outputs/lda_topics/lda_topics.csv /data/lda_outputs/lda_topics/lda_topics.csv

# HDFS setup

# write code to move from local to HDFS
sudo -u hdfs hadoop fs -rm /user/w205/project1/lda_output/lda_wordcloud/lda_wordcloud.csv
sudo -u hdfs hadoop fs -rm /user/w205/project1/lda_output/lda_cossim/lda_cossim.csv
sudo -u hdfs hadoop fs -rm /user/w205/project1/lda_output/lda_topics/lda_topics.csv

cd /home/w205/lda_outputs/lda_wordcloud/

sudo -u hdfs hadoop fs -put /data/lda_outputs/lda_wordcloud/lda_wordcloud.csv /user/w205/project1/lda_output/lda_wordcloud
sudo -u hdfs hadoop fs -put /data/lda_outputs/lda_cossim/lda_cossim.csv /user/w205/project1/lda_output/lda_cossim
sudo -u hdfs hadoop fs -put /data/lda_outputs/lda_topics/lda_topics.csv /user/w205/project1/lda_output/lda_topics


hdfs dfs -ls /user/w205/project1/lda_output/lda_wordcloud
hdfs dfs -ls /user/w205/project1/lda_output/lda_cossim
hdfs dfs -ls /user/w205/project1/lda_output/lda_topics




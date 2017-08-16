#! /bin/bash

psql -U postgres -d tcount3 -c "Copy (SELECT * FROM tweetwordcount3) To STDOUT With CSV HEADER DELIMITER ',';" > "/home/w205/twitter_fakestnews/matt_code/storm_tweets_3/sample_output/data_sample_$(date +%Y%m%d).csv"

psql -U postgres -d tcount3 -c "DELETE FROM tweetwordcount3;"

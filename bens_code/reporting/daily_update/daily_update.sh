#!/bin/bash
(echo "yesterday's headlines collected by news site"\
	;hive -f yesterday_headline_count.sql\
	;echo "number of tweets collected yesterday"\
	;hive -f yesterday_tweet_count.sql\
	;echo "top #fakenews users and times used"\
	;hive -f top_fakenews_users.sql) | mail -s "report1" ben.thompson.j@gmail.com
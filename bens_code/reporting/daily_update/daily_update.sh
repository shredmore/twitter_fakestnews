#!/bin/bash
(echo "yesterday's headlines collected by news site" \n\
	hive -f yesterday_headline_count.sql \n\
	echo "number of tweets collected yesterday" \n\
	;hive -f yesterday_tweet_count.sql \n\
	echo "top #fakenews users and times used" \n\
	;hive -f top_fakenews_users.sql) | mail -s "report1" ben.thompson.j@gmail.com
DROP TABLE IF EXISTS tweets_2_distinct;
CREATE TABLE tweets_2_distinct AS
created_at
,tweet_id
,username
,user_id
,tweet
,lang
,source
,long
,lat
FROM tweets_2;
--get number of tweets collected yesterday
SELECT from_unixtime(unix_timestamp(a.created_at, 'EEE MMM dd HH:mm:ss +SSSS yyyy'),'yyyy-MM-dd') the_date
,COUNT(*) tweets
FROM tweets_2_distinct a
GROUP BY from_unixtime(unix_timestamp(a.created_at, 'EEE MMM dd HH:mm:ss +SSSS yyyy'),'yyyy-MM-dd')
ORDER BY the_date DESC;
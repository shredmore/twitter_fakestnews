--get number of tweets collected yesterday
SELECT to_date(date_time) the_date
,COUNT(*) tweets
FROM tweets
WHERE to_date(date_time) = date_sub(current_date(),1)
GROUP BY to_date(date_time);
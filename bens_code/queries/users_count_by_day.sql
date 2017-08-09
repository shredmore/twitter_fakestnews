SELECT CONCAT(SUBSTRING(created_at,5,7),SUBSTRING(created_at,27,4)) year_month_day
,username
,MAX(followers_count) followers
,COUNT(*) counts
FROM tweets_2_distinct a
JOIN users_distinct b
ON a.user_id = b.user_id
GROUP BY CONCAT(SUBSTRING(created_at,5,7),SUBSTRING(created_at,27,4)), username;
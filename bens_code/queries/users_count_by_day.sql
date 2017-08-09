SELECT CONCAT(SUBSTRING(a.created_at,5,7),SUBSTRING(a.created_at,27,4)) year_month_day
,a.username
,b.followers
,COUNT(*) counts
FROM tweets_2_distinct a
JOIN 
(SELECT user_id
,username
,MAX(followers_count) followers
FROM users_distinct
GROUP BY user_id, username) users_distinct b
ON a.user_id = b.user_id
GROUP BY CONCAT(SUBSTRING(a.created_at,5,7),SUBSTRING(a.created_at,27,4)), a.username;
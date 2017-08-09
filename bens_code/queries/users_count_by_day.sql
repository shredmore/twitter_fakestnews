SELECT CONCAT(SUBSTRING(created_at,5,7),SUBSTRING(created_at,27,4)) year_month_day, username, COUNT(*) counts
FROM tweets_2_distinct
GROUP BY CONCAT(SUBSTRING(created_at,5,7),SUBSTRING(created_at,27,4)), username;
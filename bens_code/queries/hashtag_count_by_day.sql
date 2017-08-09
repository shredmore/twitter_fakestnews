SELECT CONCAT(SUBSTRING(created_at,5,7),SUBSTRING(created_at,27,4)) year_month_day, hashtag, COUNT(*) counts
FROM hashtags_distinct
GROUP BY CONCAT(SUBSTRING(created_at,5,7),SUBSTRING(created_at,27,4)), hashtag;
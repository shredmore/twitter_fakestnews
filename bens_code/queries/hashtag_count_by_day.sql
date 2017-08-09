SELECT to_date(created_at) year_month_day, hashtag, COUNT(*) counts
FROM hashtags_distinct
GROUP BY to_date(created_at), hashtag;
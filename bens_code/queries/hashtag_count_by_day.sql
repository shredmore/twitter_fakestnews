SELECT to_date(date_time) year_month_day, hashtag, COUNT(*) counts
FROM hashtags_distinct
GROUP BY to_date(date_time), hashtag;
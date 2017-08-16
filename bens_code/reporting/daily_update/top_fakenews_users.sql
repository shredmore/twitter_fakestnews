--top fake news tweeters to date
SELECT username
,COUNT(*) appearances
FROM tweets_2_distinct
GROUP BY username
ORDER BY appearances DESC
LIMIT 5;
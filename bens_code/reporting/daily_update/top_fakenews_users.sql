--top fake news tweeters to date
SELECT username
,COUNT(*) appearances
FROM tweets_distinct_2
GROUP BY username
ORDER BY appearances DESC
LIMIT 5;
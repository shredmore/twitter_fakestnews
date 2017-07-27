--top fake news tweeters to date
SELECT username
,COUNT(*) appearances
FROM tweets
GROUP BY username
ORDER BY appearances DESC
LIMIT 5;
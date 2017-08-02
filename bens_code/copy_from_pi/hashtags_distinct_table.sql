DROP TABLE IF EXISTS hashtags_distinct;
CREATE TABLE hashtags_distinct AS
SELECT DISTINCT created_at, tweet_id, hashtag_type, hashtag
FROM hashtags;
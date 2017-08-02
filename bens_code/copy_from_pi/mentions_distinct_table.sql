DROP TABLE IF EXISTS mentions_distinct;
CREATE TABLE mentions_distinct AS
SELECT DISTINCT created_at
,tweet_id string
,mentioned_user_id
,mentioned_user_name
,mentioned_user_screen_name
FROM mentions;
DROP TABLE IF EXISTS urls_distinct;
CREATE TABLE urls_distinct AS
SELECT DISTINCT created_at
,tweet_id
,url_type
,url
FROM urls;
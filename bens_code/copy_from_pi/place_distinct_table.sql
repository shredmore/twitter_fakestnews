DROP TABLE IF EXISTS places_distinct;
CREATE TABLE places_distinct AS
SELECT DISTINCT created_at
,tweet_id
,country
,country_code
,full_name
,place_id
,place_name
,place_type
,twitter_place_url
FROM places;
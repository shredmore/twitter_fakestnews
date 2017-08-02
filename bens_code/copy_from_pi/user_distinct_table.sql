DROP TABLE IF EXISTS users_distinct;
CREATE TABLE users_distinct AS
SELECT DISTINCT created_at
,user_id
,username
,screen_name
,is_verified
,description
,url
,location
,timezone
,statuses_count
,followers_count
,friends_count
,listed_count
,geo_enabled
,lang
,favourites_count
,default_profile_image
,withheld_in_countries
,withhel_scope
FROM users;
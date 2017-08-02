DROP TABLE IF EXISTS users;
CREATE EXTERNAL TABLE users (
	created_at date
	,user_id string
	,username string
	,screen_name string
	,is_verified string
	,description string
	,url string
	,location string
	,timezone string
	,statuses_count int
	,followers_count int
	,friends_count int
	,listed_count int
	,geo_enabled string
	,lang string
	,favourites_count int
	,default_profile_image string
	,withheld_in_countries string
	,withhel_scope string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/users'
TBLPROPERTIES('serialization.null.format'='');
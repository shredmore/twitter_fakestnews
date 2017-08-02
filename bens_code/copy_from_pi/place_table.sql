DROP TABLE IF EXISTS places;
CREATE EXTERNAL TABLE places (
	created_at date
	,tweet_id string
	,country string
	,country_code string
	,full_name string
	,place_id string
	,place_name string
	,place_type string
	,twitter_place_url string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/places'
TBLPROPERTIES('serialization.null.format'='');
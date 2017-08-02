DROP TABLE IF EXISTS hashtags;
CREATE EXTERNAL TABLE hashtags (
	created_at date
	,tweet_id string
	,hashtag_type string
	,hashtag string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/hashtags'
TBLPROPERTIES('serialization.null.format'='');
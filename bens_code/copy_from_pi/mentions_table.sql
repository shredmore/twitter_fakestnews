DROP TABLE IF EXISTS mentions;
CREATE EXTERNAL TABLE mentions (
	created_at date
	,tweet_id string
	,mentioned_user_id string
	,mentioned_user_name string
	,mentioned_user_screen_name string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/mentions'
TBLPROPERTIES('serialization.null.format'='');
DROP TABLE IF EXISTS tweets_2;
CREATE EXTERNAL TABLE tweets_2 (
	created_at date
	,tweet_id string
	,username string
	,user_id string
	,tweet string
	,lang string
	,source string
	,long string
	,lat string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/tweets_2'
TBLPROPERTIES('serialization.null.format'='');
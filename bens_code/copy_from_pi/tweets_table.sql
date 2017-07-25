DROP TABLE IF EXISTS headlines;
CREATE EXTERNAL TABLE tweets (
	username string
	,date_time date
	,retweets int
	,favorites int
	,tweet string
	,geo string
	,mentions string
	,hastags string
	,id string
	permalink string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/tweets';
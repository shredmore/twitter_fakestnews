DROP TABLE IF EXISTS urls;
CREATE EXTERNAL TABLE urls (
	created_at date
	,tweet_id string
	,url_type string
	,url string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/urls'
TBLPROPERTIES('serialization.null.format'='');
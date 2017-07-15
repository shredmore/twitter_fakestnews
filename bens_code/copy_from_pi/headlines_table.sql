DROP TABLE IF EXISTS headlines;
CREATE EXTERNAL TABLE headlines (
	date_time date
	,site_code string
	,headline string
	,headline_id string
	)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES (
"separatorChar" = ",", "quoteChar" = '"', "escapeChar" = '\\' )
STORED AS TEXTFILE
LOCATION '/user/w205/project1/headlines';
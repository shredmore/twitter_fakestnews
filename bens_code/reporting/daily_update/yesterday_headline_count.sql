--get number of headlines collected by site for yesterday
SELECT to_date(date_time) the_date
,site_code
,COUNT(*)
FROM headlines a
WHERE to_date(a.date_time) IN (SELECT MAX(to_date(date_time)) FROM headlines)
GROUP BY to_date(date_time), site_code;
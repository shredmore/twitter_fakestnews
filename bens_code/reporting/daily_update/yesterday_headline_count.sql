--get number of headlines collected by site for yesterday
SELECT to_date(date_time) the_date
,site_code
,COUNT(*)
FROM headlines
WHERE to_date(date_time) = date_sub(current_date(),1)
GROUP BY to_date(date_time), site_code;
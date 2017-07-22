--how many rows
SELECT COUNT(*) FROM headlines;
--2063

--how many rows per news source
SELECT site_code, COUNT(*) FROM headlines GROUP BY site_code;
-- 001	94
-- 002	1760
-- 003	209

--check date range
--min:2017-07-07 21:51:05
--MAX:2017-07-14 19:01:14
SELECT MAX(date_time) FROM headlines;

--check records per day and
--bring any non-dates to surface
SELECT to_date(date_time), COUNT(*) FROM headlines GROUP BY to_date(date_time);
-- 2017-07-07	129
-- 2017-07-08	247
-- 2017-07-09	256
-- 2017-07-10	256
-- 2017-07-11	264
-- 2017-07-12	401
-- 2017-07-13	263
-- 2017-07-14	247
--I wonder why double on 7/12. Might of been the day I ran an extra time

--see how many distinct headlines
SELECT COUNT(*) FROM
(SELECT headline, site_code, MIN(date_time) FROM headlines GROUP BY headline, site_code) a;
--1076

--how long do some headlnes run?
SELECT headline, site_code, first_appeared, last_appeared, (unix_timestamp(last_appeared) - unix_timestamp(first_appeared)) / 3600 duration
FROM
(SELECT headline, site_code, MIN(date_time) first_appeared, MAX(date_time) last_appeared
FROM headlines
GROUP BY headline, site_code) a
ORDER BY duration DESC
LIMIT 100;

--how many headlines mentione trump and obama
SELECT * FROM headlines WHERE headline LIKE '%Trump%Obama%' OR headline LIKE '%Obama%Trump%';

--what percent of headlines contain trump
SELECT y.site_code, y.trump_hl / z.all_hl
FROM
(SELECT site_code, COUNT(*) trump_hl FROM
(SELECT headline, site_code, MIN(date_time) FROM headlines GROUP BY headline, site_code) a
WHERE headline LIKE '%Trump%'
GROUP BY site_code) y
JOIN
(SELECT site_code, COUNT(*) all_hl FROM
(SELECT headline, site_code, MIN(date_time) FROM headlines GROUP BY headline, site_code) b
GROUP BY site_code) z
ON y.site_code=z.site_code;







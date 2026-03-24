
WITH
  TIV2015_Count AS (
    SELECT
      tiv_2015
    FROM
      Insurance
    GROUP BY
      tiv_2015
    HAVING
      COUNT(pid) > 1
  ),
  Location_Count AS (
    SELECT
      lat,
      lon
    FROM
      Insurance
    GROUP BY
      lat,
      lon
    HAVING
      COUNT(pid) = 1
  )
SELECT
  ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM
  Insurance AS i
JOIN
  TIV2015_Count AS tc
  ON i.tiv_2015 = tc.tiv_2015
JOIN
  Location_Count AS lc
  ON i.lat = lc.lat AND i.lon = lc.lon;

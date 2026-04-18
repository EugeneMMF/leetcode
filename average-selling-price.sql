# Write your MySQL query statement below
WITH sales AS (
 SELECT us.product_id,
        SUM(us.units * p.price) AS total_revenue,
        SUM(us.units) AS total_units
 FROM UnitsSold us
 JOIN Prices p
   ON us.product_id = p.product_id
  AND us.purchase_date BETWEEN p.start_date AND p.end_date
 GROUP BY us.product_id
)
SELECT pid.product_id,
       ROUND(COALESCE(s.total_revenue / NULLIF(s.total_units,0),0),2) AS average_price
FROM (
   SELECT product_id FROM Prices
   UNION
   SELECT product_id FROM UnitsSold
) pid
LEFT JOIN sales s ON pid.product_id = s.product_id;

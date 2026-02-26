
SELECT
    T.request_at AS Day,
    ROUND(
        SUM(CASE WHEN T.status LIKE 'cancelled%' THEN 1 ELSE 0 END) * 1.0 / COUNT(T.id),
        2
    ) AS "Cancellation Rate"
FROM
    Trips AS T
JOIN
    Users AS U_client
ON
    T.client_id = U_client.users_id
JOIN
    Users AS U_driver
ON
    T.driver_id = U_driver.users_id
WHERE
    U_client.banned = 'No' AND U_driver.banned = 'No'
    AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    T.request_at
HAVING
    COUNT(T.id) > 0;

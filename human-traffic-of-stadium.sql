
WITH FilteredStadium AS (
    SELECT
        id,
        visit_date,
        people
    FROM
        Stadium
    WHERE
        people >= 100
),
ConsecutiveGroups AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS group_key
    FROM
        FilteredStadium
)
SELECT
    id,
    visit_date,
    people
FROM
    ConsecutiveGroups
WHERE
    group_key IN (
        SELECT
            group_key
        FROM
            ConsecutiveGroups
        GROUP BY
            group_key
        HAVING
            COUNT(*) >= 3
    )
ORDER BY
    visit_date ASC;

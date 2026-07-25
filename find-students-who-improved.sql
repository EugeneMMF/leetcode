# Write your MySQL query statement below

WITH ranked AS (
  SELECT student_id, subject, score,
         ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS rn_start,
         ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS rn_end,
         COUNT(*) OVER (PARTITION BY student_id, subject) AS cnt
  FROM Scores
)
SELECT student_id, subject,
       MAX(CASE WHEN rn_start = 1 THEN score END) AS first_score,
       MAX(CASE WHEN rn_end = 1 THEN score END) AS latest_score
FROM ranked
WHERE cnt > 1
GROUP BY student_id, subject
HAVING latest_score > first_score
ORDER BY student_id, subject;

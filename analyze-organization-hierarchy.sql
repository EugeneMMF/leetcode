# Write your MySQL query statement below
WITH RECURSIVE hierarchy AS (
  SELECT employee_id, employee_name, manager_id, salary, department, 1 AS level
  FROM Employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, e.employee_name, e.manager_id, e.salary, e.department, h.level + 1
  FROM Employees e
  JOIN hierarchy h ON e.manager_id = h.employee_id
),
descendants AS (
  SELECT employee_id AS manager_id, employee_id AS descendant_id
  FROM Employees
  UNION ALL
  SELECT d.manager_id, e.employee_id
  FROM descendants d
  JOIN Employees e ON e.manager_id = d.descendant_id
),
team_budget AS (
  SELECT d.manager_id,
         COUNT(*) - 1 AS team_size,
         SUM(e.salary) AS budget
  FROM descendants d
  JOIN Employees e ON e.employee_id = d.descendant_id
  GROUP BY d.manager_id
)
SELECT h.employee_id,
       h.employee_name,
       h.level,
       COALESCE(tb.team_size, 0) AS team_size,
       tb.budget
FROM hierarchy h
LEFT JOIN team_budget tb ON h.employee_id = tb.manager_id
ORDER BY h.level ASC, tb.budget DESC, h.employee_name ASC;
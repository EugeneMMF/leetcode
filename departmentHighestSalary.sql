# Write your MySQL query statement below
select t3.name as Department, t1.name as Employee, t1.salary as Salary from Employee t1
join (select max(salary) as Salary, departmentId from Employee group by departmentId) t2
on t1.departmentId = t2.departmentId
join Department t3 on t1.departmentId = t3.id
where t1.salary = t2.salary;
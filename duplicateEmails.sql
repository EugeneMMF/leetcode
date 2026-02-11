# Write your MySQL query statement below
select email as Email from (select email, count(*) as ct from Person group by email) tt where ct > 1;
# Write your MySQL query statement below
select t1.id from Weather t1
join Weather t2 on date_sub(str_to_date(t1.recordDate, '%Y-%m-%d'), interval 1 day) = t2.recordDate
where t1.temperature > t2.temperature;
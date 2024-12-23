# Write your MySQL query statement below
select a1.machine_id, avg(a2.timestamp) as processing_time 
from Activity a1
join Activity a2 
on a1.activity_type= a2. activity_type 
group by a1.machine_id ;
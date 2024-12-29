select distinct(query_name), round(avg(rating/position),2) as quality, round(AVG(rating < 3) * 100, 2) as poor_query_percentage 
from Queries 
group by query_name;
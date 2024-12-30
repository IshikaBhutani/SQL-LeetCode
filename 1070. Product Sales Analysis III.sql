select 
s.product_id,s.year as first_year , s.quantity, s.price 
from Sales s 
join (
select product_id, min(year) as first_year 
from Sales
group by product_id) as first_year_sales on s.product_id=first_year_sales.product_id AND s.year = first_year_sales.first_year;

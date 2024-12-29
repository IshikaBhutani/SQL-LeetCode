select contest_id, ROUND((COUNT(user_id) / (SELECT COUNT(*) FROM Users) * 100), 2) as percentage
from Register 
group by contest_id
order by percentage DESC, contest_id ASC;
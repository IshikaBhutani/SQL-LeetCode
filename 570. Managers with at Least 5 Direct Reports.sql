select e.name from employee e
inner join employee y 
on e.id=y.managerId 
group by e.name, e.id
having count(y.managerId)>=5;
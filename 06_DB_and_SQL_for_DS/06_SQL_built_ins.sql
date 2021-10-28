-- aggregate functions: sum(), min(), max(), avg()
select sum(cost) as sum_of_cost
from petrescue;

select max(quantity)
from petrescue;

select min(id)
from petrescue
where animal = 'Dog';

select avg(cost)
from petresue;

-- average cost per dog
select avg(cost / quantiy)
from petrescue
where animal = 'Dog';

select round(cost)
from petrescue;

select length(animal)
from petrescue;

select ucase(animal), lcase(animal)
from petrescue;

-- date & time functions
select day(rescuedate)
from petrescue;

-- time since rescue in YMMDD
select (current_date - rescuedate)
from petrescue;

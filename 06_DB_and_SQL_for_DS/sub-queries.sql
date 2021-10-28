-- employees with higher than average salary
select * from Employees
 where salary > (select avg(salary) from Employee);

-- column expression
select emp_id, salary,
 (select avg(salary) from Employees) as avg_salary
from Employees;

-- in FROM clause
select * from
(select emp_id, f_name, l_name, dep_id from Employees) as emp4all;

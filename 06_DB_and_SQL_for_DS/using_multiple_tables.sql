-- there are 3 ways to use multiple tables:
-- a) sub-queries
-- b) implicit join
-- c) join operators (inner, outer...)

-- sub-queries:
-- only employees records that correspond
-- to departments with a certain location
select * from employees
where dep_id in
(select dept_id_dep from departments where loc_id = 'L002');

-- String Patterns
select * from author where f_name like 'R%';


-- Ranges
select title, pages from Book
  where pages >= 290 and pages <= 300;
-- or
select title, pages from Book
  where pages between 290 and 300;


-- Set of Values
select f_name, l_name, country from author
  where country = 'AU' or country = 'BR';
-- or
select f_name, l_name, country from author
  where country in ('AU', 'BR');


-- Sort Result Set
select title from Book
  order by title;
-- descendend
select title from Book
  order by title desc;
-- column number
select title, pages from Book
  order by 2;


-- Grouping (how many authors come from each country)
select country, count(country) as Count
  from author
group by country;

-- GROUP BY and HAVING
select country, count(country) as Count
  from author
group by country
having count(country) > 4;

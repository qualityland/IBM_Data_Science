create table author

insert into author
  (author_id, lastname, firstname, email, city, country)
  values
  (1, 'Chong', 'Raoul', 'rfc@ibm.com', 'Toronto', 'CA'),
  (2, 'Ahuja', 'Rav', 'ra@ibm.com', 'Toronto', 'CA'),
  (3, 'Hakes', 'Ian', 'ih@ibm.com', 'Toronto', 'CA'),
  (4, 'Sharma', 'Neeraj', 'ns@ibm.com', 'Chennai', 'IN'),
  (5, 'Perniu', 'Liviu', 'lp@ibm.com', 'Transylvania', 'RO');

update author set lastname = 'Katta', firstname = 'Laksmi'
  where author_id = 2;

delete from author
  where author_id in (2, 3);

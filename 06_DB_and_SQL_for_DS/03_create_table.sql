CREATE TABLE provinces (
  id char(2) PRIMARY KEY NOT NULL,
  name varchar(24)
)

CREATE TABLE author (
  author_id CHAR(2) PRIMARY KEY NOT NULL,
  lastname VARCHAR(15) NOT NULL,
  firstname VARCHAR(15) NOT NULL,
  email VARCHAR(40),
  city VARCHAR(15),
  coutry VARCHAR(2)
)

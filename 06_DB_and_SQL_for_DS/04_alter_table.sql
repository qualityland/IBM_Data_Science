ALTER TABLE author
  ADD COLUMN telephone_number BIGINT;


ALTER TABLE author
  ALTER COLUMN telephone_number SET DATA TYPE CHAR(20);

ALTER TABLE author
  DROP COLUMN telephone_number;

DROP TABLE author;

TRUNCATE TABLE author IMMEDIATE;

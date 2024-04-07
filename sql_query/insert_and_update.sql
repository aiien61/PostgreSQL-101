CREATE TABLE examples (
	
	example_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30)
);

/*
ALTER TABLE tablename
ADD COLUMN columnname data_type constraint;
*/

ALTER TABLE examples
ADD COLUMN email VARCHAR(50) UNIQUE;


ALTER TABLE examples
ADD COLUMN nationality VARCHAR(30),
ADD COLUMN age INT NOT NULL;

/*
ALTER TABLE tablename
ALTER COLUMN columnname TYPE new_data_type;
*/

ALTER TABLE examples
ALTER COLUMN nationality TYPE CHAR(3);


ALTER TABLE examples
ALTER COLUMN last_name TYPE VARCHAR(50),
ALTER COLUMN email TYPE VARCHAR(80);

-- Insert data into a table

/*

INSERT INTO tablename (columnname1, columnname2, columnname3)
VALUES ('value1', 'value2', 'value3');

*/

INSERT INTO examples (first_name, last_name, email, nationality, age)
VALUES ('David', 'Mitchell', 'dmitch@gmail.com', 'GBR', 43);

INSERT INTO examples (first_name, last_name, email, nationality, age)
VALUES ('Emily', 'Watson', 'ewatson@gmail.com', 'USA', 29), ('Theo', 'Scott', 'tscott@gmail.com', 'AUS', 33), ('Emily', 'Smith', 'esmith@gmail.com', 'GBR', 29), ('Jim', 'Burr', 'jburr@gmail.com', 'USA', 54);

-- Update data in a table

/*

UPDATE tablename
SET columnname = 'newvalue'
WHERE columnname = 'value';

*/

UPDATE examples
SET email = 'davidmitchell@gmail.com'
WHERE example_id = 1;


UPDATE examples
SET nationality = 'CAN'
WHERE nationality = 'USA';


UPDATE examples
SET first_name = 'James', age = '55'
WHERE example_id = 5;


-- Delete data from a table

/*

DELETE FROM tablename
WHERE columnname = 'value';

*/

DELETE FROM examples
WHERE example_id = 2;

DELETE FROM examples
WHERE nationality = 'GBR';


-- Delete all the data from the table

DELETE FROM examples;

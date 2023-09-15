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


-- Create the owners table

CREATE TABLE owners (
	
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	city VARCHAR(30),
	state CHAR(2)
);


-- Create the pets table (with a foreign key)

CREATE TABLE pets (
	
	id SERIAL PRIMARY KEY,
	species VARCHAR(30),
	full_name VARCHAR(30),
	age INT,
	owner_id INT REFERENCES owners (id)
);

-- add an email column to the owners table

ALTER TABLE owners
ADD COLUMN email VARCHAR(50) UNIQUE;

-- Change the data type of the last_name column in the owners table to VARCHAR(50)

ALTER TABLE owners
ALTER COLUMN last_name TYPE VARCHAR(50);
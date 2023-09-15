-- deleting tables from a database

CREATE TABLE practice (
	
	id SERIAL PRIMARY KEY,
	product_name VARCHAR(50),
	product_price NUMERIC(4,2)
);

DROP TABLE practice;
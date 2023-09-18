-- Insert the data into the owners table

INSERT INTO owners (first_name, last_name, city, state, email) 
VALUES ('Samuel', 'Smith', 'Boston', 'MA', 'samsmith@gmail.com'),
('Emma', 'Johnson', 'Seattle', 'WA', 'emjohnson@gmail.com'),
('John', 'Oliver', 'New York', 'NY', 'johnoliver@gmail.com'),
('Olivia', 'Brown', 'San Francisco', 'CA', 'oliviabrown@gmail.com'),
('Simon', 'Smith', 'Dallas', 'TX', 'sismith@gmail.com'),
(null, 'Maxwell', null, 'CA', 'lordmaxwell@gmail.com');

-- Insert the data into the pets table

INSERT INTO pets (species, full_name, age, owner_id)
VALUES ('Dog', 'Rex', 6, 1), ('Rabbit', 'Fluffy', 2, 5), ('Cat', 'Tom', 8, 2), 
('Mouse', 'Jerry', 2, 2), ('Dog', 'Biggles', 4, 2), ('Tortoise', 'Squirtle', 42, 3);

-- Update Fluffy the rabbits age to 3

UPDATE pets
SET age = 3
WHERE full_name = 'Fluffy';

-- Delete Mr Maxwell from the owners table

DELETE FROM owners
WHERE last_name = 'Maxwell';

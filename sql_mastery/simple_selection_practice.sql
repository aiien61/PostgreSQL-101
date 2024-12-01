-- 1. Select all fields, and all records from actor table
SELECT *
FROM actor;

-- 2. Select all fields and records from film table
SELECT *
FROM film;

-- 3. Select all fields and records from staff table
SELECT *
FROM staff;

-- 4. Select address and district columns from address table
SELECT address, district
FROM address;

-- 5. Select title and description from film table
SELECT title, description
FROM film;

-- 6. Select city and country_id from city table
SELECT city, country_id
FROM city;

-- 7. Select all the distinct last names from customer table
SELECT DISTINCT(last_name)
FROM customer;

-- 8. Select all the distinct first names from the actor table
SELECT DISTINCT(first_name)
FROM actor;

-- 9. Select all the distinct inventory_id values from rental table
SELECT DISTINCT(inventory_id)
FROM rental;

-- 10. Find the number of actors(COUNT)
SELECT COUNT(*)
FROM actor;

-- 11. Find the number of categories
SELECT COUNT(*)
FROM category

-- 12. Find the number of distinct first names in actor table
SELECT COUNT(DISTINCT(first_name))
FROM actor;

-- 13. Select rental_id and the difference between return_date and rental_date in rental table
SELECT rental_id, return_date - rental_date AS rental_length
FROM rental;



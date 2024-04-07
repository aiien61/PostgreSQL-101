-- UPPER AND LOWER FUNCTIONS

/*
SELECT UPPER('string');

SELECT LOWER('string');

SELECT UPPER(column_name) FROM table_name;

SELECT LOWER(column_name) FROM table_name;
*/

SELECT UPPER('hello world');

SELECT first_name, UPPER(last_name) AS last_name FROM actors;

SELECT LOWER('HEllO WOrlD');

SELECT LOWER(movie_name) FROM movies;

SELECT movie_name FROM movies;

-- INITCAP STRING FUNCTION

/*
SELECT INITCAP('example string');

SELECT INITCAP(column_name) FROM table_name;
*/

SELECT INITCAP('eXamplE sTRING');

SELECT movie_name FROM movies;

SELECT INITCAP(movie_name) FROM movies;

-- LEFT AND RIGHT STRING FUNCTIONS

/*
SELECT LEFT('string', int);

SELECT LEFT(column_name, int) FROM table_name;

SELECT RIGHT('string', int);

SELECT RIGHT(column_name, int) FROM table_name;
*/


SELECT LEFT('string', 3);

SELECT LEFT('string', -2);

SELECT LEFT(movie_name, 5) FROM movies;

SELECT RIGHT('example', 3);

SELECT RIGHT('example', -3);

SELECT RIGHT(first_name, 2) FROM actors;

-- REVERSE FUNCTION

/*
SELECT REVERSE('string');

SELECT REVERSE(column_name) FROM table_name;
*/


SELECT REVERSE('reverse');

SELECT movie_name, REVERSE(movie_name) FROM movies;


-- Select the directors first and last names and movie names in upper case.
SELECT UPPER(d.first_name) AS first_name, UPPER(d.last_name) AS last_name, UPPER(mo.movie_name) AS movie_name FROM directors d
JOIN movies mo ON d.director_id = mo.director_id;

-- Select the first and last names, in initial capitalisation format, of all the actors who have starred in a Chinese or Korean movie.
SELECT DISTINCT INITCAP(ac.first_name) AS first_name, INITCAP(ac.last_name) AS last_name FROM actors ac
JOIN movies_actors ma ON ma.actor_id = ac.actor_id
JOIN movies mo ON mo.movie_id = ma.movie_id
WHERE mo.movie_lang IN ('Chinese', 'Korean');

SELECT INITCAP(ac.first_name) AS first_name, INITCAP(ac.last_name) AS last_name FROM actors ac
WHERE ac.actor_id IN
(SELECT ma.actor_id FROM movies_actors ma
WHERE ma.movie_id IN
(SELECT mo.movie_id FROM movies mo
WHERE mo.movie_lang IN ('Chinese', 'Korean')));

-- Retrieve the reversed first and last names of each directors and the first three characters of their nationality.
SELECT REVERSE(first_name) AS rev_first_name, REVERSE(last_name) AS rev_surname, LEFT(nationality, 3) AS nat FROM directors;


-- Retrieve the initials of each director and display it in one column named 'initials'.
SELECT CONCAT_WS('.', LEFT(first_name, 1), LEFT(last_name, 1)) AS initials FROM directors;


-- SUBSTRING FUNCTION

/*
SELECT SUBSTRING('string', from, count);

SELECT SUBSTRING(column_name, from, count) FROM table_name;
*/

SELECT SUBSTRING('long string', 2, 6);

SELECT first_name, SUBSTRING(first_name, 3, 4) FROM actors; 

-- REPLACE FUNCTION

/*
SELECT REPLACE('source_string', 'old_string', 'new_string');

SELECT REPLACE(column_name, 'old_string', 'new_string') FROM table_name;

UPDATE table_name
SET column_name = REPLACE(column_name, 'old_string', 'new_string')
WHERE column_name = 'value';
*/

SELECT REPLACE('a cat plays with another cat', 'cat', 'dog');

SELECT * FROM actors;

SELECT first_name, last_name, REPLACE(gender, 'M', 'Male') FROM actors;

SELECT * FROM directors;

UPDATE directors
SET nationality = REPLACE(nationality, 'American', 'USA')
WHERE nationality = 'American';


UPDATE directors
SET nationality = REPLACE(nationality, 'Brit', 'Engl')
WHERE nationality = 'British';


-- SPLIT_PART FUNCTION

/*
SELECT SPLIT_PART('string', 'delimiter', 'field_number');

SELECT SPLIT_PART(column_name, 'delimiter', 'field_number') FROM table_name;
*/


SELECT SPLIT_PART('first_name.last_name@gmail.com', '@', 2);

SELECT SPLIT_PART('first_name.last_name@gmail.com', '.', 1);

SELECT movie_name, SPLIT_PART(movie_name, ' ', 1) AS first_word FROM movies;

SELECT movie_name, SPLIT_PART(movie_name, ' ', 1) AS first_word,
SPLIT_PART(movie_name, ' ', 2) AS second_word
FROM movies;

-- Using Casting to apply String Functions to Non String Data Types

/*
SELECT column_name::DATATYPE FROM table_name;
*/

SELECT * FROM directors;

SELECT date_of_birth::TEXT FROM directors;

SELECT SPLIT_PART(date_of_birth::TEXT, '-', 1) FROM directors;

-- Can't work because date_of_birth is date type instead of string.
SELECT SPLIT_PART(date_of_birth, '-', 1) FROM directors;

SELECT SPLIT_PART(date_of_birth::VARCHAR(20), '-', 1) FROM directors;

SELECT SPLIT_PART(date_of_birth::VARCHAR(3), '-', 1) FROM directors;

SELECT date_of_birth::VARCHAR(3) FROM directors;

-- Can't convert date type into integer type or other numeric types.
SELECT SPLIT_PART(date_of_birth:INT, '-', 1) FROM directors;


-- Use the substring function to retrieve the first 6 characters of each movie name and the year they released.
SELECT SUBSTRING(movie_name, 1, 6) AS movie_name, SUBSTRING(release_date::TEXT, 1, 4) AS year FROM movies;

-- Retrieve the first name initial and last name of every actor born in May.
SELECT SUBSTRING(first_name, 1, 1) AS fn_initial, last_name, date_of_birth FROM actors
WHERE SPLIT_PART(date_of_birth::TEXT, '-', 2 ) = '05';

-- Replace the movie language for all English language movies, with age certificate rating 18, to 'Eng'.
SELECT REPLACE(movie_lang, 'English', 'Eng') FROM movies
WHERE age_certificate = '18';

UPDATE movies
SET movie_lang = REPLACE(movie_lang, 'English', 'Eng')
WHERE age_certificate = '18';

SELECT * FROM movies;

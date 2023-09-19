SELECT * FROM directors;

SELECT first_name FROM directors;

SELECT first_name, last_name FROM directors;

SELECT first_name, last_name, nationality FROM directors;

-- Retrieving data with a where clause

/*
SELECT columnname FROM tablename
WHERE columnname = 'value';
*/

SELECT * FROM movies
WHERE age_certificate = '15';

SELECT * FROM movies
WHERE age_certificate = '15'
AND movie_lang = 'Chinese';

SELECT * FROM movies
WHERE age_certificate = '15'
OR movie_lang = 'Chinese';

SELECT * FROM movies
WHERE movie_lang = 'English'
AND age_certificate = '15'
AND director_id = 27;

-- Using logical operators (>, >=, <, <=)

SELECT movie_name, movie_length FROM movies
WHERE movie_length > 120;

SELECT movie_name, movie_length FROM movies
WHERE movie_length >= 120;

SELECT movie_name, movie_length FROM movies
WHERE movie_length < 120;

SELECT movie_name, movie_length FROM movies
WHERE movie_length <= 120;


SELECT * FROM movies
WHERE release_date > '1999-12-31';

SELECT * FROM movies
WHERE release_date < '1999-12-31';

-- This query doesn't realy make sense because it follows alphabetic order
SELECT * FROM movies
WHERE movie_lang < 'English';


-- Select the movie_name and release_date of every movie.

SELECT movie_name, release_date FROM movies;

-- Select the first and last names of all American directors.

SELECT first_name, last_name FROM directors
WHERE nationality = 'American';

-- Select all male actors born after the 1st of January 1970.

SELECT * FROM actors
WHERE gender = 'M'
AND date_of_birth > '1970-01-01';

-- Select the names of all movies which are over 90 minutes long and movie language is English.

SELECT movie_name FROM movies
WHERE movie_length > 90
AND movie_lang = 'English';

-- Using IN and NOT IN

/*
SELECT columnname1, columnname2 FROM tablename
WHERE columnname3 IN ('value1', 'value2');

SELECT columnname1, columnname2 FROM tablename
WHERE columnname3 NOT IN ('value1', 'value2');
*/

SELECT first_name, last_name FROM actors
WHERE first_name IN ('Bruce', 'John');

SELECT first_name, last_name FROM actors
WHERE first_name IN ('Bruce', 'John', 'Peter');

SELECT first_name, last_name FROM actors
WHERE first_name NOT IN ('Bruce', 'John', 'Peter');

SELECT actor_id, first_name, last_name FROM actors
WHERE actor_id IN (2,3,4,5,6,8);

SELECT actor_id, first_name, last_name FROM actors
WHERE actor_id NOT IN (2,3,4,5,6,8);

-- Using LIKE with % and _ for pattern recognition

/*
SELECT columnname FROM table
WHERE columnname LIKE '%pattern%';

SELECT columnname FROM table
WHERE columnname LIKE '_pattern_';
*/

SELECT * FROM actors 
WHERE first_name LIKE 'P%';

SELECT * FROM actors 
WHERE first_name LIKE 'Pe_';

SELECT * FROM actors 
WHERE first_name LIKE '%r';

SELECT * FROM actors 
WHERE first_name LIKE '%r%';

SELECT * FROM actors 
WHERE first_name LIKE '%rl%';

SELECT * FROM actors 
WHERE first_name LIKE '_rl_';

SELECT * FROM actors 
WHERE first_name LIKE '__rl_';

SELECT * FROM actors 
WHERE first_name LIKE '__rl__';

-- Selecting data where a column is between 2 values

/*
SELECT columnname1, columnname2 FROM tablename
WHERE columnname3 BETWEEN value1 AND value2;
*/

SELECT * FROM movies;

SELECT movie_name, release_date FROM movies
WHERE release_date BETWEEN '1995-01-01' AND '1999-12-31';

SELECT movie_name, movie_length FROM movies
WHERE movie_length BETWEEN 90 AND 120;

-- this query doesn't make sense
SELECT movie_name, movie_lang FROM movies
WHERE movie_lang BETWEEN 'E' AND 'Portuguese';

-- Select the movie names and movie language of all movies with a movie language of English, Spanish or Korean.
SELECT movie_name, movie_lang FROM movies
WHERE movie_lang IN ('English', 'Spanish', 'Korean');

-- Select the first and last names of the actors whose last name begins with M and were born between 01/01/1940 and 31/12/1969.
SELECT first_name, last_name FROM actors
WHERE last_name LIKE 'M%'
AND date_of_birth BETWEEN '1940-01-01' AND '1969-12-31';

-- Select the first and last names of the directors with nationality of British, French or German born between 01/01/1950 and 31/12/1980.
SELECT first_name, last_name FROM directors
WHERE nationality IN ('British', 'French', 'German')
AND date_of_birth BETWEEN '1950-01-01' AND '1980-12-31';
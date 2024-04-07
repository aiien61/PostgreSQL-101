-- Aggregate Functions: COUNT

/*
SELECT COUNT(columnname) FROM tablename;
*/

SELECT COUNT(*) FROM movie_revenues;

SELECT COUNT(international_takings) FROM movie_revenues;

SELECT COUNT(*) FROM movies
WHERE movie_lang = 'English';


-- Aggregate Functions: SUM

/*
SELECT SUM(columnname) FROM tablename;
*/

SELECT SUM(domestic_takings) FROM movie_revenues;

SELECT SUM(domestic_takings) FROM movie_revenues
WHERE domestic_takings > 100.0;

SELECT SUM(movie_length) FROM movies
WHERE movie_lang = 'Chinese';


-- Aggregate Functions: MIN and MAX

/*
SELECT MIN(columnname) FROM tablename;
SELECT MAX(columnname) FROM tablename;
*/

SELECT MAX(movie_length) FROM movies;
SELECT MIN(movie_length) FROM movies;

SELECT MIN(movie_length) FROM movies
WHERE movie_lang = 'Japanese';

SELECT MAX(release_date) FROM movies;

SELECT MIN(release_date) FROM movies;

-- Return the movie_name that the first letter is the last word in alphabetic order, instead of the longest length of movie_name
SELECT MAX(movie_name) FROM movies;

SELECT MIN(movie_name) FROM movies;


-- Aggregate Functions: AVG

/*
SELECT AVG(columnname) FROM tablename;
*/

SELECT AVG(movie_length) FROM movies;

SELECT AVG(movie_length) FROM movies
WHERE age_certificate = '18';

-- Count the number of actors born after the 1st of January 1970
SELECT COUNT(*) FROM actors
WHERE date_of_birth > '1970-01-01';

-- What was the highest and lowest domestic takings for a movie?
SELECT MAX(domestic_takings) FROM movie_revenues;

SELECT MIN(domestic_takings) FROM movie_revenues;

-- What is the sum total movie length for movies rated 15?
SELECT SUM(movie_length) FROM movies
WHERE age_certificate = '15';

-- How many Japanese directors are in the directors table?
SELECT COUNT(*) FROM directors
WHERE nationality = 'Japanese';

-- What is the average movie length for Chinese movies?
SELECT AVG(movie_length) FROM movies
WHERE movie_lang = 'Chinese';

-- Grouping data

/*
SELECT column1, AGGFUN(column2) FROM tablename
GROUP BY column1;
*/

SELECT COUNT(movie_lang) FROM movies;

SELECT movie_lang, COUNT(movie_lang) FROM movies
GROUP BY movie_lang;

SELECT movie_lang, AVG(movie_length) FROM movies
GROUP BY movie_lang;

SELECT movie_lang, age_certificate, AVG(movie_length) FROM movies
GROUP BY movie_lang, age_certificate;

SELECT movie_lang, age_certificate, AVG(movie_length) FROM movies
WHERE movie_length > 120
GROUP BY movie_lang, age_certificate;

SELECT movie_lang, MIN(movie_length), MAX(movie_length) FROM movies
WHERE age_certificate = '15'
GROUP BY movie_lang;

-- Having clauses

/*
SELECT column1, AGGFUN(column2) FROM tablename
GROUP BY column1
HAVING AGGFUN(column3) = value;
*/

SELECT movie_lang, COUNT(movie_lang) FROM movies
GROUP BY movie_lang
HAVING COUNT(movie_lang) > 1;

SELECT movie_lang, COUNT(movie_lang) FROM movies
WHERE movie_length > 120
GROUP BY movie_lang
HAVING COUNT(movie_lang) > 1;

-- How many directors are there per nationality?
SELECT nationality, COUNT(*) FROM directors
GROUP BY nationality;

-- What is the sum total movie length for each age certificate and movie language combination?
SELECT age_certificate, movie_lang, SUM(movie_length) AS total_length FROM movies
GROUP BY age_certificate, movie_lang;

SELECT movie_lang, age_certificate, SUM(movie_length) AS total_length FROM movies
GROUP BY movie_lang, age_certificate
ORDER BY movie_lang, age_certificate;


-- Return the movie language which have a sum total movie language of over 500 minutes.
SELECT movie_lang, SUM(movie_length) FROM movies
GROUP BY movie_lang
HAVING SUM(movie_length) > 500;

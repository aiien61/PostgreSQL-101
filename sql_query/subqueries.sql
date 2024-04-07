-- Uncorrelated Subqueries

SELECT AVG(movie_length) FROM movies;

SELECT movie_name, movie_length FROM movies
WHERE movie_length > 
(SELECT AVG(movie_length) FROM movies);

SELECT movie_name, movie_length FROM movies
WHERE movie_length > 126.13;

SELECT first_name, last_name, date_of_birth FROM directors
WHERE date_of_birth > 
(SELECT date_of_birth  FROM directors
WHERE first_name = 'James'
AND last_name = 'Cameron');

SELECT first_name, last_name, date_of_birth FROM directors
WHERE date_of_birth > 
(SELECT date_of_birth  FROM actors
WHERE first_name = 'Tom'
AND last_name = 'Cruise');

SELECT movie_name FROM movies
WHERE movie_id IN 
(SELECT movie_id FROM movie_revenues
WHERE international_takings > domestic_takings);

SELECT mo.movie_id, mo.movie_name, d.first_name, d.last_name FROM movies mo
JOIN directors d ON mo.director_id = d.director_id
WHERE mo.movie_id IN 
(SELECT movie_id FROM movie_revenues
WHERE international_takings > domestic_takings);

-- Select first and last names of all the actors older than Marlon Brando.
SELECT first_name, last_name FROM actors
WHERE date_of_birth < 
(SELECT date_of_birth FROM actors
WHERE first_name = 'Marlon'
AND last_name = 'Brando');

-- Select the movie names of all movies that have doemstic takings above 300 million.
SELECT movie_name FROM movies
WHERE movie_id IN 
(SELECT movie_id FROM movie_revenues
WHERE domestic_takings > 300.0);

-- Return the shortest and longest movie length for movies with an above average domestic takings.
SELECT MIN(movie_length) AS shortest_length, MAX(movie_length) AS longest_length FROM movies
WHERE movie_id IN 
(SELECT movie_id FROM movie_revenues
WHERE domestic_takings > 
(SELECT AVG(domestic_takings) FROM movie_revenues));


-- Correlated Subqueries


SELECT d1.first_name, d1.last_name, d1.date_of_birth FROM directors d1
WHERE d1.date_of_birth = 
(SELECT MIN(date_of_birth) FROM directors d2
WHERE d2.nationality = d1.nationality);

-- inner query is not allowed to be executed independently
SELECT MIN(date_of_birth) FROM directors d2
WHERE d2.nationality = d1.nationality;


SELECT mo1.movie_name, mo1.movie_lang, mo1.movie_length FROM movies mo1
WHERE mo1.movie_length = 
(SELECT MAX(movie_length) FROM movies mo2
WHERE mo2.movie_lang = mo1.movie_lang);

-- Select the first name, last name and date of birth for the oldest actors of each gender.
SELECT ac1.first_name, ac1.last_name, ac1.date_of_birth FROM actors ac1
WHERE ac1.date_of_birth = 
(SELECT MIN(ac2.date_of_birth) FROM actors ac2
WHERE ac2.gender = ac1.gender);

-- Select the movie name, movie length and age certificate for movies with an above average length for their age certificate.
SELECT mo1.movie_name, mo1.movie_length, mo1.age_certificate FROM movies mo1
WHERE mo1.movie_length > 
(SELECT AVG(mo2.movie_length) FROM movies mo2
WHERE mo2.age_certificate = mo1.age_certificate)
ORDER BY mo1.age_certificate;
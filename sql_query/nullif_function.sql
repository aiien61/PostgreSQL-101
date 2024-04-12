-- Database: movie_data

-- DROP DATABASE IF EXISTS movie_data;

CREATE DATABASE movie_data
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


-- NULLIF FUNCTION
-- Return a NULL value if both arguments are equal, otherwise it returns the first argument

SELECT NULLIF('A', 'A');

SELECT NULLIF('A', 'B');

SELECT NULLIF('B', 'A');


-- Both arguments must be convertable to a common data type

-- Error
SELECT NULLIF('A', 1);

SELECT NULLIF(1.0, 1);

SELECT NULLIF(1.0, 2);

SELECT first_name, last_name,
NULLIF(last_name, 'Anderson') AS "Mr Anderson"
FROM directors;


-- Challenge

-- Return the movie names, movie languages and age certificates - return NULL if the movie language is English or the age certificate is U
SELECT movie_name, NULLIF(movie_lang, 'English') AS movie_language, NULLIF(age_certificate, 'U') AS age_certificate
FROM movies;







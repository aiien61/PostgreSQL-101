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
	

-- SQL uses CASE EXPRESSIONS for conditional statements same as IF-ELSE syntax in other programming languages

/*
CASE
	WHEN column_condition THEN do this
	WHEN column_condition THEN do this
	ELSE do this
END column_name_alias
*/

SELECT movie_name, movie_length,
CASE
    WHEN movie_length > 150 THEN 'over 2.5 hours'
    WHEN movie_length > 90 THEN 'over 1.5 hours'
    ELSE '1.5 hours or under'
END movie_time_hours
FROM movies;


SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings > 300 THEN 'BOX OFFICE SMASH'
    WHEN domestic_takings > 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
END box_office_success
FROM movie_revenues;

-- domestic_takings null is being dealt with 
SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings >= 300 THEN 'BOX OFFICE SMASH'
    WHEN domestic_takings >= 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
    ELSE 'MISSING INFO'
END box_office_success
FROM movie_revenues;


SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
    WHEN domestic_takings >= 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 300 THEN 'BOX OFFICE SMASH'
    ELSE 'MISSING INFO'
END box_office_success
FROM movie_revenues;


SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings >= 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
    WHEN domestic_takings >= 300 THEN 'BOX OFFICE SMASH'
    ELSE 'MISSING INFO'
END box_office_success
FROM movie_revenues;

-- CASE Expression with aggregate function
SELECT 
CASE
    WHEN nationality = 'British' THEN 'UK'
    ELSE 'Not UK' 
END British,
COUNT(1) AS count
FROM directors
GROUP BY 
CASE 
    WHEN nationality = 'British' THEN 'UK' 
    ELSE 'Not UK' 
END;


SELECT 
CASE
    WHEN nationality = 'British' THEN 'UK'
    WHEN nationality = 'French' THEN 'France'
    WHEN nationality = 'German' THEN 'Germany'
    WHEN nationality = 'Swedish' THEN 'Sweden'
    ELSE 'Not European' 
END European,
COUNT(1) AS tally
FROM directors
GROUP BY 
CASE 
    WHEN nationality = 'British' THEN 'UK' 
    WHEN nationality = 'French' THEN 'France'
    WHEN nationality = 'German' THEN 'Germany'
    WHEN nationality = 'Swedish' THEN 'Sweden'
    ELSE 'Not European' 
END;


SELECT 
SUM(
    CASE 
        WHEN movie_length BETWEEN 0 AND 90 THEN 1 
        ELSE 0 
    END
) AS Short,
SUM(
    CASE 
        WHEN movie_length BETWEEN 91 AND 120 THEN 1 
        ELSE 0 
    END
) AS Medium,
SUM(
    CASE 
        WHEN movie_length BETWEEN 121 AND 150 THEN 1 
        ELSE 0 
    END
) AS Long,
SUM(
    CASE 
        WHEN movie_length > 150 THEN 1 
        ELSE 0 
    END
) AS "Very Long"
FROM movies;


-- Challenge:

-- Return the movie names and whether they were international box office smashes, hits or flops.
SELECT mo.movie_name,
CASE
    WHEN mr.international_takings >= 300 THEN 'International Box Office Smash'
    WHEN mr.international_takings >= 100 THEN 'International Box Office Hit'
    WHEN mr.international_takings >= 0 THEN 'International Box Office Flop'
    ELSE 'MISSING INFO'
END international_box_office
FROM movies mo
JOIN movie_revenues mr ON mr.movie_id = mo.movie_id



-- Return the continent that the directors are from based off of their nationality
SELECT first_name, last_name,
CASE
    WHEN nationality IN ('American', 'Mexican') THEN 'North America'
    WHEN nationality IN ('Brazilian') THEN 'South America'
    WHEN nationality IN ('British', 'German', 'French', 'Swedish') THEN 'Europe'
    WHEN nationality IN ('Chinese', 'Japanese', 'South Korean') THEN 'Asia'
    WHEN nationality IN ('Australian') THEN 'Oceania'
    ELSE 'no info'
END continent
FROM directors;

-- Return the number of movies suitable for children (U, PG) and not suitable for children (12, 15, 18)
SELECT 
CASE
	WHEN age_certificate IN ('U', 'PG') THEN 'suitable'
	ELSE 'not suitable'
END children,
COUNT(1) AS Total
FROM movies
GROUP BY
CASE
	WHEN age_certificate IN ('U', 'PG') THEN 'suitable'
	ELSE 'not suitable'
END;

-- For each age certificate: return an average of the domestic takings for English language movies and 
-- international takings for non-English language movies
SELECT mo.age_certificate,
AVG(
	CASE
		WHEN mo.movie_lang = 'English' THEN mr.domestic_takings
		ELSE mr.international_takings
	END
) AS takings
FROM movies mo
JOIN movie_revenues mr ON mr.movie_id = mo.movie_id
GROUP BY mo.age_certificate;

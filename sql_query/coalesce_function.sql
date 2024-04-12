-- COALESCE FUNCTION
-- Takes an unlimited number of arguments and outputs the first non-null value

SELECT COALESCE(5, 7, 4);

SELECT COALESCE(NULL, NULL, 7, 4);

-- return null if all null values
SELECT COALESCE(NULL, NULL, NULL);

SELECT * FROM movie_revenues;

SELECT movie_id, (domestic_takings + international_takings) AS total_takings
FROM movie_revenues;

-- replace null value with 0 if domestic takings or international takings is null
SELECT movie_id,
(COALESCE(domestic_takings, 0) + COALESCE(international_takings, 0)) AS total_takings
FROM movie_revenues;


-- Challenge

-- Return a column which contains the difference in values between the domestic takings and international takings for each movie
SELECT mo.movie_name, (COALESCE(mr.domestic_takings, 0) - COALESCE(mr.international_takings, 0)) AS difference
FROM movies mo
JOIN movie_revenues mr ON mr.movie_id = mo.movie_id;

-- if forcing to get absolute values
SELECT mo.movie_name, ABS(COALESCE(mr.domestic_takings, 0) - COALESCE(mr.international_takings, 0)) AS difference
FROM movies mo
JOIN movie_revenues mr ON mr.movie_id = mo.movie_id;
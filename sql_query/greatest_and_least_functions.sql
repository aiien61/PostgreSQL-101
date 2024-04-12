-- GREATEST and LEAST Functions

-- Return the greatest and least values from a number of arguments

SELECT GREATEST(1, 2, NULL, 3);

SELECT LEAST(1, 2, NULL, 3);

SELECT GREATEST('B', 'A', 'a', 'b', NULL, 'c', 'C');

SELECT LEAST('B', 'A', 'a', 'b', NULL, 'c', 'C');

-- PostgreSQL will ignore NULL values unless all values are NULL,
-- then it will return NULL.

SELECT movie_id, domestic_takings, international_takings, LEAST(domestic_takings, international_takings) AS smallest_market
FROM movie_revenues;

SELECT movie_id, domestic_takings, international_takings, GREATEST(domestic_takings, international_takings) AS biggest_market
FROM movie_revenues;

SELECT movie_id, domestic_takings, international_takings, GREATEST(domestic_takings, international_takings, 0) AS biggest_market
FROM movie_revenues;
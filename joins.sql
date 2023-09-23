-- INNER JOINS:

/*
SELECT table1.column1, table1.column2, table2.column1 FROM table1
INNER JOIN table2 on table1.column3 = table2.column3;
*/

SELECT * FROM directors;
SELECT * FROM movies;

INSERT INTO directors (first_name, last_name, date_of_birth, nationality)
VALUES ('Christopher', 'Nolan', '1970-07-30', 'British');


SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name FROM directors
INNER JOIN movies ON directors.director_id = movies.director_id;

SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name FROM directors
INNER JOIN movies ON directors.director_id = movies.director_id
WHERE movies.movie_lang = 'Japanese'
ORDER BY movies.movie_length;

SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name FROM movies
INNER JOIN directors ON directors.director_id = movies.director_id
WHERE movies.movie_lang = 'Japanese'
ORDER BY movies.movie_length;

/*
SELECT t1.column1, t1.column2, t2.column1 FROM table1 t1
JOIN table2 t2 on t1.column3 = t2.column3;
*/

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM directors d
JOIN movies mo ON d.director_id = mo.director_id
WHERE mo.movie_lang = 'Japanese'
ORDER BY mo.movie_length; 

SELECT mo.movie_name, mr.domestic_takings, mr.international_takings FROM movies mo
JOIN movie_revenues mr ON mo.movie_id = mr.movie_id
ORDER BY mr.domestic_takings;

-- ONLY WHEN THE JOINING COLUMNS HAVE THE SAME NAME 
/*
SELECT t1.column1, t1.column2, t2.column1 FROM table t1
JOIN table2 t2 USING (column3);
*/

SELECT mo.movie_name, mr.domestic_takings FROM movies mo
JOIN movie_revenues mr USING (movie_id)
WHERE mo.age_certificate IN ('12', '15', '18')
ORDER BY mr.domestic_takings DESC;

-- Select the directors first and last names and release dates for all Chinese, Korean and Japanese movies.
SELECT d.first_name, d.last_name, mo.movie_name, mo.release_date FROM directors d
INNER JOIN movies mo ON d.director_id = mo.director_id
WHERE mo.movie_lang IN ('Chinese', 'Korean', 'Japanese')
ORDER BY d.director_id;

-- Select the movie names, release dates and international takings of all English language movies.
SELECT mo.movie_name, mo.release_date, mr.international_takings FROM movies mo
INNER JOIN movie_revenues mr USING (movie_id)
WHERE mo.movie_lang = 'English';

-- Select the movie names, domestic takings, and international takings for all movies with either missing domestic takings 
-- or international takings and order the results by movie name.
SELECT mo.movie_name, mr.domestic_takings, mr.international_takings FROM movies mo
INNER JOIN movie_revenues mr USING (movie_id)
WHERE mr.domestic_takings IS NULL
OR mr.international_takings IS NULL
ORDER BY mo.movie_name;

-- LEFT JOINS

/*
SELECT t1.column1, t1.column2, t2.column1 FROM table t1
LEFT JOIN table2 t2 ON t1.column3 = t2.column3;
*/

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM directors d
LEFT JOIN movies mo ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM movies mo
LEFT JOIN directors d ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM directors d
LEFT JOIN movies mo ON d.director_id = mo.director_id
WHERE d.nationality = 'British';


-- RIGHT JOINS

/*
SELECT t1.column1, t1.column2, t2.column1 FROM table t1
RIGHT JOIN table2 t2 ON t1.column3 = t2.column3;
*/

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM directors d
RIGHT JOIN movies mo ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM movies mo
RIGHT JOIN directors d ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM movies mo
RIGHT JOIN directors d ON d.director_id = mo.director_id
WHERE mo.age_certificate = '18';

-- FULL OUTER JOINS

/*
SELECT t1.column1, t1.column2, t2.column1 FROM table t1
FULL JOIN table2 t2 ON t1.column3 = t2.column3;
*/

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM movies mo
FULL JOIN directors d ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM directors d
FULL JOIN movies mo ON d.director_id = mo.director_id;

SELECT d.director_id, d.first_name, d.last_name, mo.movie_name FROM directors d
FULL JOIN movies mo ON d.director_id = mo.director_id
WHERE mo.movie_lang IN ('German', 'Korean')
ORDER BY d.last_name;
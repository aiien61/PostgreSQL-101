import json
import pandas as pd
import psycopg2 as pg


QUERY = """
SELECT movie_name, release_date FROM movies;
"""

QUERY = """
SELECT first_name, last_name FROM directors
WHERE nationality = 'American';
"""

QUERY = """
SELECT * FROM actors
WHERE gender = 'M'
AND date_of_birth > '1970-01-01';
"""

QUERY = """
SELECT movie_name FROM movies
WHERE movie_length > 90
AND movie_lang = 'English';
"""

QUERY = """
SELECT movie_name, movie_lang FROM movies
WHERE movie_lang IN ('English', 'Spanish', 'Korean');
"""

QUERY = """
SELECT first_name, last_name FROM actors
WHERE last_name LIKE 'M%'
AND date_of_birth BETWEEN '1940-01-01' AND '1969-12-31';
"""

QUERY = """
SELECT first_name, last_name FROM directors
WHERE nationality IN ('British', 'French', 'German')
AND date_of_birth BETWEEN '1950-01-01' AND '1980-12-31';
"""

QUERY = """
SELECT * FROM directors
WHERE nationality = 'American'
ORDER BY date_of_birth ASC
"""

QUERY = """
SELECT DISTINCT nationality FROM directors
"""

QUERY = """
SELECT first_name, last_name, date_of_birth FROM actors
WHERE gender = 'F'
ORDER BY date_of_birth DESC
LIMIT 10
"""

QUERY = """
SELECT * FROM movie_revenues
WHERE international_takings IS NOT NULL
ORDER BY international_takings DESC
LIMIT 3;
"""

QUERY = """
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM directors;
"""

QUERY = """
SELECT * FROM actors
WHERE first_name IS NULL 
OR date_of_birth IS NULL;
"""

QUERY = """
SELECT COUNT(*) FROM actors
WHERE date_of_birth > '1970-01-01';
"""

QUERY = """
SELECT MAX(domestic_takings), MIN(domestic_takings) FROM movie_revenues;
"""

QUERY = """
SELECT SUM(movie_length) FROM movies
WHERE age_certificate = '15';
"""

QUERY = """
SELECT COUNT(*) FROM directors
WHERE nationality = 'Japanese';
"""

QUERY = """
SELECT AVG(movie_length) FROM movies
WHERE movie_lang = 'Chinese';
"""

QUERY = """
SELECT nationality, COUNT(*) FROM directors
GROUP BY nationality;
"""

QUERY = """
SELECT age_certificate, movie_lang, SUM(movie_length) FROM movies
GROUP BY age_certificate, movie_lang;
"""

QUERY = """
SELECT movie_lang, SUM(movie_length) FROM movies
GROUP BY movie_lang
HAVING SUM(movie_length) > 500;
"""

QUERY = """
SELECT d.first_name, d.last_name, mo.movie_name, mo.release_date
FROM directors d
INNER JOIN movies mo USING (director_id)
WHERE mo.movie_lang IN ('Chinese', 'Korean', 'Japanese');
"""

QUERY = """
SELECT mo.movie_name, mo.release_date, mr.international_takings
FROM movie_revenues mr
INNER JOIN movies mo ON mo.movie_id = mr.movie_id
WHERE mo.movie_lang = 'English';
"""

QUERY = """
SELECT mo.movie_name, mr.domestic_takings, mr.international_takings
FROM movie_revenues mr
INNER JOIN movies mo ON mo.movie_id = mr.movie_id
WHERE mr.international_takings IS NULL
OR mr.domestic_takings IS NULL
ORDER BY mo.movie_name;
"""

QUERY = """
SELECT d.first_name, d.last_name, mo.movie_name, mo.age_certificate
FROM directors d
LEFT JOIN movies mo ON d.director_id = mo.director_id
WHERE d.nationality = 'British';
"""

QUERY = """
SELECT d.first_name, d.last_name, COUNT(mo.movie_id)
FROM directors d
LEFT JOIN movies mo ON d.director_id = mo.director_id
GROUP BY d.first_name, d.last_name;
"""

QUERY = """
SELECT ac.first_name, ac.last_name, mo.movie_name, d.first_name, d.last_name
FROM actors ac
JOIN movies_actors ma ON ma.actor_id = ac.actor_id
JOIN movies mo ON mo.movie_id = ma.movie_id
JOIN directors d ON d.director_id = mo.director_id
WHERE d.first_name = 'Wes' AND d.last_name = 'Anderson';
"""

QUERY = """
SELECT d.first_name, d.last_name, SUM(mr.domestic_takings) AS total_domestic_takings
FROM directors d
JOIN movies mo ON mo.director_id = d.director_id
JOIN movie_revenues mr ON mr.movie_id = mo.movie_id
WHERE mr.domestic_takings IS NOT NULL
GROUP BY d.first_name, d.last_name
ORDER BY total_domestic_takings DESC
LIMIT 1;
"""

QUERY = """
SELECT first_name, last_name, date_of_birth FROM directors
UNION ALL
SELECT first_name, last_name, date_of_birth FROM actors
ORDER BY date_of_birth;
"""

QUERY = """
SELECT first_name, last_name FROM directors 
WHERE date_of_birth BETWEEN '1960-01-01' AND '1969-12-31'
UNION ALL
SELECT first_name, last_name FROM actors
WHERE date_of_birth BETWEEN '1960-01-01' AND '1969-12-31'
ORDER BY last_name
"""

# Intersect the first name, last name and date of birth columns in the directors and actors tables.
QUERY = """
SELECT first_name, last_name, date_of_birth FROM directors
INTERSECT
SELECT first_name, last_name, date_of_birth FROM actors;
"""

# Retrieve the first names of male actors unless they have the same first name as any British directors.
QUERY = """
SELECT first_name FROM actors
WHERE gender = 'M'
EXCEPT
SELECT first_name FROM directors
WHERE nationality = 'British';
"""

# Select the first and last names of all the actors older than Marlon Brando
QUERY = """
SELECT first_name, last_name FROM actors
WHERE date_of_birth < 
(SELECT date_of_birth FROM actors
WHERE first_name = 'Marlon' AND last_name = 'Brando');
"""

# Select the movie names of all movies that have domestic takings above 300 million.
# Sol 1
QUERY = """
SELECT mo.movie_name FROM movies mo
JOIN movie_revenues mr ON mr.movie_id = mo.movie_id
WHERE mr.domestic_takings > 300;
"""
# Sol 2
QUERY = """
SELECT movie_name FROM movies
WHERE movie_id IN 
(SELECT movie_id FROM movie_revenues
WHERE domestic_takings > 300.0);
"""

# Return the shortest and longest movie length for movies with an above average domestic takings
# Sol 1
QUERY = """
SELECT MIN(movie_length), MAX(movie_length) FROM movies
WHERE movie_id IN
(
    SELECT movie_id FROM movie_revenues
    WHERE domestic_takings > 
    (SELECT AVG(domestic_takings) FROM movie_revenues)
);
"""
# Sol 2
QUERY = """
SELECT MIN(mo.movie_length), MAX(mo.movie_length) FROM movies mo
JOIN movie_revenues mr ON mo.movie_id = mr.movie_id
WHERE mr.domestic_takings > 
(SELECT AVG(domestic_takings) FROM movie_revenues);
"""

# Select the first name, last name and date of birth for the oldest actors of each gender.
QUERY = """
SELECT ac1.first_name, ac1.last_name, ac1.date_of_birth FROM actors ac1
WHERE ac1.date_of_birth = 
(SELECT MIN(ac2.date_of_birth) FROM actors ac2
WHERE ac2.gender = ac1.gender);
"""

# Select the movie name, movie length and age certificate for movies with 
# an above average length for their age certificate.
QUERY = """
SELECT mo1.movie_name, mo1.movie_length, mo1.age_certificate FROM movies mo1
WHERE mo1.movie_length > 
(SELECT AVG(mo2.movie_length) FROM movies mo2
WHERE mo2.age_certificate = mo1.age_certificate)
ORDER BY mo1.age_certificate ASC, mo1.movie_length DESC;
"""

# Select the directors' first and last names and movie names in upper case.
QUERY = """
SELECT UPPER(d.first_name) AS first_name, UPPER(d.last_name) AS last_name, UPPER(m.movie_name) AS movie_name
FROM directors d
INNER JOIN movies m ON m.director_id = d.director_id;
"""

# Select the first and last names, in initial capitalisation format, 
# of all the actors who have starred in a Chinese or Korean movie.
QUERY = """
SELECT DISTINCT INITCAP(ac.first_name) AS first_name, INITCAP(ac.last_name) AS last_name
FROM actors ac
JOIN movies_actors ma ON ma.actor_id = ac.actor_id
JOIN movies mo ON mo.movie_id = ma.movie_id
WHERE mo.movie_lang IN ('Chinese', 'Korean');
"""

# Retrieve the reversed first and last names of each directors and the first three characters of their nationality
QUERY = """
SELECT REVERSE(first_name) AS first_name, REVERSE(last_name) AS last_name, LEFT(nationality, 3) AS nationality
FROM directors;
"""

# Retrieve the initials of each director and display it in one column named 'initials'.
QUERY = """
SELECT CONCAT(LEFT(first_name, 1), '.', LEFT(last_name, 1)) AS initials
FROM directors
"""

# Use the substring function to retrieve the first 6 characters of each movie name and the year they released
QUERY = """
SELECT SUBSTRING(movie_name, 1, 6) AS movie_name, SUBSTRING(release_date::TEXT, 1, 4) AS year
FROM movies;
"""

# Retrieve the first name initial and last name of every actor born in May.
QUERY = """
SELECT SUBSTRING(first_name, 1, 1) AS fn_initial, last_name, date_of_birth
FROM actors
WHERE SPLIT_PART(date_of_birth::TEXT, '-', 2) = '05';
"""

# Replace the movie language for all English language movies, with age certificate rating 18, to 'Eng'.
QUERY = """
UPDATE movies
SET movie_lang = REPLACE(movie_lang, 'English', 'Eng')
WHERE age_certificate = '18';
"""

# Return the movie names and whether they were international box office smashes, hits or flops.
QUERY = """
SELECT mo.movie_name,
CASE
    WHEN mr.international_takings >= 300 THEN 'International Box Office Smash'
    WHEN mr.international_takings >= 100 THEN 'International Box Office Hit'
    WHEN mr.international_takings >= 0 THEN 'International Box Office Flop'
    ELSE 'MISSING INFO'
END international_box_office
FROM movies mo
JOIN movie_revenues mr ON mr.movie_id = mo.movie_id
"""

# Return the continent that the directors are from based off of their nationality
QUERY = """
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
"""

# Return the number of movies suitable for children (U, PG) and not suitable for children (12, 15, 18)
QUERY = """
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
"""

# For each age certificate: return an average of the domestic takings for English language movies and 
# international takings for non-English language movies
QUERY = """
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
"""


def select(cursor) -> None:
    cursor.execute(QUERY)
    return None


def main():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        
        connection = pg.connect(**config, dbname="movie_data")
        cursor = connection.cursor()
        
        select(cursor)
        
        connection.commit()

        column_names = [col.name for col in cursor.description]
        result = pd.DataFrame(cursor.fetchall(), columns=column_names)
        print(result)
        
    except (Exception, pg.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == '__main__':
    main()
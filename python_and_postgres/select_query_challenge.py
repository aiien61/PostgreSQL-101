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
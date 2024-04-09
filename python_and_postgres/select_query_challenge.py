import json
import pandas as pd
import psycopg2 as pg


QUERY1 = """
SELECT movie_name, release_date FROM movies;
"""

QUERY2 = """
SELECT first_name, last_name FROM directors
WHERE nationality = 'American';
"""

QUERY3 = """
SELECT * FROM actors
WHERE gender = 'M'
AND date_of_birth > '1970-01-01';
"""

QUERY4 = """
SELECT movie_name FROM movies
WHERE movie_length > 90
AND movie_lang = 'English';
"""

QUERY5 = """
SELECT movie_name, movie_lang FROM movies
WHERE movie_lang IN ('English', 'Spanish', 'Korean');
"""

QUERY6 = """
SELECT first_name, last_name FROM actors
WHERE last_name LIKE 'M%'
AND date_of_birth BETWEEN '1940-01-01' AND '1969-12-31';
"""

QUERY7 = """
SELECT first_name, last_name FROM directors
WHERE nationality IN ('British', 'French', 'German')
AND date_of_birth BETWEEN '1950-01-01' AND '1980-12-31';
"""


def select(cursor, query) -> None:
    cursor.execute(query)
    return None


def main():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        
        connection = pg.connect(**config, dbname="movie_data")
        cursor = connection.cursor()
        
        select(cursor, QUERY7)
        
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
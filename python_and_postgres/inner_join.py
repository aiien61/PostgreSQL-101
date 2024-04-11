import json
import pandas as pd
import psycopg2 as pg

QUERY = """
SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name 
FROM directors 
INNER JOIN movies ON directors.director_id = movies.director_id;
"""

QUERY = """
SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name 
FROM directors 
INNER JOIN movies ON directors.director_id = movies.director_id
WHERE movies.movie_lang = 'Japanese';
"""

QUERY = """
SELECT directors.director_id, directors.first_name, directors.last_name, movies.movie_name 
FROM directors 
INNER JOIN movies ON directors.director_id = movies.director_id
WHERE movies.movie_lang = 'Japanese'
ORDER BY movies.movie_length;
"""

# JOIN is defaulted to be INNER JOIN
QUERY = """
SELECT d.director_id, d.first_name, d.last_name, mo.movie_name 
FROM directors d
JOIN movies mo ON d.director_id = mo.director_id
WHERE mo.movie_lang = 'Japanese'
ORDER BY mo.movie_length;
"""

QUERY = """
SELECT mo.movie_name, mr.domestic_takings, mr.international_takings
FROM movies mo
JOIN movie_revenues mr ON mo.movie_id = mr.movie_id
ORDER BY mr.domestic_takings;
"""

# only when two tables share the same column name
QUERY = """
SELECT mo.movie_name, mr.domestic_takings, mr.international_takings
FROM movies mo
JOIN movie_revenues mr USING (movie_id);
"""

QUERY = """
SELECT mo.movie_name, mr.domestic_takings, mr.international_takings
FROM movies mo
JOIN movie_revenues mr USING (movie_id)
WHERE mo.age_certificate IN ('12', '15', '18')
AND mr.domestic_takings IS NOT NULL
AND mr.international_takings IS NOT NULL
ORDER BY mr.domestic_takings DESC;
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
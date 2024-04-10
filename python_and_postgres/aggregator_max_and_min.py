import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT MAX(movie_length) FROM movies;
"""

QUERY2 = """
SELECT MIN(movie_length) FROM movies;
"""

QUERY3 = """
SELECT MIN(movie_length) FROM movies
WHERE movie_lang = 'Japanese';
"""

QUERY4 = """
SELECT MAX(release_date) FROM movies;
"""

QUERY5 = """
SELECT MIN(release_date) FROM movies;
"""

# Return max movie name alphebatically
QUERY6 = """
SELECT MAX(movie_name) FROM movies;
"""

# Return max movie name alphebatically
QUERY7 = """
SELECT MIN(movie_name) FROM movies;
"""

MyQuery = QUERY7

def select(cursor) -> None:
    cursor.execute(MyQuery)
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
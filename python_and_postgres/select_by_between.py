import json
import pandas as pd
import psycopg2 as pg


QUERY1 = """
SELECT * FROM movies;
"""

QUERY2 = """
SELECT movie_name, release_date FROM movies
WHERE release_date BETWEEN '1995-01-01' AND '1999-12-31';
"""

QUERY3 = """
SELECT movie_name, movie_length FROM movies
WHERE movie_length BETWEEN 90 AND 120;
"""

QUERY4 = """
SELECT movie_name, movie_lang FROM movies
WHERE movie_lang BETWEEN 'E' AND 'Portuguese';
"""

# get rid of English movies
QUERY5 = """
SELECT movie_name, movie_lang FROM movies
WHERE movie_lang BETWEEN 'Eo' AND 'Portuguese';
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
        
        select(cursor, QUERY5)
        
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
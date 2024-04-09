import json
import pandas as pd
import psycopg2 as pg


QUERY1 = """SELECT * FROM movies
WHERE age_certificate = '15';
"""
QUERY2 = """SELECT * FROM movies
WHERE age_certificate = '15'
AND movie_lang = 'Chinese';
"""

QUERY3 = """SELECT * FROM movies
WHERE age_certificate = '15'
OR movie_lang = 'Chinese';
"""

QUERY4 = """SELECT * FROM movies
WHERE age_certificate = '15'
AND movie_lang = 'English'
AND director_id = 27;
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
        
        select(cursor, QUERY4)
        
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
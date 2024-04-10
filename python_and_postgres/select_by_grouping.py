import json
import pandas as pd
import psycopg2 as pg

QUERY = """
SELECT movie_lang, COUNT(movie_lang) FROM movies
GROUP BY movie_lang;
"""

QUERY = """
SELECT movie_lang, AVG(movie_length) FROM movies
GROUP BY movie_lang;
"""

QUERY = """
SELECT movie_lang, age_certificate, AVG(movie_length) FROM movies
GROUP BY movie_lang, age_certificate;
"""

QUERY = """
SELECT movie_lang, age_certificate, AVG(movie_length) FROM movies
WHERE movie_length > 120
GROUP BY movie_lang, age_certificate;
"""

QUERY = """
SELECT movie_lang, MIN(movie_length), MAX(movie_length) FROM movies
WHERE age_certificate = '15'
GROUP BY movie_lang;
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
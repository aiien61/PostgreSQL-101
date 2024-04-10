import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT DISTINCT movie_lang FROM movies
ORDER BY movie_lang;
"""

# return distinct pair of movie language and age certificate
QUERY2 = """
SELECT DISTINCT movie_lang, age_certificate FROM movies
ORDER BY movie_lang;
"""

# Same as query 4
QUERY3 = """
SELECT DISTINCT * FROM movies
ORDER BY movie_lang;
"""

QUERY4 = """
SELECT * FROM movies;
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
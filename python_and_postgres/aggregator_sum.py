import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT SUM(domestic_takings) FROM movie_revenues;
"""

# only sum up the values that are greater than 100.0
QUERY2 = """
SELECT SUM(domestic_takings) FROM movie_revenues
WHERE domestic_takings > 100.0;
"""

QUERY3 = """
SELECT SUM(movie_length) FROM movies
WHERE movie_lang = 'Chinese';
"""

# Error: can't do sum on string type
QUERY4 = """
SELECT SUM(movie_name) FROM movies;
"""

MyQuery = QUERY3

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
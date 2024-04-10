import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT movie_id, movie_name FROM movies
FETCH FIRST 1 ROW ONLY;
"""

QUERY2 = """
SELECT movie_id, movie_name FROM movies
FETCH FIRST 10 ROW ONLY;
"""

# skip first 8 rows and starts from 9th row to fetch 10 rows only
QUERY3 = """
SELECT movie_id, movie_name FROM movies
OFFSET 8 ROWS
FETCH FIRST 10 ROW ONLY;
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
        
        select(cursor, QUERY3)
        
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
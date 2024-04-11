import json
import pandas as pd
import psycopg2 as pg

QUERY = """
SELECT d.director_id, d.first_name, d.last_name, mo.movie_name 
FROM directors d
LEFT JOIN movies mo ON d.director_id = mo.director_id;
"""

QUERY = """
SELECT d.director_id, d.first_name, d.last_name, mo.movie_name 
FROM movies mo
LEFT JOIN directors d ON d.director_id = mo.director_id;
"""


QUERY = """
SELECT d.director_id, d.first_name, d.last_name, mo.movie_name 
FROM directors d
LEFT JOIN movies mo ON d.director_id = mo.director_id
WHERE d.nationality = 'British';
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
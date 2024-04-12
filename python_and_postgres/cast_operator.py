import json
import pandas as pd
import psycopg2 as pg


# Using Casting to apply String Function to Non String Data Types

# SELECT column_name::DATATYPE FROM table_name;


QUERY = """
SELECT date_of_birth::TEXT FROM directors;
"""

QUERY = """
SELECT SPLIT_PART(date_of_birth::TEXT, '-', 1) AS year_of_birth,
SPLIT_PART(date_of_birth::TEXT, '-', 2) AS month_of_birth,
SPLIT_PART(date_of_birth::TEXT, '-', 3) AS day_of_birth,
date_of_birth
FROM directors;
"""

QUERY = """
SELECT SPLIT_PART(date_of_birth::VARCHAR(20), '-', 1) FROM directors;
"""

QUERY = """
SELECT SPLIT_PART(date_of_birth::VARCHAR(3), '-', 1) FROM directors;
"""

# Error: date can't be cast to integer
QUERY = """
SELECT SPLIT_PART(date_of_birth::INT, '-', 1) FROM directors;
"""


def select(cursor) -> None:
    cursor.execute(QUERY)
    return None


def main():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        
        connection = pg.connect(**config, dbname="movie_data_clone")
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
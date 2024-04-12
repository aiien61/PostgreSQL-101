import json
import pandas as pd
import psycopg2 as pg

# COALESCE FUNCTION
# Takes an unlimited number of arguments and outputs the first non-null value

QUERY = """
SELECT COALESCE(5, 7, 4);
"""

QUERY = """
SELECT COALESCE(NULL, NULL, 7, 4);
"""

# return null if all null values
QUERY = """
SELECT COALESCE(NULL, NULL, NULL);
"""

QUERY = """
SELECT movie_id, (domestic_takings + international_takings) AS total_takings
FROM movie_revenues;
"""

# replace null value with 0 if domestic takings or international takings is null
QUERY = """
SELECT movie_id,
(COALESCE(domestic_takings, 0) + COALESCE(international_takings, 0)) AS total_takings
FROM movie_revenues;
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
import json
import pandas as pd
import psycopg2 as pg


# SELECT SUBSTRING('string to be parsed', from, count)

# substring counts from 2nd character and count 6 characters in total
QUERY = """
SELECT SUBSTRING('long string', 2, 6)
"""

QUERY = """
SELECT first_name, SUBSTRING(first_name, 3, 4) FROM actors;
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
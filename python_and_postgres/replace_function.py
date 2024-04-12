import json
import pandas as pd
import psycopg2 as pg


# SELECT REPLACE('source string', 'old string', 'new string)

QUERY = """
SELECT REPLACE('a cat plays with another cat', 'cat', 'dog');
"""

QUERY = """
SELECT first_name, last_name, REPLACE(gender, 'M', 'Male') FROM actors;
"""

QUERY = """
UPDATE directors
SET nationality = REPLACE(nationality, 'American', 'USA')
WHERE nationality = 'American';
"""

QUERY = """
UPDATE directors
SET nationality = REPLACE(nationality, 'Brit', 'Engl')
WHERE nationality = 'British';
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

        # column_names = [col.name for col in cursor.description]
        # result = pd.DataFrame(cursor.fetchall(), columns=column_names)
        # print(result)
        
    except (Exception, pg.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == '__main__':
    main()
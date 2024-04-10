import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT last_name AS surname FROM directors;
"""

# Error: can't use alias in conditionals but original column names are allowed
QUERY2 = """
SELECT last_name AS surname FROM directors
WHERE surname = 'Anderson';
"""

QUERY3 = """
SELECT last_name AS surname FROM directors
WHERE last_name LIKE 'A%'
ORDER BY surname;
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
        
        select(cursor, QUERY2)
        
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
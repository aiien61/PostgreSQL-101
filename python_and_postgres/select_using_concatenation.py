import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT 'concat' || 'together' AS new_string;
"""

QUERY2 = """
SELECT 'concat' || ' ' || 'together' AS new_string;
"""

QUERY3 = """
SELECT CONCAT(first_name, last_name) AS full_name FROM actors;
"""

QUERY4 = """
SELECT CONCAT(first_name, ' ',last_name) AS full_name FROM actors;
"""

QUERY5 = """
SELECT first_name || ' ' || last_name AS full_name FROM actors;
"""

QUERY6 = """
SELECT CONCAT_WS(' ', first_name, last_name) AS full_name FROM actors;
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
        
        select(cursor, QUERY6)
        
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
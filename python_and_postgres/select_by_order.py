import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT first_name, last_name, date_of_birth FROM actors
ORDER BY first_name;
"""

QUERY2 = """
SELECT first_name, last_name, date_of_birth FROM actors
ORDER BY first_name DESC;
"""

QUERY3 = """
SELECT first_name, last_name, date_of_birth FROM actors
ORDER BY first_name ASC;
"""

QUERY4 = """
SELECT actor_id, first_name, last_name, date_of_birth FROM actors
ORDER BY actor_id DESC;
"""

QUERY5 = """
SELECT actor_id, first_name, last_name, date_of_birth FROM actors
ORDER BY date_of_birth;
"""

QUERY6 = """
SELECT actor_id, first_name, last_name, date_of_birth FROM actors
WHERE gender = 'F'
ORDER BY date_of_birth DESC;
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
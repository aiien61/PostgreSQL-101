import json
import pandas as pd
import psycopg2 as pg

# NULLIF FUNCTION
# Return a NULL value if both arguments are equal, otherwise it returns the first argument

QUERY = """
SELECT NULLIF('A', 'A');
"""

QUERY = """
SELECT NULLIF('A', 'B');
"""

QUERY = """
SELECT NULLIF('B', 'A');
"""

# Both arguments must be convertable to a common data type

# Error
QUERY = """
SELECT NULLIF('A', 1);
"""

QUERY = """
SELECT NULLIF(1.0, 1);
"""

QUERY = """
SELECT NULLIF(1.0, 2);
"""

QUERY = """
SELECT first_name, last_name,
NULLIF(last_name, 'Anderson') AS "Mr Anderson"
FROM directors;
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
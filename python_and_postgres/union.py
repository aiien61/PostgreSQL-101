import json
import pandas as pd
import psycopg2 as pg


# SQL: Must select same number of columns from both tables, and columns selected
# from both tables must be corresponding to each other e.g. compatible data type

# SELECT column1, column2 FROM table1
# UNION
# SELECT column1, column2 FROM table2

QUERY = """
SELECT first_name, last_name FROM directors
UNION
SELECT first_name, last_name FROM actors;
"""

QUERY = """
SELECT first_name, last_name FROM directors
WHERE nationality = 'American'
UNION
SELECT first_name, last_name FROM actors
WHERE gender = 'F';
"""

QUERY = """
SELECT first_name, last_name, date_of_birth FROM directors
WHERE nationality = 'American'
UNION
SELECT first_name, last_name, date_of_birth FROM actors
WHERE gender = 'F'
ORDER BY first_name;
"""


# Error: incompatible data type
QUERY = """
SELECT date_of_birth, last_name FROM directors
UNION
SELECT first_name, last_name FROM actors;
"""

# SELECT column1, column2 FROM table1
# UNION ALL
# SELECT column1, column2 FROM table2

# auto remove duplicated first names
QUERY = """
SELECT first_name FROM directors
UNION
SELECT first_name FROM actors
ORDER BY first_name;
"""

# auto keep duplicated first names
QUERY = """
SELECT first_name FROM directors
UNION ALL
SELECT first_name FROM actors
ORDER BY first_name;
"""

# UNION exclude duplicated records but UNION ALL include duplicated records

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
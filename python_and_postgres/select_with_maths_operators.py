import json
import pandas as pd
import psycopg2 as pg

# addition
QUERY = """
SELECT 5 + 6 AS addition;
"""

# subtraction
QUERY = """
SELECT 5 - 6 AS subtraction;
"""

# division
QUERY = """
SELECT 30 / 6 AS division;
"""

# doesn't return decimal part
QUERY = """
SELECT 31 / 6 AS division;
"""

# multiplication
QUERY = """
SELECT 5 * 6 AS multiplication;
"""

# modulus: return remainder
QUERY = """
SELECT 31 % 6 AS modulus;
"""

QUERY = """
SELECT movie_id, (domestic_takings + international_takings) AS total_takings FROM movie_revenues;
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
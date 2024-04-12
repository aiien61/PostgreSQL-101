import json
import pandas as pd
import psycopg2 as pg

# GREATEST and LEAST Functions

# Return the greatest and least values from a number of arguments

QUERY = """
SELECT GREATEST(1, 2, NULL, 3);
"""

QUERY = """
SELECT LEAST(1, 2, NULL, 3);
"""

QUERY = """
SELECT GREATEST('B', 'A', 'a', 'b', NULL, 'c', 'C');
"""

QUERY = """
SELECT LEAST('B', 'A', 'a', 'b', NULL, 'c', 'C');
"""

# PostgreSQL will ignore NULL values unless all values are NULL,
# then it will return NULL.

QUERY = """
SELECT movie_id, domestic_takings, international_takings, LEAST(domestic_takings, international_takings) AS smallest_market
FROM movie_revenues;
"""

QUERY = """
SELECT movie_id, domestic_takings, international_takings, GREATEST(domestic_takings, international_takings) AS biggest_market
FROM movie_revenues;
"""

QUERY = """
SELECT movie_id, domestic_takings, international_takings, GREATEST(domestic_takings, international_takings, 0) AS biggest_market
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
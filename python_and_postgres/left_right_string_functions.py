import json
import pandas as pd
import psycopg2 as pg

# return the first 5 characters from left hand side
QUERY = """
SELECT LEFT('string', 5);
"""

# mask the 4 characters from right end, and return the remaining left part
QUERY = """
SELECT LEFT('string', -4);
"""

QUERY = """
SELECT LEFT(movie_name, 5) FROM movies;
"""

# return the final 3 characters from right hand side
QUERY = """
SELECT RIGHT('example', 3);
"""

# mask the 3 characters from left end, and return the remaining right part
QUERY = """
SELECT RIGHT('example', -3);
"""

QUERY = """
SELECT RIGHT(first_name, 2) FROM actors;
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
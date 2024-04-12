import json
import pandas as pd
import psycopg2 as pg


# SELECT SPLIT_PART('string', 'delimiter', field_number)

# Return the first field after splitting the string
QUERY = """
SELECT SPLIT_PART('first_name.last_name@gmail.com', '@', 1);
"""

# Return the second field after splitting the string
QUERY = """
SELECT SPLIT_PART('first_name.last_name@gmail.com', '@', 2);
"""

QUERY = """
SELECT SPLIT_PART('first_name.last_name@gmail.com', '.', 3);
"""

QUERY = """
SELECT movie_name, SPLIT_PART(movie_name, ' ', 1) AS first_word FROM movies;
"""

QUERY = """
SELECT movie_name, 
SPLIT_PART(movie_name, ' ', 1) AS first_word,
SPLIT_PART(movie_name, ' ', 2) AS second_word
FROM movies;
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
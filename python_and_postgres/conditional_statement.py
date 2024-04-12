import json
import pandas as pd
import psycopg2 as pg


# SQL uses CASE EXPRESSIONS for conditional statements same as IF-ELSE syntax in other programming languages

# CASE
#     WHEN column_condition THEN do this
#     WHEN column_condition THEN do this
#     ELSE do this
# END column_name_alias


QUERY = """
SELECT movie_name, movie_length,
CASE
    WHEN movie_length > 150 THEN 'over 2.5 hours'
    WHEN movie_length > 90 THEN 'over 1.5 hours'
    ELSE '1.5 hours or under'
END movie_time_hours
FROM movies;
"""

QUERY = """
SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings > 300 THEN 'BOX OFFICE SMASH'
    WHEN domestic_takings > 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
END box_office_success
FROM movie_revenues;
"""

# domestic_takings null is being dealt with 
QUERY = """
SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings >= 300 THEN 'BOX OFFICE SMASH'
    WHEN domestic_takings >= 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
    ELSE 'MISSING INFO'
END box_office_success
FROM movie_revenues;
"""

QUERY = """
SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
    WHEN domestic_takings >= 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 300 THEN 'BOX OFFICE SMASH'
    ELSE 'MISSING INFO'
END box_office_success
FROM movie_revenues;
"""

QUERY = """
SELECT movie_id, domestic_takings, 
CASE
    WHEN domestic_takings >= 100 THEN 'BOX OFFICE HIT'
    WHEN domestic_takings >= 0 THEN 'BOX OFFICE FLOP'
    WHEN domestic_takings >= 300 THEN 'BOX OFFICE SMASH'
    ELSE 'MISSING INFO'
END box_office_success
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
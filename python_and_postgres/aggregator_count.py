import json
import pandas as pd
import psycopg2 as pg

QUERY1 = """
SELECT * FROM movie_revenues;
"""

# COUNT aggregation function doesn't count null values
QUERY2 = """
SELECT COUNT(international_takings) FROM movie_revenues;
"""

# Count total records that meet the specified condition
QUERY3 = """
SELECT COUNT(*) FROM movies
WHERE movie_lang = 'English';
"""

MyQuery = QUERY3

def select(cursor) -> None:
    cursor.execute(MyQuery)
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
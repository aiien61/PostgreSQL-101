import json
import pandas as pd
import psycopg2 as pg

# Subqueries are nested queries

# 1. The inner query executes first, and the result of the inner query are then passed to the outer query.
# 2. Subqueries can be nested inside a select, insert, update or delete query.
# 3. Subqueries can be used after FROM or WHERE
# 4. Two types of subquery: Uncorrelated and Correlated subqueries.
# 5. Uncorrelated Subqueries: The inner query could be executed on its own from the outer query.
# 6. Correlated Subqueries: The inner query references a table from the outer query, 
#    so the inner query can't be executed independently from the outer query.


# Correlated Subqueries
QUERY = """
SELECT mo1.movie_name, mo1.movie_lang, mo1.movie_length FROM movies mo1
WHERE mo1.movie_length =
(SELECT MAX(movie_length) FROM movies mo2
WHERE mo2.movie_lang = mo1.movie_lang);
"""

QUERY = """
SELECT d1.first_name, d1.last_name, d1.date_of_birth, d1.nationality
FROM directors d1
WHERE d1.date_of_birth = 
(SELECT MIN(date_of_birth) FROM directors d2
WHERE d2.nationality = d1.nationality);
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
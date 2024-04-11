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


# Uncorrelated Subqueries
QUERY = """
SELECT movie_name, movie_length FROM movies
WHERE movie_length >  
(SELECT AVG(movie_length) FROM movies)
ORDER BY movie_length DESC;
"""

QUERY = """
SELECT first_name, last_name, date_of_birth FROM directors
WHERE date_of_birth > 
(SELECT date_of_birth FROM directors
WHERE first_name = 'James' 
AND last_name = 'Cameron');
"""

QUERY = """
SELECT first_name, last_name, date_of_birth FROM directors
WHERE date_of_birth > 
(SELECT date_of_birth FROM actors
WHERE first_name = 'Tom' 
AND last_name = 'Cruise');
"""

QUERY = """
SELECT movie_name FROM movies
WHERE movie_id IN 
(SELECT movie_id FROM movie_revenues
WHERE international_takings > domestic_takings);
"""

QUERY = """
SELECT mo.movie_id, mo.movie_name, d.first_name, d.last_name FROM movies mo
JOIN directors d ON d.director_id = mo.director_id
WHERE mo.movie_id IN 
(SELECT movie_id FROM movie_revenues
WHERE international_takings > domestic_takings);
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
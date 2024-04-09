import json
import pandas as pd
import psycopg2 as pg


# any actor whose first name starts with P
QUERY1 = """
SELECT * FROM actors
WHERE first_name LIKE 'P%';
"""

# any actor whose first name starts with P and only followed by exactly one character
QUERY2 = """
SELECT * FROM actors
WHERE first_name LIKE 'P_';
"""

# any actor whose first name starts with P and only followed by exactly two characters
QUERY3 = """
SELECT * FROM actors
WHERE first_name LIKE 'P__';
"""

# any actor whose first name starts with Pe and only followed by exactly one character
QUERY4 = """
SELECT * FROM actors
WHERE first_name LIKE 'Pe_';
"""

# any actor whose first name ends with r
QUERY5 = """
SELECT * FROM actors
WHERE first_name LIKE '%r';
"""

# any actor whose first name contains r
QUERY6 = """
SELECT * FROM actors
WHERE first_name LIKE '%r%';
"""

# any actor whose first name contains rl
QUERY7 = """
SELECT * FROM actors
WHERE first_name LIKE '%rl%';
"""

# any actor whose first name contains rl in the middle and only has 4 characters
QUERY8 = """
SELECT * FROM actors
WHERE first_name LIKE '_rl_';
"""

# any actor whose first name contains rl in the middle and only has 5 characters
QUERY9 = """
SELECT * FROM actors
WHERE first_name LIKE '__rl_';
"""

# any actor whose first name contains rl in the middle and only has 6 characters
QUERY10 = """
SELECT * FROM actors
WHERE first_name LIKE '__rl__';
"""

def select(cursor, query) -> None:
    cursor.execute(query)
    return None


def main():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        
        connection = pg.connect(**config, dbname="movie_data")
        cursor = connection.cursor()
        
        select(cursor, QUERY10)
        
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
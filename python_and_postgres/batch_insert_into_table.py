import json
import psycopg2 as pg
from striprtf.striprtf import rtf_to_text


def batch_load(filename) -> str:
    with open(filename, 'r') as file:
        data = file.read()
        text = rtf_to_text(data)
    return text


def batch_insert(cursor, data) -> None:
    cursor.execute(data)
    return None


def main():
    with open("config.json", "r") as f:
        config = json.load(f)
    
    conn = pg.connect(**config, dbname="movie_data")
    cur = conn.cursor()

    directors_data = batch_load('data_to_input/INSERT_INTO_directors_script.rtf')
    batch_insert(cur, directors_data)

    actors_data = batch_load('data_to_input/INSERT_INTO_actors_script.rtf')
    batch_insert(cur, actors_data)

    movies_data = batch_load('data_to_input/INSERT_INTO_movies_script.rtf')
    batch_insert(cur, movies_data)

    movies_actors_data = batch_load('data_to_input/INSERT_INTO_movies_actors_script.rtf')
    batch_insert(cur, movies_actors_data)

    movie_revenues_data = batch_load('data_to_input/INSERT_INTO_movie_revenues_script.rtf')
    batch_insert(cur, movie_revenues_data)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
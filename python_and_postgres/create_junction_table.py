import json
import psycopg2 as pg

with open("config.json", "r") as f:
    config = json.load(f)

conn = pg.connect(**config, dbname="movie_data")
cur = conn.cursor()

cur.execute("""CREATE TABLE movies_actors (
    movie_id INT REFERENCES movies (movie_id),
    actor_id INT REFERENCES actors (actor_id),
    PRIMARY KEY (movie_id, actor_id)
);
""")

conn.commit()
cur.close()
conn.close()

import json
import psycopg2 as pg

with open("config.json", "r") as openfile:
	db_config = json.load(openfile)

conn = pg.connect(**db_config, dbname="movie_data")
cur = conn.cursor()

# Create the directors table
cur.execute("""CREATE TABLE IF NOT EXISTS directors (
	director_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30) NOT NULL,
	date_of_birth DATE,
	nationality VARCHAR(20)
);
""")

# Create the actors table
cur.execute("""CREATE TABLE IF NOT EXISTS actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30) NOT NULL,
    gender CHAR(1),
    date_of_birth DATE
);
""")

# Create the movies table
cur.execute("""CREATE TABLE IF NOT EXISTS movies (
	movie_id SERIAL PRIMARY KEY,
	movie_name VARCHAR(50) NOT NULL,
	movie_length INT,
	movie_lang VARCHAR(20),
	release_date DATE,
	age_certificate VARCHAR(5),
	director_id INT REFERENCES directors (director_id)
);
""")

# Create the movie_revenues table
cur.execute("""CREATE TABLE IF NOT EXISTS movie_revenues (
	revenue_id SERIAL PRIMARY KEY,
	movie_id INT REFERENCES movies (movie_id),
	domestic_takings NUMERIC(6, 2),
	international_takings NUMERIC(6, 2)
);
""")

conn.commit()
cur.close()
conn.close()

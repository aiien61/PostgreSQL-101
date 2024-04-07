import json
import psycopg2 as pg

with open("config.json", "r") as openfile:
	db_config = json.load(openfile)

conn = pg.connect(**db_config, dbname="owners_pets")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30) NOT NULL,
    city VARCHAR(30),
    state CHAR(2)
);
""")

cur.execute("""
CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    species VARCHAR(30),
    full_name VARCHAR(30),
    age INT,
    owner_id INT REFERENCES owners (id)
);
""")

cur.execute("""ALTER TABLE owners
ADD COLUMN email VARCHAR(50) UNIQUE;
""")

cur.execute("""ALTER TABLE owners
ALTER COLUMN last_name TYPE VARCHAR(50);
""")

conn.commit()
cur.close()
conn.close()
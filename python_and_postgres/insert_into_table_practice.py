import json
import psycopg2 as pg

with open("config.json", "r") as f:
    config = json.load(f)

conn = pg.connect(**config, dbname="test")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS examples (
	example_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(50),
    email VARCHAR(80) UNIQUE,
    nationality CHAR(3), 
    age INT NOT NULL
);
""")

# cur.execute("""INSERT INTO examples (first_name, last_name, email, nationality, age)
# VALUES ('David', 'Mitchell', 'dmitch@gmail.com', 'GBR', 43);
# """)

cur.execute("""INSERT INTO examples (first_name, last_name, email, nationality, age)
VALUES ('Emily', 'Watson', 'ewatson@gmail.com', 'USA', 29),
('Theo', 'Scott', 'tscott@gmail.com', 'AUS', 33),
('Emily', 'Smith', 'esmith@gmail.com', 'GBR', 29),
('Jim', 'Burr', 'jburr@gmail.com', 'USA', 54);
""")

conn.commit()
cur.close()
conn.close()
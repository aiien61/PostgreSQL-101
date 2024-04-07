import json
import psycopg2 as pg

with open("config.json", "r") as f:
    config = json.load(f)

conn = pg.connect(**config, dbname="test")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS examples (
	example_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30)
);
""")

# modifying tables and add a column

cur.execute("""ALTER TABLE examples
ADD COLUMN email VARCHAR(50) UNIQUE;
""")

cur.execute("""ALTER TABLE examples
ADD COLUMN nationality VARCHAR(30), 
ADD COLUMN age INT NOT NULL;
""")

# modifying a column data type

cur.execute("""ALTER TABLE examples
ALTER COLUMN nationality TYPE CHAR(3); 
""")

cur.execute("""ALTER TABLE examples
ALTER COLUMN last_name TYPE VARCHAR(50),
ALTER COLUMN email TYPE VARCHAR(80);
""")

conn.commit()
cur.close()
conn.close()

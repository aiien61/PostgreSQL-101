import json
import psycopg2 as pg

with open("config.json", "r") as f:
    config = json.load(f)

conn = pg.connect(**config, dbname="test")
cur = conn.cursor()

# delete tables from a database
cur.execute("""CREATE TABLE IF NOT EXISTS practice (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(50),
    product_price NUMERIC(4, 2)
);
""")

cur.execute("""DROP TABLE practice;""")

conn.commit()
cur.close()
conn.close()
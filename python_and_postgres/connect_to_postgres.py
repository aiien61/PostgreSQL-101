import psycopg2 as pg

conn = pg.connect(
    host="localhost", dbname="postgres", user="postgres", 
    password="YOUR_PASSWORD_FOR_POSTGRES", port=5432
)

cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     id INT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     gender CHAR
# );
# """)

# cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
# (1, 'Mike', 30, 'M'),
# (2, 'Lisa', 33, 'F'),
# (3, 'John', 31, 'M'),
# (4, 'Bob', 51, 'M'),
# (5, 'Julie', 27, 'F');
# """)

cur.execute("""SELECT * FROM person WHERE name='Bob';
""")

print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age < 50;
""")

print(cur.fetchall())

cur.execute("""SELECT * FROM person WHERE gender = 'M';
""")

for row in cur.fetchall():
    print(row)

sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ('J', 30))
print(sql)
cur.execute(sql)
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
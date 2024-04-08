import json
import psycopg2 as pg


def batch_insert_owners(connection, cursor) -> None:
    cursor.execute("""INSERT INTO owners (first_name, last_name, city, state, email) VALUES
    ('Samuel', 'Smith', 'Boston', 'MA', 'samsmith@gmail.com'),
    ('Emma', 'Johnson', 'Seattle', 'WA', 'emjohnson@gmail.com'),
    ('John', 'Oliver', 'New York', 'NY', 'johnoliver@gmail.com'),
    ('Olivia', 'Brown', 'San Francisco', 'CA', 'oliviabrown@gmail.com'),
    ('Simon', 'Smith', 'Dallas', 'TX', 'sismith@gmail.com'),
    (null, 'Maxwell', null, 'CA', 'lordmaxwell@gmail.com');
    """)
    connection.commit()
    return None

def batch_insert_pets(connection, cursor) -> None:
    cursor.execute("""INSERT INTO pets (species, full_name, age, owner_id) VALUES
    ('Dog', 'Rex', 6, 1),
    ('Rabbit', 'Fluffy', 2, 5),
    ('Cat', 'Tom', 8, 2),
    ('Mouse', 'Jerry', 2, 2),
    ('Dog', 'Biggles', 4, 1),
    ('Tortoise', 'Squirtle', 42, 3);
    """)
    connection.commit()
    return None

def update_pet(connection, cursor) -> None:
    cursor.execute("""UPDATE pets
    SET age = 3
    WHERE species = 'Rabbit' AND full_name = 'Fluffy';
    """)
    connection.commit()
    return None


def delete_owner(connection, cursor) -> None:
    cursor.execute("""DELETE FROM owners
    WHERE last_name = 'Maxwell';
    """)
    connection.commit()
    return None



def main():
    with open("config.json", "r") as f:
        config = json.load(f)
    
    conn = pg.connect(**config, dbname="owners_pets")
    cur = conn.cursor()

    batch_insert_owners(conn, cur)
    batch_insert_pets(conn, cur)

    update_pet(conn, cur)
    delete_owner(conn, cur)

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
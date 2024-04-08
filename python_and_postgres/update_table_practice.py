import json
import psycopg2 as pg


def main():
    with open("config.json", "r") as f:
        config = json.load(f)
    
    conn = pg.connect(**config, dbname="test")
    cur = conn.cursor()

    update_name(cur)
    
    conn.commit()
    cur.close()
    conn.close()


def update_email(cursor) -> None:
    cursor.execute("""UPDATE examples
    SET email = 'davidmitchell@gmail.com'
    WHERE example_id = 1;
    """)

    return None

def update_nationality(cursor) -> None:
    cursor.execute("""UPDATE examples
    SET nationality = 'CAN'
    WHERE nationality = 'USA';
    """)

    return None


def update_name(cursor) -> None:
    cursor.execute("""UPDATE examples
    SET first_name = 'James', age = 55
    WHERE example_id = 5;
    """)

    return None

if __name__ == '__main__':
    main()

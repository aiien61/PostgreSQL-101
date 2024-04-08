import json
import psycopg2 as pg


def delete_row_by_id(cursor) -> None:
    cursor.execute("""DELETE FROM examples
    WHERE example_id = 2;
    """)

    return None


def delete_row_by_nationality(cursor) -> None:
    cursor.execute("""DELETE FROM examples
    WHERE nationality = 'GBR';
    """)

    return None


def delete_all_rows(cursor) -> None:
    cursor.execute("""DELETE FROM examples;""")

    return None


def main():
    with open("config.json", "r") as f:
        config = json.load(f)
    
    conn = pg.connect(**config, dbname="test")
    cur = conn.cursor()

    delete_all_rows(cur)
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()

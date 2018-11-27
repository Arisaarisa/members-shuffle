import sqlite3


def main():
    conn = sqlite3.connect("members.sqlite")
    cursor = conn.cursor()

    sql = """ CREATE TABLE members (
                name TEXT
                )"""

    cursor.executescript(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()

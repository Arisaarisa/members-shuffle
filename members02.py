import sqlite3


def main():
    conn = sqlite3.connect("members.sqlite")

    cursor = conn.cursor()

    sql = """INSERT INTO members (name) VALUES ('
                '内田',
                '大江',
                '則也',
                '美香子',
                '鹿糠',
                '川合',
                '工藤',
                '杉村',
                '高橋',
                '中川',
                '中俣',
                '松本',
                '三村',
                '横川',
                '吉田'
            )"""

    cursor.executescript(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()
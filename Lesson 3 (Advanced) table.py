import sqlite3 as sq


with sq.connect('my_table.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS tables")
    cur.execute("""CREATE TABLE IF NOT EXISTS tables(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        purchase TEXT,
        summa INTEGER,
        time INTEGER
        )""")
    cur.execute("""INSERT INTO tables(purchase, summa, time) VALUES('food', '560', '28112021');""")
    cur.execute("""INSERT INTO tables(purchase, summa, time) VALUES('dress', '1100', '7112021');""")
    cur.execute("""INSERT INTO tables(purchase, summa, time) VALUES('water', '20', '27112021');""")
    for row in cur.execute("SELECT * FROM tables;"):
        print(row)

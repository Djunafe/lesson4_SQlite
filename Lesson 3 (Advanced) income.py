import sqlite3 as sq

with sq.connect("my_list.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS lists")
    cur.execute("""CREATE TABLE IF NOT EXISTS lists(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            purchase TEXT,
            summa INTEGER,
            time INTEGER
            )""")
    cur.execute('ALTER TABLE lists ADD COLUMN income INTEGER')
    cur.execute("""INSERT INTO lists(purchase, summa, time, income) VALUES('food', '560', '28.11.2021', '1200');""")
    cur.execute("""INSERT INTO lists(purchase, summa, time, income) VALUES('dress', '1100', '7.11.2021', '2300');""")
    cur.execute("""INSERT INTO lists(purchase, summa, time, income) VALUES('water', '20', '27.11.2021', '1240');""")


for row in cur.execute('SELECT * FROM lists'):
    print(row)



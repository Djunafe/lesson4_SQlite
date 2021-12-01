import click
import sqlite3 as sq


@click.group()
def cli():
    pass


@click.command()
def data():
    with sq.connect('my_table.db') as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS tables")
        cur.execute("""CREATE TABLE IF NOT EXISTS tables(
                table_id INTEGER PRIMARY KEY AUTOINCREMENT,
                purchase TEXT NOT NULL,
                price INTEGER NOT NULL,
                date
                )""")
        print("You connected to SQLite")
        question = input('Do you want to add ( yes / no ) : ')
        while question == 'yes':
            question_1 = input("Enter purchase name: ")
            question_2 = input("Enter purchase price: ")
            question_3 = input("Enter purchase date (in format d.m.y): ")
            cur.execute("DROP TABLE IF EXISTS 'my_table'")
            cur.execute("INSERT INTO tables(purchase, price, date) VALUES(?, ?, ?)",
                        (question_1, question_2, question_3))
            question = input('Do you want to add ( yes / no ) : ')
        print("Yours values added to the db my_table", cur.rowcount)
        print("SQLite connection closed")


@click.command()
def select_pro():
    with sq.connect('my_table.db') as con:
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM tables WHERE price > 100"):
            print(row)


cli.add_command(data)
cli.add_command(select_pro)

if __name__ == '__main__':
    cli()

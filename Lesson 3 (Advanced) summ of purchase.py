"""Создайтб агрегатные функции для подсчёта общего количества расходов и расходов за месяц. Обеспечить соответствующий интерфейс для пользователя"""

import sqlite3 as sq


with sq.connect('my_table.db') as con:
    cur = con.cursor()


purchase_1 = input('Enter the start date of the period: ')
purchase_2 = input('Enter the end date of the period: ')
cur.execute('SELECT SUM(summa) FROM tables WHERE time BETWEEN ' + purchase_1 + ' AND ' + purchase_2)

all_results = cur.fetchall()
print('The amount of purchases for the selected period was', all_results)



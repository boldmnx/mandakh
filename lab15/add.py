from faker import Faker
import sqlite3 as sql


a = Faker()


def addData():
    for i in range(60):
        con = sql.connect('lab15.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(
            f'insert into test values(null ,"{a.name()}","{a.ascii_email()}")')
        con.commit()
        con.close()

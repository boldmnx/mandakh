import sqlite3 as sql

from faker import Faker


fk = Faker()
fk_addres=fk.ad
def insert_worker():
    for i in range(10):
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute(f'INSERT INTO branch VALUES(null, "{fk.address()}")')
            con.commit()

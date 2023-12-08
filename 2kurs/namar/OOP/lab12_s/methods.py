
from faker import Faker
import sqlite3 as sql

allowExt = set(['png', 'jpg', 'jpeg'])


def allowed_file(e):
    return '.' in e and e.split('.')[1].lower() in allowExt


b = Faker()


def addData():
    with sql.connect('mu.db') as con:
        cur = con.cursor()
        for i in range(23):
            cur.execute(
                f'insert into hicheel values(null,"{b.name()}","{b.country()}",1,1)')
            con.commit()


# addData()

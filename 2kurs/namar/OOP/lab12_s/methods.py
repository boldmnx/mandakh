
from faker import Faker
import hashlib
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


def hash(some):
    hash256 = hashlib.sha256()
    hash256.update(some.encode('utf-8'))
    hashPass = hash256.hexdigest()
    return hashPass


# print(hash('1234'))

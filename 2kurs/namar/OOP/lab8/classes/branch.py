import sqlite3 as sql


class Branch:
    def __init__(self):
        pass

    def getRecords(self):
        with sql.connect('data/employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM branch')
            data = cur.fetchall()
        return data

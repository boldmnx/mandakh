import sqlite3


class Branch:
    def __init__(self):
        pass

    def getRecord(self, id):
        pass

    def getRecords(self):
        with sqlite3.connect('data/Employee.db') as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM tbl_branch')
            data = cur.fetchall()
        return data

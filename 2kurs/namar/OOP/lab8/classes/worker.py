import sqlite3


class Worker:
    def __init__(self):
        pass

    def getRecord(self, id):
        with sqlite3.connect('data/Employee.db') as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(f'\
                SELECT *\
                FROM tbl_worker\
                INNER JOIN tbl_branch \
                ON tbl_worker.b_id = {id}')
            data = cur.fetchall()
            return data

    def getRecords(self):
        with sqlite3.connect('data/Employee.db') as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(
                '''SELECT *
                FROM tbl_worker
                INNER JOIN tbl_branch 
                ON tbl_worker.b_id = tbl_branch.bid''')
            data = cur.fetchall()
        return data

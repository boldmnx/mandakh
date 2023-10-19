import sqlite3 as sql
import json


class Worker:
    def __init__(self) -> None:
        pass

    def getRecord(self, id):
        with sql.connect('data/employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('''
                        SELECT w.id,
                            w.name,
                            b.bname
                        FROM worker AS w
                            INNER JOIN branch AS b ON w.b_id = b.id
                        WHERE w.id = '''+id+'''''')
            data = cur.fetchone()
            return data

    def getRecords(self):
        with sql.connect('data/employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('''
                SELECT w.id,w.name,b.bname
                FROM worker AS w
                INNER JOIN branch AS b 
                ON w.b_id = b.id''')
            data = cur.fetchall()
        return data

import json
import sqlite3 as sql


class Branch:
    def __init__(self):
        pass

    def getItems(self):
        with sql.connect('employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM branch')
            data = cur.fetchall()
        return data


class Worker:
    def __init__(self):
        pass

    def addItem(self, name, b_id):
        try:
            with sql.connect('employee.db') as con:
                cur = con.cursor()
                cur.execute(
                    f'INSERT INTO worker VALUES(null, "{name}", {b_id})')
                con.commit()
            print('Амжилттай')
        except Exception as e:
            print(f'Таны алдаа: {e}')

    def getItems(self):
        with sql.connect('employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('''
                SELECT w.id,w.name,b.bname
                FROM worker AS w
                INNER JOIN branch AS b 
                ON w.b_id = b.id''')
            data = cur.fetchall()
        return data

    # def getItem(self, id):
    #     with sql.connect('data/employee.db') as con:
    #         con.row_factory = sql.Row
    #         cur = con.cursor()
    #         cur.execute('''
    #                     SELECT w.id,
    #                         w.name,
    #                         b.bname
    #                     FROM worker AS w
    #                         INNER JOIN branch AS b ON w.b_id = b.id
    #                     WHERE w.id = '''+id+'''''')
    #         data = cur.fetchone()
    #         return data

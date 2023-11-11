import json
import sqlite3 as sql


class Branch:
    def __init__(self):
        pass

    def get_all(self):
        with sql.connect('employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM branch')
            data = cur.fetchall()
        return data

    def add(self, name):
        try:
            with sql.connect('employee.db') as con:
                cur = con.cursor()
                cur.execute(f'INSERT INTO branch VALUES(null,"{name}")')
                con.commit()
            return 'Amjiltai'
        except:
            return 'Aldaa: ' + con.rollback

    def get(self, id):
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM branch WHERE id={id}')
            data = cur.fetchone()
        return data[1]

    def edit(self, id, name):
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute(
                f'UPDATE branch SET bname = "{name}" WHERE id = {id}')
            con.commit()
        return print("Amjilttai zaslaa")

    def delete(self, id):
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute(f'DELETE FROM branch WHERE id={id}')
            con.commit()


class Worker:
    def __init__(self):
        pass

    def add(self, name, b_id):
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute(
                f'INSERT INTO worker VALUES(null, "{name}", {b_id})')
            con.commit()

    def get_all(self):
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

    def edit(self, id,  name, b_id):
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute(
                f'UPDATE worker SET name = "{name}", b_id={b_id} WHERE id = {id}')
            con.commit()
        return 'aa'

    def get(self, id):
        with sql.connect('employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(
                f'SELECT * FROM worker w INNER JOIN branch b ON w.b_id = b.id WHERE w.id = {id}')
            data = cur.fetchone()
        return data

    def delete(self, id):
        with sql.connect('employee.db') as con:
            cur = con.cursor()
            cur.execute(f'DELETE FROM worker WHERE id={id}')
            con.commit()

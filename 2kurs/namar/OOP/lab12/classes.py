import sqlite3 as sql


class Alban:
    def getRecords(self):
        try:
            with sql.connect('mu.db') as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute('SELECT * FROM alban')
                msg = cur.fetchall()
        except sql.Error as e:
            msg = 'amjiltgui: '+str(e)
        finally:
            return msg

    def getRecord(self, id):
        try:
            with sql.connect('mu.db') as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute(f'SELECT * FROM alban WHERE aid={id}')
                msg = cur.fetchone()
        except sql.Error as e:
            msg = 'amjiltgui: '+str(e)
        finally:
            return msg

    def add(self, name):
        try:
            albanD = Alban()
            datas = albanD.getRecords()
            j = 1
            for i in datas:
                if i[0] != j:
                    with sql.connect('mu.db') as con:
                        cur = con.cursor()
                        cur.execute('INSERT INTO alban VALUES(?,?)', (j, name))
                        con.commit()
                        break
                j += 1
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO alban VALUES(?,?)', (j, name))
                con.commit()
            msg = 'amjiltai', 'success'
        except sql.Error as e:
            msg = str(e), 'error'
        finally:
            return msg

    def edit(self, id, name):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'UPDATE alban SET aname="{name}" WHERE aid={id}')
                con.commit()
                msg = 'amjiltai'
        except sql.Error as e:
            msg = 'amjiltgui: '+str(e)
        finally:
            return msg

    def delete(self, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM alban WHERE aid={id}')
                con.commit()
                msg = 'amjiltai', 'success'
        except sql.Error as e:
            msg = (str(e)+'error')
        finally:
            return msg

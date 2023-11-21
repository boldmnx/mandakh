import sqlite3 as sql
from flask import flash, Flask


class MU:
    def getRecords(self, table):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {table}')
            datas = cur.fetchall()
        return datas

    def getRecord(self, id):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM tenhim WHERE tid={id}')
            datas = cur.fetchone()
        return datas[1]

    def add(self, table, value):
        try:
            tenhimD = Tenhim()
            datas = tenhimD.getRecords()
            j = 1
            for i in datas:
                if i[0] != j:
                    with sql.connect('mu.db') as con:
                        cur = con.cursor()
                        cur.execute(
                            f'INSERT INTO {table} VALUES({j},"{value}")')
                        con.commit()
                        flash('amjilttai nemegdleei', 'success')
                        break
                j += 1
            if len(datas) < j:
                with sql.connect('mu.db') as con:
                    cur = con.cursor()
                    cur.execute(
                        f'INSERT INTO {table} VALUES({j},"{value}")')
                    con.commit()
                    flash('amjilttai nemegdleeij', 'success')
        except:
            con.rollback()
            flash('ustgaj chdsangui', 'danger')

    def edit(self, table, id, value):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()        # aname iig clientees how to get??
                
                cur.execute(
                    f'UPDATE {table} SET tname="{value}" WHERE tid={id}')
                con.commit()
                flash('amjilttai zaswarllaa', 'success')
        except:
            con.rollback()
            flash('zaswarlahd aldaa garlaa', 'danger')

    def delete(self, table, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM {table} WHERE tid={id}')
                con.commit()
            flash('amjilttai ustgalaa', 'success')
        except:
            con.rollback()
            flash('ustgaj chadsangui', 'danger')


class Mergejil:
    def getRecords(self, table):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {table}')
            datas = cur.fetchall()
        return datas

    def getRecord(self, id):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM mergejil WHERE mid={id}')
            datas = cur.fetchone()
        return datas[1]

    def add(self, name):
        try:
            mergejilD = Mergejil()
            datas = mergejilD.getRecords()
            j = 1
            for i in datas:
                if i[0] != j:
                    with sql.connect('mu.db') as con:
                        cur = con.cursor()
                        cur.execute(
                            f'INSERT INTO mergejil VALUES({j},"{name}")')
                        con.commit()
                        flash('amjilttai nemegdleei', 'success')
                        break
                j += 1
            if len(datas) < j:
                with sql.connect('mu.db') as con:
                    cur = con.cursor()
                    cur.execute(
                        f'INSERT INTO mergejil VALUES({j},"{name}")')
                    con.commit()
                    flash('amjilttai nemegdleeij', 'success')
        except:
            con.rollback()
            flash('ustgaj chdsangui', 'danger')

    def edit(self, id, name):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(
                    f'UPDATE mergejil SET mname="{name}" WHERE mid={id}')
                con.commit()
                flash('amjilttai zaswarllaa', 'success')
        except:
            con.rollback()
            flash('zaswarlahd aldaa garlaa', 'danger')

    def delete(self, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM mergejil WHERE mid={id}')
                con.commit()
            flash('amjilttai ustgalaa', 'success')
        except:
            con.rollback()
            flash('ustgaj chadsangui', 'danger')


class Tenhim:
    def getRecords(self):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM tenhim')
            datas = cur.fetchall()
        return datas

    def getRecord(self, id):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM tenhim WHERE tid={id}')
            datas = cur.fetchone()
        return datas[1]

    def add(self, name):
        try:
            tenhimD = Tenhim()
            datas = tenhimD.getRecords()
            j = 1
            for i in datas:
                if i[0] != j:
                    with sql.connect('mu.db') as con:
                        cur = con.cursor()
                        cur.execute(f'INSERT INTO tenhim VALUES({j},"{name}")')
                        con.commit()
                        flash('amjilttai nemegdleei', 'success')
                        break
                j += 1
            if len(datas) < j:
                with sql.connect('mu.db') as con:
                    cur = con.cursor()
                    cur.execute(
                        f'INSERT INTO tenhim VALUES({j},"{name}")')
                    con.commit()
                    flash('amjilttai nemegdleeij', 'success')
        except:
            con.rollback()
            flash('ustgaj chdsangui', 'danger')

    def edit(self, id, name):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'UPDATE tenhim SET tname="{name}" WHERE tid={id}')
                con.commit()
                flash('amjilttai zaswarllaa', 'success')
        except:
            con.rollback()
            flash('zaswarlahd aldaa garlaa', 'danger')

    def delete(self, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM tenhim WHERE tid={id}')
                con.commit()
            flash('amjilttai ustgalaa', 'success')
        except:
            con.rollback()
            flash('ustgaj chadsangui', 'danger')


class Zereg:
    def getRecords(self):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM zereg')
            datas = cur.fetchall()
        return datas

    def getRecord(self, id):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM zereg WHERE zid={id}')
            datas = cur.fetchone()
        return datas[1]

    def add(self, name):
        try:
            zeregD = Zereg()
            datas = zeregD.getRecords()
            j = 1
            for i in datas:
                if i[0] != j:
                    with sql.connect('mu.db') as con:
                        cur = con.cursor()
                        cur.execute(f'INSERT INTO zereg VALUES({j},"{name}")')
                        con.commit()
                        flash('amjilttai nemegdleei', 'success')
                        break
                j += 1
            if len(datas) < j:
                with sql.connect('mu.db') as con:
                    cur = con.cursor()
                    cur.execute(
                        f'INSERT INTO zereg VALUES({j},"{name}")')
                    con.commit()
                    flash('amjilttai nemegdleeij', 'success')
        except:
            con.rollback()
            flash('ustgaj chdsangui', 'danger')

    def edit(self, id, name):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'UPDATE zereg SET zname="{name}" WHERE zid={id}')
                con.commit()
                flash('amjilttai zaswarllaa', 'success')
        except:
            con.rollback()
            flash('zaswarlahd aldaa garlaa', 'danger')

    def delete(self, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM zereg WHERE zid={id}')
                con.commit()
            flash('amjilttai ustgalaa', 'success')
        except:
            con.rollback()
            flash('ustgaj chadsangui', 'danger')


class Alban:
    def getRecords(self):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM alban')
            datas = cur.fetchall()
        return datas

    def getRecord(self, id):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM alban WHERE aid={id}')
            datas = cur.fetchone()
        return datas[1]

    def add(self, name):
        try:
            albanD = Alban()
            datas = albanD.getRecords()
            j = 1
            for i in datas:
                if i[0] != j:
                    with sql.connect('mu.db') as con:
                        cur = con.cursor()
                        cur.execute(f'INSERT INTO alban VALUES({j},"{name}")')
                        con.commit()
                        flash('amjilttai nemegdleei', 'success')
                        break
                j += 1
            if len(datas) < j:
                with sql.connect('mu.db') as con:
                    cur = con.cursor()
                    cur.execute(
                        f'INSERT INTO alban VALUES({j},"{name}")')
                    con.commit()
                    flash('amjilttai nemegdleeij', 'success')
        except:
            con.rollback()
            flash('ustgaj chdsangui', 'danger')

    def edit(self, id, name):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'UPDATE alban SET aname="{name}" WHERE aid={id}')
                con.commit()
                flash('amjilttai zaswarllaa', 'success')
        except:
            con.rollback()
            flash('zaswarlahd aldaa garlaa', 'danger')

    def delete(self, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'DELETE FROM alban WHERE aid={id}')
                con.commit()
            flash('amjilttai ustgalaa', 'success')
        except:
            con.rollback()
            flash('ustgaj chadsangui', 'danger')

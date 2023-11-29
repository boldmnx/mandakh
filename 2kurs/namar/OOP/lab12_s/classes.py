import sqlite3 as sql
from flask import flash, Flask


class Oyutan:

    def getRecords(self):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'''SELECT *
                            FROM oyutan b
                                INNER JOIN tenhim t ON t.tid = b.tcode
                        ''')
            data = cur.fetchall()
        return data

    def getRecord(self, id):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'''SELECT *
                            FROM oyutan b
                                INNER JOIN tenhim t ON t.tid = b.tcode
                            where id = {id}''')
            data = cur.fetchone()
        return data

    def add(self, scode, sovog, sner, gender, elssen, register, tcode, mcode, simage):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'''insert into oyutan
                                values(
                                        null,
                                        "{scode}",
                                        "{sovog}",
                                        "{sner}",
                                        "{gender}",
                                        "{elssen}",
                                        "{register}",
                                        { tcode },
                                        { mcode },
                                        "{simage}"
                                    )''')
                con.commit()
            flash('Амжилттай нэмэгдлээ.', 'success')
        except:
            con.rollback()
            flash(f'Алдаа гарлаа.', 'danger')

    def edit(self, id, scode, sovog, sner, gender, elssen, tcode, mcode, simage, register):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'''update oyutan
                                set scode = "{scode}",
                                    sovog = "{sovog}",
                                    sner = "{sner}",
                                    gender = "{gender}",
                                    elssen = "{elssen}",
                                    register = "{register}",
                                    tcode = {tcode},
                                    mcode = {mcode},
                                    simage = '{simage}'
                                WHERE id = {id}''')
                con.commit()
            flash('Амжилттай засварлалаа.', 'success')
        except sql as er:
            con.rollback()
            flash('Засварлахад алдаа гарлаа.'+er, 'danger')

    def delete(self, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(F'''delete from oyutan
                                where id = {id}''')
                con.commit()
            flash('Амжилттай устгалаа.', 'success')
        except:
            con.rollback()
            flash('Устгахад алдаа гарлаа.', 'danger')

class Bagsh:

    def getRecords(self):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'''SELECT *
                            FROM bagsh b
                                INNER JOIN tenhim t ON t.tid = b.tcode
                        ''')
            data = cur.fetchall()
        return data

    def getRecord(self, id):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'''SELECT *
                            FROM bagsh b
                                INNER JOIN tenhim t ON t.tid = b.tcode
                            where id = {id}''')
            data = cur.fetchone()
        return data

    def add(self, bcode, bovog, bner, gender, ajild_orson, tcode, atcode, ecode):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'''insert into bagsh
                                values(
                                        null,
                                        "{bcode}",
                                        "{bovog}",
                                        "{bner}",
                                        "{gender}",
                                        "{ajild_orson}",
                                        {atcode},
                                        {ecode},
                                        {tcode}
                                    )''')
                con.commit()
            flash('Амжилттай нэмэгдлээ.', 'success')
        except:
            con.rollback()
            flash(f'Алдаа гарлаа.', 'danger')

    def edit(self, id, bcode, bovog, bner, gender, ajild_orson, atcode, ecode, tcode):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'''update bagsh
                                set bcode = "{bcode}",
                                    bovog = "{bovog}",
                                    bner = "{bner}",
                                    gender = "{gender}",
                                    ajild_orson = "{ajild_orson}",
                                    atcode = {atcode},
                                    ecode = {ecode},
                                    tcode = {tcode}
                                WHERE id = {id}''')
                con.commit()
            flash('Амжилттай засварлалаа.', 'success')
        except:
            con.rollback()
            flash('Засварлахад алдаа гарлаа.', 'danger')

    def delete(self, id):
        try:
            with sql.connect('mu.db') as con:
                cur = con.cursor()
                cur.execute(f'''delete from bagsh
                                where id = {id}''')
                con.commit()
            flash('Амжилттай устгалаа.', 'success')
        except:
            con.rollback()
            flash('Устгахад алдаа гарлаа.', 'danger')


class Mergejil:
    def getRecords(self):
        with sql.connect('mu.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM mergejil')
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
            flash('nemj chdsangui', 'danger')

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
                cur.execute(f'''DELETE FROM alban WHERE aid={id}''')
                con.commit()
            flash('amjilttai ustgalaa', 'success')
        except:
            con.rollback()
            flash('ustgaj chadsangui', 'danger')

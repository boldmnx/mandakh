from flask import Flask, render_template, request, redirect, url_for, abort
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/worker', methods=['GET', 'POST'])
def list_worker():
    if request.method == 'GET':
        with sql.connect('employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM branch')
            branch = cur.fetchall()
            cur.execute(
                f'SELECT * FROM worker INNER JOIN branch ON branch.bid=worker.bid')
            worker = cur.fetchall()

            return render_template('worker/list.html', branches=branch, workers=worker)
    elif request.method == 'POST':
        with sql.connect('employee.db') as con:
            wid = 1
            wname = request.form['wname']
            branch = request.form['branch']
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM worker')
            datas = cur.fetchall()
            if not datas:
                cur.execute(
                    f'INSERT INTO worker VALUES({wid},"{wname}",{branch})')
                con.commit()
            else:
                for i in datas:
                    if i['wid'] != wid:
                        cur.execute(
                            f'INSERT INTO worker VALUES({wid},"{wname}",{branch})')
                        con.commit()
                        break
                    wid += 1

            return redirect(url_for('list_worker'))


@app.route('/<int:wid>')
def delete_worker(wid):
    with sql.connect('employee.db') as con:
        cur = con.cursor()
        cur.execute(f'DELETE FROM worker WHERE wid={wid}')
        con.commit()
        return redirect(url_for('list_worker'))


if __name__ == '__main__':
    app.run(debug=True)

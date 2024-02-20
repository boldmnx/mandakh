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
            wname = request.form['wname']
            branch = request.form['branch']
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'SELECT * FROM worker')
            datas = cur.fetchall()

            if datas:
                existing_wids = {data['wid'] for data in datas}
                wid = 1
                # existing_wids dotor 3 bhgui bol davtalt shuud duusna
                while wid in existing_wids:
                    wid += 1

                cur.execute(f'INSERT INTO worker VALUES({
                            wid}, "{wname}", {branch})')

            else:
                cur.execute(
                    f'INSERT INTO worker VALUES(1, "{wname}", {branch})')

            return redirect(url_for('list_worker'))


@app.route('/worker/update<int:id>', methods=['GET', 'POST'])
def update_worker(id):
    if request.method == 'GET':
        with sql.connect('employee.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(
                f'select * from worker w inner join branch b on w.bid=b.bid where wid={id} ')
            data = cur.fetchone()
            cur.execute(f'select * from branch ')
            branches = cur.fetchall()
            return render_template('worker/update.html', data=data, branches=branches)
    elif request.method == 'POST':
        with sql.connect('employee.db') as con:
            wname = request.form['wname']
            bid = request.form['bid']
            cur = con.cursor()
            cur.execute(f'''update worker set wname="{
                        wname}", bid={bid} where wid={id}''')
            con.commit()
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

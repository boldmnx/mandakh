from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql
from faker import Faker

app = Flask(__name__)


def insertData():
    f = Faker()
    with sql.connect('exam.db') as con:
        cur = con.cursor()
        for i in range(30):
            cur.execute(f'''insert into user
                            values(null,'{f.name()}','{f.email()}')''')
            con.commit()


@app.route('/')
def index():
    with sql.connect('exam.db') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f'select * from user')
        data = cur.fetchall()
    return render_template('index.html', users=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        with sql.connect('exam.db') as con:
            cur = con.cursor()
            cur.execute(f'insert into user values(null,"{name}","{email}")')
            con.commit()
        return redirect(url_for('index'))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    id = request.args.get('id')
    if request.method == 'GET':
        with sql.connect('exam.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute(f'select * from user where id={id}')
            data = cur.fetchone()
        return render_template('edit.html', user=data)
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        with sql.connect('exam.db') as con:
            cur = con.cursor()
            cur.execute(
                f'update user set name="{name}", email="{email}" where id={id}')
            con.commit()
        return redirect(url_for('index'))


@app.route('/delete')
def delete():
    id = request.args.get('id')
    with sql.connect('exam.db') as con:
        cur = con.cursor()
        cur.execute(f'delete from user where id={id}')
        con.commit()
    return redirect(url_for('index'))


app.run(debug=True)

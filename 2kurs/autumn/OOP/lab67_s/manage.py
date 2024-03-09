from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def salbarInsert():
    if request.method == 'GET':
        with sql.connect('employer.db') as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM branch')
            branch = cur.fetchall()
        return render_template('index.html', branchs=branch)
    elif request.method == 'POST':
        con = sql.connect('employer.db')
        cur = con.cursor()
        sNer = request.form['sName']
        cur.execute(f'INSERT INTO branch VALUES(NOT NULL, "{sNer}")')
        con.commit()
        return redirect(url_for('salbarInsert'))
    return render_template('index.html')


# @app.route('/login')
# @app.route('/jishee')
# def log():
#     return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

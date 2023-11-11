from flask import Flask, flash, render_template, request, redirect, session, url_for
import sqlite3
import hashlib


def hash_pass(code):
    hash = hashlib.sha256()
    hash.update(code.encode('utf-8'))
    hashCode = hash.hexdigest()
    return hashCode


app = Flask(__name__)
app.secret_key = b'_5mdskmc]/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if not session:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            code = hash_pass(password)
            with sqlite3.connect('user.db') as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute(
                    f'SELECT * FROM user WHERE username="{username}" and password="{code}"')
                data = cur.fetchone()
                print(data)
                if data:
                    session['user'] = username
                    session['role'] = data[3]
                    flash('succesfully login')
                    return render_template('index.html')
                else:
                    flash('no such user')
                    return render_template('login.html')
    else:
        return redirect('/')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if not session:
        if request.method == 'GET':
            return render_template('register.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            repassword = request.form['repassword']
            if password == repassword:
                with sqlite3.connect('user.db') as con:
                    cur = con.cursor()

                    cur.execute(
                        f'INSERT INTO user VALUES(null, "{username}", "{hash_pass(password)}", 2')
                    con.commit()
                    flash('Succesfully signup')
                    return redirect(url_for('login'))
            else:
                flash('error password')
                return render_template('register.html')
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if '__main__' == __name__:
    app.run(debug=True)

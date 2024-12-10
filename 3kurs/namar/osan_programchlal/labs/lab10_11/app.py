from flask import Flask, jsonify, render_template, session, request, redirect, url_for, flash
from neo4j import GraphDatabase

app = Flask(__name__)

app.secret_key = 'sarnai_nomio-boldoo'

uri = 'bolt://localhost:7687'
username = 'neo4j'
password = 'admin123'


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            query = 'match(m:Movie) return m.title as title, m.img as img, m.released as released, m.tagline as tagline'
            movies, b, c = driver.execute_query(query)

            restjson = []

            for i in movies:

                restjson.append({
                    'title': i['title'],
                    'released': i['released']
                })

            return render_template('movie/movie.html', movies=restjson)


@app.route('/people', methods=['GET', 'POST'])
def people():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            query = 'match(p:Person) return p.name as name, p.img as img, p.born as born'
            person, b, c = driver.execute_query(query)

            restjson = []

            for i in person:

                restjson.append({
                    'name': i['name'],
                    'born': i['born']
                })

            return render_template('person/people.html', person=restjson)


@app.route('/')
def index():
    return render_template('index.html')
# index


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')

    elif request.method == 'POST':
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            ner = request.form['name']
            pwd = request.form['password']

            query = '''MATCH(p:Person{name:$name,password:$pwd}) return p.name as name, p.userRole as role'''

            person, b, c = driver.execute_query(query, name=ner, pwd=pwd)

            if not person:
                flash('Бүртгэлгүй хэрэглэгч байна')
                return redirect(url_for('login'))

            session['name'] = person[0]['name']
            session['role'] = person[0]['role']

            return redirect(url_for('index'))
# login


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
# logout


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('login/register.html')
    elif request.method == 'POST':
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            ner = request.form['name']
            role = request.form['role']
            pwd = request.form['password']
            repassword = request.form['repassword']

            if pwd != repassword:
                flash('Нууц үг таарсангүй')
                return redirect(url_for('register'))

            query = '''CREATE(p:Person{name:$name, password:$password, userRole:$role})  '''

            driver.execute_query(query, name=ner, password=pwd, role=role)

            return redirect(url_for('login'))
# register


if __name__ == '__main__':
    app.run(debug=True)

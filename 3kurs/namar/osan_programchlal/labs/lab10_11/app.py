from flask import Flask, jsonify, render_template, session, request, redirect, url_for, flash
from neo4j import GraphDatabase
from flask_paginate import Pagination
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'sarnai_nomio-boldoo'

uri = 'bolt://localhost:7687'
username = 'neo4j'
password = 'admin123'


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if not 'name' in session:
        return redirect(url_for('index'))

    elif request.method == 'POST':
        pass
    elif request.method == 'GET':

        limit = 6
        page = request.args.get('page', type=int, default=1)
        start = (page-1)*limit

        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            query = '''match(m:Movie) 
                        return m.title as title,
                        m.img as img,
                        m.released as released,
                        m.tagline as tagline, 
                        id(m) as mid'''
            moviePage, b, c = driver.execute_query(query)

            pn = Pagination(page=page, per_page=limit,
                            total=len(moviePage))

            pnQuery = '''MATCH(m:Movie) 
                        return m.title as title,
                        m.img as img,
                        m.released as released,
                        m.tagline as tagline, 
                        id(m) as mid skip $start limit $limit'''
            movies, summary, keys = driver.execute_query(
                pnQuery, start=start, limit=limit)

            return render_template('movie/movie.html', movies=movies, pn=pn, count=len(moviePage))
# movies


@app.route('/searchMovie', methods=['POST'])
def searchMovie():
    if not 'name' in session:
        return redirect(url_for('index'))

    elif request.method == 'POST':
        limit = 6
        page = request.args.get('page', type=int, default=1)
        start = (page-1)*limit

        with GraphDatabase.driver(uri=uri, auth=(username, password)) as driver:
            title = request.form['searchTitle']
            query = '''
                    MATCH(m:Movie)
                        WHERE toLower(m.title)=toLower($title)
                    return 
                        m.title as title,
                        m.img as img,
                        m.released as released,
                        m.tagline as tagline, 
                        id(m) as mid'''
            resultMovie, _, _ = driver.execute_query(query, title=title)
        return render_template('movie/movieSearch.html', resultMovie=resultMovie, countM=len(resultMovie), pn=None)


@app.route('/addMovie', methods=['POST', 'GET'])
def addMovie():
    if not 'name' in session:
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('movie/addMovie.html')
    elif request.method == 'POST':
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            title = request.form['title']
            img = request.files['img']
            released = request.form['released']
            tagline = request.form['tagline']

            if img:
                # img=title
                imgName = secure_filename(img.filename)
                pathImg = os.path.join('static/media/', imgName)
                print(f'##################################{imgName}')
                img.save()
            else:
                pathImg = 'default.jpg'

            query = '''MERGE(m:Movie{title: $title})
                            ON CREATE SET m={img: $img, released: $released, tagline: $tagline}
                            ON MATCH SET m.updateDate=''
                        return m.updateDate'''
            movieAdd, b, c = driver.execute_query(
                query, title=title, img=pathImg, released=released, tagline=tagline)

            if 'updateDate' in movieAdd:
                flash('Бүртгэлтэй кино байна', 'warning')
                return redirect(url_for('addMovie'))

            flash('Амжилттай кино бүргэгдлээ', 'success')
            return redirect(url_for('index'))


@app.route('/movieDetails/<int:mid>', methods=['GET', 'POST'])
def movieDetails(mid):
    if not 'name' in session:
        return redirect(url_for('index'))
    with GraphDatabase.driver(uri=uri, auth=(username, password)) as driver:
        query = '''MATCH (m:Movie)
                    WHERE id(m)=$mid
                    OPTIONAL MATCH    (m)-[:ACTED_IN]-(a:Person)
                    OPTIONAL MATCH    (m)-[:DIRECTED]-(d:Person)
                    OPTIONAL MATCH    (m)-[:REVIEWED]-(r:Person)
                    OPTIONAL MATCH    (m)-[:PRODUCED]-(p:Person)
                    OPTIONAL MATCH    (m)-[:WROTE]-(w:Person)
                RETURN 
                    m.title as name,m.img as img, m.released as released, id(m) as mid ,
                    COLLECT(DISTINCT a.name) as aname,
                    COLLECT(DISTINCT d.name) as dname,
                    COLLECT(DISTINCT r.name) as rname,
                    COLLECT(DISTINCT p.name) as pname,
                    COLLECT(DISTINCT w.name) as wname
                '''
        getMovie, b, c = driver.execute_query(query, mid=mid)

        return render_template('movie/movieDetail.html', getMovie=getMovie)


@app.route('/people', methods=['GET', 'POST'])
def people():
    if not 'name' in session:
        return redirect(url_for('index'))

    elif request.method == 'POST':
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
    if 'name' in session:
        return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('login/login.html')

    elif request.method == 'POST':
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            ner = request.form['name']
            pwd = request.form['password']

            query = '''MATCH(p:Person{name:$name,password:$pwd}) return p.name as name, p.userRole as role'''

            person, b, c = driver.execute_query(query, name=ner, pwd=pwd)

            if not person:
                flash('Бүртгэлгүй хэрэглэгч байна', 'warning')
                return redirect(url_for('login'))

            session['name'] = person[0]['name']
            session['role'] = person[0]['role']

            flash(f"Амжилттай нэмтэрлээ. {session['name']}", "success")

            return redirect(url_for('index'))
# login


@app.route('/logout')
def logout():
    if 'name' in session:
        session.clear()
        return redirect(url_for('index'))

# logout


@app.route('/register', methods=['GET', 'POST'])
def register():

    # session name key baugaa uguig shalghd if 'name' in session. Name yumtai uguig shalgajda if session['name']
    if 'name' in session:
        return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('login/register.html')

    elif request.method == 'POST':
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            ner = request.form['name']
            pwd = request.form['password']
            repassword = request.form['repassword']

            checkQuery = '''MATCH(p:Person{name:$name}) return p.name'''
            checkPerson, b, c = driver.execute_query(checkQuery, name=ner)

            if checkPerson:
                flash('Бүртгэлтэй хэрэглэгч байна', 'warning')
                return redirect(url_for('register'))

            if pwd != repassword:
                flash('Нууц үг таарсангүй', 'warning')
                return redirect(url_for('register'))

            query = '''CREATE(p:Person{name:$name, password:$password, userRole:2})  '''

            driver.execute_query(query, name=ner, password=pwd)

            flash('Амжилттай бүртгэгдлээ', 'success')
            return redirect(url_for('login'))
# register


if __name__ == '__main__':
    app.run(debug=True)

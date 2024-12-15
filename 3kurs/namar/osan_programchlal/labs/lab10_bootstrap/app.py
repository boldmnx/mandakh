from flask import Flask, jsonify, render_template, session, request, redirect, url_for, flash
from neo4j import GraphDatabase
from flask_paginate import Pagination
import os
from werkzeug.utils import secure_filename
import re



app = Flask(__name__)
app.secret_key = 'sarnai_nomio-boldoo'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# uri = 'neo4j+s://353cbf19.databases.neo4j.io'
# username = 'neo4j'
# password = 'FYqGqHbWq4pdWYCKXUtNRSHpaD56T-8mqIMeQI-tS9I'

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


@app.route('/searchMovie', methods=['POST', 'GET'])
def searchMovie():
    if not 'name' in session:
        return redirect(url_for('index'))
    elif request.method == 'POST':
        with GraphDatabase.driver(uri=uri, auth=(username, password)) as driver:
            title = request.form['searchTitle']
            query = '''
                    MATCH(m:Movie)
                        WHERE toLower(m.title)  CONTAINS toLower($title)
                    return 
                        m.title as title,
                        m.img as img,
                        m.released as released,
                        m.tagline as tagline, 
                        id(m) as mid'''
            resultMovie, _, _ = driver.execute_query(query, title=title)

            session['resultMovie'] = resultMovie
            session['countM'] = len(resultMovie)

        return render_template('movie/movieSearch.html', resultMovie=resultMovie, countM=len(resultMovie),)
    elif request.method == 'GET':

        jsonDetail = [{
            'title': session['resultMovie'][0][0],
            'img': session['resultMovie'][0][1],
            'released': session['resultMovie'][0][2],
            'tagline': session['resultMovie'][0][3],
            'mid': session['resultMovie'][0][4]
        }]

        return render_template('movie/movieSearch.html', resultMovie=jsonDetail, countM=session['countM'])
# searchMovie

@app.route('/addMember',methods=['GET','POST'])
def addMember():
    if not 'name' in session:
        return redirect(url_for('index'))
    elif request.method=='GET':
        with GraphDatabase.driver(auth=(username,password),uri=uri) as driver:

            allMovieQuery='''MATCH(m:Movie) return m.title as title'''
            data,_,_=driver.execute_query(allMovieQuery)
            
            allPersonQuery='''MATCH(m:Person) return m.name as name'''
            person,_,_=driver.execute_query(allPersonQuery)

            allRel='''MATCH (p:Person)-[r]->(m:Movie)
                        WHERE type(r) IN ['ACTED_IN', 'DIRECTED', 'PRODUCED', 'WROTE']
                    RETURN DISTINCT 
                        CASE 
                            WHEN type(r) = 'ACTED_IN' THEN 'Жүжигчин'  
                            WHEN type(r) = 'DIRECTED' THEN 'Найруулагч' 
                            WHEN type(r) = 'PRODUCED' THEN 'Продюсер'
                            WHEN type(r) = 'WROTE' THEN 'Зохиолч'  
                        END AS role, 
                        type(r) AS id
                    ''' 
            rel,_,_=driver.execute_query(allRel)
            return render_template('addMember.html',result=data,person=person,rel=rel)
    elif request.method=='POST':
        with GraphDatabase.driver(auth=(username,password),uri=uri) as driver:
            # Baazad movie bnuu
            clientMovie=request.form['movie']
            filterMovieQuery='''MATCH(m:Movie{title: $title}) return m.title as title'''
            dbMovie,_,_=driver.execute_query(filterMovieQuery,title=clientMovie)
            if not dbMovie:
                flash('Таны оруулсан кино баазад бүртгэлгүй байна','warning')        
                return redirect('/addMember')
        
            # Role bichsen bnuu
            role=request.form['role']
            relRole=request.form['roleName']
            rel=f'''{role}'''

            if not relRole and  'ACTED_IN' in role:
                flash('Жүжигчинг сонгосон бол та үүрэг role-уудаа бичиж оруулна уу','warning')
                return redirect('/addMember')
            elif 'ACTED_IN' in role:
                listRole=relRole.split(',')
                rel=f'''{role}{{role:{listRole}}}'''

            # Baazad hun bnuu
            clientName=request.form['name']
            filterPersonQuery='''MATCH(m:Person{name: $name}) return m.name as name'''
            dbPerson,_,_=driver.execute_query(filterPersonQuery,name=clientName)
            if not dbPerson:
                flash('Таны оруулсан хүн баазад бүртгэлгүй байна','warning')        
                return redirect('/addMember')
            
            
            addQuery=f'''MATCH(m:Movie{{title: '{clientMovie}'}}),(p:Person{{name: '{clientName}'}})
                        MERGE (m)<-[:{rel}]-(p)'''
            
            try :
                driver.execute_query(addQuery)
                flash('Амжилттай','success')
            except Exception as e:
                flash(f'Амжилтгүй: {e}','warning')
        return redirect('/addMember')
#addMember

@app.route('/addMovie', methods=['POST', 'GET'])
def addMovie():
    if not 'name' in session or not session['role'] == 1:
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
                if not "." in img.filename or img.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
                    flash(f'''Зурагны өргөтгөл зөвшөөрөлгүй байна.
                            Та зөвхөн дараах өргөтгөлтэй зурагуудыг оруулж болно:
                            {', '.join(ALLOWED_EXTENSIONS)}.''', 'warning')
                    return redirect(url_for('addMovie'))

                urgutgul = img.filename.rsplit('.', 1)[1].lower()

                secTitle = re.sub(r'[^\wа-яА-ЯөүӨҮ.]+', '_', f'{title}.{urgutgul}')
                pathImg = os.path.join('static/media/' + secTitle)
                img.save(pathImg)
            else:
                secTitle = 'image.png'

            query = '''MERGE(m:Movie{title: $title})
                            ON CREATE SET m +={img: $secTitle, released: $released, tagline: $tagline}
                            ON MATCH SET m.updateDate='created'
                        return m.updateDate as updateDate'''
            movieAdd, b, c = driver.execute_query(
                query, title=title, secTitle=secTitle, released=released, tagline=tagline)

            if movieAdd[0]['updateDate']:
                flash('Бүртгэлтэй кино байна', 'warning')
                return redirect(url_for('addMovie'))

            flash('Амжилттай кино бүргэгдлээ', 'success')
            return redirect(url_for('index'))


@app.route('/movieDetails/<int:mid>', methods=['GET', 'POST'])
def movieDetails(mid):
    if not 'name' in session:
        return redirect(url_for('index'))
    elif request.method == 'GET':
        with GraphDatabase.driver(uri=uri, auth=(username, password)) as driver:

            query = '''MATCH (m:Movie)
                        WHERE id(m)=$mid
                        OPTIONAL MATCH    (m)-[:ACTED_IN]-(a:Person)
                        OPTIONAL MATCH    (m)-[:DIRECTED]-(d:Person)
                        OPTIONAL MATCH    (m)-[com:REVIEWED]-(r:Person)
                        OPTIONAL MATCH    (m)-[:PRODUCED]-(p:Person)
                        OPTIONAL MATCH    (m)-[:WROTE]-(w:Person)
                    RETURN 
                        m.title as name,m.img as img, m.released as released, id(m) as mid ,
                        COLLECT(DISTINCT a.name) as aname,
                        COLLECT(DISTINCT com.summary) as summary,
                        COLLECT(DISTINCT d.name) as dname,
                        COLLECT(DISTINCT r.name) as rname,
                        COLLECT(DISTINCT p.name) as pname,
                        COLLECT(DISTINCT w.name) as wname
                    '''
            getMovie, b, c = driver.execute_query(query, mid=mid)

            return render_template('movie/movieDetail.html', getMovie=getMovie)
    elif request.method == 'POST':
        with GraphDatabase.driver(uri=uri, auth=(username, password)) as driver:
            comment = request.form['comment']

            matchQuery = '''MATCH (m:Movie),(p:Person)
                                WHERE id(m)=5 and id(p)=69
                                MERGE    (p)-[s:REVIEWED]->(m)
                            RETURN 
                                s.summary as summary
                            '''
            summaryList, _, _ = driver.execute_query(matchQuery)

            jsonSummaryList = []
            for i in summaryList:
                for j in i['summary']:
                    jsonSummaryList.append(j)

            jsonSummaryList.insert(0,comment)

            query = '''MATCH (m:Movie),(p:Person)
                            WHERE id(m)=$mid and id(p)=$pid
                            MERGE    (p)-[s:REVIEWED]->(m)
                            SET s={summary: $jsonSummaryList}
                        RETURN 
                            m.title as name,p.name,
                            s.summary as summary
                            '''
            driver.execute_query(
                query, mid=mid, pid=session['pid'], jsonSummaryList=jsonSummaryList)
            return redirect(url_for('movieDetails', mid=mid))
# movieDetail


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



            query = '''MATCH(p:Person{name:$name,password:$pwd}) return p.name as name, p.userRole as role, id(p) as pid'''

            person, b, c = driver.execute_query(query, name=ner, pwd=pwd)

            if not person:
                flash('Бүртгэлгүй хэрэглэгч байна', 'warning')
                return redirect(url_for('login'))

            session['name'] = person[0]['name']
            session['role'] = person[0]['role']
            session['pid'] = person[0]['pid']

            flash(f"Амжилттай нэмтэрлээ. {session['name']}", "success")

            return redirect(url_for('index'))
# login


@app.route('/logout')
def logout():
    if not 'name' in session:
        return redirect(url_for('index'))
    elif 'name' in session:
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
            role = 2

            if ner.lower() == 'admin':
                role = 1

            checkQuery = '''MATCH(p:Person{name:$name}) return p.name'''
            checkPerson, b, c = driver.execute_query(checkQuery, name=ner)

            if checkPerson:
                flash('Бүртгэлтэй хэрэглэгч байна', 'warning')
                return redirect(url_for('register'))

            if pwd != repassword:
                flash('Нууц үг таарсангүй', 'warning')
                return redirect(url_for('register'))

            query = '''CREATE(p:Person{name:$name, password:$password, userRole:$role})  '''

            driver.execute_query(query, name=ner, password=pwd, role=role)

            flash('Амжилттай бүртгэгдлээ', 'success')
            return redirect(url_for('login'))
# register


if __name__ == '__main__':
    app.run(debug=True)

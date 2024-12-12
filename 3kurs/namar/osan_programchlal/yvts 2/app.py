from flask import Flask, render_template, request, redirect, url_for
from neo4j import GraphDatabase


app = Flask(__name__)


URI = 'bolt://localhost:7687'
AUTH = ('neo4j', 'admin123')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        with GraphDatabase.driver(auth=AUTH, uri=URI) as driver:
            query = '''MATCH(b:AlbanTushaal) return  b.name as name'''
            allAlbanTushaal, b, c = driver.execute_query(query)

            
            queryErdmiinZereg = '''MATCH(b:ErdmiinZereg) return  b.name as name'''
            allErdmiinZereg, b, c = driver.execute_query(queryErdmiinZereg)

            
            queryTenhim = '''MATCH(b:Tenhim) return  b.name as name'''
            allTenhim, b, c = driver.execute_query(queryTenhim)

            bagshQuery = '''MATCH(b:Bagsh)-[:AlbanTushaal]-(a),
                                (b)-[:ErdmiinZereg]-(e),
                                (b)-[:Tenhim]-(t)
                            return  DISTINCT b.name as name, a.name as albanTushaal 
                                ,e.name as ErdmiinZereg,t.name as Tenhim'''
            allBagsh, b, c = driver.execute_query(bagshQuery)
            return render_template('index.html', allAlbanTushaal=allAlbanTushaal, allBagsh=allBagsh, allTenhim=allTenhim, allErdmiinZereg=allErdmiinZereg)


@app.route('/addTenhim', methods=['POST'])
def addTemhim():
    if request.method == 'POST':
        with GraphDatabase.driver(auth=AUTH, uri=URI) as driver:
            acode = request.form['acode']
            name = request.form['name']

            query = '''MERGE(at:Tenhim{tcode: $acode,name: $name}) '''

            bagsh, b, c = driver.execute_query(query, acode=acode, name=name)

        return redirect(url_for('index'))


@app.route('/albantushaal', methods=['POST'])
def albantushaal():
    if request.method == 'POST':
        with GraphDatabase.driver(auth=AUTH, uri=URI) as driver:
            acode = request.form['acode']
            name = request.form['name']

            query = '''MERGE(at:AlbanTushaal{acode: $acode,name: $name}) '''

            bagsh, b, c = driver.execute_query(query, acode=acode, name=name)

        return redirect(url_for('index'))


@app.route('/erdmiinZereg', methods=['POST'])
def erdmiinZereg():
    if request.method == 'POST':
        with GraphDatabase.driver(auth=AUTH, uri=URI) as driver:
            acode = request.form['acode']
            name = request.form['name']

            query = '''MERGE(at:ErdmiinZereg{ecode: $acode,name: $name}) '''

            bagsh, b, c = driver.execute_query(query, acode=acode, name=name)

        return redirect(url_for('index'))


@app.route('/bagsh', methods=['POST'])
def bagsh():
    if request.method == 'POST':
        with GraphDatabase.driver(auth=AUTH, uri=URI) as driver:
            acode = request.form['acode']
            name = request.form['name']
            atushaal = request.form['atushaal']
            ezereg = request.form['ezereg']
            tenhim = request.form['tenhim']
            createdDate = request.form['createdDate']

            query = '''
                    MERGE(b:Bagsh{name:$name,createdDate:$createdDate})
                    MERGE(a:AlbanTushaal{name:$atushaal})
                    MERGE(e:ErdmiinZereg{z:$ezereg})
                    MERGE(t:Tenhim{name:$tenhim})
                    Merge (b)-[:AlbanTushaal]-(a)
                    Merge (b)-[:ErdmiinZereg]-(e)
                    Merge (b)-[:Tenhim]-(t)
                    '''
            bagsh, b, c = driver.execute_query(
                query, acode=acode, name=name,  atushaal=atushaal, ezereg=ezereg, tenhim=tenhim, createdDate=createdDate)

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

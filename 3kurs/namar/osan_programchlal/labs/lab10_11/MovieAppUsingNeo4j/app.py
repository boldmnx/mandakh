from flask import Flask, render_template
from neo4j import GraphDatabase
import os

app = Flask(__name__)


MOVIE_IMG = os.path.join('static', 'movies')

app.config['UPLOAD_FOLDER'] = MOVIE_IMG


URI = 'bolt://localhost:7687'
AUTH = ('neo4j', 'admin123')


@app.route('/')
def index():
    with GraphDatabase.driver(uri=URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        records, summary, keys = driver.execute_query(
            "match(m:Movie) return m.title as title, m.released as released, m.image as image, m.tagline as tagline limit 6"
        )
    return render_template('base.html', data=records)
# index


@app.route('/movies')
def movies():
    with GraphDatabase.driver(uri=URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        records, summary, keys = driver.execute_query(
            "match(m:Movie) return m.title as title, m.released as released, m.image as image, m.tagline as tagline"
        )
    return render_template('movies.html', data=records)
# movies


@app.route('/director')
def director():
    with GraphDatabase.driver(uri=URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        records, summary, keys = driver.execute_query(
            "match(p:Person)-[r:DIRECTED]-() return distinct p.name as name, p.born as born"
        )
    return render_template('director.html', data=records)
# director


if __name__ == '__main__':
    app.run(debug=True, port=5001)

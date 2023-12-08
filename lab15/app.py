from flask import Flask, render_template, request
from flask_paginate import Pagination
import sqlite3

app = Flask(__name__)


def index(limit=10):
    page = request.args.get('page')
    paginate = Pagination()
    user = ''
    start = ()*limit
    end = ''
    with sqlite3.connect('lab15.db') as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(f'select * from test limit {start}, {limit}')
    return render_template('index.html', paginate=paginate, user=user)


app.run(debug=True)

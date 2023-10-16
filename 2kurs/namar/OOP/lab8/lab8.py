from flask import Flask, render_template
from classes.worker import Worker
from classes.branch import Branch

app = Flask(__name__)
w = Worker()
b = Branch()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/branch')
def branch():
    return render_template('branch/branch.html', branches=b.getRecords())


@app.route('/workers')
def worker():
    return render_template('worker/workers.html', workers=w.getRecords())


# @app.route('/worker<int: id>')
# def worker(id):
#     return render_template('worker/worker.html', workers=w.getRecord(id))


if __name__ == '__main__':
    app.run(debug=True)

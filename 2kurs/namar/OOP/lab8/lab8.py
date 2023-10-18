from flask import Flask, render_template, request
from classes.worker import Worker
from classes.branch import Branch

app = Flask(__name__)
w = Worker()
b = Branch()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/branches')
def branch():
    return render_template('branch/list_branch.html', branches=b.getRecords())


@app.route('/workers')
def workers():
    return render_template('worker/list_worker.html', workers=w.getRecords())


@app.route('/worker')
def worker():
    id = request.args.get('detail')
    return render_template('worker/worker.html', detail=w.getRecord(id))


if __name__ == '__main__':
    app.run(debug=True)

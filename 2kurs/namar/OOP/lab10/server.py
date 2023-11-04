from flask import Flask, render_template, request, redirect, url_for
from employee import Worker, Branch

app = Flask(__name__)
worker_obj = Worker()
branch_obj = Branch()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/branch')
def branch():
    return render_template('branch/list.html', branches=branch_obj.get_all())


@app.route('/branch/add', methods=['GET', 'POST'])
def add_branch():
    if request.method == 'POST':
        bname = request.form['bname']
        branch_obj.add(bname)
        return redirect(url_for('branch'))
    elif request.method == 'GET':
        return render_template('branch/add.html')


@app.route('/branch/edit/<int:id>', methods=['GET', 'POST'])
def edit_branch(id):
    if request.method == 'GET':
        bname = branch_obj.get(id)
        return render_template('branch/edit.html', bname=bname)
    elif request.method == 'POST':
        bname = request.form['bname']
        branch_obj.edit(id, bname)
        return redirect(url_for('branch'))


@app.route('/branch/delete/<int:id>', methods=['GET', 'POST'])
def delete_branch(id):
    if request.method == 'GET':
        bname = branch_obj.get(id)
        return render_template('/branch/delete.html', bname=bname)
    elif request.method == 'POST':
        branch_obj.delete(id)
        return redirect(url_for('branch'))


@app.route('/worker')
def worker():
    wData = worker_obj.get_all()
    return render_template('worker/list.html', wData=wData)


@app.route('/worker/add', methods=['GET', 'POST'])
def add_worker():
    if request.method == 'GET':
        bData = branch_obj.get_all()
        return render_template('/worker/add.html', bData=bData)
    elif request.method == 'POST':
        name = request.form['name']
        bid = request.form['b_id']
        worker_obj.add(name, bid)
        return redirect(url_for('worker'))


@app.route('/worker/edit/<int:id>', methods=['GET', 'POST'])
def edit_worker(id):
    if request.method == 'GET':
        wdata = worker_obj.get(id)
        bdata = branch_obj.get_all()
        return render_template('worker/edit.html', wdata=wdata, bdata=bdata)
    if request.method == 'POST':
        wname = request.form['name']
        b_id = request.form['b_id']
        worker_obj.edit(id, wname, b_id)
        return redirect(url_for('worker'))


@app.route('/worker/delete/<int:id>', methods=['GET', 'POST'])
def delete_worker(id):
    if request.method == 'GET':
        wdata = worker_obj.get(id)
        bdata = branch_obj.get_all()
        return render_template('worker/delete.html', wdata=wdata, bdata=bdata)
    elif request.method == 'POST':
        worker_obj.delete(id)
        return redirect(url_for('worker'))


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for, request, redirect, flash
from mu import MU

app = Flask(__name__)
app.secret_key = 'asas'

mu = MU()


@app.route('/')
def index():
    return render_template('index.html')


# Mergejil


@app.route('/mergejil', methods=['GET', 'POST'])
def list_mergejil():
    if request.method == 'GET':
        datas = mu.getRecords('mergejil')
        return render_template('mergejil/list.html', datas=datas)
    elif request.method == 'POST':
        aname = request.form['aname']
        mu.add(aname)
        return redirect(url_for('list_mergejil'))


@app.route('/mergejil/edit/<int:id>', methods=['GET', 'POST'])
def edit_mergejil(id):
    if request.method == 'GET':
        mergejilName = mergejil.getRecord(id)

        return render_template('mergejil/edit.html', aname=mergejilName)
    elif request.method == 'POST':
        aname = request.form['aname']
        mergejil.edit(id, aname)
        return redirect(url_for('list_mergejil'))


@app.route('/mergejil/delete/<int:id>')
def delete_mergejil(id):
    mergejil.delete(id)
    return redirect(url_for('list_mergejil'))


# Tenhim


# @app.route('/tenhim', methods=['GET', 'POST'])
# def list_tenhim():
#     if request.method == 'GET':
#         datas = tenhim.getRecords()
#         return render_template('tenhim/list.html', datas=datas)
#     elif request.method == 'POST':
#         aname = request.form['aname']
#         tenhim.add(aname)
#         return redirect(url_for('list_tenhim'))


# @app.route('/tenhim/edit/<int:id>', methods=['GET', 'POST'])
# def edit_tenhim(id):
#     if request.method == 'GET':
#         tenhimName = tenhim.getRecord(id)
#         return render_template('tenhim/edit.html', aname=tenhimName)
#     elif request.method == 'POST':
#         aname = request.form['aname']
#         tenhim.edit(id, aname)
#         return redirect(url_for('list_tenhim'))


# @app.route('/tenhim/delete/<int:id>')
# def delete_tenhim(id):
#     tenhim.delete(id)
#     return redirect(url_for('list_tenhim'))


# # Zereg


# @app.route('/zereg', methods=['GET', 'POST'])
# def list_zereg():
#     if request.method == 'GET':
#         datas = zereg.getRecords()
#         return render_template('zereg/list.html', datas=datas)
#     elif request.method == 'POST':
#         aname = request.form['aname']
#         zereg.add(aname)
#         return redirect(url_for('list_zereg'))


# @app.route('/zereg/edit/<int:id>', methods=['GET', 'POST'])
# def edit_zereg(id):
#     if request.method == 'GET':
#         zeregName = zereg.getRecord(id)
#         return render_template('zereg/edit.html', aname=zeregName)
#     elif request.method == 'POST':
#         aname = request.form['aname']
#         zereg.edit(id, aname)
#         return redirect(url_for('list_zereg'))


# @app.route('/zereg/delete/<int:id>')
# def delete_zereg(id):
#     zereg.delete(id)
#     return redirect(url_for('list_zereg'))


# # Alban


# @app.route('/alban', methods=['GET', 'POST'])
# def list_alban():
#     if request.method == 'GET':
#         datas = alban.getRecords()
#         return render_template('alban/list.html', datas=datas)
#     elif request.method == 'POST':
#         aname = request.form['aname']
#         alban.add(aname)
#         return redirect(url_for('list_alban'))


# @app.route('/alban/edit/<int:id>', methods=['GET', 'POST'])
# def edit_alban(id):
#     if request.method == 'GET':
#         albanName = alban.getRecord(id)
#         return render_template('alban/edit.html', aname=albanName)
#     elif request.method == 'POST':
#         aname = request.form['aname']
#         alban.edit(id, aname)
#         return redirect(url_for('list_alban'))


# @app.route('/alban/delete/<int:id>')
# def delete_alban(id):
#     alban.delete(id)
#     return redirect(url_for('list_alban'))


if __name__ == '__main__':
    app.run(debug=True)

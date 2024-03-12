
from django.shortcuts import render, redirect
import psycopg2 as sql
from django.urls import reverse

# Create your views here.
# crud,details
# cleaned data
# csrf


def read_branch(request):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM tbl_branch')
        d = cur.fetchall()
    return render(request, 'readBranch.html', {'branches': d})


def create_branch(request):
    if request.method == 'POST':
        with sql.connect(database='lab8',
                         user='postgres',
                         password='1000',
                         host='localhost',
                         port='5432'
                         ) as con:
            cur = con.cursor()
            bname = request.POST.get('bname')
            cur.execute(f"INSERT INTO tbl_branch values(default,'{bname}')")
            con.commit()
        return redirect(reverse('readBranch'))


def update_branch(request, id):
    if request.method == 'POST':
        with sql.connect(database='lab8',
                         user='postgres',
                         password='1000',
                         host='localhost',
                         port='5432'
                         ) as con:
            cur = con.cursor(cursor_factory=extras.DictCursor)
            bname = request.POST.get('bname')
            cur.execute(f'''UPDATE tbl_branch SET bname='{
                        bname}' WHERE bid={id}''')
            con.commit()
        return redirect(reverse('readBranch'))
    elif request.method == 'GET':
        with sql.connect(database='lab8',
                         user='postgres',
                         password='1000',
                         host='localhost',
                         port='5432'
                         ) as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM tbl_branch WHERE bid={id}')
            d = cur.fetchone()
        return render(request, 'update.html', {'branch': d})


def delete_branch(request, id):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM tbl_branch WHERE bid={id}")
        con.commit()
    return redirect(reverse('readBranch'))


def detail_branch(request, id):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:
        cur = con.cursor()
        cur.execute(f'SELECT * FROM tbl_branch WHERE bid={id}')
        d = cur.fetchone()
    return render(request, 'detail.html', {'branch': d})

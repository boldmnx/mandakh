from django.shortcuts import render
import sqlite3 as sql
# Create your views here.


def read_branch(request):
    with sql.connect('db_employee') as con:
        cur = con.cursor()
        cur.execute(f'SELECT * FROM tbl_branch')
        branches = cur.fetchall()
    return render(request, 'read_branch.html', {'branches': branches})


def create_branch(request):
    if request.method == 'GET':
        with sql.connect('db_employee') as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM tbl_branch')
            branches = cur.fetchall()
        return render(request, 'read_branch.html', {'branches': branches})
    elif request.method=='POST':
        with sql.connect('db_employee') as con:
            cur = con.cursor()
            cur.execute(f'INSERT INTO * FROM tbl_branch')
            branches = cur.fetchall()
        
        return render(request, 'create_branch.html')

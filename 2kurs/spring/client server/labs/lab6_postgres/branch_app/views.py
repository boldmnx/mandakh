from django.shortcuts import render
import psycopg2 as sql


def branch(request):
    con = sql.connect(
        database='lab6',
        user='postgres',
        password='1000',
        host='localhost',
        port='5432'
    )
    cur = con.cursor()
    cur.execute(f'SELECT * FROM salbar')
    salbars = cur.fetchall()
    return render(request, 'salbar.html', {'branches': salbars})

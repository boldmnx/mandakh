from django.shortcuts import render
import psycopg2 as sql
# Create your views here.


def read_worker(request):
    with sql.connect(database='lab6', user='postgres', password='1000', host='localhost', port=5432) as con:
        cur = con.cursor()
        cur.execute(f'''SELECT wid, wname, sname FROM worker  w
                        INNER JOIN salbar  b ON b.sid=w.bid''')
        workers = cur.fetchall()
    return render(request, 'readWorker.html', {'workers': workers})

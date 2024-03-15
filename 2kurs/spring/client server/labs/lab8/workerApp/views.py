
from django.shortcuts import render, redirect
import psycopg2 as sql
from django.urls import reverse

# Create your views here.
# crud,details
# cleaned data
# csrf


def read(request):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:
        cur = con.cursor()
        cur.execute('''SELECT wid,wname,bname FROM tbl_worker w
                        INNER JOIN tbl_branch b ON w.bid_id=b.bid
                        ''')
        d = cur.fetchall()
        cur.execute('SELECT * FROM tbl_branch')
        branches = cur.fetchall()
    return render(request, 'read.html', {'workers': d, 'branches': branches})


def create(request):
    if request.method == 'POST':
        with sql.connect(database='lab8',
                         user='postgres',
                         password='1000',
                         host='localhost',
                         port='5432'
                         ) as con:
            cur = con.cursor()
            wname = request.POST.get('wname')
            bid = request.POST.get('bid')
            print(bid)
            cur.execute(
                f"INSERT INTO tbl_worker values(default,'{wname}',{bid})")
            con.commit()
        return redirect(reverse('read'))


def update(request, wid):
    if request.method == 'POST':
        with sql.connect(database='lab8',
                         user='postgres',
                         password='1000',
                         host='localhost',
                         port='5432'
                         ) as con:
            cur = con.cursor()
            wname = request.POST.get('wname')
            bid = request.POST.get('bid')
            cur.execute(f'''UPDATE tbl_worker
                        SET wname='{wname}',bid_id={bid}
                        WHERE wid={wid}''')
            con.commit()
        return redirect(reverse('read'))
    elif request.method == 'GET':
        with sql.connect(database='lab8',
                         user='postgres',
                         password='1000',
                         host='localhost',
                         port='5432'
                         ) as con:
            cur = con.cursor()
            cur.execute(f'''SELECT wname,bname,bid_id FROM tbl_worker w
                        INNER JOIN tbl_branch b ON w.bid_id=b.bid
                        WHERE wid={wid}
                            ''')
            d = cur.fetchone()
            cur.execute('SELECT * FROM tbl_branch')
            branches = cur.fetchall()
        return render(request, 'edit.html', {'worker': d, 'branches': branches})


def delete(request, wid):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM tbl_worker WHERE wid={wid}")
        con.commit()
    return redirect(reverse('read'))


def detail(request, wid):
    with sql.connect(database='lab8',
                            user='postgres',
                            password='1000',
                            host='localhost',
                            port='5432'
                            ) as con:
                cur = con.cursor()
                cur.execute(f'''SELECT wname,bname,bid_id FROM tbl_worker w
                            INNER JOIN tbl_branch b ON w.bid_id=b.bid
                            WHERE wid={wid}
                                ''')
                d = cur.fetchone()
    return render(request, 'detailWorker.html', {'worker': d})


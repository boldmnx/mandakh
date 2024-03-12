
from django.shortcuts import render
import psycopg2 as sql

# Create your views here.
# crud,details
#cleaned data
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
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:

        pass
    pass


def update_branch(request):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:

        pass
    pass


def delete_branch(request):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:

        pass
    pass


def detail_branch(request):
    with sql.connect(database='lab8',
                     user='postgres',
                     password='1000',
                     host='localhost',
                     port='5432'
                     ) as con:

        pass
    pass

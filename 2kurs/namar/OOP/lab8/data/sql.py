import sqlite3


# CREATE TABLE departments (
#     id INTEGER PRIMARY KEY,
#     name TEXT
# );

# CREATE TABLE employees (
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     department_id INTEGER,
#     FOREIGN KEY (department_id) REFERENCES departments (id)
# );
with sqlite3.connect('Employee.db') as con:
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('''
        SELECT *
        FROM tbl_worker
        INNER JOIN tbl_branch 
        ON tbl_worker.b_id = tbl_branch.bid''')
    data = cur.fetchall()
    for i in data:
        print(i)
    # for i in range(len(data)):
    #     print(data[i][4])

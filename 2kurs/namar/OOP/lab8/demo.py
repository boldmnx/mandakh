# import sqlite3

from classes.worker import Worker

w = Worker()
print(w.getRecords())


# # 'Employee' нэртэй баазтай холбогдох эсвэл шинээр үүсгэх
# conn = sqlite3.connect('Employer.db')
# c = conn.cursor()
# # Branch буюу салбар хүснэгт
# c.execute('''CREATE TABLE IF NOT EXISTS branch (
# id integer PRIMARY KEY,
# bname text NOT NULL);''')
# # worker буюу ажилтан хүснэгт
# c.execute('''CREATE TABLE IF NOT EXISTS worker (
# id integer PRIMARY KEY,
# wname text NOT NULL,
# FOREIGN KEY (id) REFERENCES branch (id));''')
# # үр дүнг ажиллуулах
# conn.commit()

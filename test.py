import sqlite3


conn = sqlite3.connect('data.db')

cursor = conn.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'
cursor.execute(create_table)

user = (1, 'john', 'asd')
insert = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert, user)

users = [
    (2, 'jane', 'qwe'),
    (3, 'doe', 'zxc')
]

cursor.executemany(insert, users)

select = 'SELECT * FROM users'
for row in cursor.execute(select):
    print(row)

conn.commit()

conn.close()

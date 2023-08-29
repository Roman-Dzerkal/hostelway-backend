import sqlite3

conn = sqlite3.connect("sql_app.db")
cur = conn.cursor()


cur.execute("SELECT * FROM users")

list = cur.fetchall()

for i in list:
    print(i[0])

cur.execute("INSERT INTO users(email, name, hashed_password, role) VALUES (?,?,?,?)", ("aaa@gmail.com", "Inna", "awdasd", "manager"))

conn.commit()

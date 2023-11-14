from sqlite3 import Connection, connect

conn: Connection = connect('sql_app1.db')
cur = conn.cursor()


from sqlite3 import Connection, connect

conn: Connection = connect('sql_app.db')
cur = conn.cursor()

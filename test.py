"""import requests
import json

url = "http://127.0.0.1:8000/signin"

payload = json.dumps({
  "email": "www@gmail.com",
  "hashed_password": "123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)"""

import sqlite3

conn = sqlite3.connect('sql_app1.db')
cursor = conn.cursor()
c = cursor.execute("SELECT * FROM users WHERE name == \'Inna\'")
result = c.fetchone()

if result is None:
    print('Net polzovatelya')


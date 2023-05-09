import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("SELECT * FROM user_info")

data = c.fetchall()

conn.close()

print(data)



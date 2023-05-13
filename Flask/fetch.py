import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("SELECT * FROM user_info")
data = c.fetchall()
# c.execute("INSERT INTO user_info (Name ,Last_name, Email , Password , Type) VALUES('Sanjay','Sujir','sujirsanjay@gmail.com','#Python_Coding==Fvrt:','Admin')")

# conn.commit()
conn.close()

print(data)



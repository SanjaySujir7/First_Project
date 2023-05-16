import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("SELECT * FROM user_info")
data = c.fetchall()
c.execute("DELETE FROM user_csv")
csv_data = c.fetchall()
# c.execute("INSERT INTO user_info (Name ,Last_name, Email,Password,Language,Status,Radio,Type) VALUES('Nishan','N','Nishan@gmail.com','nnnnnnn','python','student','Machine-Learning','Normal')")
# c.execute("INSERT INTO user_info (Name,Last_name,Email,Password,Type) VALUES('sanjay','sujir','sujirsanjay@gmail.com','admin77','Admin')")
# conn.commit()
conn.close()

print(data)
print()
print(csv_data)


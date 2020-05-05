import sqlite3 as sql

#_______connecting to sqliteDB_________#
db = sql.connect("contacts.sqlite3")

#_______executing commands________#
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone_no INTEGER, email_id TEXT)")
db.execute("INSERT INTO contacts (name, phone_no, email_id) VALUES('Tim', 16556846, 'tim@gmail.com')")
db.execute("INSERT INTO contacts (name, phone_no, email_id) VALUES('Brian', 123456, 'brian@gmail.com')")

#_______creating a cursor object________#
cursor = db.cursor()
cursor.execute('SELECT * FROM contacts')
print(cursor.fetchall())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('=' * 20)
cursor.close()      #setting a cursor

db.commit()         #Fixing the changes permanently
db.close()          #ending connection with Database
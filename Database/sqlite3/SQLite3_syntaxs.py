"""https://docs.python.org/3.7/library/sqlite3.html#controlling-transactions"""

import sqlite3 as sql

#____________creating a connection object_____________#
"""connection objects represesnts the database.
   isolation_level=None autocommits transactions"""

db1 = sql.connect('contacts.sqlite3', isolation_level=None)

#__________connection Methods____________#
k = db1.execute('SELECT * FROM contacts')        #execute executes the passed SQL queries by creating cursor implisitly
for name, phone, email in k:
    print(f"Name: {name}, Phone no: {phone}, email: {email}")

db1.commit()                                     #saves any changes since last commit to the database

db1.rollback()                                   #rolling back the last transactions to the database

#_________________Cursors Objects_________________#
db1_cursor = db1.cursor()                        #making a cursor object.

#___________Cursor methods____________#

db1_cursor.execute(f"INSERT INTO contacts(name, phone_no, email_id) VALUES ('Ken', {int(828265489)}, 'Joker@moker')")

db1_cursor.execute("SELECT * FROM contacts")

print(db1_cursor.fetchone())                     #Fetches the first row of retrival query
print(db1_cursor.fetchmany(2))                   #Fetches passed no of rows from retrival query
print(db1_cursor.fetchall())                     #fetches all rows

#_____executemany_____#
"""executemany uses a sequence or a generator"""

info = [('Ben', 456789, 'ben@hotmail'), ('Peter', 7979456, 'Peter@gmail')]      #creating sequence

db1_cursor.executemany("INSERT INTO contacts(name, phone_no, email_id) VALUES (?, ?, ?)", info)

db1_cursor.execute("SELECT * FROM contacts")
print(db1_cursor.fetchall())                     #fetches all rows

#_____executescript_____#
db1_cursor.executescript("SQL SCRIPT")           #executes an entire SQL script

#_________cursor variables_________#
print(db1_cursor.rowcount)                       #gives the number of affected rows from last transactions
print(db1_cursor.connection)                     #gives connection object of the cursor
print(db1_cursor.description)                    #gives the column name of affected rows from last transactions

db1_cursor.connection.commit()                   #A way of commiting through cursor object

db1_cursor.close()                               #closes cursor
db1.close()                                      #closing the connection
import sqlite3 as sql

db = sql.connect('contacts.sqlite3')

new_email = input("Enter your email: ")
phone = 123456


update_sql = f"UPDATE contacts SET email_id = ? WHERE phone_no = ?"     #? is a place holder who's values are given in execute method
print(update_sql)
 
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
"""While passing values for replacement field in .execute() method
   it must be passed in a tupple format. for single values use (x, )"""
# update_cursor.executescript(update_cursor)    #can rum multiple SQL queries separated by ;

print(f"{update_cursor.rowcount} rows are updated")

update_cursor.connection.commit()   #commiting through cursor
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('='*30)

db.close()
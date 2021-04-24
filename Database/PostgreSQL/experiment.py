"""https://www.postgresql.org/docs/current/functions-sequence.html"""

import psycopg2 as pg2

# data to insert into database
role_list = ['killer', 'Bean', 'Forever']

my_pass = r'MargretThacheris100%sexy'

# connection to learning database
learning_db = pg2.connect(database='learning', user='postgres', password=my_pass)
# cursor for learning database
learning_cursor = learning_db.cursor()

#_________playing with serials________#
# sets the serial cursor at database to the last value in the serial column
# execute this before inserting values in a table with serial column, EVERYTIME!
learning_cursor.execute("SELECT setval('role_id_seq', (SELECT MAX(id) FROM role))")

for i in role_list:
    print(f'i = {i}')
    learning_cursor.execute(f"""INSERT INTO role (role_name) VALUES ('{i}');""")

# Commiting the changes to database
learning_db.commit()

# Shutting down cursor and connection
learning_cursor.close()
learning_db.close()
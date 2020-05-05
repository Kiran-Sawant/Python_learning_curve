import sqlite3 as sql
import pytz

db = sql.connect('accounts.sqlite3', detect_types=sql.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM localhistory"):
    print(row)
    # local = pytz.utc.localize(utc).astimezone()
    # print(f"{utc}\t{local}")

db.close()
import sqlite3

conn = sqlite3.connect('clients.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS clients(
   userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   first_name TEXT,
   last_name TEXT,
   surname TEXT,
   city TEXT,
   address TEXT,
   phone1 TEXT,
   phone2 TEXT,
   reason TEXT,
   comment TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS offers(
   userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   offer TEXT
   );
""")
conn.commit()
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO test (name) VALUES (?)", ('John',))
conn.commit()

cursor.execute("SELECT * FROM test")
print(cursor.fetchall())

conn.close()
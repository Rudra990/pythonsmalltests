import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()
conn.close()
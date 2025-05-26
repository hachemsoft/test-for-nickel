import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS tickets")
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
cursor.execute("CREATE TABLE tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, status TEXT NOT NULL, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))")

for i in range(1, 101):
    cursor.execute("INSERT INTO users (name) VALUES (?)", (f'User {i}',))

for i in range(1, 1001):
    status = 'open' if i % 3 == 0 else 'closed'
    user_id = (i % 100) + 1
    cursor.execute("INSERT INTO tickets (title, status, user_id) VALUES (?, ?, ?)", (f'Ticket #{i}', status, user_id))

conn.commit()
conn.close()
print("Database initialized.")

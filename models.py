import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all_tickets():
    conn = get_db_connection()
    tickets = conn.execute('SELECT * FROM tickets').fetchall()
    conn.close()
    return tickets

def get_all_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users

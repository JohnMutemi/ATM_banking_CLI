import sqlite3

#connect to the database
CONN=sqlite3.connect('bank.db')
CURSOR=CONN.cursor()

# Create tables if they don't exist
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    pin TEXT NOT NULL,
    balance REAL NOT NULL
)
''')

CURSOR.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id TEXT PRIMARY KEY,
    user_id TEXT,
    amount REAL NOT NULL,
    type TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

CONN.commit()

import sqlite3
import uuid

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

class User:
    def __init__(self, username, pin):
        self.id = str(uuid.uuid4())
        self.username = username
        self.pin = pin
        self.balance = 0.0

    def save(self):
        cursor.execute('INSERT INTO users (id, username, pin, balance) VALUES (?, ?, ?, ?)', 
                       (self.id, self.username, self.pin, self.balance))
        conn.commit()

    @classmethod
    def find_by_id(cls, user_id):
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            user = cls(user_data[1], user_data[2])
            user.id = user_data[0]
            user.balance = user_data[3]
            return user
        return None

    @classmethod
    def find_by_username(cls, username):
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = cursor.fetchone()
        if user_data:
            user = cls(user_data[1], user_data[2])
            user.id = user_data[0]
            user.balance = user_data[3]
            return user
        return None

    @classmethod
    def get_all(cls):
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

    def update_balance(self, amount):
        self.balance += amount
        cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (self.balance, self.id))
        conn.commit()

    def delete(self):
        cursor.execute('DELETE FROM users WHERE id = ?', (self.id,))
        conn.commit()

class Transaction:
    def __init__(self, user_id, amount, type):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.amount = amount
        self.type = type

    def save(self):
        cursor.execute('INSERT INTO transactions (id, user_id, amount, type) VALUES (?, ?, ?, ?)', 
                       (self.id, self.user_id, self.amount, self.type))
        conn.commit()

    @classmethod
    def find_by_id(cls, transaction_id):
        cursor.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,))
        transaction_data = cursor.fetchone()
        if transaction_data:
            transaction = cls(transaction_data[1], transaction_data[2], transaction_data[3])
            transaction.id = transaction_data[0]
            return transaction
        return None

    @classmethod
    def find_by_user_id(cls, user_id):
        cursor.execute('SELECT * FROM transactions WHERE user_id = ?', (user_id,))
        return cursor.fetchall()

    @classmethod
    def get_all(cls):
        cursor.execute('SELECT * FROM transactions')
        return cursor.fetchall()

    def delete(self):
        cursor.execute('DELETE FROM transactions WHERE id = ?', (self.id,))
        conn.commit()

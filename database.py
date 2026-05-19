import sqlite3

DB_NAME = "inspire_bot.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, notify_time TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, message TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def add_user(user_id, username, first_name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id, username, first_name) VALUES (?, ?, ?)", (user_id, username, first_name))
    conn.commit()
    conn.close()

def update_time(user_id, notify_time):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET notify_time = ? WHERE user_id = ?", (notify_time, user_id))
    conn.commit()
    conn.close()

def add_feedback(user_id, message):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO feedback (user_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
    conn.close()

def get_all_users_with_time():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT user_id, notify_time FROM users WHERE notify_time IS NOT NULL")
    rows = c.fetchall()
    conn.close()
    return rows
import sqlite3 as sq3
from datetime import datetime

class Database:
    def __init__(self, db="test.db"):
        self.conn = sq3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, createdAt TEXT)")
        self.conn.commit()

    def createUser(self, user_name, pword):
        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        try:
            self.cursor.execute("INSERT INTO users VALUES(NULL,?,?,?)",(user_name,pword,time))
        except:
            return "error occurred"
        self.conn.commit()

    def __del__(self):
        self.conn.close()
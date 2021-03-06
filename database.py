import sqlite3 as sq3
from datetime import datetime

class Database:
    def __init__(self, db="test.db"):
        self.conn = sq3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, createdAt TEXT)")
        self.conn.commit()

    def validate(self, username, password):
        if len(username) == 0 or len(password) == 0:
            print('Missing username and/or password')
            return "blank"
        else : 
            x= len(self.cursor.execute("SELECT * FROM users WHERE username =?",(username,)).fetchall())
            print(x)
            if x > 0:
                return "uname_in_use"
            else :
                return "Success"

    def checkCreds(self, username, password):
        if len(self.cursor.execute("SELECT * FROM users WHERE username =? AND password =?",(username,password)).fetchall()) == 1:
            return "correct"
        else :
            return "wrong"
        
    def createUser(self, user_name = "", pword=""):
        if self.validate(user_name, pword) == "uname_in_use" or self.validate(user_name, pword) == "blank" :
            return "Fail"
        else : 
            time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") 
            try:
                self.cursor.execute("INSERT INTO users VALUES(NULL,?,?,?)",(user_name,pword,time,))
            except:
                return "error occurred"
            

        self.conn.commit()

    def __del__(self):
        self.conn.close()
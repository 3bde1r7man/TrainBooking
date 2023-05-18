import sqlite3

class Admin():
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.adminId = ""
    
    def signUp(self):
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute(f''' SELECT email FROM Admin WHERE email = "{email}" ''')
        if cursor.fetchone() == None:
            cursor.execute(f''' INSERT INTO Admin (name, email, password) VALUES ("{name}", "{email}", "{password}") ''')
            conn.commit()
            cursor.execute(f''' SELECT email FROM Admin WHERE email = "{email}" ''')
            if cursor.fetchone() == None:
                print("Error\n")
            else:
                print("Account created successfully\n")
                return
        else:
            print("Email already exists!\n")


    def signIn(self):
        email = input("Enter your email address: ")
        password = input("Enter your password: ")

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        cursor.execute(f''' SELECT adminId FROM Admin WHERE email = "{email}" ''')
        adminId = cursor.fetchone()
        if adminId == None:
            print("Error\n")
        else:
            cursor.execute(f''' SELECT password FROM Admin WHERE adminId = "{adminId}" ''')
            if cursor.fetchone() == password:
                cursor.execute(f''' SELECT name FROM Admin WHERE adminId = "{adminId}" ''')
                name = cursor.fetchone()
                print(f"Welcome {name}\n")
            else:
                print("Error\n")
import sqlite3
from Train import Train
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
            cursor.execute(f''' SELECT adminId FROM Admin WHERE email = "{email}" ''')
            if cursor.fetchone() == None:
                print("Error\n")
            else:
                self.adminId = cursor.fetchone()[0]
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
        adminId = cursor.fetchone()[0]
        if adminId == None:
            print("Error\n")
        else:
            cursor.execute(f''' SELECT password FROM Admin WHERE adminId = "{adminId}" ''')
            if cursor.fetchone() == password:
                cursor.execute(f''' SELECT adminId, name, email, password  FROM Admin WHERE adminId = "{adminId}" ''')
                row = cursor.fetchone()
                self.adminId = row[0]
                self.name = row[1]
                self.email = row[2]
                self.password = row[3]
                print(f"Welcome {self.name}\n")
            else:
                print("Error\n")

    #def upadteCustomerDetails():

    def addTrain(self):
        train = Train()
        train.addTrain(self.adminId)
        return
    
    def editTrain(self):
        train = Train()
        train.editTrain(self.adminId)
        return


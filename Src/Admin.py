import sqlite3
from Train import Train
class Admin():
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.adminId = ""
    
    def signUp(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email address: ")
        self.password = input("Enter your password: ")

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute(f' SELECT email FROM Admin WHERE email = "{self.email}" ')
        if cursor.fetchone() == None:
            cursor.execute(f' INSERT INTO Admin (name, email, password) VALUES ("{self.name}", "{self.email}", "{self.password}") ')
            conn.commit()
            cursor.execute(f' SELECT adminId FROM Admin WHERE email = "{self.email}" ')
            adminId = cursor.fetchone()
            if adminId == None:
                print("Error\n")
            else:
                self.adminId = adminId[0]
                print("Account created successfully\n")
                return True
        else:
            print("Email already exists!\n")
        
        conn.close()
        return False


    def signIn(self):
        email = input("Enter your email address: ")
        password = input("Enter your password: ")

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        cursor.execute(f' SELECT adminId FROM Admin WHERE email = "{email}" ')
        adminId = cursor.fetchone()[0]
        if adminId == None:
            print("Error\n")
        else:
            cursor.execute(f' SELECT password FROM Admin WHERE adminId = "{adminId}" ')
            if cursor.fetchone() == password:
                cursor.execute(f' SELECT adminId, name, email, password  FROM Admin WHERE adminId = "{adminId}"')
                row = cursor.fetchone()
                self.adminId = row[0]
                self.name = row[1]
                self.email = row[2]
                self.password = row[3]
                print(f"Welcome {self.name}\n")
                return True
            else:
                print("Error\n")

        conn.close()
        return False

    #def upadteCustomerDetails():

    def addTrain(self, name, description, classes):
        train = Train()
        # train.name = input("Enter train name: ")
        # train.description = input("Enter train description: ")
        # train.Class()
        train.name = name
        train.description = description
        train.classes = classes
        train.addTrain(self.adminId)
        return
    
    def editTrainClass(name, description, classes):
        return  


    def editTrain(name, description, classes, choose = None, whichClass = None):
        train = Train()
        # conn = sqlite3.connect('db.sqlite3')
        # cursor = conn.cursor()
        # cursor.execute('SELECT trainId, name, adminId, details FROM Train')
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row[0] + " - " + row[1] + " - " + row[2] + " - " + row[3])
        # choose = int(input("Select the train to edit: "))
        # cursor.execute(f'SELECT name, adminId, details FROM Train WHERE trainId = "{choose}"')
        # row = cursor.fetchone()
        # train.name = row[0]
        # train.description = row[2]
        # train.getClasses(choose)
        # whatToEdit = int(input("What to edit\n1- Train\n2- classes in the train\n-->"))
        train.name = name
        train.description = description
        train.classes = classes
        if whatToEdit == 1:
            # train.name = input("Enter train name: ")
            # train.description = input("Enter train description: ")
            train.editTrain(choose)
        elif whatToEdit == 2:
            # whichClass = int(input("Enter which class to edit: "))
            # train.classes[whichClass][1] = input("Enter number of seats in "+ train.classes[whichClass][0][0] + " for train: ")
            train.editTrainClass(whichClass)
        return


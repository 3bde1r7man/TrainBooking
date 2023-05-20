import sqlite3
from Train import Train
from Trip import Trip

class Admin:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.adminId = ""

    def signUp(self, name, email, password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if email already exists in the Admin table
        cursor.execute('''SELECT email FROM Admin WHERE email = ?''', (email,))
        if cursor.fetchone() is not None:
            conn.close()
            raise ValueError("Email already exists!")

        # Insert a new admin into the Admin table
        cursor.execute('''INSERT INTO Admin (name, email, password) VALUES (?, ?, ?)''', (name, email, password))
        conn.commit()

        # Retrieve the adminId of the newly inserted row
        cursor.execute('''SELECT adminId FROM Admin WHERE email = ?''', (email,))
        admin_id = cursor.fetchone()
        if admin_id is not None:
            self.adminId = admin_id[0]
            conn.close()
            return True
        else:
            conn.close()
            raise ValueError("Error occurred while retrieving adminId.")

    def signIn(self, email, password):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        # Check if email exists in the Admin table
        cursor.execute('''SELECT adminId FROM Admin WHERE email = ?''', (email,))
        admin_id = cursor.fetchone()
        if admin_id is None:
            conn.close()
            return False

        admin_id = admin_id[0]
        # Check if the provided password matches the one in the Admin table
        cursor.execute('''SELECT password FROM Admin WHERE adminId = ?''', (admin_id,))
        stored_password = cursor.fetchone()[0]
        if password != stored_password:
            conn.close()
            raise ValueError("Invalid password.")

        # Retrieve the admin details
        cursor.execute('''SELECT adminId, name, email, password FROM Admin WHERE adminId = ?''', (admin_id,))
        row = cursor.fetchone()
        self.adminId = row[0]
        self.name = row[1]
        self.email = row[2]
        self.password = row[3]

        conn.close()
        return True

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

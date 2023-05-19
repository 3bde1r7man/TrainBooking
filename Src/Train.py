import sqlite3
class Train():
    def __init__(self):
        self.name = ""
        self.description = ""
        self.classes = {}

    def addTrain(self, adminId):
        self.name = input("Enter train name: ")
        self.description = input("Enter train description: ")
        self.classes = self.Class()
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO Train (name, description, adminId) VALUES ("{self.name}", "{self.description}", "{adminId}"')
        conn.commit()
        cursor.execute(f'SELECT trainId FROM Train WHERE name = "{self.name}", description = "{self.description}")')
        trainId = cursor.fetchone()
        for Class in self.classes:
            nSeats = input("Enter number of seats in "+ self.classes[Class] + " for train: ")
            cursor.execute(f'INSERT INTO TrainClass (trainId, classId, nSeats) VALUES ("{trainId[0]}", "{Class}", "{nSeats}")')
            conn.commit()
        conn.close()
        print("Train added successfully\n")


    def Class(self):
        conn = sqlite3.connect('db.sqlite3')  
        cursor = conn.cursor()
        cursor.execute('SELECT classId, name, price FROM Class')
        rows = cursor.fetchall()
        classdict = {}
        for row in rows:
            classdict[row[0]] = row[1]
            print(row[0] + "- " + row[1] + '\n')
        
        classes = input("Select the classes that in the Train (1, 2, 3): ")
        classes = classes.split(', ')
        for Class in classes:
            self.classes[Class] = classdict[Class]
        conn.close()
        return self.classes

    def editTrain(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT trainId, name, adminId, details FROM Train')
        rows = cursor.fetchall()
        for row in rows:
            print(row[0] + " - " + row[1] + " - " + row[2] + " - " + row[3])
        choose = int(input("Select the train to edit: "))
        cursor.execute(f'SELECT name, adminId, details FROM Train WHERE trainId = "{choose}"')
        row = cursor.fetchone()
        self.name = row[0]
        self.description = row[2]
        self.getClasses(row[0])
        
        whatToEdit = int(input("What to edit\n1- Train\n2- classes in the train\n-->"))

        if whatToEdit == 1:
            self.name = input("Enter train name: ")
            self.description = input("Enter train description: ")
            cursor.execute(f'UPDATE Train SET name = "{self.name}", description = "{self.description}" WHERE trainId = "{choose}"')
            conn.commit()
        elif whatToEdit == 2:
            whichClass = int(input("Enter which class to edit: "))
            nSeats = input("Enter number of seats in "+ self.classes[whichClass] + " for train: ")
            price = input("Enter price for "+ self.classes[whichClass] + " for train: ")
            cursor.execute(f'UPDATE TrainClass SET nSeats = "{nSeats}", price = "{price}" WHERE trainId = "{choose}" AND classId = "{whichClass}"')
            conn.commit()
        
        conn.close()



    def getClasses(self, trainId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        cursor.execute(f'SELECT classId, nSeats FROM TrainClass WHERE trainId = "{trainId}"')
        rows = cursor.fetchall()
        for row in rows:
            print(row[0] + " - " + row[1] + " - " + '\n')
            cursor2.execute(f'SELECT name FROM Class WHERE classId = "{row[0]}"')
            self.classes[row[0]]= cursor2.fetchone()[0]
        conn.close()

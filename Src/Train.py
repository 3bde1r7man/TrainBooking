import sqlite3
class Train():
    def __init__(self):
        self.name = ""
        self.description = ""
        self.classes = {}

    def addTrain(self, adminId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO Train (name, description, adminId) VALUES ("{self.name}", "{self.description}", "{adminId}")')
        conn.commit()
        cursor.execute(f'SELECT trainId FROM Train WHERE name = "{self.name}", description = "{self.description}")')
        trainId = cursor.fetchone()
        for Class in self.classes:
            cursor.execute(f'INSERT INTO TrainClass (trainId, classId, nSeats) VALUES ("{trainId[0]}", "{Class}", "{self.classes[Class][1]}")')
            conn.commit()
        conn.close()
        print("Train added successfully\n")
        return


    def Class(self):
        conn = sqlite3.connect('db.sqlite3')  
        cursor = conn.cursor()
        cursor.execute('SELECT classId, className, price FROM Class')
        rows = cursor.fetchall()
        classdict = {}
        for row in rows:
            classdict[row[0]] = [row[1], row[2]]
            print(row[0] + " - " + row[1] +  " - " + row[2] + '\n')
        
        classes = input("Select the classes that in the Train (1, 2, 3): ")
        classes = classes.split(', ')
        for Class in classes:
            nSeats = int(input("Enter the number of Seats for the class " + classdict[Class][0] + "for the Train: "))
            self.classes[Class] = [classdict[Class], nSeats]
        conn.close()
        return self.classes

    def editTrain(self,choose):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'UPDATE Train SET name = "{self.name}", description = "{self.description}" WHERE trainId = "{choose}"')
        conn.commit()
        conn.close()

    def editTrainClass(self, whichClass, choose):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'UPDATE TrainClass SET nSeats = "{self.classes[whichClass][1]}" WHERE trainId = "{choose}" AND classId = "{whichClass}"')
        conn.commit()


    def getClasses(self, trainId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        cursor.execute(f'SELECT classId, nSeats FROM TrainClass WHERE trainId = "{trainId}"')
        rows = cursor.fetchall()
        for row in rows:
            print(row[0] + " - " + row[1] + " - " + '\n')
            cursor2.execute(f'SELECT className FROM Class WHERE classId = "{row[0]}"')
            self.classes[row[0]][0][0]= cursor2.fetchone()[0]
        conn.close()

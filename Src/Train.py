import sqlite3
class Train():
    def __init__(self):
        self.name = ""
        self.description = ""
        self.classes = {}

    def addTrain(self, adminId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'INSERT INTO Train (name, description, adminId) VALUES (?, ?, ?)'
        values = (self.name, self.description, adminId)
        cursor.execute(query, values)
        conn.commit()
        cursor.execute(f'SELECT trainId FROM Train WHERE name = "{self.name}" AND description = "{self.description}")')
        trainId = cursor.fetchone()
        query = 'INSERT INTO TrainClass (trainId, classId, nSeats) VALUES (?, ?, ?)'
        for Class in self.classes:
            values = (trainId[0], Class, self.classes[Class][1])
            cursor.execute(query, values)
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
        return

    def editTrain(self,choose):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'UPDATE Train SET name = ?, description = ? WHERE trainId = ?'
        values = (self.name, self.description, choose)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def editTrainClass(self, whichClass, choose):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'UPDATE TrainClass SET nSeats = ? WHERE trainId = ? AND classId = ?'
        values = (self.classes[whichClass][1], choose, whichClass)
        cursor.execute(query , values)
        conn.commit()
        conn.close()


    def getClasses(self, trainId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        query = 'SELECT classId, nSeats FROM TrainClass WHERE trainId = ?'
        values = (trainId)
        cursor.execute(query, values)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0] + " - " + row[1] + " - " + '\n')
            cursor2.execute(f'SELECT className FROM Class WHERE classId = "{row[0]}"')
            self.classes[row[0]][0][0]= cursor2.fetchone()[0]
        conn.close()

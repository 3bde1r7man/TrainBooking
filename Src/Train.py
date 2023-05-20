import sqlite3
class Train():
    def __init__(self, trainId = None):
        self.name 
        self.description 
        self.trainId
        self.adminId 
        self.classes = {}
        if trainId is not None:
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            query = 'SELECT name, details, adminId FROM Train WHERE trainId= ?'
            values = (trainId)
            cursor.execute(query, values)
            row = cursor.fetchone() 
            self.name = row[0]
            self.description = row[1]
            self.adminId = row[2]
            query = 'SELECT classId, nSeats From TrainCLass WHERE trainId = ?'
            values = (trainId)
            cursor.execute(query, values)
            rows = cursor.fetchall()
            query = 'SELECT className, price FROM Class where classId = ?'
            for row in rows:
                classId = row[0]
                nSeats = row[1]
                values = (classId)
                cursor.execute(query, values)
                row2 = cursor.fetchone()
                self.classes[classId][0][0] = row2[0]
                self.classes[classId][0][1] = row2[1]
                self.classes[classId][1] = nSeats
            conn.close()


    def addTrain(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'INSERT INTO Train (name, details, adminId) VALUES (?, ?, ?)'
        values = (self.name, self.description, self.adminId)
        cursor.execute(query, values)
        conn.commit()
        cursor.execute(f'SELECT trainId FROM Train WHERE name = "{self.name}" AND details = "{self.description}")')
        self.trainId = cursor.fetchone()[0]
        query = 'INSERT INTO TrainClass (trainId, classId, nSeats) VALUES (?, ?, ?)'
        for Class in self.classes:
            values = (self.trainId, Class, self.classes[Class][1])
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
        return self.classes

    def editTrain(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'UPDATE Train SET name = ?, details = ? WHERE trainId = ?'
        values = (self.name, self.description, self.trainId)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def editTrainClass(self, whichClass):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'UPDATE TrainClass SET nSeats = ? WHERE trainId = ? AND classId = ?'
        values = (self.classes[whichClass][1], self.trainId, whichClass)
        cursor.execute(query , values)
        conn.commit()
        conn.close()


    def getClasses(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        query = 'SELECT classId, nSeats FROM TrainClass WHERE trainId = ?'
        values = (self.trainId)
        cursor.execute(query, values)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0] + " - " + row[1] + " - " + '\n')
            cursor2.execute(f'SELECT className, price FROM Class WHERE classId = "{row[0]}"')
            row2 = cursor2.fetchall()
            self.classes[row[0]][0][0]= row2[0]
            self.classes[row[0]][0][1] = row2[1]
        conn.close()
        return self.classes

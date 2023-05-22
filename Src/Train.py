import sqlite3
import time
class Train():
    def __init__(self, trainId = None):
        self.name = None
        self.description = None
        self.trainId = None
        self.adminId = None
        self.classes = {} 
        if trainId is not None:
            self.trainId = trainId
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            cursor.execute('SELECT name, details, adminId FROM train WHERE trainId =?', (trainId,))
            row = cursor.fetchone() 
            self.name = row[0]
            self.description = row[1]
            self.adminId = row[2]
            cursor.execute('SELECT classId, nSeats From TrainCLass WHERE trainId = ?', (trainId,))
            rows = cursor.fetchall()
            
            for row in rows:
                classId = row[0]
                nSeats = row[1]
                cursor.execute('SELECT className, price FROM Class where classId = ?', (classId,))
                row2 = cursor.fetchone()
                classatt = [row2[0], row2[1], nSeats]
                self.classes[classId] = classatt
            conn.close()

    def addTrain(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'INSERT INTO Train (name, details, adminId) VALUES (?, ?, ?)'
        values = (self.name, self.description, self.adminId)
        cursor.execute(query, values)
        conn.commit()
        cursor.execute(f'SELECT max(trainId) FROM Train WHERE name = "{self.name}" AND details = "{self.description}"')
        
        self.trainId = cursor.fetchone()[0]
        if self.trainId is not None:
            query = 'INSERT INTO TrainClass (trainId, classId, nSeats) VALUES (?, ?, ?)'
            for Class in self.classes:
                values = (self.trainId, Class, self.classes[Class][2])
                cursor.execute(query, values)
                conn.commit()
            conn.close()
            return True
        else: 
            conn.close()
            return False

    def editTrain(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'UPDATE Train SET name = ?, details = ? WHERE trainId = ?'
        values = (self.name, self.description, self.trainId)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        return True

    def editTrainClass(self, whichClass):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'UPDATE TrainClass SET nSeats = ? WHERE trainId = ? AND classId = ?'
        values = (self.classes[whichClass][2], self.trainId, whichClass)
        cursor.execute(query , values)
        conn.commit()
        conn.close()
        return True


import sqlite3
class Train():
    def __init__(self):
        self.name 
        self.description 
        self.trainId
        self.adminId 
        self.classes = {}

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



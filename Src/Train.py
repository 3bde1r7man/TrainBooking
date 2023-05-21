import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


class Train:
    def __init__(self, trainId=None):
        self.name = None
        self.description = None
        self.trainId = None
        self.adminId = None
        self.classes = None
        if trainId is not None:
            self.trainId = trainId
            cursor.execute(f'SELECT name, details, adminId FROM Train WHERE trainId = {trainId}')
            row = cursor.fetchone()
            self.name = row[0]
            self.description = row[1]
            self.adminId = row[2]
            cursor.execute(f'SELECT classId, nSeats FROM TrainCLass WHERE trainId = {trainId}')
            rows = cursor.fetchall()
            self.classes = {}
            for row in rows:
                classId = row[0]
                nSeats = row[1]
                cursor.execute(f'SELECT className, price FROM Class WHERE classId = {classId}')
                row2 = cursor.fetchone()
                className = row2[0]
                price = row2[1]
                self.classes[classId] = [className, price, nSeats]

    def addTrain(self):
        cursor.execute(
            f'INSERT INTO Train (name, details, adminId) VALUES (?, ?, ?)',
            (self.name, self.description, self.adminId))
        conn.commit()

        cursor.execute(f'SELECT MAX(trainId) FROM Train WHERE adminId = {self.adminId}')
        self.trainId = cursor.fetchone()[0]

        for classId, classData in self.classes.items():
            cursor.execute(
                f'INSERT INTO TrainClass (trainId, classId, nSeats) VALUES (?, ?, ?)',
                (self.trainId, classId, classData[2]))
            conn.commit()

        messagebox.showinfo("Success", "Train added successfully")

    def editTrain(self):
        cursor.execute(
            f'UPDATE Train SET name = ?, details = ? WHERE trainId = ?',
            (self.name, self.description, self.trainId))
        conn.commit()

        messagebox.showinfo("Success", "Train edited successfully")

    def editTrainClass(self, whichClass):
        classData = self.classes[whichClass]
        cursor.execute(
            f'UPDATE TrainClass SET nSeats = ? WHERE trainId = ? AND classId = ?',
            (classData[2], self.trainId, whichClass))
        conn.commit()

        messagebox.showinfo("Success", "Train class edited successfully")
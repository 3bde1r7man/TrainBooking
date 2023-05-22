import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
class Trip:
    def __init__(self, tripId=None):
        self.src = None
        self.dest = None
        self.departs = None
        self.arrives = None
        self.price = None
        self.tripId = tripId
        self.trainId = None
        if tripId is not None:
            cursor.execute(f'SELECT src, dest, departs, arrives, price, trainId FROM Trip WHERE tripId = ?', (tripId))
            data = cursor.fetchone()
            self.src = data[0]
            self.dest = data[1]
            self.departs = data[2]
            self.arrives = data[3]
            self.price = data[4]
            self.trainId = data[5]

    def add_trip_to_database(self, adminId):
        cursor.execute(
            f'INSERT INTO Trip (src, dest, departs, arrives, price, adminId, trainId) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (self.src, self.dest, self.departs, self.arrives, self.price, adminId, self.trainId))
        conn.commit()

        messagebox.showinfo("Success", "Trip added successfully")

    def update_trip_to_database(self):
        cursor.execute(
            f'UPDATE Trip SET src = ?, dest = ?, departs = ?, arrives = ?, price = ?, trainId= ? WHERE tripId = ?',
            (self.src, self.dest, self.departs, self.arrives, self.price, self.trainId, self.tripId))
        conn.commit()

        messagebox.showinfo("Success", "Trip updated successfully")



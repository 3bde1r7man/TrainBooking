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
        if tripId is not None:
            cursor.execute(f'SELECT * FROM Trip WHERE tripId = ?', (tripId))
            data = cursor.fetchone()
            self.src = data[0]
            self.dest = data[1]
            self.departs = data[2]
            self.arrives = data[3]
            self.price = data[4]

    def add_trip_to_database(self, adminId, trainId):
        cursor.execute(
            f'INSERT INTO Trip (src, dest, departs, arrives, price, adminId, trainId) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (self.src, self.dest, self.departs, self.arrives, self.price, adminId, trainId))
        conn.commit()

        messagebox.showinfo("Success", "Trip added successfully")

    def update_trip_to_database(self):
        cursor.execute(
            f'UPDATE Trip SET src = ?, dest = ?, departs = ?, arrives = ?, price = ? WHERE tripId = ?',
            (self.src, self.dest, self.departs, self.arrives, self.price, self.tripId))
        conn.commit()

        messagebox.showinfo("Success", "Trip updated successfully")



import pyodbc
import sqlite3
import datetime
class Trip():
    def __init__(self, tripId = None):
        self.src = None
        self.dest = None
        self.departs = None
        self.arrives = None
        self.price = None
        self.tripId = tripId
        if(tripId != None):
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Trip WHERE tripId = {tripId}")
            data = cursor.fetchone()
            data = data[0]
            self.src = data[0]
            self.dest = data[1]
            self.departs = data[2]
            self.arrives = data[3]
            self.price = data[4]

    def add_trip_to_database(self, adminId, trainId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = "INSERT INTO Trip (src, dest, departs, arrives, price, adminId, trainId) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (self.src, self.dest, self.departs, self.arrives, self.price, adminId, trainId)

        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def update_trip_to_database(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = "UPDATE Trip SET src=?, dest=?, departs=?, arrives=?, price=? WHERE tripId=?"  # Replace <condition> with the appropriate condition for your update

        values = (self.src, self.dest, self.departs, self.arrives, self.price, self.tripId)

        cursor.execute(query, values)
        conn.commit()
        conn.close()



import pyodbc
import sqlite3
import datetime
class Trip():
    def __init__(self):
        self.src 
        self.dest
        self.departs
        self.arrives 
        self.price 

    def add_trip_to_database(self, adminId, trainId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = "INSERT INTO Trip (src, dist, departs, arrives, price, adminId, trainId) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (self.src, self.dest, self.departs, self.arrives, self.price, adminId, trainId)

        cursor.execute(query, values)
        conn.commit()
        conn.close()

    def update_trip_to_database(self, adminId, trainId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = "UPDATE Trip SET src=?, dist=?, departs=?, arrives=?, price=? WHERE adminId = ? AND trainID = ?"  # Replace <condition> with the appropriate condition for your update

        values = (self.src, self.dest, self.departs, self.arrives, self.price, adminId, trainId)

        cursor.execute(query, values)
        conn.commit()
        conn.close()



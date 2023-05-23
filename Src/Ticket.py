import sqlite3
from Customer import Customer
from tkinter import messagebox
from Train import Train
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


class Ticket:
    def __init__(self, TicketId=None, customerId=None):
        self.ticketId = None
        self.bookedSeats = None
        self.customerId = customerId
        self.tripId = None
        self.classId = None
        self.totalPrice = None
        self.passengers = None
        if TicketId is not None:
            self.ticketId = TicketId
            cursor.execute(f'SELECT bookedSeats, customerId, tripId, classId FROM Ticket WHERE TicketId = {TicketId}')
            row = cursor.fetchone()
            self.bookedSeats = row[0]
            self.customerId = row[1]
            self.tripId = row[2]
            self.classId = row[3]
            cursor.execute(f'SELECT name, age FROM Passenger WHERE ticketId = {TicketId}')
            rows = cursor.fetchall()
            self.passengers = []
            for row in rows:
                passenger = [row[0], row[1]]
                self.passengers.append(passenger)

    def addTicket(self, isOk):
        if (self.calculatenSeats() and isOk):
            cursor.execute(
                f'INSERT INTO Ticket (bookedSeats, customerId, tripId, classId) VALUES (?, ?, ?, ?)',
                (self.bookedSeats, self.customerId, self.tripId, self.classId))
            conn.commit()
            cursor.execute(f'SELECT MAX(TicketId) FROM Ticket WHERE customerId = {self.customerId}')
            self.ticketId = cursor.fetchone()[0]

            for passenger in self.passengers:
                cursor.execute(
                    f'INSERT INTO Passenger (name, age, ticketId) VALUES (?, ?, ?)',
                    (passenger[0], passenger[1], self.ticketId))
                conn.commit()
            
            messagebox.showinfo("Success", "Ticket added successfully")
        else:
            messagebox.showerror('Error', 'No seats available')



    def deleteTicket(self, customerId, tripId, isOk):
        if isOk:
            cursor.execute('SELECT ticketId FROM Ticket WHERE customerId = ? AND tripId = ?', (customerId, tripId))
            self.ticketId = cursor.fetchone()[0]
            cursor.execute(f'DELETE FROM Ticket WHERE customerId = {self.ticketId}')
            conn.commit()

            cursor.execute(f'DELETE FROM Passenger WHERE ticketId = {self.ticketId}')
            conn.commit()
            messagebox.showinfo("Success", "Ticket deleted successfully")

    def calculatePrice(self):
        classPrice = self.classPrice()
        tripPrice = self.tripPrice()
        tripPrice += tripPrice * classPrice
        normalPrice = tripPrice
        self.totalPrice = 0
        for row in self.passengers:
            age = row[1]
            if age < 10:
                price = 0.5 * normalPrice
            elif age > 60:
                price = .5 * normalPrice
            else:
                price = normalPrice
            self.totalPrice += price
        return self.totalPrice

    def calculatenSeats(self):
        cursor.execute(f'''SELECT TrainClass.avlSeats
                            FROM Train
                            INNER JOIN Trip ON Train.trainId = Trip.trainId
                            INNER JOIN TrainClass ON TrainClass.trainId = Train.trainId
                            WHERE tripId = {self.tripId} AND ClassId = {self.classId};
        ''')
        row = cursor.fetchone()
        avlSeats = row[0]
        if self.bookedSeats > avlSeats:
            return False
        else:
            cursor.execute(f'''SELECT Train.trainId 
                                FROM Train
                                INNER JOIN Trip ON Train.trainId = Trip.trainId
                                WHERE tripId = {self.tripId}
            ''')
            row = cursor.fetchone()
            trainId = row[0]
            train = Train(trainId)
            train.updateAvlSeats(self.classId, self.bookedSeats)
            return True
        


    def classPrice(self):
        cursor.execute(f'SELECT Price FROM Class WHERE classId = {self.classId}')
        row = cursor.fetchone()
        classPrice = float(row[0])
        return classPrice

    def tripPrice(self):
        cursor.execute(f'SELECT Price FROM Trip WHERE tripId = {self.tripId}')
        row = cursor.fetchone()
        tripPrice = float(row[0])
        return tripPrice
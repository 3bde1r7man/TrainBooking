import sqlite3
from Customer import Customer


class Ticket():
    def __init__(self, TicketId = None):
        self.ticketId = None
        self.bookedSeats = None
        self.customerId = None
        self.tripId = None  
        self.classId = None
        self.totalPrice = None
        self.passengers = None  
        if TicketId is not None:
            self.ticketId = TicketId
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            query = 'SELECT bookedSeats, customerId, tripId, classId FROM Ticket WHERE TicketId = ?'
            values = (TicketId)
            cursor.execute(query, values)
            row = cursor.fetchone()
            self.bookedSeats = row[0]
            self.customerId = row[1]
            self.tripId = row[2]
            self.classId = row[3]
            query = 'SELECT name, age FROM Passenger WHERE ticketId = ?'
            values = (TicketId)
            cursor.execute(query, values)
            rows = cursor.fetchall()
            self.passengers = []
            for row in rows:
                passenger = [row[0], row[1]]
                self.passengers.append(passenger)
            conn.close()
    
    def addTicket(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'INSERT INTO Ticket  (bookedSeats, customerId, tripId, classId) VALUES (?,?,?,?)'
        values = (self.bookedSeats, self.customerId, self.tripId, self.classId)
        cursor.execute(query, values)
        conn.commit()
        query = 'INSERT INTO Passenger (name, age, ticketId)'
        for passenger in self.passengers:
            values = (passenger[0], passenger[1], self.ticketId)
            cursor.execute(query, values)
            conn.commit()
        
        customer = Customer(self.customerId)
        values = (customer.name, customer.customerAge(), self.ticketId)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
    
    def deleteTicket(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'DELETE FROM Ticket WHERE TicketId =?'
        values = (self.ticketId)
        cursor.execute(query, values)
        conn.commit()
        query = 'DELETE FROM Passenger WHERE ticketId =?'
        values = (self.ticketId)    
        cursor.execute(query, values)
        conn.commit()
        conn.close()
    
    def calculatePrice(self):
        classPrice = self.classPrice()
        tripPrice = self.tripPrice()
        tripPrice += tripPrice * classPrice
        normalPrice = tripPrice 
        for row in self.passengers:
            age = row[1]
            if age < 10:
                price = 0.5 * normalPrice
            elif age < 60:
                price = .5 * normalPrice
            else:
                price = normalPrice
            self.totalPrice += price

    def classPrice(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'SELECT Price FROM Class WHERE classId =?'
        values = (self.classId) 
        cursor.execute(query, values)
        row = cursor.fetchone()
        classPrice = float(row[0])
        conn.close()
        return classPrice
    
    def tripPrice(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = 'SELECT Price FROM Trip WHERE tripId =?'
        values = (self.tripId)
        cursor.execute(query, values)
        row = cursor.fetchone()
        tripPrice = float(row[0])
        conn.close()
        return tripPrice
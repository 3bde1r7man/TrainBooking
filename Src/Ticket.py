import sqlite3
import pyodbc
import Trip
import Class
import TrainClass

# by ahmed 
#conn = sqlite3.connect('db.sqlite3')
#cursor = conn.cursor()

class Ticket():
    
    def __init__(self):
      self.ticketId = ""
      self.bookedseats
      self.nSeats  
      self.price
     # passenger = [ name , age ]


    def add_Ticket_to_database(self.ticketId):
          conn = sqlite3.connect('db.sqlite3')
          cursor = conn.cursor()


           AAA = "INSERT INTO Ticket (ticketId ,nSeats,customerId ,tripId ,classId) VALUES (? , ?,? , ? , ? )"
           iD = (self.ticketId,self.nSeats , customerId, tripId ,classId )


           cursor.execute(AAA, iD)
          conn.commit()
          conn.close()

    def Delete_ticket_f_databacce(ticketId):
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
          
         ACA = "DELETE FROM Tickets WHERE tiketId ( tiketId ) VALUES (?) "
         ic = (self.ticketId)

          cursor.execute(ACA, ic)
           conn.commit()
           conn.close()


    def Total_Price(price):
      conn = sqlite3.connect('db.sqlite3')
      cursor = conn.cursor()

    
        cursor.execute(f'SELECT price FROM Class WHERE Class = "{price}"')  
        price_class = cursor.fetchone()[0]

       cursor.execute(f'SELECT price FROM trip WHERE price = "{price}"')  
       price_trip = cursor.fetchone()[0]

       # Calculate the total price
       total_price = (price_trip + price_class) * nSeats

       conn.close()

     return total_price


    def calculate_nseats():
       conn = sqlite3.connect('db.sqlite3')
       cursor = conn.cursor()

       # Count the number of nSeats
       cursor.execute(f'SELECT COUNT(nSeats) FROM TrianClass WHERE nSeats = "{Trinclass}"')
     
       nseats_count = cursor.fetchone()[0]

       conn.close()

       return nseats_count

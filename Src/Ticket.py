import sqlite3
import pyodbc
import Customer
import Trip
import Class

# by ahmed 
#conn = sqlite3.connect('db.sqlite3')
#cursor = conn.cursor()

class Ticket():
    
    def __init__(self):
      self.ticketId = ""


      def add_Ticket_to_database(self.TicketId):
          conn = sqlite3.connect('db.sqlite3')
          cursor = conn.cursor()


           AAA = "INSERT INTO Ticket (ticketId ,customerId ,tripId ,classId) VALUES (? , ? , ? , ? )"
           iD = (self.ticketId, customerId, tripId ,classId )


           cursor.execute(AAA, iD)
        conn.commit()
        conn.close()


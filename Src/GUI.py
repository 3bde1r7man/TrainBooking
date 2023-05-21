import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
import datetime
import sqlite3

# Create the main Tkinter window
window = tk.Tk()
window.title("Train Booking System")

# Database connection
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

        messagebox.showinfo("Success", "Ticket added successfully")

    def deleteTicket(self):
        cursor.execute(f'DELETE FROM Ticket WHERE TicketId = {self.ticketId}')
        conn.commit()

        cursor.execute(f'DELETE FROM Passenger WHERE ticketId = {self.ticketId}')
        conn.commit()

        messagebox.showinfo("Success", "Ticket deleted successfully")

    def calculatePrice(self):
        customer = Customer()
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
        cursor.execute(f'SELECT Price FROM Class WHERE classId = {self.classId}')
        row = cursor.fetchone()
        classPrice = float(row[0])
        return classPrice

    def tripPrice(self):
        cursor.execute(f'SELECT Price FROM Trip WHERE tripId = {self.tripId}')
        row = cursor.fetchone()
        tripPrice = float(row[0])
        return tripPrice


# Train Class
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

# GUI Elements
lbl_customer = tk.Label(window, text="Customer")
lbl_customer.grid(row=0, column=0, padx=5, pady=5)

lbl_ticket = tk.Label(window, text="Ticket")
lbl_ticket.grid(row=0, column=1, padx=5, pady=5)

lbl_train = tk.Label(window, text="Train")
lbl_train.grid(row=0, column=2, padx=5, pady=5)

lbl_trip = tk.Label(window, text="Trip")
lbl_trip.grid(row=0, column=3, padx=5, pady=5)

# Customer GUI
lbl_customer_name = tk.Label(window, text="Name:")
lbl_customer_name.grid(row=1, column=0, padx=5, pady=5)

entry_customer_name = tk.Entry(window)
entry_customer_name.grid(row=1, column=1, padx=5, pady=5)

lbl_customer_dob = tk.Label(window, text="DOB:")
lbl_customer_dob.grid(row=2, column=0, padx=5, pady=5)

entry_customer_dob = tk.Entry(window)
entry_customer_dob.grid(row=2, column=1, padx=5, pady=5)

lbl_customer_email = tk.Label(window, text="Email:")
lbl_customer_email.grid(row=3, column=0, padx=5, pady=5)

entry_customer_email = tk.Entry(window)
entry_customer_email.grid(row=3, column=1, padx=5, pady=5)

lbl_customer_password = tk.Label(window, text="Password:")
lbl_customer_password.grid(row=4, column=0, padx=5, pady=5)

entry_customer_password = tk.Entry(window, show="*")
entry_customer_password.grid(row=4, column=1, padx=5, pady=5)

lbl_customer_phone = tk.Label(window, text="Phone:")
lbl_customer_phone.grid(row=5, column=0, padx=5, pady=5)

entry_customer_phone = tk.Entry(window)
entry_customer_phone.grid(row=5, column=1, padx=5, pady=5)

btn_customer_signup = tk.Button(window, text="Sign Up", command=lambda: signup_customer())
btn_customer_signup.grid(row=6, column=0, padx=5, pady=5)

btn_customer_signin = tk.Button(window, text="Sign In", command=lambda: signin_customer())
btn_customer_signin.grid(row=6, column=1, padx=5, pady=5)

# Ticket GUI
lbl_ticket_customer_id = tk.Label(window, text="Customer ID:")
lbl_ticket_customer_id.grid(row=1, column=2, padx=5, pady=5)

entry_ticket_customer_id = tk.Entry(window)
entry_ticket_customer_id.grid(row=1, column=3, padx=5, pady=5)

lbl_ticket_trip_id = tk.Label(window, text="Trip ID:")
lbl_ticket_trip_id.grid(row=2, column=2, padx=5, pady=5)

entry_ticket_trip_id = tk.Entry(window)
entry_ticket_trip_id.grid(row=2, column=3, padx=5, pady=5)

lbl_ticket_class_id = tk.Label(window, text="Class ID:")
lbl_ticket_class_id.grid(row=3, column=2, padx=5, pady=5)

entry_ticket_class_id = tk.Entry(window)
entry_ticket_class_id.grid(row=3, column=3, padx=5, pady=5)

lbl_ticket_passenger_name = tk.Label(window, text="Passenger Name:")
lbl_ticket_passenger_name.grid(row=4, column=2, padx=5, pady=5)

entry_ticket_passenger_name = tk.Entry(window)
entry_ticket_passenger_name.grid(row=4, column=3, padx=5, pady=5)

lbl_ticket_passenger_age = tk.Label(window, text="Passenger Age:")
lbl_ticket_passenger_age.grid(row=5, column=2, padx=5, pady=5)

entry_ticket_passenger_age = tk.Entry(window)
entry_ticket_passenger_age.grid(row=5, column=3, padx=5, pady=5)

btn_ticket_add = tk.Button(window, text="Add Ticket", command=lambda: add_ticket())
btn_ticket_add.grid(row=6, column=2, padx=5, pady=5)

btn_ticket_delete = tk.Button(window, text="Delete Ticket", command=lambda: delete_ticket())
btn_ticket_delete.grid(row=6, column=3, padx=5, pady=5)

# Train GUI
lbl_train_name = tk.Label(window, text="Train Name:")
lbl_train_name.grid(row=1, column=4, padx=5, pady=5)

entry_train_name = tk.Entry(window)
entry_train_name.grid(row=1, column=5, padx=5, pady=5)

lbl_train_description = tk.Label(window, text="Description:")
lbl_train_description.grid(row=2, column=4, padx=5, pady=5)

entry_train_description = tk.Entry(window)
entry_train_description.grid(row=2, column=5, padx=5, pady=5)

lbl_train_class_id = tk.Label(window, text="Class ID:")
lbl_train_class_id.grid(row=3, column=4, padx=5, pady=5)

entry_train_class_id = tk.Entry(window)
entry_train_class_id.grid(row=3, column=5, padx=5, pady=5)

lbl_train_n_seats = tk.Label(window, text="Number of Seats:")
lbl_train_n_seats.grid(row=4, column=4, padx=5, pady=5)

entry_train_n_seats = tk.Entry(window)
entry_train_n_seats.grid(row=4, column=5, padx=5, pady=5)

btn_train_add = tk.Button(window, text="Add Train", command=lambda: add_train())
btn_train_add.grid(row=5, column=4, padx=5, pady=5)

btn_train_edit = tk.Button(window, text="Edit Train", command=lambda: edit_train())
btn_train_edit.grid(row=5, column=5, padx=5, pady=5)

btn_train_class_edit = tk.Button(window, text="Edit Train Class", command=lambda: edit_train_class())
btn_train_class_edit.grid(row=6, column=4, padx=5, pady=5)

# Trip GUI
lbl_trip_src = tk.Label(window, text="Source:")
lbl_trip_src.grid(row=1, column=6, padx=5, pady=5)

entry_trip_src = tk.Entry(window)
entry_trip_src.grid(row=1, column=7, padx=5, pady=5)

lbl_trip_dest = tk.Label(window, text="Destination:")
lbl_trip_dest.grid(row=2, column=6, padx=5, pady=5)

entry_trip_dest = tk.Entry(window)
entry_trip_dest.grid(row=2, column=7, padx=5, pady=5)

lbl_trip_departs = tk.Label(window, text="Departs:")
lbl_trip_departs.grid(row=3, column=6, padx=5, pady=5)

entry_trip_departs = tk.Entry(window)
entry_trip_departs.grid(row=3, column=7, padx=5, pady=5)

lbl_trip_arrives = tk.Label(window, text="Arrives:")
lbl_trip_arrives.grid(row=4, column=6, padx=5, pady=5)

entry_trip_arrives = tk.Entry(window)
entry_trip_arrives.grid(row=4, column=7, padx=5, pady=5)

lbl_trip_price = tk.Label(window, text="Price:")
lbl_trip_price.grid(row=5, column=6, padx=5, pady=5)

entry_trip_price = tk.Entry(window)
entry_trip_price.grid(row=5, column=7, padx=5, pady=5)

btn_trip_add = tk.Button(window, text="Add Trip", command=lambda: add_trip())
btn_trip_add.grid(row=6, column=6, padx=5, pady=5)

btn_trip_update = tk.Button(window, text="Update Trip", command=lambda: update_trip())
btn_trip_update.grid(row=6, column=7, padx=5, pady=5)

window.mainloop()



# Trip Class
class Trip:
    def __init__(self, tripId=None):
        self.src = None
        self.dest = None
        self.departs = None
        self.arrives = None
        self.price = None
        self.tripId = tripId
        if tripId is not None:
            cursor.execute(f'SELECT * FROM Trip WHERE id = ?', (tripId,))
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


# GUI Elements
lbl_customer = tk.Label(window, text="Customer")
lbl_customer.grid(row=0, column=0, padx=5, pady=5)

lbl_ticket = tk.Label(window, text="Ticket")
lbl_ticket.grid(row=0, column=1, padx=5, pady=5)

lbl_train = tk.Label(window, text="Train")
lbl_train.grid(row=0, column=2, padx=5, pady=5)

lbl_trip = tk.Label(window, text="Trip")
lbl_trip.grid(row=0, column=3, padx=5, pady=5)

# Customer GUI
lbl_customer_name = tk.Label(window, text="Name:")
lbl_customer_name.grid(row=1, column=0, padx=5, pady=5)

entry_customer_name = tk.Entry(window)
entry_customer_name.grid(row=1, column=1, padx=5, pady=5)

lbl_customer_dob = tk.Label(window, text="DOB:")
lbl_customer_dob.grid(row=2, column=0, padx=5, pady=5)

entry_customer_dob = tk.Entry(window)
entry_customer_dob.grid(row=2, column=1, padx=5, pady=5)

lbl_customer_email = tk.Label(window, text="Email:")
lbl_customer_email.grid(row=3, column=0, padx=5, pady=5)

entry_customer_email = tk.Entry(window)
entry_customer_email.grid(row=3, column=1, padx=5, pady=5)

lbl_customer_password = tk.Label(window, text="Password:")
lbl_customer_password.grid(row=4, column=0, padx=5, pady=5)

entry_customer_password = tk.Entry(window, show="*")
entry_customer_password.grid(row=4, column=1, padx=5, pady=5)

lbl_customer_phone = tk.Label(window, text="Phone:")
lbl_customer_phone.grid(row=5, column=0, padx=5, pady=5)

entry_customer_phone = tk.Entry(window)
entry_customer_phone.grid(row=5, column=1, padx=5, pady=5)

btn_customer_signup = tk.Button(window, text="Sign Up", command=lambda: signup_customer())
btn_customer_signup.grid(row=6, column=0, padx=5, pady=5)

btn_customer_signin = tk.Button(window, text="Sign In", command=lambda: signin_customer())
btn_customer_signin.grid(row=6, column=1, padx=5, pady=5)

# Ticket GUI
lbl_ticket_customer_id = tk.Label(window, text="Customer ID:")
lbl_ticket_customer_id.grid(row=1, column=2, padx=5, pady=5)

entry_ticket_customer_id = tk.Entry(window)
entry_ticket_customer_id.grid(row=1, column=3, padx=5, pady=5)

lbl_ticket_trip_id = tk.Label(window, text="Trip ID:")
lbl_ticket_trip_id.grid(row=2, column=2, padx=5, pady=5)

entry_ticket_trip_id = tk.Entry(window)
entry_ticket_trip_id.grid(row=2, column=3, padx=5, pady=5)

lbl_ticket_class_id = tk.Label(window, text="Class ID:")
lbl_ticket_class_id.grid(row=3, column=2, padx=5, pady=5)

entry_ticket_class_id = tk.Entry(window)
entry_ticket_class_id.grid(row=3, column=3, padx=5, pady=5)

lbl_ticket_passenger_name = tk.Label(window, text="Passenger Name:")
lbl_ticket_passenger_name.grid(row=4, column=2, padx=5, pady=5)

entry_ticket_passenger_name = tk.Entry(window)
entry_ticket_passenger_name.grid(row=4, column=3, padx=5, pady=5)

lbl_ticket_passenger_age = tk.Label(window, text="Passenger Age:")
lbl_ticket_passenger_age.grid(row=5, column=2, padx=5, pady=5)

entry_ticket_passenger_age = tk.Entry(window)
entry_ticket_passenger_age.grid(row=5, column=3, padx=5, pady=5)

btn_ticket_add = tk.Button(window, text="Add Ticket", command=lambda: add_ticket())
btn_ticket_add.grid(row=6, column=2, padx=5, pady=5)

btn_ticket_delete = tk.Button(window, text="Delete Ticket", command=lambda: delete_ticket())
btn_ticket_delete.grid(row=6, column=3, padx=5, pady=5)

# Train GUI
lbl_train_name = tk.Label(window, text="Train Name:")
lbl_train_name.grid(row=1, column=4, padx=5, pady=5)

entry_train_name = tk.Entry(window)
entry_train_name.grid(row=1, column=5, padx=5, pady=5)

lbl_train_description = tk.Label(window, text="Description:")
lbl_train_description.grid(row=2, column=4, padx=5, pady=5)

entry_train_description = tk.Entry(window)
entry_train_description.grid(row=2, column=5, padx=5, pady=5)

lbl_train_class_id = tk.Label(window, text="Class ID:")
lbl_train_class_id.grid(row=3, column=4, padx=5, pady=5)

entry_train_class_id = tk.Entry(window)
entry_train_class_id.grid(row=3, column=5, padx=5, pady=5)

lbl_train_n_seats = tk.Label(window, text="Number of Seats:")
lbl_train_n_seats.grid(row=4, column=4, padx=5, pady=5)

entry_train_n_seats = tk.Entry(window)
entry_train_n_seats.grid(row=4, column=5, padx=5, pady=5)

btn_train_add = tk.Button(window, text="Add Train", command=lambda: add_train())
btn_train_add.grid(row=5, column=4, padx=5, pady=5)

btn_train_edit = tk.Button(window, text="Edit Train", command=lambda: edit_train())
btn_train_edit.grid(row=5, column=5, padx=5, pady=5)

btn_train_class_edit = tk.Button(window, text="Edit Train Class", command=lambda: edit_train_class())
btn_train_class_edit.grid(row=6, column=4, padx=5, pady=5)

# Trip GUI
lbl_trip_src = tk.Label(window, text="Source:")
lbl_trip_src.grid(row=1, column=6, padx=5, pady=5)

entry_trip_src = tk.Entry(window)
entry_trip_src.grid(row=1, column=7, padx=5, pady=5)

lbl_trip_dest = tk.Label(window, text="Destination:")
lbl_trip_dest.grid(row=2, column=6, padx=5, pady=5)

entry_trip_dest = tk.Entry(window)
entry_trip_dest.grid(row=2, column=7, padx=5, pady=5)

lbl_trip_departs = tk.Label(window, text="Departs:")
lbl_trip_departs.grid(row=3, column=6, padx=5, pady=5)

entry_trip_departs = tk.Entry(window)
entry_trip_departs.grid(row=3, column=7, padx=5, pady=5)

lbl_trip_arrives = tk.Label(window, text="Arrives:")
lbl_trip_arrives.grid(row=4, column=6, padx=5, pady=5)

entry_trip_arrives = tk.Entry(window)
entry_trip_arrives.grid(row=4, column=7, padx=5, pady=5)

lbl_trip_price = tk.Label(window, text="Price:")
lbl_trip_price.grid(row=5, column=6, padx=5, pady=5)

entry_trip_price = tk.Entry(window)
entry_trip_price.grid(row=5, column=7, padx=5, pady=5)

btn_trip_add = tk.Button(window, text="Add Trip", command=lambda: add_trip())
btn_trip_add.grid(row=6, column=6, padx=5, pady=5)

btn_trip_update = tk.Button(window, text="Update Trip", command=lambda: update_trip())
btn_trip_update.grid(row=6, column=7, padx=5, pady=5)

window.mainloop()

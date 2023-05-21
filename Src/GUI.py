import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
import datetime
import sqlite3
from Admin import Admin

# Create the main Tkinter window
window = tk.Tk()
window.title("Train Booking System")

# Database connection
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

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

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Train Booking System")

        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()
        self.admin = Admin()

        # Initialize the GUI elements
        self.init_elements()

    def init_elements(self):
        # Add train button
        add_train_btn = tk.Button(self.root, text="Add Train", command=self.add_train)
        add_train_btn.pack()

        # Update train button
        update_train_btn = tk.Button(self.root, text="Update Train", command=self.update_train)
        update_train_btn.pack()

        # Add trip button
        add_trip_btn = tk.Button(self.root, text="Add Trip", command=self.add_trip)
        add_trip_btn.pack()

        # Update trip button
        update_trip_btn = tk.Button(self.root, text="Update Trip", command=self.update_trip)
        update_trip_btn.pack()

        # Show available seats button
        show_seats_btn = tk.Button(self.root, text="Show Available Seats", command=self.show_available_seats)
        show_seats_btn.pack()

        # Book trip button
        book_trip_btn = tk.Button(self.root, text="Book Trip", command=self.book_trip)
        book_trip_btn.pack()

        

    def add_train(self):
        # Implement the logic for adding a train
        pass

    def update_train(self):
        # Implement the logic for updating a train
        pass

    def show_available_seats(self):
        # Implement the logic for showing available seats
        pass

    def book_trip(self):
        # Implement the logic for booking a trip
        pass

    def run(self):
        self.root.mainloop()

    def __del__(self):
        self.conn.close()



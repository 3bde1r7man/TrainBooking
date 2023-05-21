import tkinter as tk
import sqlite3
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Train Booking System")

        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

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

    def add_trip(self):
        # Implement the logic for adding a trip
        pass

    def update_trip(self):
        # Implement the logic for updating a trip
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




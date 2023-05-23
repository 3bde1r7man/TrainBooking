import tkinter as tk
from tkinter import simpledialog, messagebox
from Admin import Admin
import sqlite3

class TripsView:
    def __init__(self, adminId):
        self.admin = Admin(adminId)
        self.root = tk.Tk()
        self.root.resizable()
        self.root.title("Trips")
        self.root.configure(bg="black")

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'SELECT src, dest, departs, arrives, price, trainId FROM Trip')
        data = cursor.fetchall()
        counter = 1
        for row in data:
            self.trip_num = tk.Label(self.root, text=f"Trip: {counter}", bg="black", fg="white")
            self.trip_num.pack(pady=5)
            counter += 1

            self.lbl_trip_src = tk.Label(self.root, text=f"Source: {row[0]}", bg="black", fg="white")
            self.lbl_trip_src.pack(pady=5)

            self.lbl_trip_dest = tk.Label(self.root, text=f"Destination: {row[1]}", bg="black", fg="white")
            self.lbl_trip_dest.pack(pady=5)

            self.lbl_trip_departs = tk.Label(self.root, text=f"Departs: {row[2]}", bg="black", fg="white")
            self.lbl_trip_departs.pack(pady=5)

            self.lbl_trip_arrives = tk.Label(self.root, text=f"Arrives: {row[3]}", bg="black", fg="white")
            self.lbl_trip_arrives.pack(pady=5)
            
            self.lbl_trip_price = tk.Label(self.root, text=f"Price: {row[4]}", bg="black", fg="white")
            self.lbl_trip_price.pack(pady=5)

            self.lbl_trip_train = tk.Label(self.root, text=f"Train: {row[5]}", bg="black", fg="white")
            self.lbl_trip_train.pack(pady=5)

            update_trip_btn = tk.Button(self.root, text="Update Trip", bg="red", fg="white", command=lambda: UpdateTripView(adminId, str(row[5])))
            update_trip_btn.pack(pady=5)

        self.root.mainloop()

class AddTripView:
    def __init__(self, adminId):
        self.admin = Admin(adminId)
        self.root = tk.Tk()
        self.root.geometry('1000x600+280+100')
        self.root.title("Add Trip")
        self.root.configure(bg="black")

        self.lbl_trip_src = tk.Label(self.root, text="Source:", bg="black", fg="white")
        self.lbl_trip_src.pack(pady=5)

        self.trip_src = tk.Entry(self.root)
        self.trip_src.pack(pady=5)

        self.lbl_trip_dest = tk.Label(self.root, text="Destination:", bg="black", fg="white")
        self.lbl_trip_dest.pack(pady=5)

        self.trip_dest = tk.Entry(self.root)
        self.trip_dest.pack(pady=5)

        self.lbl_trip_departs = tk.Label(self.root, text="Departs:", bg="black", fg="white")
        self.lbl_trip_departs.pack(pady=5)

        self.trip_departs = tk.Entry(self.root)
        self.trip_departs.pack(pady=5)

        self.lbl_trip_arrives = tk.Label(self.root, text="Arrives:", bg="black", fg="white")
        self.lbl_trip_arrives.pack(pady=5)

        self.trip_arrives = tk.Entry(self.root)
        self.trip_arrives.pack(pady=5)

        self.lbl_trip_price = tk.Label(self.root, text="Price:", bg="black", fg="white")
        self.lbl_trip_price.pack(pady=5)

        self.trip_price = tk.Entry(self.root)
        self.trip_price.pack(pady=5)

        self.trip_train = self.select_train()

        while self.trip_train == -1:
            self.trip_train = self.select_train()

        if self.trip_train == None:
            return

        add_trip_btn = tk.Button(self.root, text="Add Trip", bg="red", fg="white", command=lambda: self.addTrip())
        add_trip_btn.pack(pady=5)

        self.root.mainloop()

    def addTrip(self):
        if not self.admin.add_trip(self.trip_src.get(), self.trip_dest.get(), self.trip_departs.get(), self.trip_arrives.get(), self.trip_price.get(), str(self.trip_train)):
            messagebox.showerror("Error", "The Entered Dates are not valid")

    def select_train(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT trainId, name FROM Train')
        rows = cursor.fetchall()
        conn.close()

        train_names = [f"{row[0]} - {row[1]}" for row in rows]
        prompt = "\n".join(train_names)
        selected_index = simpledialog.askinteger("Select Train", f"Select a train:\n{prompt}", minvalue=1,)

        if selected_index == None:
            return None

        for ids in rows:
            if selected_index == int(ids[0]):
                return selected_index

        messagebox.showerror("Error", "Your selected index does not exist")
        return -1

class UpdateTripView:
    def __init__(self, adminId, tripId):
        self.admin = Admin(adminId)
        self.root = tk.Tk()
        self.root.geometry('1000x600+280+100')
        self.root.title("UpdateTrip")
        self.root.configure(bg="black")
        self.trip_id = tripId

        self.lbl_trip_src = tk.Label(self.root, text="Source:", bg="black", fg="white")
        self.lbl_trip_src.pack(pady=5)

        self.trip_src = tk.Entry(self.root)
        self.trip_src.pack(pady=5)

        self.lbl_trip_dest = tk.Label(self.root, text="Destination:", bg="black", fg="white")
        self.lbl_trip_dest.pack(pady=5)

        self.trip_dest = tk.Entry(self.root)
        self.trip_dest.pack(pady=5)

        self.lbl_trip_departs = tk.Label(self.root, text="Departs:", bg="black", fg="white")
        self.lbl_trip_departs.pack(pady=5)

        self.trip_departs = tk.Entry(self.root)
        self.trip_departs.pack(pady=5)

        self.lbl_trip_arrives = tk.Label(self.root, text="Arrives:", bg="black", fg="white")
        self.lbl_trip_arrives.pack(pady=5)

        self.trip_arrives = tk.Entry(self.root)
        self.trip_arrives.pack(pady=5)

        self.lbl_trip_price = tk.Label(self.root, text="Price:", bg="black", fg="white")
        self.lbl_trip_price.pack(pady=5)

        self.trip_price = tk.Entry(self.root)
        self.trip_price.pack(pady=5)

        self.trip_train = self.select_train()

        while self.trip_train == -1:
            self.trip_train = self.select_train()

        if self.trip_train == None:
            return

        update_trip_btn = tk.Button(self.root, text="Update Trip", bg="red", fg="white", command=lambda: self.updateTrip())
        update_trip_btn.pack(pady=5)

        self.root.mainloop()

    def updateTrip(self):
        if not self.admin.update_trip(self.trip_id, self.trip_src.get(), self.trip_dest.get(), self.trip_departs.get(), self.trip_arrives.get(), self.trip_price.get(), str(self.trip_train)):
            messagebox.showerror("Error", "The Entered Dates are not valid")

    def select_train(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('SELECT trainId, name FROM Train')
        rows = cursor.fetchall()
        conn.close()

        train_names = [f"{row[0]} - {row[1]}" for row in rows]
        prompt = "\n".join(train_names)
        selected_index = simpledialog.askinteger("Select Train", f"Select a train:\n{prompt}", minvalue=1,)

        if selected_index == None:
            return None

        for ids in rows:
            if selected_index == int(ids[0]):
                return selected_index

        messagebox.showerror("Error", "Your selected index does not exist")
        return -1

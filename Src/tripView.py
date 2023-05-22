import tkinter as tk
from Admin import Admin
import sqlite3

class TripsView:
    def __init__(self, adminId):
        self.admin = Admin(adminId)
        self.root = tk.Tk()
        self.root.title("Trips")

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'SELECT src, dest, departs, arrives, price, trainId FROM Trip')
        data = cursor.fetchall()
        counter = 1
        for row in data:
            self.trip_num = tk.Label(self.root, text=f"Trip: {counter}")
            self.trip_num.pack()
            counter += 1

            self.lbl_trip_src = tk.Label(self.root, text=f"Source: {row[0]}")
            self.lbl_trip_src.pack()

            self.lbl_trip_dest = tk.Label(self.root, text=f"Destination: {row[1]}")
            self.lbl_trip_dest.pack()

            self.lbl_trip_departs = tk.Label(self.root, text=f"Departs: {row[2]}")
            self.lbl_trip_departs.pack()

            self.lbl_trip_arrives = tk.Label(self.root, text=f"Arrives: {row[3]}")
            self.lbl_trip_arrives.pack()
            
            self.lbl_trip_price = tk.Label(self.root, text=f"Price:{row[4]}")
            self.lbl_trip_price.pack()

            self.lbl_trip_train = tk.Label(self.root, text=f"Train:{row[5]}")
            self.lbl_trip_train.pack()

            update_trip_btn = tk.Button(self.root, text="Update Trip", command=lambda: UpdateTripView(adminId, str(row[5])))
            update_trip_btn.pack()

        self.root.mainloop()



class AddTripView:
    def __init__(self, adminId):
        self.admin = Admin(adminId)
        self.root = tk.Tk()
        self.root.title("Add Trip")

        self.lbl_trip_src = tk.Label(self.root, text="Source:")
        self.lbl_trip_src.pack()

        self.trip_src = tk.Entry(self.root)
        self.trip_src.pack()

        self.lbl_trip_dest = tk.Label(self.root, text="Destination:")
        self.lbl_trip_dest.pack()

        self.trip_dest = tk.Entry(self.root)
        self.trip_dest.pack()

        self.lbl_trip_departs = tk.Label(self.root, text="Departs:")
        self.lbl_trip_departs.pack()

        self.trip_departs = tk.Entry(self.root)
        self.trip_departs.pack()

        self.lbl_trip_arrives = tk.Label(self.root, text="Arrives:")
        self.lbl_trip_arrives.pack()

        self.trip_arrives = tk.Entry(self.root)
        self.trip_arrives.pack()

        self.lbl_trip_price = tk.Label(self.root, text="Price:")
        self.lbl_trip_price.pack()

        self.trip_price = tk.Entry(self.root)
        self.trip_price.pack()

        add_trip_btn = tk.Button(self.root, text="Add Trip", command=lambda: self.addTrip())
        add_trip_btn.pack()

        self.root.mainloop()

    def addTrip(self):
        self.admin.add_trip(
            self.trip_src.get(), self.trip_dest.get(), self.trip_departs.get(), self.trip_arrives.get(), self.trip_price.get(),
        )
        

class UpdateTripView:
    def __init__(self, adminId, tripId):
        self.admin = Admin(adminId)
        self.root = tk.Tk()
        self.root.title("UpdateTrip")
        self.trip_id = tripId

        self.lbl_trip_src = tk.Label(self.root, text="Source:")
        self.lbl_trip_src.pack()

        self.trip_src = tk.Entry(self.root)
        self.trip_src.pack()

        self.lbl_trip_dest = tk.Label(self.root, text="Destination:")
        self.lbl_trip_dest.pack()

        self.trip_dest = tk.Entry(self.root)
        self.trip_dest.pack()

        self.lbl_trip_departs = tk.Label(self.root, text="Departs:")
        self.lbl_trip_departs.pack()

        self.trip_departs = tk.Entry(self.root)
        self.trip_departs.pack()

        self.lbl_trip_arrives = tk.Label(self.root, text="Arrives:")
        self.lbl_trip_arrives.pack()

        self.trip_arrives = tk.Entry(self.root)
        self.trip_arrives.pack()

        self.lbl_trip_price = tk.Label(self.root, text="Price:")
        self.lbl_trip_price.pack()

        self.trip_price = tk.Entry(self.root)
        self.trip_price.pack()

        update_trip_btn = tk.Button(self.root, text="Update Trip", command=lambda: self.updateTrip())
        update_trip_btn.pack()

        self.root.mainloop()

    def updateTrip(self):
        self.admin.update_trip(
            self.trip_id, self.trip_src.get(), self.trip_dest.get(), self.trip_departs.get(), self.trip_arrives.get(), self.trip_price.get(), 15
        )
        
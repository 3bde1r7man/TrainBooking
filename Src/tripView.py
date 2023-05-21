import tkinter as tk
from Admin import Admin

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
    def __init__(self, adminId):
        self.admin = Admin(adminId)
        self.root = tk.Tk()
        self.root.title("UpdateTrip")
        
        self.lbl_trip_id = tk.Label(self.root, text="ID:")
        self.lbl_trip_id.pack()

        self.trip_id = tk.Entry(self.root)
        self.trip_id.pack()

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

    def update_trip(self):
        self.admin.add_trip(
            self.trip_id.get(), self.trip_src.get(), self.trip_dest.get(), self.trip_departs.get(), self.trip_arrives.get(), self.trip_price.get(),
        )
        
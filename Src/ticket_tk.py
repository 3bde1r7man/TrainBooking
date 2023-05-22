from tkinter import *


#conn = sqlite3.connect('db.sqlite3')
#cursor = conn.cursor()

window = Tk()
window.geometry("300x400")

window.title("Train Booking System")


def __init__(self, customerId):
    self.Customer = Customer(customerId)


lbl_ticket = Label(window, text="   Ticket",)
lbl_ticket.grid(row=0 , column=0, padx=5, pady=5)

lbl_ticket_customer_id = Label(window, text="Customer ID :")
lbl_ticket_customer_id.grid(row=1, column=0, padx=5, pady=5)

entry_ticket_customer_id = Entry(window)
entry_ticket_customer_id.grid(row=1, column=1, padx=5, pady=5)

lbl_ticket_trip_id = Label(window, text="Trip ID :")
lbl_ticket_trip_id.grid(row=2, column=0, padx=5, pady=5)

entry_ticket_trip_id = Entry(window)
entry_ticket_trip_id.grid(row=2, column=1, padx=5, pady=5)

lbl_ticket_class_id = Label(window, text="Class ID :")
lbl_ticket_class_id.grid(row=3, column=0, padx=5, pady=5)

entry_ticket_class_id = Entry(window)
entry_ticket_class_id.grid(row=3, column=1, padx=5, pady=5)

lbl_ticket_passenger_name = Label(window, text="Passenger Name :")
lbl_ticket_passenger_name.grid(row=4, column=0, padx=5, pady=5)

entry_ticket_passenger_name = Entry(window)
entry_ticket_passenger_name.grid(row=4, column=1, padx=5, pady=5)

lbl_ticket_passenger_age = Label(window, text="Passenger Age :")
lbl_ticket_passenger_age.grid(row=5, column=0, padx=5, pady=5)

entry_ticket_passenger_age = Entry(window)
entry_ticket_passenger_age.grid(row=5, column=1, padx=5, pady=5)


   #  Add tiket button

btn_ticket_add = Button(window, text="Add Ticket", command=lambda: self.Addticket())
btn_ticket_add.grid(row=7, column=0, padx=5, pady=5)


def add_ticket(self):
    self.Cus.add_ticket(
        lbl_ticket.get(), lbl_ticket_customer_id.get(), lbl_ticket_trip_id.get(),
        lbl_ticket_class_id.get(), lbl_ticket_passenger_name.get(),lbl_ticket_passenger_age.get()
    )

   # delete ticket button

btn_ticket_delete = Button(window, text="Delete Ticket", command=lambda: delete_ticket())
btn_ticket_delete.grid(row=7, column=1, padx=5, pady=5)

def delete_ticket():

    customer_id = customer_id_entry.get()
    cursor.execute("DELETE FROM tickets WHERE customer_id = ?", (customer_id,))
    conn.commit()

  # total  pricec button

calculate_price_button = Button(window, text="Total Price", command= lambda :self.calculatePrice())
calculate_price_button.grid(row=8, column=0, padx=5, pady=5)

    # class price button

class_price_button = Button(window, text="class price", command= lambda :self.classPrice())
class_price_button.grid(row=8, column=1, padx=5, pady=5)

    #trip Price button

trip_prie_button = Button(window, text="class price", command= lambda :self.tripPrice())
trip_prie_button.grid(row=9, column=0, padx=5, pady=5)






def DeleteTicket(self):
    self.Customer.DeleteTi(
        self.trip_id.get(), self.trip_src.get(), self.trip_dest.get(), self.trip_departs.get(), self.trip_arrives.get(),
        self.trip_price.get(),
    )




window.mainloop()

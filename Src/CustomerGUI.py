import sqlite3
from tkinter import simpledialog, messagebox
from tkinter import*
from tkinter import ttk
import tkinter as tk
from Customer import Customer
from Ticket import Ticket

class CustomerMain:
    def __init__(self):
        self.customer = CustomerGUI()
        self.b=tk.Tk()
        self.b.geometry('1000x600+280+100')
        self.b.configure(bg="black")
        self.style = ttk.Style()
        self.style.theme_use('default')
    def Sign(self):
        a = self.b
        L1=Label(a,text="Sign Up - Sign In",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        Button1=Button(text='SignUp',fg='white',bg='red',font=('Liberation Sans bold',15), command=lambda:self.customer.signUp(a),cursor='hand2').place(relx=0.3, rely=0.55,anchor=tk.CENTER,width=250,height=70)
        Button1=Button(text='SignIn',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:self.customer.signIn(a),cursor='hand2').place(relx=0.7, rely=0.55,anchor=tk.CENTER,width=250,height=70)
        a.mainloop()
        return True
    
        

    
class CustomerGUI:
    def __init__(self, ):
        self.data = Customer()

    def signUp(self,root):
        root.destroy()

        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        L1=Label(root,text="Sign Up",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L2=Label(root,text="UserName",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.3,anchor=tk.CENTER)
        username=StringVar()
        text=Entry(root,textvariable=username,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.3,anchor=tk.CENTER,height=40,width=550)
        L3=Label(root,text="BirthDate",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        birthdate=StringVar()        
        text=Entry(root,textvariable=birthdate,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L4=Label(root,text="PhoneNum",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.5,anchor=tk.CENTER)
        phonenum=StringVar()        
        text=Entry(root,textvariable=phonenum,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.5,anchor=tk.CENTER,height=40,width=550)
        L5=Label(root,text="Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.6,anchor=tk.CENTER)
        email=StringVar()        
        text=Entry(root,textvariable=email,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.6,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text="Password",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.7,anchor=tk.CENTER)
        password=StringVar()   
        text=Entry(root,textvariable=password,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.7,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Submit',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.data.Sign_up(username.get(),birthdate.get(),phonenum.get(),email.get(),password.get()), cursor='hand2').place(relx=0.5, rely=0.85,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()
        
        
    def functions(self):
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        a = root
        L1=Label(a,text="Main Menu",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        Button1=Button(text='Book Trip',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:self.Book_trip(),cursor='hand2').place(relx=0.5, rely=0.4,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Cancel Trip',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:self.Cancel_trip(),cursor='hand2').place(relx=0.7, rely=0.4,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Name',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:self.update_name(a),cursor='hand2').place(relx=0.3, rely=0.4,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Password',fg='white',bg='red',font=('Liberation Sans bold',13),command=lambda:self.update_password(a),cursor='hand2').place(relx=0.5, rely=0.6,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Email',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:self.update_email(a),cursor='hand2').place(relx=0.7, rely=0.6,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Phone',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:self.update_phoneNum(a),cursor='hand2').place(relx=0.3, rely=0.6,anchor=tk.CENTER,width=150,height=50)
        a.mainloop()

    def signIn(self,root):
        root.destroy()
        
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        result_variable=StringVar()   
        L1=Label(root,text="Sign IN",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L5=Label(root,text="Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        Email=StringVar()        
        text=Entry(root,textvariable=Email,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text="Password",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.5,anchor=tk.CENTER)
        Password=StringVar()
        text=Entry(root,textvariable=Password,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.5,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Login',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.handle_login(Email.get(),Password.get(),root),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()

    def handle_login(self,Email,Password,root):
        result_variable=StringVar() 
        result_variable.set(self.data.Sign_in(Email, Password))
        check = int(result_variable.get())
        if check==1:
            root.destroy()
            self.functions()
    
    def update_name(self,root):
        root.destroy()
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        L1=Label(root,text="Update Name",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L6=Label(root,text="Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        Email=StringVar()
        text=Entry(root,textvariable=Email,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text=" New Name",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.53,anchor=tk.CENTER)
        Name=StringVar()
        text=Entry(root,textvariable=Name,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.53,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Update Name',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.data.Upadte_Name(Email.get(),Name.get()),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()    
        
    def update_password(self,root):
        root.destroy()
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        L1=Label(root,text="Update Password",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L6=Label(root,text="Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        Email=StringVar()
        text=Entry(root,textvariable=Email,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text=" New Passowrd",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.53,anchor=tk.CENTER)
        Passowrd=StringVar()
        text=Entry(root,textvariable=Passowrd,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.53,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Update Password',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.data.update_password(Email.get(),Passowrd.get()),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()    
    
    def update_phoneNum(self,root):
        root.destroy()
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        L1=Label(root,text="Update Phone",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L6=Label(root,text="Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        Email=StringVar()
        text=Entry(root,textvariable=Email,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text=" New Phone",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.53,anchor=tk.CENTER)
        Phone=StringVar()
        text=Entry(root,textvariable=Phone,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.53,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Update Phone',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.data.update_phoneNum(Email.get(),Phone.get()),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()       

    def update_email(self,root):
        root.destroy()
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        L1=Label(root,text="Update Email",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L6=Label(root,text="Old Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        Email=StringVar()
        text=Entry(root,textvariable=Email,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text=" New Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.53,anchor=tk.CENTER)
        NEmail=StringVar()
        text=Entry(root,textvariable=NEmail,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.53,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Update Email',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.data.update_email(Email.get(),NEmail.get()),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()
        
    
    def Book_trip(self):
        BookTrip(customerId= self.data.customerId)

    def Cancel_trip(self):
        CancelTrip(customerId= self.data.customerId)

class BookTrip:
    def __init__(self, customerId):
        self.customerId = customerId        
        self.root = tk.Tk()
        self.root.title("Book Trips")
        self.passengers = []  
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'SELECT src, dest, departs, arrives, price, trainId, tripId FROM Trip')
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

            update_trip_btn = tk.Button(self.root, text="Book Trip", command=lambda: self.bookTrip(row[5], row[6]))
            update_trip_btn.pack()

        self.root.mainloop()
    
    def bookTrip(self, trainId, tripId ):
        ticket = Ticket(customerId = self.customerId)
        bookSeats = simpledialog.askinteger("book Seats", f"enter Seats:\n", minvalue=1)
        if bookSeats == None:
            return

        for i in range(0, bookSeats):
            name = simpledialog.askstring("Passenger name", f"Enter Passenger Name:\n",)
            age = simpledialog.askinteger("Passenger Age", f"enter Passenger Age for Passenger {name}:\n")
            passenger = [name, age]
            self.passengers.append(passenger)
        
        selected_class = self.select_class(trainId)
        while selected_class == -1:
              selected_class = self.select_class(trainId)

        if selected_class == None:
            return
        
        ticket.bookedSeats = bookSeats
        ticket.passengers = self.passengers
        ticket.classId = selected_class
        ticket.tripId = tripId
        price_label = tk.Label(self.root, text=f"Total Price: $ {ticket.calculatePrice()}")
        price_label.pack()
        customer = Customer(customerId= self.customerId) 
        book_Trip_btn = tk.Button(self.root, text="Confirm", command=lambda: ticket.addTicket(customer.Booktrip(tripId= tripId)))
        book_Trip_btn.pack()


    def select_class(self, trainId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f'SELECT Class.classId, Class.className FROM Class, TrainClass WHERE TrainClass.classId = Class.classId AND TrainClass.trainId = {trainId}')
        classes = cursor.fetchall()
        class_names = [f"{row[0]} - {row[1]}" for row in classes]
        prompt = "\n".join(class_names)
        selected_index = simpledialog.askinteger("Select Class", f"Select a Class:\n{prompt}", minvalue=1)
        
        if selected_index == None:
            return None
        
        for ids in classes:
            if selected_index == int(ids[0]):
                return selected_index
                
                
        messagebox.showerror("Error", "Your selected index does not exist")
        return -1
        
    
class CancelTrip:
    def __init__(self, customerId):
        self.customer = Customer(customerId= customerId)

        self.root = tk.Tk()
        self.root.title("Cancel booking")
        Trip = self.customer.View_trip()
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        if Trip[0] is not None:
            cursor.execute(f'SELECT src, dest, departs, arrives, price, trainId, tripId FROM Trip WHere tripId = {Trip[0]}')
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
                ticket = Ticket()
                update_trip_btn = tk.Button(self.root, text="Cancel Trip", command=lambda: ticket.deleteTicket(customerId, row[6], self.customer.Cancel_trip(row[6])))
                update_trip_btn.pack()
        else:
            messagebox.showerror("Error", "You didn't book any trip")

        self.root.mainloop()


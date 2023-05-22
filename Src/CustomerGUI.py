import sqlite3
import datetime
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
import tkinter as tk
from Customer import CustomerData
class Main:
    def main_fuc():
        a=tk.Tk()
        a.geometry('1000x600+280+100')
        a.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        customer = Customer()
        L1=Label(a,text="Main menu",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        Button1=Button(text='SignUp',fg='white',bg='red',font=('Liberation Sans bold',15), command=lambda:customer.signUp(a),cursor='hand2').place(relx=0.18, rely=0.4,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='SignIn',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:customer.signIn(a),cursor='hand2').place(relx=0.38, rely=0.4,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Book Trip',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:customer.Book_trip(a),cursor='hand2').place(relx=0.58, rely=0.4,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Cancel Trip',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:customer.Cancel_trip(a),cursor='hand2').place(relx=0.78, rely=0.4,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Name',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:customer.update_name(a),cursor='hand2').place(relx=0.18, rely=0.6,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Password',fg='white',bg='red',font=('Liberation Sans bold',13),command=lambda:customer.update_password(a),cursor='hand2').place(relx=0.38, rely=0.6,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Email',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:customer.update_email(a),cursor='hand2').place(relx=0.58, rely=0.6,anchor=tk.CENTER,width=150,height=50)
        Button1=Button(text='Update Phone',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:customer.update_phoneNum(a),cursor='hand2').place(relx=0.78, rely=0.6,anchor=tk.CENTER,width=150,height=50)
        a.mainloop()
        return True
        
class Customer:
    def __init__(self, customerId=None):
        self.name = ""
        self.DOB  = None
        self.email = ""
        self.password = ""
        self.phone = ""
        self.data = CustomerData()

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
        


    def signIn(self,root):
        root.destroy()
        
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        L1=Label(root,text="Sign IN",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L5=Label(root,text="Email",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        Email=StringVar()        
        text=Entry(root,textvariable=Email,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text="Password",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.5,anchor=tk.CENTER)
        Password=StringVar()
        text=Entry(root,textvariable=Password,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.5,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Login',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.data.Sign_in(Email.get(),Password.get()),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()

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
        
    
    def Book_trip(self,root):
        root.destroy()
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f''' SELECT src,dist,departs,arrives,price FROM Trip''')
        trip = cursor.fetchall()
        label_list = []            
        for row in trip:
            label_list.append(row)
        
        a = tk.Tk()
        t="Source-Destination-Departs-Arrives-Price"
        label = tk.Label(a, text=t)
        label.pack()
        for string in enumerate(label_list):
            label = tk.Label(a, text=string)
            label.pack()
        L1=Label(root,text="Book Trip",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L5=Label(root,text="Source",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.4,anchor=tk.CENTER)
        Src=StringVar()        
        text=Entry(root,textvariable=Src,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.4,anchor=tk.CENTER,height=40,width=550)
        L6=Label(root,text="Destination",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.5,anchor=tk.CENTER)
        Dest=StringVar()
        text=Entry(root,textvariable=Dest,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.5,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Book Trip',fg='white',bg='red',font=('Liberation Sans bold',20),command=lambda:self.data.Booktrip(Src.get(),Dest.get()),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()

    def Cancel_trip(self,root):
        root.destroy()
        root=tk.Tk()
        root.geometry('1000x600+280+100')
        root.configure(bg="black")
        style = ttk.Style()
        style.theme_use('default')
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f''' SELECT t1.tripId,t2.src,t2.dist FROM TripCustomer AS t1 JOIN Trip AS t2 ON t1.tripId = t2.tripId ''')
        trip = cursor.fetchall()
        label_list = []
        for row in trip:
            label_list.append(row)
        
        a = tk.Tk()
        t="TripId-Src-Dest"
        label = tk.Label(a, text=t)
        label.pack()
        for string in enumerate(label_list):
            label = tk.Label(a, text=string)
            label.pack()
        L1=Label(root,text="Cancel Trip",fg='white',font=('Hey Comic',50), background="black").place(relx=0.5, rely=0.1,anchor=tk.CENTER)
        L6=Label(root,text="Tripid",fg='white',font=('Liberation Sans bold',20), background="black").place(relx=0.1, rely=0.5,anchor=tk.CENTER)
        Tripid=StringVar()
        text=Entry(root,textvariable=Tripid,font=('Liberation Sans', 12, 'bold')).place(relx=0.5, rely=0.5,anchor=tk.CENTER,height=40,width=550)
        Button1=Button(root,text='Cancel Trip',fg='white',bg='red',font=('Liberation Sans bold',20),command = lambda:self.data.Booktrip(Tripid.get()),cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()
    def customerAge(self):
        today = datetime.date.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age




isSigned = Main.main_fuc()
    

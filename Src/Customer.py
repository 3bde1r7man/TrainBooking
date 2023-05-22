import sqlite3
import datetime
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
import tkinter as tk

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
        Button1=Button(text='Update Password',fg='white',bg='red',font=('Liberation Sans bold',15),command=lambda:customer.update_password(a),cursor='hand2').place(relx=0.38, rely=0.6,anchor=tk.CENTER,width=150,height=50)
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

    def signUp(self,root):
        root.destroy()
        def data():

            self.name = username.get()
            self.DOB = birthdate.get()
            self.phone = phonenum.get()
            self.email = email.get()
            self.password = password.get()

            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()

            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                cursor.execute(f''' INSERT into Customer (name, DOB, email, password) values ("{self.name}", "{self.DOB}", "{self.email}", "{self.password}") ''')
                conn.commit()
                cursor.execute(f''' SELECT custmerId FROM Customer WHERE email = "{self.email}" ''')
                customerId = cursor.fetchone()
                if customerId == None:
                    messagebox.showerror("Error", "email is not exist")
                else:
                    messagebox.showinfo("success", "Account created successfully")
                    cursor.execute(f'''INSERT INTO Customer_PhoneNum (custmerId, phoneNum) values ("{customerId[0]}","{self.phone}") ''')
                    conn.commit()
                    return True
            else:
                messagebox.showerror("Error", "An account with this email already exists.")

            conn.close()
            return False
            
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
        Button1=Button(root,text='Submit',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.85,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()
        





    def signIn(self,root):
        root.destroy()
        def data():
            
            email = Email.get()
            password = Password.get()
            
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            
            cursor.execute(f''' SELECT password FROM Customer WHERE email = "{email}" ''')
            result = cursor.fetchone()
            if result == None:
                messagebox.showerror("Error", "email is not correct or you did not register")
            else:
                if result[0] == password:
                    print("Login successful\n")
                    cursor.execute(f''' SELECT name, DOB, email, password FROM Customer WHERE email = "{email}" ''')
                    result2 = cursor.fetchone()
                    self.name = result2[0]
                    self.DOB = result2[1]
                    self.email = result2[2]
                    self.password = result2[3]
                    messagebox.showinfo("Success", f"Welcome {self.name}")
                    return True
                else:
                    messagebox.showerror("Error", "password is wrong")

            conn.close()
            return False
        
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
        Button1=Button(root,text='Login',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()

    def update_name(self,root):
        root.destroy()
        def data():
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =Email.get()
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showerror("Error","Name updated successfully")
                conn.close()
                return False
            else:
                self.name =Name.get()
                cursor.execute(f''' UPDATE Customer SET name="{self.name}" WHERE email = "{self.email}" ''')
                messagebox.showinfo("Success","Name updated successfully")
                conn.commit()
                conn.close()
                return True
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
        Button1=Button(root,text='Update Name',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()    
        
    def update_password(self,root):
        root.destroy()
        def data():
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =Email.get()
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showerror("Error","Email not found please sign up first")
                conn.close()
                return False
            else:
                self.password =Passowrd.get()
                cursor.execute(f''' UPDATE Customer SET password ="{self.password}" WHERE email = "{self.email}" ''')
                messagebox.showinfo("Success","Password updated successfully")
                conn.commit()
                conn.close()
                return True
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
        Button1=Button(root,text='Update Password',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()    
    
    def update_phoneNum(self,root):
        root.destroy()
        def data():
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =Email.get()
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showinfo("Error","Email not found please sign up first")
                conn.close()
                return False
            else:
                self.phone =Phone.get()
                cursor.execute(f''' SELECT custmerID FROM Customer WHERE email = "{self.email}" ''')
                customerid = cursor.fetchone()
                cursor.execute(f''' UPDATE Customer_phoneNum SET phoneNum ="{self.phone}" WHERE custmerId = "{customerid[0]}" ''')
                messagebox.showinfo("Success","Phone updated successfully")
                conn.commit()
                conn.close()
                return True
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
        Button1=Button(root,text='Update Phone',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()       

    def update_email(self,root):
        root.destroy()
        def data():
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =input("please enter your email: ")
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showerror("Erroe","Email not found please sign up first")
                conn.close()
                return False
            else:
                old_email = self.email
                self.email =NEmail.get()
                cursor.execute(f''' UPDATE Customer SET email ="{self.email}" WHERE email = "{old_email}" ''')
                messagebox.showinfo("Success","Email updated successfully")
                conn.commit()
                conn.close()
                return True
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
        Button1=Button(root,text='Update Email',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()         
        
    
    def Book_trip(self,root):
        root.destroy()
        def data():
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            src = Src.get()
            dist = Dest.get()
            cursor.execute(f''' SELECT t1.tripId FROM Trip AS t1 JOIN TripCustomer AS t2 ON t1.tripId = t2.tripId WHERE t1.src = "{src}" AND t1.dist = "{dist}" ''')
            Tid = cursor.fetchone()
            if Tid != None:
                messagebox.showerror("Error", "this trip already booked")
                return False
            cursor.execute(f''' SELECT tripId FROM Trip where src = "{src}" and dest = "{dist}"''')
            tripid = cursor.fetchone()
            if tripid == None:
                print("this trip is not exist\n")
                return False
            cursor.execute(f''' SELECT MAX(custmerId) FROM TripCustomer''')
            customerid = cursor.fetchone()
            if customerid[0] == None:
                cursor.execute(f'''INSERT INTO TripCustomer (tripId,custmerId) values ("{tripid[0]}","{1}") ''')
            else:
                Cid = int(customerid[0]) + 1
                cursor.execute(f'''INSERT INTO TripCustomer (tripId,custmerId) values ("{tripid[0]}","{Cid}") ''')
            messagebox.showinfo("success", "trip booked successfully")
            conn.commit()
            conn.close()
            return True
        
        
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
        Button1=Button(root,text='Book Trip',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()

    def Cancel_trip(self,root):
        root.destroy()
        def data():
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            tripid =Tripid.get()
            cursor.execute(f''' select tripId FROM TripCustomer WHERE tripId = "{tripid}" ''')
            if cursor.fetchone() == None:
                messagebox.showerror("Error", "this trip is not exist")
                return False
            cursor.execute(f''' DELETE FROM TripCustomer WHERE tripId = "{tripid}" ''')
            messagebox.showinfo("Success", "trip canceled successfully")
            conn.commit()
            conn.close()
            return True
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
        Button1=Button(root,text='Cancel Trip',fg='white',bg='red',font=('Liberation Sans bold',20),command = data,cursor='hand2').place(relx=0.5, rely=0.7,anchor=tk.CENTER,width=250,height=60)
        root.mainloop()
    def customerAge(self):
        today = datetime.date.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age




isSigned = Main.main_fuc()
    

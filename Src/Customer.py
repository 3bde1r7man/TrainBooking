import sqlite3
import datetime
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
import tkinter as tk
class CustomerData:
    def __init__(self, customerId=None):
        self.name = ""
        self.DOB  = None
        self.email = ""
        self.password = ""
        self.phone = ""
    
    def Sign_up(self,username,birthdate,phonenum,email,password):

        self.name = username
        self.DOB = birthdate
        self.phone = phonenum
        self.email = email
        self.password = password

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
    
    def Sign_in(self,Email,Password):
            
            email = Email
            password = Password
            
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            
            cursor.execute(f''' SELECT password FROM Customer WHERE email = "{email}" ''')
            result = cursor.fetchone()
            if result == None:
                messagebox.showerror("Error", "email is not correct or you did not register")
            else:
                if result[0] == password:
                    cursor.execute(f''' SELECT name, DOB, email, password FROM Customer WHERE email = "{email}" ''')
                    result2 = cursor.fetchone()
                    self.name = result2[0]
                    self.DOB = result2[1]
                    self.email = result2[2]
                    self.password = result2[3]
                    messagebox.showinfo("Success", f"Login successful, Welcome {self.name}")
                    return True
                else:
                    messagebox.showerror("Error", "password is wrong")

            conn.close()
            return False
    def Upadte_Name(self,Email,Name):
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =Email
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showerror("Error","Name updated successfully")
                conn.close()
                return False
            else:
                self.name =Name
                cursor.execute(f''' UPDATE Customer SET name="{self.name}" WHERE email = "{self.email}" ''')
                messagebox.showinfo("Success","Name updated successfully")
                conn.commit()
                conn.close()
                return True
    def update_password(self,Email,Password):
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =Email
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showerror("Error","Email not found please sign up first")
                conn.close()
                return False
            else:
                self.password =Password
                cursor.execute(f''' UPDATE Customer SET password ="{self.password}" WHERE email = "{self.email}" ''')
                messagebox.showinfo("Success","Password updated successfully")
                conn.commit()
                conn.close()
                return True
    def update_phoneNum(self,Email,Phone):
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =Email
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showinfo("Error","Email not found please sign up first")
                conn.close()
                return False
            else:
                self.phone =Phone
                cursor.execute(f''' SELECT custmerID FROM Customer WHERE email = "{self.email}" ''')
                customerid = cursor.fetchone()
                cursor.execute(f''' UPDATE Customer_phoneNum SET phoneNum ="{self.phone}" WHERE custmerId = "{customerid[0]}" ''')
                messagebox.showinfo("Success","Phone updated successfully")
                conn.commit()
                conn.close()
                return True  
    def update_email(self,Email,NEmail):
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            self.email =Email
            cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
            if cursor.fetchone() == None:
                messagebox.showerror("Erroe","Email not found please sign up first")
                conn.close()
                return False
            else:
                old_email = self.email
                self.email =NEmail
                cursor.execute(f''' UPDATE Customer SET email ="{self.email}" WHERE email = "{old_email}" ''')
                messagebox.showinfo("Success","Email updated successfully")
                conn.commit()
                conn.close()
                return True
    def Booktrip(self,Src,Dest):
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            src = Src
            dist = Dest
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
    def Cancel_trip(self,Tripid):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        tripid =Tripid
        cursor.execute(f''' select tripId FROM TripCustomer WHERE tripId = "{tripid}" ''')
        if cursor.fetchone() == None:
            messagebox.showerror("Error", "this trip is not exist")
            return False
        cursor.execute(f''' DELETE FROM TripCustomer WHERE tripId = "{tripid}" ''')
        messagebox.showinfo("Success", "trip canceled successfully")
        conn.commit()
        conn.close()
        return True                 
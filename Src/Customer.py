import sqlite3
import datetime
from tkinter import messagebox

class Customer:
    def __init__(self, customerId=None):
        self.customerId = customerId
        self.name = None
        self.DOB = None
        self.email = None
        self.password = None
        self.phone = None
        if customerId is not None:
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            cursor.execute(f"SELECT name, password, DOB, email FROM Customer WHERE customerId = {customerId}")
            data = cursor.fetchone()
            self.name = data[0]
            self.password = data[1]
            self.DOB = datetime.datetime.strptime(data[2], "%d-%m-%Y")
            self.email = data[3]

            cursor.execute(f"SELECT phoneNum FROM Customer_phoneNum WHERE customerId = {customerId}")
            data = cursor.fetchall()
            self.phone = []
            for row in data:
                self.phone.append(row[0])
    
    def Sign_up(self, username, birthdate, phonenum, email, password):

        self.name = username
        self.DOB = datetime.datetime.strptime(birthdate, "%d-%m-%y")
        self.phone = phonenum
        self.email = email
        self.password = password

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            cursor.execute(f''' INSERT into Customer (name, DOB, email, password) values ("{self.name}", "{self.DOB}", "{self.email}", "{self.password}") ''')
            conn.commit()
            cursor.execute(f''' SELECT customerId FROM Customer WHERE email = "{self.email}" ''')
            self.customerId = cursor.fetchone()[0]
            if self.customerId == None:
                messagebox.showerror("Error", "email is not exist")
            else:
                messagebox.showinfo("success", "Account created successfully")
                cursor.execute(f'''INSERT INTO Customer_PhoneNum (customerId, phoneNum) values ("{self.customerId[0]}","{self.phone}") ''')
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
                    cursor.execute(f''' SELECT name, DOB, email, password, customerId FROM Customer WHERE email = "{email}" ''')
                    result2 = cursor.fetchone()
                    self.name = result2[0]
                    self.DOB = result2[1]
                    self.email = result2[2]
                    self.password = result2[3]
                    self.customerId = result2[4]
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
                cursor.execute(f''' SELECT customerID FROM Customer WHERE email = "{self.email}" ''')
                customerid = cursor.fetchone()
                cursor.execute(f''' UPDATE Customer_phoneNum SET phoneNum ="{self.phone}" WHERE customerId = "{customerid[0]}" ''')
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
    def Booktrip(self, tripId):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f''' SELECT customerId FROM TripCustomer WHERE tripId = {tripId} AND customerId = {self.customerId} ''')
        if cursor.fetchone() == None:
            cursor.execute(f''' INSERT INTO TripCustomer (customerId, tripId) VALUES(?, ?)''' , (self.customerId, tripId))
            conn.commit()
            messagebox.showinfo("Success","Booked successfully")
            return True
        else:
            messagebox.showinfo("ERROR","You aleardy booked this Trip")
            return False

    def Cancel_trip(self, Tripid):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        tripid =Tripid
        cursor.execute(f''' SELECT tripId FROM TripCustomer WHERE tripId = ? AND  customerId = ? ''', (tripid, self.customerId))
        if cursor.fetchone() == None:
            messagebox.showerror("Error", "this trip is not exist")
            return False
        cursor.execute(f'''DELETE FROM TripCustomer WHERE tripId = ? AND customerId = ?''', (tripid, self.customerId))
        conn.commit()
        messagebox.showinfo("Success", "Trip canceled successfully")
        conn.close()
        return True

    def View_trip(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f''' SELECT MAX(tripId) FROM TripCustomer WHERE customerId = "{self.customerId}" ''')   
        row = cursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "You have not booked any trip")
        else:
            return row


    def customerAge(self):
        today = datetime.date.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age
import sqlite3
import datetime
from tkinter import messagebox

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
class Customer:
    def __init__(self, customerId=None):
        self.customerId = customerId
        self.name = None
        self.DOB = None
        self.email = None
        self.password = None
        self.phone = None
        if customerId is not None:
            cursor.execute(f"SELECT name, password, DOB, email FROM Customer WHERE customerId = {customerId}")
            data = cursor.fetchone()
            self.name = data[0]
            self.password = data[1]
            self.DOB = data[2]
            self.email = data[3]

            cursor.execute(f"SELECT phoneNum FROM Customer_phoneNum WHERE customerId = {customerId}")
            data = cursor.fetchall()
            self.phone = []
            for row in data:
                self.phone.append(row[0])

    def signUp(self):
        if self.email and self.password and self.name and self.DOB and self.phone:
            cursor.execute(f'SELECT email FROM Customer WHERE email = "{self.email}"')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO Customer (name, DOB, email, password) VALUES (?, ?, ?, ?)',
                               (self.name, self.DOB, self.email, self.password))
                conn.commit()
                cursor.execute(f'SELECT customerId FROM Customer WHERE email = "{self.email}"')
                customerId = cursor.fetchone()
                if customerId is None:
                    messagebox.showerror("Error", "Error creating account")
                else:
                    cursor.execute(f'INSERT INTO Customer_PhoneNum (customerId, phoneNum) VALUES (?, ?)',
                                   (customerId[0], self.phone[0]))
                    conn.commit()
                    messagebox.showinfo("Success", "Account created successfully")
                    return True
            else:
                messagebox.showerror("Error", "An account with this email already exists.")
        else:
            messagebox.showerror("Error", "Please fill in all the required fields.")
        return False

    def signIn(self):
        if self.email and self.password:
            cursor.execute(f'SELECT password FROM Customer WHERE email = "{self.email}"')
            if cursor.fetchone() is not None:
                cursor.execute(f'SELECT name, DOB, email, password FROM Customer WHERE email = "{self.email}"')
                data = cursor.fetchone()
                if data[3] == self.password:
                    self.name = data[0]
                    self.DOB = data[1]
                    self.email = data[2]
                    self.password = data[3]
                    messagebox.showinfo("Success", "Login successful")
                    messagebox.showinfo("Welcome", f"Welcome {self.name}")
                    return True
                else:
                    messagebox.showerror("Error", "Incorrect password")
            else:
                messagebox.showerror("Error", "Account does not exist")
        else:
            messagebox.showerror("Error", "Please enter your email and password")
        return False

    def customerAge(self):
        today = datetime.date.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age
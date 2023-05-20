import sqlite3
import datetime
class Customer():
    
    def __init__(self):
        self.name = ""
        self.DOB  = None
        self.email = ""
        self.password = ""
        self.phone = ""
    
    def signUp(self):
        
        self.name = input("Enter your name: ")
        dob_input = input("Enter your Date Of Birth (Y-M-D): ")
        self.DOB = datetime.datetime.strptime(dob_input, "%Y-%m-%d")
        self.phone = input("Enter your phone number: ")
        self.email = input("Enter your email address: ")
        self.password = input("Enter your password: ")

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            cursor.execute(f''' INSERT into Customer (name, DOB, email, password) values ("{self.name}", "{self.DOB}", "{self.email}", "{self.password}") ''')
            conn.commit()
            cursor.execute(f''' SELECT custmerId FROM Customer WHERE email = "{self.email}" ''')
            customerId = cursor.fetchone()
            if customerId == None:
                print("Error\n")
            else:
                print("Account created successfully\n")
                cursor.execute(f'''INSERT INTO Customer_PhoneNum (custmerId, phoneNum) values ("{customerId[0]}","{self.phone}") ''')
                conn.commit()
                return True
        else:
            print("An account with this email already exists.\n")

        conn.close()
        return False



    def signIn(self):
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        cursor.execute(f''' SELECT password FROM Customer WHERE email = "{email}" ''')
        if cursor.fetchone() == None:
            print("Error\n")
        else:
            if cursor.fetchone()[0] == password:
                print("Login successful\n")
                cursor.execute(f''' SELECT name, DOB, email, password FROM Customer WHERE email = "{email}" ''')
                self.name = cursor.fetchone()[0]
                self.DOB = cursor.fetchone()[1]
                self.email = cursor.fetchone()[2]
                self.password = cursor.fetchone()[3]
                print(f"Welcome {self.name}\n")
                return True
            else:
                print("Error\n")

        conn.close()
        return False
    
    
    def update_name(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        self.email =input("please enter your email: ")
        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            print("Email not found please sign up first\n")
            conn.close()
            return False
        else:
            self.name =input("please enter your new name: ")
            cursor.execute(f''' UPDATE Customer SET name="{self.name}" WHERE email = "{self.email}" ''')
            print("Name updated successfully\n")
            conn.commit()
            conn.close()
            return True
    
    def update_password(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        self.email =input("please enter your email: ")
        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            print("Email not found please sign up first\n")
            conn.close()
            return False
        else:
            self.password =input("please enter your new password: ")
            cursor.execute(f''' UPDATE Customer SET password ="{self.password}" WHERE email = "{self.email}" ''')
            print("Password updated successfully\n")
            conn.commit()
            conn.close()
            return True
    
    def update_phoneNum(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        self.email =input("please enter your email: ")
        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            print("Email not found please sign up first\n")
            conn.close()
            return False
        else:
            self.phone =str(input("please enter your new phone number : "))
            cursor.execute(f''' SELECT custmerID FROM Customer WHERE email = "{self.email}" ''')
            customerid = cursor.fetchone()
            cursor.execute(f''' UPDATE Customer_phoneNum SET phoneNum ="{self.phone}" WHERE custmerId = "{customerid[0]}" ''')
            print("phone number updated successfully\n")
            conn.commit()
            conn.close()
            return True         

    def update_email(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        self.email =input("please enter your email: ")
        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            print("Email not found please sign up first\n")
            conn.close()
            return False
        else:
            old_email = self.email
            self.email =input("please enter your new email: ")
            cursor.execute(f''' UPDATE Customer SET email ="{self.email}" WHERE email = "{old_email}" ''')
            print("email updated successfully\n")
            conn.commit()
            conn.close()
            return True
    
    def Book_trip(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f''' SELECT src,dist,departs,arrives,price FROM Trip''')
        trip = cursor.fetchall()
        for row in trip:
            print(row)
        src =input("please enter the source : ")
        dist =input("please enter the distenation : ")
        cursor.execute(f''' SELECT t1.tripId FROM Trip AS t1 JOIN TripCustomer AS t2 ON t1.tripId = t2.tripId WHERE t1.src = "{src}" AND t1.dist = "{dist}" ''')
        Tid = cursor.fetchone()
        if Tid != None:
            print("this trip already booked")
            return False
        cursor.execute(f''' SELECT tripId FROM Trip where src = "{src}" and dist = "{dist}"''')
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
        print("trip booked successfully\n")
        conn.commit()
        conn.close()
        return True

    def Cancel_trip(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(f''' SELECT t1.tripId,t2.src,t2.dist FROM TripCustomer AS t1 JOIN Trip AS t2 ON t1.tripId = t2.tripId ''')
        trip = cursor.fetchall()
        for row in trip:
            print(row)
        tripid =input("please enter the tripid to cancel : ")
        cursor.execute(f''' select tripId FROM TripCustomer WHERE tripId = "{tripid}" ''')
        if cursor.fetchone() == None:
            print("this trip is not exist\n")
            return False
        cursor.execute(f''' DELETE FROM TripCustomer WHERE tripId = "{tripid}" ''')
        print("trip canceled successfully\n")
        conn.commit()
        conn.close()
        return True





customer = Customer()
isSigned = customer.Cancel_trip()

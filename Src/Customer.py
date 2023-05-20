import sqlite3
import datetime
class Customer():
    def __init__(self):
        self.name = ""
        self.DOB  = None
        self.email = ""
        self.password = ""
        self.phone = []
    
    def signUp(self,name,dob,email,password,phone):

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{email}" ''')
        if cursor.fetchone() == None:
            cursor.execute(f''' INSERT into Customer (name, DOB, email, password) values ("{name}", "{dob}", "{email}", "{password}") ''')
            conn.commit()
            cursor.execute(f''' SELECT customerId FROM Customer WHERE email = "{email}" ''')
            customerId = cursor.fetchone()
            if customerId == None:
                print("Error\n")
            else:
                print("Account created successfully\n")
                cursor.execute(f'''INSERT INTO Customer_PhoneNum (customerId, phoneNum) values ("{customerId[0]}","{phone}") ''')
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
    

    
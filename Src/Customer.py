import sqlite3
import datetime
class Customer():
    def __init__(self, customerId= None):
        self.customerId = customerId
        self.name = None
        self.DOB  = None
        self.email = None
        self.password = None
        self.phone = None
        if customerId != None:
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            cursor.execute(f"SELECT name, password, DOB, email FROM Customer Where customerId = {customerId}")
            data = cursor.fetchone()
            self.name = data[0]
            self.password = data[1]
            self.DOB = data[2]
            self.email = data[3]

            cursor.execute(f"SELECT phoneNum FROM Customer_phoneNum Where customerId = {customerId}")
            data = cursor.fetchall()
            self.phone = []
            for row in data:
                self.phone.append(row[0])

    
    def signUp(self):

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            cursor.execute(f''' INSERT into Customer (name, DOB, email, password) values ("{self.name}", "{self.DOB}", "{self.email}", "{self.password}") ''')
            conn.commit()
            cursor.execute(f''' SELECT customerId FROM Customer WHERE email = "{self.email}" ''')
            customerId = cursor.fetchone()
            if customerId == None:
                print("Error\n")
            else:
                print("Account created successfully\n")
                cursor.execute(f'''INSERT INTO Customer_PhoneNum (customerId, phoneNum) values ("{customerId[0]}","{self.phone[0]}") ''')
                conn.commit()
                return True
        else:
            print("An account with this email already exists.\n")

        conn.close()
        return False



    def signIn(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        cursor.execute(f''' SELECT password FROM Customer WHERE email = "{self.email}" ''')
        if cursor.fetchone() == None:
            print("Error\n")
        else:
            if cursor.fetchone()[0] == self.password:
                print("Login successful\n")
                cursor.execute(f''' SELECT name, DOB, email, password FROM Customer WHERE email = "{self.email}" ''')
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
    
    def customerAge(self):
        today = datetime.date.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age
    
    

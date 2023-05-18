import sqlite3

class Customer():
    def __init__(self):
        self.name = ""
        self.DOB  = ""
        self.email = ""
        self.password = ""
    
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
    
    def signUp(self):
        name = input("Enter your name: ")
        DOB = input("Enter your Date Of Birth (D/M/Y): ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")

        # Convert DOB to SQLite date format (YYYY-MM-DD)
        dob_parts = DOB.split('/')
        dob_sqlite = f"{dob_parts[2]}-{dob_parts[1]}-{dob_parts[0]}"

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()

        cursor.execute(f''' SELECT email FROM Customer WHERE email = "{email}" ''')
        if cursor.fetchone() == None:
            cursor.execute(f''' INSERT into Customer (name, DOB, email, password) values ("{name}", "{DOB}", "{email}", "{password}") ''')
            conn.commit()
            cursor.execute(f''' SELECT customerId FROM Customer WHERE email = "{email}" ''')
            if cursor.fetchone() == None:
                print("Error\n")
            else:
                print("Account created successfully\n")
                cursor.execute(f'''INSERT INTO Customer_PhoneNum (cusmerIdm, phoneNum) values ("{cursor.fetchone()[0]}","{phone}") ''')
                conn.commit()
                return True
        else:
            print("An account with this email already exists.\n")

        conn.close()
        return False

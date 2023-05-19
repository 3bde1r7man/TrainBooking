import sqlite3
from . import Admin, Customer


# this is how u can use the sqlite database in python

# conn = sqlite3.connect('db.sqlite3')  
# cursor = conn.cursor()

# conn.commit()
# conn.close()

class main():
    isSigned = False
    
    def signUp():
        while True:
            signAs = input("1- To sign Up as admin\n2- To sign Up as customer")
            if signAs == 1:
                admin = Admin()
                isSigned = admin.signUp()
                if isSigned:
                    admin.
                break
            elif signAs == 2:
                customer = Customer()
                isSigned = Customer.signUp()
                break
            else:
                print("Invalid Input")
                continue
        

    def signIn():
        while True:
            signInAs = input("1- To sign In as admin\n2- To sign In as customer")
            if signInAs == 1:
                admin = Admin()
                isSigned = admin.signIn()
                break
            elif signInAs == 2:
                customer = Customer()
                isSigned = customer.signIn()
                break
            else:
                print("Invalid Input")
                continue
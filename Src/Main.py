import sqlite3
# from . import Admin, Customer


# this is how u can use the sqlite database in python

conn = sqlite3.connect('db.sqlite3')  
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Customer
(
    custmerId INTEGER PRIMARY KEY AUTOINCREMENT,
    password VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    DOB DATE NOT NULL,
    name VARCHAR(20) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE Admin
(
    adminId INTEGER PRIMARY KEY AUTOINCREMENT,
    password VARCHAR(20) NOT NULL,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL
);
''')

cursor.execute(''' 
CREATE TABLE Train
(
    trainId INTEGER PRIMARY KEY AUTOINCREMENT,
    adminId INT NOT NULL,
    details VARCHAR(20) NOT NULL,
    FOREIGN KEY (adminId) REFERENCES Admin(adminId)
);

''')

cursor.execute('''
CREATE TABLE Class
(
    classId INTEGER PRIMARY KEY AUTOINCREMENT,
    className VARCHAR(20) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE TrainClass
(
    nSeats INT NOT NULL,
    price FLOAT NOT NULL,
    trainId INT NOT NULL,
    classId INT NOT NULL,
    PRIMARY KEY (trainId, classId),
    FOREIGN KEY (trainId) REFERENCES Train(trainId),
    FOREIGN KEY (classId) REFERENCES Class(classId)
);

''')

cursor.execute('''

CREATE TABLE Customer_phoneNum
(
    phoneNum INT NOT NULL,
    custmerId INT NOT NULL,
    PRIMARY KEY (phoneNum, custmerId),
    FOREIGN KEY (custmerId) REFERENCES Customer(custmerId)
);

''')

cursor.execute('''

CREATE TABLE Trip
(
    src VARCHAR(20) NOT NULL,
    dist VARCHAR(20) NOT NULL,
    departs DATE NOT NULL,
    arrives DATE NOT NULL,
    tripId INTEGER PRIMARY KEY AUTOINCREMENT,
    adminId INT NOT NULL,
    trainId INT NOT NULL,
    FOREIGN KEY (adminId) REFERENCES Admin(adminId),
    FOREIGN KEY (trainId) REFERENCES Train(trainId)
);
''')


cursor.execute('''

CREATE TABLE TripCustomer
(
    custmerId INT NOT NULL,
    tripId INT NOT NULL,
    PRIMARY KEY (custmerId, tripId),
    FOREIGN KEY (custmerId) REFERENCES Customer(custmerId),
    FOREIGN KEY (tripId) REFERENCES Trip(tripId)
);
''')

cursor.execute('''
CREATE TABLE Ticket
(
    ticketId INTEGER PRIMARY KEY AUTOINCREMENT,
    bookedSeats INT NOT NULL,
    custmerId INT NOT NULL,
    tripId INT NOT NULL,
    classId INT NOT NULL,
    FOREIGN KEY (custmerId) REFERENCES Customer(custmerId),
    FOREIGN KEY (tripId) REFERENCES Trip(tripId),
    FOREIGN KEY (classId) REFERENCES Class(classId)
);
''')

cursor.execute('''
CREATE TABLE Passenger
(
    name VARCHAR(20) NOT NULL,
    age INT NOT NULL,
    ticketId INT NOT NULL,
    FOREIGN KEY (ticketId) REFERENCES Ticket(ticketId)
);
''')


















conn.commit()
conn.close()

# class main():
    
    
#     def signUp():
#         while True:
#             signAs = input("1- To sign Up as admin\n2- To sign Up as customer")
#             if signAs == 1:
#                 admin = Admin()
#                 admin.signUp()
#                 break
#             elif signAs == 2:
#                 customer = Customer()
#                 Customer.signUp()
#                 break
#             else:
#                 print("Invalid Input")
#                 continue
        

#     def signIn():
#         while True:
#             signInAs = input("1- To sign In as admin\n2- To sign In as customer")
#             if signInAs == 1:
#                 admin = Admin()
#                 admin.signIn()
#                 break
#             elif signInAs == 2:
#                 customer = Customer()
#                 customer.signIn()
#                 break
#             else:
#                 print("Invalid Input")
#                 continue
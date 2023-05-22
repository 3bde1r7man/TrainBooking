import sqlite3


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
    name VARCHAR(20) NOT NULL,
    adminId INT NOT NULL,
    details VARCHAR(20) NOT NULL,
    FOREIGN KEY (adminId) REFERENCES Admin(adminId)
);

''')

cursor.execute('''
CREATE TABLE Class
(
    classId INTEGER PRIMARY KEY AUTOINCREMENT,
    price FLOAT NOT NULL,
    className VARCHAR(20) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE TrainClass
(
    nSeats INT NOT NULL,
    trainId INT NOT NULL,
    classId INT NOT NULL,
    avlSeats INT NOT NULL,
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
    price FLOAT NOT NULL,
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

# c.execute('INSERT INTO Class (ClassName, price) VALUES(?, ?)',("Class A",  700))
# conn.commit()
# c.execute('INSERT INTO Class (ClassName, price) VALUES(?,?)',("Class B",  600))
# conn.commit()
# c.execute('INSERT INTO Class (ClassName, price) VALUES(?,?)',("Class C",  500))
# conn.commit()
conn.close()

class Class():
    def __init__(self):
        self.classId = None
        self.name = None
        self.price = None


    def addClass(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        class_name = input('Class name: ')
        price = int(input('Price :'))
        cursor.execute(f'SELECT className FROM Class WHERE name = "{class_name}"')
        if cursor.fetchone() == None:
            cursor.execute(f'INSERT INTO Class (className, price) VALUES ("{class_name}", "{price}")')
            conn.commit()
        else:
            print('Class already exists\n')


    def getClasses(self):
        conn = sqlite3.connect('db.sqlite3')  
        cursor = conn.cursor()
        cursor.execute('SELECT classId, className, price FROM Class')
        rows = cursor.fetchall()
        conn.close()
        return rows
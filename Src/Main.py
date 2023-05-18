import sqlite3

conn = sqlite3.connect('db.sqlite3')  
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE Customer
# (
#     custmerId INT NOT NULL,
#     password VARCHAR(20) NOT NULL,
#     email VARCHAR(20) NOT NULL,
#     DOB DATE NOT NULL,
#     name VARCHAR(20) NOT NULL,
#     PRIMARY KEY (custmerId)
# );
# ''')

# cursor.execute('''
# CREATE TABLE Ticket
# (
#     ticketId INT NOT NULL,
#     bookedSeats INT NOT NULL,
#     custmerId INT NOT NULL,
#     PRIMARY KEY (ticketId),
#     FOREIGN KEY (custmerId) REFERENCES Customer(custmerId)
# );

# ''')

# cursor.execute('''
# CREATE TABLE Admin
# (
#     adminId INT NOT NULL,
#     password VARCHAR(20) NOT NULL,
#     name VARCHAR(20) NOT NULL,
#     email VARCHAR(20) NOT NULL,
#     PRIMARY KEY (adminId)
# );

# ''')

# cursor.execute(''' CREATE TABLE Model
# (
#     modelId INT NOT NULL,
#     PRIMARY KEY (modelId)
# );

# ''')
# cursor.execute(''' 
# CREATE TABLE Passenger
# (
#     name VARCHAR(20) NOT NULL,
#     passengerId INT NOT NULL,
#     ticketId INT NOT NULL,
#     FOREIGN KEY (ticketId) REFERENCES Ticket(ticketId)
# );

# ''')

# cursor.execute('''
# CREATE TABLE Class
# (
#     classId INT NOT NULL,
#     className VARCHAR(10) NOT NULL,
#     PRIMARY KEY (classId)
# );

# ''')

# cursor.execute('''
# CREATE TABLE Customer_phoneNum
# (
#     phoneNum INT NOT NULL,
#     custmerId INT NOT NULL,
#     PRIMARY KEY (phoneNum, custmerId),
#     FOREIGN KEY (custmerId) REFERENCES Customer(custmerId)
# );
# ''')

# cursor.execute('''
# CREATE TABLE Train
# (
#     trainId INT NOT NULL,
#     modelId INT NOT NULL,
#     adminId INT NOT NULL,
#     PRIMARY KEY (trainId),
#     FOREIGN KEY (modelId) REFERENCES Model(modelId),
#     FOREIGN KEY (adminId) REFERENCES Admin(adminId)
# );

# ''')

# cursor.execute('''

# CREATE TABLE TrainClass
# (
#     nSeats INT NOT NULL,
#     price INT NOT NULL,
#     trainId INT NOT NULL,
#     classId INT NOT NULL,
#     PRIMARY KEY (trainId, classId),
#     FOREIGN KEY (trainId) REFERENCES Train(trainId),
#     FOREIGN KEY (classId) REFERENCES Class(classId)
# );

# ''')

# cursor.execute('''

# CREATE TABLE Trip
# (
#     src VARCHAR(20) NOT NULL,
#     dist VARCHAR(20) NOT NULL,
#     departs DATE NOT NULL,
#     arrives DATE NOT NULL,
#     tripId INT NOT NULL,
#     adminId INT NOT NULL,
#     trainId INT NOT NULL,
#     PRIMARY KEY (tripId),
#     FOREIGN KEY (adminId) REFERENCES Admin(adminId),
#     FOREIGN KEY (trainId) REFERENCES Train(trainId)
# );

# ''')

# cursor.execute('''

# CREATE TABLE TripCustomer
# (
#     custmerId INT NOT NULL,
#     tripId INT NOT NULL,
#     PRIMARY KEY (custmerId, tripId),
#     FOREIGN KEY (custmerId) REFERENCES Customer(custmerId),
#     FOREIGN KEY (tripId) REFERENCES Trip(tripId)
# );
# ''')


conn.commit()
conn.close()
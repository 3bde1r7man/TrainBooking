
CREATE TABLE Customer
(
  customerId INT IDENTITY(1,1) PRIMARY KEY,
  password VARCHAR(20) NOT NULL,
  email VARCHAR(20) NOT NULL,
  DOB DATE NOT NULL,
  name VARCHAR(20) NOT NULL
);

CREATE TABLE Admin
(
  adminId INT IDENTITY(1,1) PRIMARY KEY,
  password VARCHAR(20) NOT NULL,
  name VARCHAR(20) NOT NULL,
  email VARCHAR(20) NOT NULL
);

CREATE TABLE Train
(
  trainId INT IDENTITY(1,1) PRIMARY KEY,
  details VARCHAR(20) NOT NULL,
  name VARCHAR(20) NOT NULL,
  adminId INT NOT NULL,
  FOREIGN KEY (adminId) REFERENCES Admin(adminId)
);

CREATE TABLE Class
(
  classId INT IDENTITY(1,1) PRIMARY KEY,
  className VARCHAR NOT NULL,
  price FLOAT NOT NULL
);

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

CREATE TABLE Customer_phoneNum
(
  phoneNum VARCHAR(20) NOT NULL,
  custmerId INT NOT NULL,
  PRIMARY KEY (phoneNum, custmerId),
  FOREIGN KEY (custmerId) REFERENCES Customer(custmerId)
);

CREATE TABLE Trip
(
  src VARCHAR(20) NOT NULL,
  dist VARCHAR(20) NOT NULL,
  departs DATE NOT NULL,
  arrives DATE NOT NULL,
  tripId INT IDENTITY(1,1) PRIMARY KEY,
  price FLOAT NOT NULL,
  adminId INT NOT NULL,
  trainId INT NOT NULL,
  FOREIGN KEY (adminId) REFERENCES Admin(adminId),
  FOREIGN KEY (trainId) REFERENCES Train(trainId)
);

CREATE TABLE TripCustomer
(
  custmerId INT NOT NULL,
  tripId INT NOT NULL,
  PRIMARY KEY (custmerId, tripId),
  FOREIGN KEY (custmerId) REFERENCES Customer(custmerId),
  FOREIGN KEY (tripId) REFERENCES Trip(tripId)
);

CREATE TABLE Ticket
(
  ticketId INT IDENTITY(1,1) PRIMARY KEY,
  bookedSeats INT NOT NULL,
  custmerId INT NOT NULL,
  tripId INT NOT NULL,
  classId INT NOT NULL,
  FOREIGN KEY (custmerId) REFERENCES Customer(custmerId),
  FOREIGN KEY (tripId) REFERENCES Trip(tripId),
  FOREIGN KEY (classId) REFERENCES Class(classId)
);

CREATE TABLE Passenger
(
  name VARCHAR(20) NOT NULL,
  age INT NOT NULL,
  ticketId INT NOT NULL,
  FOREIGN KEY (ticketId) REFERENCES Ticket(ticketId)
);